不到 4 万元的 DeepSeek-R1-671B-Q8 部署方案
===============
                                                                          

             

  

![Image 1: cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dWDic6IAXZscygCcrEXpBuiclykcqQAUZsdc4Wd8hoRNwvic91iayF39DkQO4RaIgnmLn8bxick5JgZdAyPNZoicBWRQ/0?wx_fmt=jpeg)

不到 4 万元的 DeepSeek-R1-671B-Q8 部署方案
=================================

Original Admin [腾讯玄武实验室](javascript:void(0);)

![Image 2: profile_qrcode](https://mp.weixin.qq.com/mp/qrcode?scene=10000005&size=102&__biz=MzA5NDYyNDI0MA==&mid=2651960051&idx=1&sn=6ba8b7473d0779d41d1e48c4fc2adda6&send_time=)

腾讯玄武实验室

深圳市腾讯计算机系统有限公司

腾讯玄武实验室官方微信公众号

1407篇原创内容

_2025年03月17日 12:50_

虽然 DeepSeek-R1 是开源模型，理论上每个技术爱好者都可以在家里部署一套自己的 DeepSeek-R1，但由于其模型总参数高达 671B，典型的私有化部署方案需要 8 张 141G 的 H20，成本超过 150 万元。

在 DeepSeek-R1 发布后，Rasim Nadzhafov 等人发现可以用基于 CPU 的硬件方案进行部署。腾讯玄武实验室在网上诸多相关实践的基础上进行了深入研究，从硬件、系统、推理框架等各个层面进行优化，在使用更低成本、更低功耗硬件的同时实现了长文本生成速度提升约 25%、峰值输出速度提升约 15%、预填充速度提升约 20%。使用玄武实验室的软硬件优化方案，只需不到 4 万元人民币的硬件就可部署 DeepSeek-R1-671B-Q8，峰值生成速度 7.17 tokens/s，即每秒输出约 10 个汉字，且整机功耗和噪音和家用台式机类似。

![Image 3](https://mp.weixin.qq.com/s/vIrvbVJ6Nv00Ehre1zZwMw)

已关注

Follow

Replay Share Like

Close

**观看更多**

更多

_退出全屏_

[](javascript:;)

视频加载失败，请刷新页面再试

 [![Image 4](blob:https://mp.weixin.qq.com/48a490773e6215eef2b6036ff496e1c9) Refresh](javascript:void(0);)

![Image 5](blob:https://mp.weixin.qq.com/ed9b55868b8ba2468c6a25d2e4ae64af)

[Video Details](javascript:;)

根据我们的研究，在 CPU 推理方案中：内存带宽直接影响生成速度；CPU 核心数影响预填充和并发输出速度；SSD 读写速度影响模型加载速度和Prompt Cache 读写速度；CPU 主频对性能影响较小。所以在硬件选型中应按照如下优先级分配预算：

**“内存带宽” \> “CPU 核心数” \> “SSD 读写速度”\> “CPU 主频”**

同时我们还发现不应用两颗 CPU 运行一个实例，因为双路 NUMA 冲突会导致内存带宽严重恶化，而所有优化 NUMA 冲突的方案都会消耗宝贵的内存容量。

另外 12 个内存通道必须插满，这样才能获得 CPU 所支持的全部带宽。单条内存应选择 64GB，因为 12 路 64GB 共 768GB 总容量装下 Q8 量化后的模型权重后，剩下的存储空间做为 KV Cache 还能支持 22K 的模型上下文。

主板选择的时候不应选择支持 2DPC（2 DIMMs Per Channel）内存插槽的主板，即使使用这类主板也要确保每个通道只插一根内存，否则主板会对该通道进行降频，如 5600MHz 降到 4800MHz，从而导致总体带宽大幅下降。

CPU 使用风冷即可，但内存的散热非常重要，长时间内存过热可能会导致降频，内存降频后会损失高达 20% 的生成速度。

基于以上研究结果，我们规划了一套基于 AMD EPYC 5th Gen 9005 系列处理器的方案（价格为当前零售市场报价）：

**MZ33-AR1（5950 元）**

**EPYC 9115（5400 元）或者 EPYC 9135（7900 元）**

**DDR5 5600MHz 64GB x 12（22800 元）**

**1TB SSD（338 元）**

**850W 电源（349 元）**

**CPU 散热器（294 元）**

**内存散热器（368 元）**

**机箱（187 元）**

**总计：35686 元（选择 EPYC 9135 则为 38186 元）**

如追求更好的扩展性，也可将主板更换为支持双路的 MZ73-LM1。这样成本仍然在 4 万元以内，但未来可增加另一颗 CPU 和相应内存，同时运行两个实例。

![Image 6: Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dWDic6IAXZscygCcrEXpBuiclykcqQAUZsmJjRz1v6PnlRZoD3NXrryHEfOrDGrFMjcHJicSEe8iaol6D3MNATJZ3A/640?wx_fmt=jpeg&from=appmsg)

在硬件优化上，最重要的就是前面提到的内存散热。其次，由于 CPU 和主板均支持 6000MHz，因此可以对内存进行小幅度超频处理，将频率从默认频率 5600MHz 提升到 6000MHz。超频选择的入口位置：AMD CBS -\> UMC Common Options -\> Enforce PDR -\> Memory Target Speed -\> DDR6000，如下图所示：

![Image 7: Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dWDic6IAXZscygCcrEXpBuiclykcqQAUZs7HfUGv1qHezVX67DsqShwz5JWpsnRc2Hn9TPLfQicomO4Y1BTMMfPpA/640?wx_fmt=jpeg&from=appmsg)

在系统优化上，主要是配置系统使用 1G 大页（HugePages），并预分配 671 个 1G 大页。在 Grub 配置文件中增加如下设定：

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash default_hugepagesz=1G hugepagesz=1G hugepages=671"
```

重启后系统就会开启 1G 大页，预留足够的内存空间加载 Q8 精度的权重文件。

除了硬件、系统层面的优化，还需要对推理框架进行优化，修改 llama.cpp 中的 llama-mmap.cpp，以使用预留的 1G 大页来提高性能。

我们修改后的 llama-mmap.cpp 代码可从下面的地址获得：

[https://github.com/XuanwuLab/llama.cpp\_deepseek/blob/main/llama-mmap.cpp](https://github.com/XuanwuLab/llama.cpp_deepseek/blob/main/llama-mmap.cpp)

用修改后的 llama-mmap.cpp 替换 llama.cpp 中对应的文件，编译后执行下面的命令加载模型权重即可：

```
./llama-server -m ./DeepSeek-R1-Zero-Q8_K_M/DeepSeek-R1-Zero-BF16-256x20B-Q8_0-00001-of-00016.gguf  --host 0.0.0.0 --port 8008 --temp 0.6 --cache-type-k q8_0 -t 16 -tb 32 --ctx-size 4096 -np 1 --jinja --chat-template-file ../../models/templates/llama-cpp-deepseek-r1.jinja --reasoning-format deepseek
```

\--jinja --chat-template-file ./llama.cpp/models/templates/llama-cpp-deepseek-r1.jinja --reasoning-format deepseek 参数会强制模型进行深度思考，若不需要强制思考则不需要这些参数。

\-t 16 和 -tb 32 参数分别指定生成和预填充时的核心数量，可以避免因抢夺 CCD 带宽时的系统开销同时合理充分利用超线程带来的的额外算力。一般情况下生成使用超线程是负优化，但是在预填充时使用超线程则可以提高速度。

**FAQ：**

**Q：为什么用 CPU 就能推理参数高达 671B 的大模型呢？**

A：DeepSeek 是一种高稀疏度的 MoE（Mixture of Experts）模型，每层包含 256 个专家（Expert），但实际推理时，每生成一个 Token 仅激活其中的 8 个专家。这种“按需激活”机制意味着，尽管模型总参数高达 671B，但实际参与计算的参数只有约 37B，仅占整体参数量的 5.5%。因此，大幅降低了推理过程对计算资源的需求，纯 CPU 部署如此规模的模型成为可能。

**Q：既然用 CPU 就能跑 DeepSeek-R1，****那 GPU 是不是就不重要了？**

A：对于个人技术爱好者来说，这套基于 CPU 的硬件方案用一台高性能游戏主机的价格就可实现比较流畅的输出速度，让个人部署 DeepSeek-R1 不再遥不可及。但 CPU 方案也有其先天缺陷。例如，在多并发和输入较长时，速度会大幅下降。从每百万 Token 成本的角度来看，CPU 方案也比 GPU 高。所以 CPU 方案有其适用场景，但并不能代替 H20 等 GPU。

**Q：为什么要量化为 Q8 ？**

A：DeepSeek-R1 的原生精度是 FP8。由于 CPU 没有专门的 FP8 硬件指令支持，而现代 CPU 的 AVX512 等 SIMD 指令集可以加速整数的处理，所以使用 CPU 推理需要将 DeepSeek-R1 量化为 Q8。从我们的测试看来，Q8 和 FP8 的推理能力差别不大。

**Q：为什么不量化为 Q4？**

A：虽然 Q4 比 Q8 消耗的内存更少，生成 Token 更快，但 Q8 相较 Q4 在实际推理能力上还是具有明显优势。另外，在使用 CPU 推理时，由于 SIMD 指令集对 8-bit 整数的点积运算有原生支持，更重要的是我们发现 Q4 的思维链平均长度比 Q8 长了 45%，也就是说多输出了 45% 的无效 Token，所以虽然 Q4 生成 Token 速度较快，但完成任务甚至会更慢。这是我们最终选择 Q8 的原因。

**Q：这套方案除了 DeepSeek-R1，是否也可以用于 DeepSeek-V3？**

A：是的，这套方案也可用于 DeepSeek-V3。理论上参数量小于等于 DeepSeek-R1 规模的 MoE 模型都可以。

**Q：有没有什么地方可以体验一下 CPU 部署 DeepSeek-R1 的效果？**

A：我们已将类似优化方案发布在了腾讯云原生构建（CNB）平台，在 CNB 上可以快速体验纯 CPU 部署方案的效果：[https://cnb.cool/ai-models/deepseek-ai/DeepSeek-R1-GGUF/DeepSeek-R1-Q8\_0](https://cnb.cool/ai-models/deepseek-ai/DeepSeek-R1-GGUF/DeepSeek-R1-Q8_0)

**如果想了解更多相关技术细节，请关注玄武实验室的 Blog（[https://xlab.tencent.com/cn/](https://xlab.tencent.com/cn/)）。我们会发布更详细的相关技术文章。**

预览时标签不可点

Close

更多

Name cleared

![Image 8: 赞赏二维码](https://mp.weixin.qq.com/s/vIrvbVJ6Nv00Ehre1zZwMw)**微信扫一扫赞赏作者**

Like the Author[Other Amount](javascript:;)

Articles

No articles

Like the Author

Other Amount

¥

最低赞赏 ¥0

OK

Back

**Other Amount**

更多

赞赏金额

¥

最低赞赏 ¥0

1

2

3

4

5

6

7

8

9

0

.

Close

更多

搜索「」网络结果

​

暂无留言

已无更多数据

[Send Message](javascript:;)

  写留言:

[](javascript:; "轻点两下打开表情键盘")

Close

**Comment**

Submit更多

[表情](javascript:;)

![Image 9](https://mp.weixin.qq.com/mp/qrcode?scene=10000004&size=102&__biz=MzA5NDYyNDI0MA==&mid=2651960051&idx=1&sn=6ba8b7473d0779d41d1e48c4fc2adda6&send_time=)Scan to Follow

继续滑动看下一个

轻触阅读原文

![Image 10](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

向上滑动看下一个

当前内容可能存在未经审核的第三方商业营销信息，请确认是否继续访问。

[继续访问](javascript:)[Cancel](javascript:)

[微信公众平台广告规范指引](javacript:;)

[Got It](javascript:;)

 

![Image 11](https://mp.weixin.qq.com/s/vIrvbVJ6Nv00Ehre1zZwMw) Scan with Weixin to  
use this Mini Program

[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

× 分析

 : ， ， ， ， ， ， ， ， ， ， ， ， .   Video Mini Program Like ，轻点两下取消赞 Wow ，轻点两下取消在看 Share Comment Favorite 听过            

![Image 12](blob:https://mp.weixin.qq.com/18e05c31c61e67e7341d77add9851c34)

**腾讯玄武实验室**

不到 4 万元的 DeepSeek-R1-671B-Q8 部署方案

,

,

选择留言身份
