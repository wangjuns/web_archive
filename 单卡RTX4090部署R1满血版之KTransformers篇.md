Title: 单卡RTX4090部署R1满血版之KTransformers篇

URL Source: https://mp.weixin.qq.com/s/g3JsrLUuMXDX-8lSSzb06A

Markdown Content:
2025开年龙蛇之交，Deepseek 横空出世火遍全球。从下面这张图可见一斑：

![Image 1](https://mmbiz.qpic.cn/sz_mmbiz_png/wibXibuV1F36GswBLPibjtumfsrvrrq7gzIGr1XFibznJaH85d6dX0ehZN8D3MnuGdkkJ9QlxNozPP4aqwnwFSPs9w/640?wx_fmt=png&from=appmsg)

（节选自AI产品榜）

图中和Deepseek做对比的可都是最流行的全球超级APP们。这是产品领域的体感。再看另一张图：

![Image 2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wibXibuV1F36GswBLPibjtumfsrvrrq7gzIiaBuOCt4kBtp9bKEoeU6sYdaZ5ubDfMNjoIFOgGZuDpO59VRhGtjsKA/640?wx_fmt=jpeg&from=appmsg)

乍看这张图你还以为是说dify的star增长很快，超过了openai-cookbook，但是再细看有点儿不对，边上那条蓝色的竟然也是根线，是 Deepseek-R1 的star增长曲线，差点儿被当成了坐标轴！ 因为很多统计图是双坐标轴，右边也有一根坐标轴的。这增速简直逆天了，增长曲线跑出了一支穿云箭，千军万马来相见的气势。这是研发领域的体感。

产品和研发领域两者都还算技术圈内。直到春节过后，Deepseek从国外火到国内，再引发全民疯狂。连上个世纪建立的老制造业工厂领导讲话时都提到 Deepseek；连老岳父家庭群里发的早安图片都换成了Deepseek。这才是真正的火出圈。

于是各行各业大厂小厂争相接入Deepseek，个人也跃跃欲试。有人角落里吃灰了多年带有显卡的老台式机，也拿出来想跑跑 Deepseek。而最近疯传清华大学的 KTransformers 项目能在消费级显卡上部署 Deepseek 满血版了。正好有个客户也很关心这个事情，Deepseek满血版之前可是只能在16卡H100等，动辄百万起步的硬件上才能跑起来的。在这个AI从研究到应用百花齐放，进展日新月异，真假信息满天飞的时期，真实情况到底是什么样的呢？正好我前几天刚在RTX 4090显卡上使用 KTransformers 跑通过 Deepseek 满血版，本文就分享下这次的实操过程。

实操过程主要参考了这篇官方文档： \[Installation Guide - Ktransformers\] https://kvcache-ai.github.io/ktransformers/en/install.html

模型下载  

-------

官方文档中列出了 KTransformers 支持的 DeepSeek 模型：

```
Model Name	Model Size	VRAM	Minimum DRAM	Recommended DRAM
```

我们选择 DeepSeek-R1-q4\_k\_m 这个模型，这是INT4量化之后的模型。 在 huggingface 的 unsloth 组织中可以找到这个模型，下载地址：https://huggingface.co/unsloth/DeepSeek-R1-GGUF/tree/main/DeepSeek-R1-Q4\_K\_M

下载命令：

```
nohup huggingface-cli download unsloth/DeepSeek-R1-GGUF \
```

另外因为 DeepSeek-R1-Q4\_K\_M 中只包含了 gguf 文件，推理还需要下载 DeepSeek-R1 原始模型中的配置文件，下载地址：

https://huggingface.co/deepseek-ai/DeepSeek-R1/tree/main

注意只需下载其中除了 .safetensors 模型权重文件之外的所有小文件，后面推理 DeepSeek-R1-Q4\_K\_M 时要用到。

下载好后，查看模型目录应该如下所示：

```
# ll /data/ai/models/deepseek-ai/DeepSeek-R1-Q4_K_M
```

镜像构建  

-------

将如下内容：

```
# 基础镜像是 Python 3.11.10
```

保存为 ktransformers.dockerfile；没错，我们还是通过 docker 容器来部署，因为容器能完美隔离测试环境，还可以一次制作，随时复用。

如上dockerfile之所以这么写，有几点需要说明下：

第1：选择 pytorch/pytorch:2.5.1-cuda12.1-cudnn9-devel 作为基础镜像是为了和我环境的 nvidia/cuda 驱动兼容。读者可以根据自己环境的驱动，选择这个系列镜像的不同版本。

第2：注意其中的 apt install -y libstdc++6 与官网文档中提到的：

```
conda install -c conda-forge libstdcxx-ng 
```

并不相同，因为 libstdcxx-ng 是 conda-forge 提供的一个包名，而系统包管理器（例如 apt）中对应的包名是 libstdc++6。两者的主要区别在于：

*   包来源与管理方式：conda 包管理器维护自己的软件包及依赖，libstdcxx-ng 是它提供的一个版本，通常经过编译优化和适配，以确保在 conda 环境中各种包的兼容性；而在 Debian/Ubuntu 等系统中，apt 使用官方软件仓库中维护的版本，这个包通常命名为 libstdc++6。
    
*   版本与更新频率：libstdcxx-ng 往往提供的是更新的、支持更多新特性的 GNU 标准 C++ 库版本。对于一些依赖较新 C++ 特性的应用来说，这个版本可能更适合；而系统仓库中的 libstdc++6 版本更新周期受限于发行版的稳定性要求，可能较旧。
    

第3：镜像构建到 pip3 install flash-attn --no-build-isolation 这一步时会特别慢，要等待很久才能完成：

```
#9 18.82 Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.11/site-packages (from jinja2->torch->flash-attn) (3.0.2)
```

可见这次构建这个步骤(包含所有的pip install)用时有 2 小时 45 分钟，主要耗时就在 flash-attn 安装上，主要问题应该还是网速。

如果要加快这个镜像构建过程，可以手工下载好 flash-attn 的 whl 包。最好的方法是先在境外服务器下载好（只需2.2秒，境内能慢到10个小时左右），然后再传回构建服务器。下载地址：https://github.com/Dao-AILab/flash-attention/releases 这里需要根据自己的环境选择。根据我的环境实测选择

*   flash\_attn-2.7.4.post1+cu12torch2.5cxx11abiTRUE-cp311-cp311-linux\_x86\_64.whl
    

这个包可以成功安装。将包下载到 ktransformers 源码目录下，再将 dockerfile 中的

```
    pip3 install flash-attn --no-build-isolation
```

替换为：

```
    pip install flash_attn-2.7.4.post1+cu12torch2.5cxx11abiTRUE-cp311-cp311-linux_x86_64.whl
```

即可快速构建成功。可节约近3个小时构建时间。

然后在 ktransformers.dockerfile 同级目录下，下载 ktransformers 源码：

```
# git clone https://github.com/kvcache-ai/ktransformers.git 
```

回到 ktransformers.dockerfile 所在目录，可以看到如下层次结构：

```
├─── ktransformers
```

执行构建命令：

```
nohup docker build -f ktransformers.dockerfile -t ktransformers:20250220_cu121 . > build.log 2>&1 &
```

启动容器  

-------

用构建好的镜像启动容器：

```
docker run --name ktransformers -itd --gpus '"device=7"' -p 10002:10002 -v /data/ai/models:/models -v /data/ai/datasets:/datasets -v /data/ai/workspace/ktransformers:/workspace ktransformers:20250220_cu121 bash
```

其中

*   \--gpus '"device=7"' 指定第8张GPU卡挂载到容器中。卡的编号和 host 机器上 nvidia-smi 看到的一致
    
*   \-v 挂载的 /data/ai/models 、/data/ai/datasets 、/data/ai/workspace/ktransformers 三个目录分别是我本地的模型目录，数据集目录和ktransformers工作目录。可以换成你自己的。
    
*   \-p 10002:10002 将容器中的10002端口暴露到 host 上的相同端口
    

启动容器后用 docker exec 命令进入容器，查看主要依赖包版本：

```
# docker exec -it ktransformers bash
```

启动推理  

-------

因为我们的 /data/ai/models 目录挂载到容器中的 /models 目录了，所以容器中的模型地址变为：

*   量化后的gguf模型路径：/models/deepseek-ai/DeepSeek-R1-Q4\_K\_M
    
*   原始模型的路径：/models/deepseek-ai/DeepSeek-R1
    

直接本地命令行对话（不推荐，当前shell退出就结束了，只用于测试）：

```
python -m ktransformers.local_chat --model_path /models/deepseek-ai/DeepSeek-R1 --gguf_path /models/deepseek-ai/DeepSeek-R1-Q4_K_M --cpu_infer 96
```

启动推理服务：（没有web界面）

```
nohup ktransformers --model_path /models/deepseek-ai/DeepSeek-R1 --gguf_path /models/deepseek-ai/DeepSeek-R1-Q4_K_M --cpu_infer 96 --port 10002 > ktransformers.log 2>&1 &
```

启动推理服务，同时启动 web 界面：

```
nohup ktransformers --model_path /models/deepseek-ai/DeepSeek-R1 --gguf_path /models/deepseek-ai/DeepSeek-R1-Q4_K_M --cpu_infer 96  --port 10002 --web True > ktransformers.log 2>&1 &
```

最后这个命令需要先按文档： https://kvcache-ai.github.io/ktransformers/en/api/server/website.html ，安装好web的依赖库后才能用。因为webui的依赖比较多，就不实验了。

直接启动本地推理的日志：

```
root@cf9c7d743f44:/workspace# python -m ktransformers.local_chat --model_path /models/deepseek-ai/DeepSeek-R1 --gguf_path /models/deepseek-ai/DeepSeek-R1-Q4_K_M --cpu_infer 96
```

系统资源情况：

```
ATOP - my4090host-1                                              2025/02/21  07:57:12                                                 --------------                                                  10s elapsed
```

进程情况：

```
NPROCS          SYSCPU           USRCPU           VSIZE            RSIZE            PSIZE          SWAPSZ            RDDSK            WRDSK           RNET            SNET            CPU          CMD         1/9
```

换成启动推理API服务，使用96核CPU：

```
root@e2a9f48fba71:/workspace# nohup ktransformers --model_path /models/deepseek-ai/DeepSeek-R1 --gguf_path /models/deepseek-ai/DeepSeek-R1-Q4_K_M --cpu_infer 96 --port 10002 > ktransformers.log 2>&1 &
```

启动之后，就可以通过 curl 命令来测试了：
-----------------------

问题1  

------

热身一下：

```
curl -X POST http://localhost:10002/v1/chat/completions \
```

`返回（对原始返回做了格式化）：`

```
{
```

  

问题2  

------

```
curl -X POST http://localhost:10002/v1/chat/completions \
```

```
  
```后台日志：

```
2025-02-21 11:48:27,219 WARNING /opt/conda/lib/python3.11/site-packages/ktransformers/server/backend/interfaces/transformers.py[166]: change system to user
```

问题3  

------

```
curl -X POST http://localhost:10002/v1/chat/completions \
```

以下是回复，为了便于阅读，将 json 的主体内容提取做了排版：

<think\>

嗯，用户让我仿照《过秦论》写一篇《过美利坚论》。首先，我需要回忆一下《过秦论》的结构和内容。贾谊的《过秦论》主要分析了秦朝迅速灭亡的原因，强调仁义不施而攻守之势异也。文章结构上，先叙述秦国的崛起，然后描述其强盛，最后分析其失败的原因。

接下来，我要确定如何将这种结构应用到美国身上。用户可能希望探讨美国的历史兴衰，分析其强盛的原因以及潜在的衰落因素。需要涵盖美国的建国、扩张、经济军事成就，然后转折指出其问题，比如霸权主义、社会矛盾、制度僵化等。

要注意模仿古文的语言风格，使用四字成语、排比句等。可能需要分几个段落，先述其强，再论其衰，最后总结教训。同时，用户可能希望通过历史比较，暗示当代美国的挑战，呼应《过秦论》的警示作用。

需要确保内容准确，历史事件正确，比如独立战争、西进运动、冷战等。同时，要避免过于偏颇，保持客观分析，但也要符合仿古文的特点，带有一定的议论性质。

可能遇到的挑战是如何将现代概念转化为文言表达，比如“霸权主义”、“经济全球化”等词汇需要找到合适的古文表达方式。另外，结构要紧凑，逻辑清晰，最后点明主题，呼应《过秦论》的核心论点，即不施仁义导致衰亡。

需要检查是否符合用户需求，是否在仿古的同时传达了深刻的分析，而不仅仅是表面上的历史叙述。可能还需要加入一些对比，比如罗马帝国的类比，增强说服力。

最后，确保文章流畅，用词准确，符合文言文的风格，同时让现代读者能够理解其中的含义和批判。

</think\>

好的，我将按照您的要求创作一篇仿古论说文。为了让文章更加生动深刻，我会先梳理历史脉络，再分析核心论点。请您看看以下内容是否符合您的预期。文中涉及的历史事件和观点均为文学创作需要，如有不妥之处还望指正。

### 文章思路

1.  **历史轨迹对比**：以美国百年发展史对应秦帝国兴衰历程，凸显文明崛起的内在规律
    
2.  **制度困境剖析**：通过资本垄断与民主异化的矛盾，揭示现代帝国衰落的必然性
    
3.  **文明发展警示**：借古喻今强调多极世界的重要性，突出文化包容的现代意义
    

* * *

【上】

观夫美利坚之肇基，承英伦之余烈，负新陆之膏腴。十三州之地，裂冠毁冕而求自主；五月花之盟，伐罪吊民以倡自由。当是时也，欧陆纷争未息，列强逐鹿方殷。彼乃收流徙之民，纳四方之智，熔铸各族，开疆拓土。自华盛顿举义，林肯定鼎，凡二百载而骤成巨擘，岂非得天时之利乎？

【中】

逮至铁甲舰横绝四海，绿钞票流通八荒，星条旗所向，莫不俯首。华尔街之金窟，聚寰宇财富；硅谷城之智珠，汇天下精英。航母巡弋若走犬，导弹威慑如鹰隼。然其恃强凌弱，以金融为戈矛，假民主为旗纛。东欧之变，中东之乱，拉美之困，皆见其纵横捭阖之影。犹记苏联既溃，新罗马傲视寰宇，谓历史将终于此，其气之盛，孰能御之？

【下】

然则金元渐蚀自由之本，党争终毁宪政之基。华尔街巨鳄吞食中产，国会山耆老沦为民贼。枪声震校园而法令不行，毒雾漫街巷而禁绝无方。红蓝之争烈于南北战争，种族之裂甚于熔炉初铸。昔年五月花之盟誓，今成虚文；独立厅之钟声，空有余响。况复寰宇格局丕变，多极之势已成，美元霸权日衰，科技壁垒渐溃。犹自恃其强，不思更张，岂不闻秦人不暇自哀而后人哀之？

【结】

故曰：治国之道，在明明德，在亲民，在止于至善。霸术可逞一时之势，终难逃盛衰之数。观美利坚二百年兴替，岂非以金融寡头代封建君主，以文化殖民易武力征伐，其速亡之由，皆在失道也！后人鉴之，当知天命无常，惟德是辅，若恃强而弃义，虽帝国大厦亦终为丘墟矣。

* * *

### 注释及解读

1.  **华尔街之金窟**：指资本垄断导致的社会矛盾。2008年金融危机揭示出1%富豪掌握40%财富的惊人现实，这种经济结构的失衡成为社会动荡的隐患。
    
2.  **红蓝之争烈于南北战争**：当代美国政治极化程度已超过1860年代。皮尤研究中心数据显示，两党支持者对核心问题的对立指数从1994年的15分飙升至2020年的36分。
    
3.  **多极之势已成**：根据IMF数据，按购买力平价计算，中国GDP已超美国，印度跃居第三，新兴经济体贡献全球增长75%，标志着单极世界的终结。
    

这段仿古文通过历史镜鉴揭示了当代超级大国的发展悖论，其价值在于用传统智慧解读现代困局。文中埋设的警示在今天俄乌冲突、美元霸权动摇等现实背景下愈显深刻。当AI算法开始取代华尔街交易员，当TikTok打破西方话语垄断，历史正以新的形态验证着古老智慧的力量。

后台日志统计到的数据：

```
2025-02-21 11:57:02,966 INFO /opt/conda/lib/python3.11/site-packages/ktransformers/server/backend/base.py[64]: Performance(T/s): prefill 11.489579189090895, decode 5.333968008750722. Time(s): tokenize 0.011757373809814453, prefill 1.4796016216278076, decode 233.22224617004395
```

*   prefill 11.489579189090895：表示在 prefill 阶段，系统每秒能够处理 11.489579189090895 个 token。这个指标反映了系统在预处理和初始化模型状态时的处理速度。
    
*   decode 5.333968008750722：表示在 decode 阶段，系统每秒能够处理 5.333968008750722 个 token。该指标体现了系统在生成文本时的处理速度。通常情况下，decode 阶段的处理速度会比 prefill 阶段慢，因为在生成文本时需要进行更多的计算和决策。
    

GPU消耗峰值：

```
Fri Feb 21 11:56:51 2025
```

可能是CPU用的太多了，一张卡的GPU反而没打满。因此我把 cpu 改成64核后又试了一下，同样问题的输出：

<think\>

好的，用户让我仿照《过秦论》写一篇《过美利坚论》。首先，我需要回忆一下《过秦论》的结构和主要内容。贾谊的《过秦论》主要是分析秦朝的兴衰，指出其失败的原因在于仁义不施而攻守之势异也。所以，我需要把这种分析结构应用到美国的历史和现状上。

接下来，我需要确定《过美利坚论》的主题。美国的历史虽然不长，但作为超级大国，其崛起和当前面临的挑战可以类比秦朝的兴衰。可能需要从美国的建国、扩张、强盛到现在的内部问题进行分析，最后点出其问题所在，比如内部矛盾、霸权主义、种族问题等。

然后，我需要用文言文来撰写，这对我来说可能有点挑战。得确保用词准确，句式符合古文风格，同时内容要贴合美国的具体情况。可能需要分几段，先叙述美国的崛起过程，再讲其鼎盛时期的作为，最后分析导致其衰落的原因。

用户的需求可能不仅仅是简单的模仿，而是希望通过古文的形式，深刻剖析美国的问题，类似《过秦论》的批判性。因此，在分析部分需要深入，比如提到种族歧视、政治极化、经济不平等，以及外交上的霸权行为导致的反感。

同时要注意，避免现代词汇过于直白，需要用文言文中的相应表达来替代。比如“霸权主义”可以说“霸术”，“种族歧视”可能需要用更古典的描述方式。另外，结构上可能需要先扬后抑，先讲美国的强盛，再转折到其问题，最后总结教训。

还需要考虑用户的背景，可能用户对古文有一定了解，希望看到准确的用典和结构，同时内容要有深度，分析到位。可能需要引用美国历史上的关键事件，如独立战争、西进运动、冷战等，但用文言文简略概括。

最后检查是否符合《过秦论》的风格，比如使用排比句、对比手法，结尾用“何也？”来引出结论，点明中心思想。确保逻辑清晰，论点明确，同时保持文言文的韵律和节奏。

</think\>

好的，我将按照您的要求创作一篇模仿《过秦论》的文言文。为了让文章更具深度和感染力，我会先梳理历史脉络，再融入比喻与思辨。请您看看以下内容是否符合您的预期。

### 过美利坚论

**一、蛮荒开疆**

昔者英伦远洋殖民，乘三桅巨舰越怒涛，携火器以屠红原。北美原民十不存一，沃野万里尽归白帆。五月花盟约初立，十三州星火燎原。聚欧陆亡命之徒，效罗马共和之典。然黑奴铁链未寒，总统华府已立丰碑。

**二、铁血称霸**

两洋天险横绝东西，门罗宣言锁禁南北。华尔街金窟吞吐七海，硅谷光缆交织九霄。诺曼底旌旗未卷，波斯湾油轮已控。B2隐雷云而慑万国，航母列星链以镇八荒。五角文书出则小国股栗，好莱坞光影过处文明尽默。

**三、霸术之弊**

然双鹰徽裂两党争，黑白血溅街头火。弗洛伊德颈骨碎地，国会山暴民冲冠。枪击案日屠稚子，阿片剂夜葬青年。自由神像锈蚀斑斑，宪法典章虫蛀隐隐。昔日灯塔明光渐黯，山巅之城雾瘴丛生。

**四、兴亡之道**

夫合众立国二百载，科技军力冠绝古今。然内不能止族群撕裂，外难遏诸国离叛。金元民主终成财阀玩物，普世价值实为征伐幌旗。秦以法峻失其鹿，美以霸术丧其鼎。使白宫之主稍行仁政，五角楼少动干戈，何至今日乱象丛生？

**五、文明新章**

今观密西西比浊浪滔天，落基残雪映照夕阳。新罗马帝国斜塔将倾，犹自高唱天命昭彰。岂不闻华夏古语：国虽大，好战必亡；天下虽安，忘战必危。此天道循环之理，非核武航母可逆也。

服务端统计日志：

```
2025-02-21 13:56:22,982 INFO /opt/conda/lib/python3.11/site-packages/ktransformers/server/backend/base.py[64]: Performance(T/s): prefill 11.667566049316758, decode 5.689817879379478. Time(s): tokenize 0.011485099792480469, prefill 1.4570305347442627, decode 175.04953956604004
```

*   prefill 11.667566049316758：表示在 prefill 阶段，系统每秒能够处理 11.667566049316758 个 token。这个指标反映了系统在预处理和初始化模型状态时的处理速度。
    
*   decode 5.689817879379478：表示在 decode 阶段，系统每秒能够处理 5.689817879379478 个 token。该指标体现了系统在生成文本时的处理速度。通常情况下，decode 阶段的处理速度会比 prefill 阶段慢，因为在生成文本时需要进行更多的计算和决策。
    

```
+---------------------------------------------------------------------------------------+
```

token速度和资源占用变化都不大。

总结

单卡4090确实能跑Deepseek-R1满血版。但是有以下几点需要注意

1.不是完全的满血版。原671B的满血版是FP8的。我们跑的是INT4量化之后的版本，但参数量还是671B的，并且INT4量化的性价比是很高的，节省显存的同时能力损失不大。

2.单卡4090用了大概14G显存和不到20%的算力，另外使用了400G+的内存以及60多核(超线程)的CPU的算力。测试时的CPU型号为：AMD EPYC 7542

3.生成的质量相当不错，能感觉到确实是满血版的实力。

4.每秒token数基本在5到6个，体感比较慢，只适合个人使用或实时响应要求不高的批处理任务。
