Title: 老显卡福音！美团开源首发INT8无损满血版DeepSeek R1

URL Source: https://mp.weixin.qq.com/s/Rsv0ELMbJpeCqgYsMy1PkA

Markdown Content:
##### 美团搜推团队 投稿  
量子位 | 公众号 QbitAI

满血版DeepSeek R1部署**A100**，基于INT8量化，相比BF16实现**50%吞吐提升**！

美团搜推机器学习团队最新开源，实现对DeepSeek R1模型基本无损的INT8精度量化。

要知道，DeepSeek R1原生版本的模型权重为FP8数据格式，**对GPU芯片类型有严格限制**，仅能被英伟达新型GPU支持（如Ada、Hopper架构芯片），其他型号GPU（如A100）无法直接部署。

目前，**量化代码已经合入到了开源LLM推理框架SGLang**，量化模型已经发布到了Hugging Face社区，方便用户使用。

INT8: 友好的“平替”
-------------

根据DeepSeek最新发布的技术报告，V3/R1突破性的训练成本控制主要依托FP8精度训练方案。FP8是一种典型的模型量化技术，相较于业界常用的BF16精度，FP8精度通过将数据位宽减半显著降低了单次计算开销，但也会带来一定的精度损失。

在实践中，DeepSeek R1采用了混合精度训练机制有效缓解了精度损失问题。

为了继续保持高吞吐性能，美团技术团队**选择了和FP8精度等位宽的INT8精度。**同时，INT8精度被广泛硬件原生支持，基于INT8精度可以极大拓展DeepSeek模型的硬件部署范围。以硬件友好的INT8精度为中心，美团技术团队开始探索FP8“平替”的落地方案。

![Image 1](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtBaKYKk4UzwhFibLaZ5w7jIicW19hYW0NSS9mZwRBiaXibpQD3KANMrh5AVOUj6yHgZejnhWTQ7SkvvyA/640?wx_fmt=png&from=appmsg)

量化技术的探索
-------

具体来说，**分块量化**（Block-wise Quantization）是DeepSeek V3/R1降低量化损失的关键技术之一。分块量化通过对权重矩阵的细粒度切分，将量化操作的范围控制在\[128, 128\]的矩阵内，减少了分布分散的出现概率，从而很好地控制了每次量化过程中的损失。

美团技术团队延续了DeepSeek训练的量化策略，同样在\[128, 128\]的矩阵内进行分块量化操作，保证训练和推理的一致性。在量化目标的选型上，INT8的优势在于其与FP8享有相同的位宽，且大部分硬件都对INT8的数据计算原生支持。

在实践中，由于DeepSeek官方并没有提供半精度浮点型（BF16）的权重，因此首先需要将原生的FP8模型权重反量化成BF16，再分块量化成INT8类型。另外在推理过程中，为了匹配权重的分块量化，激活值采用在线逐token-group的量化方式，即每个token的嵌入向量分为多个组，逐组进行量化。分块量化的激活值和权重的乘法过程如下左图所示。

除了上述的分块量化外，美团技术团队还探索了**更高效的通道量化****（Channel-wise Quantization），即权****重的每列为一组进行量化。**

通道量化在执行完INT8的矩阵乘法后，只需进行一次反量化计算，计算开销更低。在具体实践中，同样地先将原生FP8的模型权重反量化成BF16，之后逐通道量化成INT8类型。同时，对激活值采用在线逐token量化，最大程度地减少activation的量化损失。通道量化的激活值和权重的乘法过程如下右图所示。

**目前，两种INT8量化权重均已开源到Hugging Face。**

INT8量化模型精度
----------

分别应用上述的两种量化方法，对开源的DeepSeek R1模型进行了INT8量化处理，并在GSM8K和MMLU两个数据集上对量化后的模型进行了精度评估。评估结果如下表所示，相比基线的BF16和FP8模型，两种INT8量化模型的精度基本无损。

![Image 2](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtBaKYKk4UzwhFibLaZ5w7jIicQtPrAYWueC4WUp59rhOu3WormFut3KnEHc9CQNzT8gYHAQnoNfsn4w/640?wx_fmt=png&from=appmsg)

注：表中的精度结果是多次测试的均值。

INT8量化模型推理吞吐
------------

在知名开源推理框架SGLang上，对上述两种INT8量化方法进行了推理支持，并进行了推理吞吐评估。SGLang是当前SOTA的开源LLM推理框架，在DeepSeek系列模型上有着最优的推理性能，被业界广泛使用。

在A100 GPU上对两种INT8模型和BF16模型进行推理吞吐评估。得益于更低的显存要求，INT8量化模型仅需要16张A100 GPU即可推理，但是BF16模型需要32张A100 GPU。为了比较的公平性，统一在32张A100 GPU上进行吞吐测试。结果如下表所示，**分块量化的INT8推理相比BF16可以提升33%的吞吐；通道量化的INT8推理可以进一步达到50%的吞吐提升。**

![Image 3](https://mmbiz.qpic.cn/mmbiz_png/YicUhk5aAGtBaKYKk4UzwhFibLaZ5w7jIic9IlsvuuMcZABZYoIAibcxdD9sH5XIU98icuEibpVEg8utuDtnSicAJPRgQ/640?wx_fmt=png&from=appmsg)

INT8量化模型部署
----------

以双节点各8张A100 GPU为例，开发者需要在双部署节点安装最新版本的SGLang，然后分别执行下面命令：

```
# 分块量化INT8推理
```

```
# 通道量化INT8推理
```

下面是一些有趣的case：

### 深度思考能力展示

这里以curl为例发送一条请求：

```
curl -X POST 'http://HEAD_IP:5000/v1/chat/completions' \
```

在INT8 R1的回答中（由于篇幅限制省略部分内容），能看到其风格独特的反思：

> 不过，我需要确认这一点是否正确。比如，有没有可能其他选项中也有合金？比如，锡有时候会和其他金属混合使用，但锡本身是纯金属。同样，铝、铁、铜都是纯金属。所以钢作为合金，应该是一个关键的不同点。另外，可以考虑其他属性，比如它们的用途、物理性质或化学性质。例如，导电性：银是最好的导体，但这里没有银，而铜的导电性也很好，铝也不错，铁和钢的导电性相对差一些。但这样分类的话，可能难以确定哪一个不同。……不过回到最初的分类，钢是唯一的合金，而其他都是纯金属，这一点可能更为基础。因此答案应该是3.钢。不过需要再验证一下这个结论是否正确。

**最终答案也是正确的：**

答案：3.钢

### 模拟海量小球运动

参考其他LLM测试的prompts作为输入，对比INT8（上）和FP8（下）输出代码的运行效果，INT8完全不逊于FP8。

> write a script for 100 bouncing balls within a sphere, make sure to handle collision detection properly. make the sphere slowly rotate. make sure balls stays within the sphere. implement it in p5.js

![Image 4](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtBaKYKk4UzwhFibLaZ5w7jIicZiaCWHBY310IzO7GgkP02DaLCiaicWgpAn6JaibglsicNThnpb717nVZE4g/640?wx_fmt=gif&from=appmsg)

![Image 5](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtBaKYKk4UzwhFibLaZ5w7jIicIWuVW6rNLiaib5arTRqia6nWGib5g8VkOngSpWzR5C5lsFfWjGic3Q37R1g/640?wx_fmt=gif&from=appmsg)

总结与展望
-----

综上，研究团队在DeepSeek R1上进行了INT8量化技术的探索，并基于SGLang框架进行了推理能力的支持，在保证量化后模型精度的前提下，让DeepSeek R1可以在如A100等老型号GPU上进行部署，并且提升了推理吞吐。我们希望开源的代码和权重可以让更多用户和业务方受益，也欢迎大家积极交流相关技术，共同建设、回馈开源社区。

📮交流邮箱：search.platform@meituan.com

参考文献  
\[1\] 技术报告：Liu A, Feng B, Xue B, et al. Deepseek-v3 technical report\[J\]. arXiv preprint arXiv:2412.19437, 2024.  
\[2\] Hugging Face：https://huggingface.co/meituan/DeepSeek-R1-Block-INT8，https://huggingface.co/meituan/DeepSeek-R1-Channel-INT8  
\[3\] 推理支持：Block-wise INT8 DeepSeek R1支持（https://github.com/sgl-project/sglang/pull/3730）、Channel-wise INT8 DeepSeek R1支持（https://github.com/sgl-project/sglang/pull/3888）  
\[4\] 其他LLM测试：https://qwenlm.github.io/blog/qwq-max-preview/

— **完** —

**学术**投稿请于**工作日**发邮件到：

**ai@qbitai.com**

标题注明【投稿】，告诉我们：

你是谁，从哪来，投稿内容

附上论文/项目主页链接，以及联系方式哦

我们会（尽量）及时回复你

![Image 6](https://mmbiz.qpic.cn/mmbiz_gif/YicUhk5aAGtC5nGy7YMGhQ0ZJeyibWyL0KVCtiaLEPMyd4Bszuo0bFIOxZOvdmqdxnOosYXyu5aI7MXpyUrUWfz6g/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

**一键关注 👇 点亮星标**

**科技前沿进展每日见**

**一键三连****「点赞」「转发」「小心心」**

**欢迎在评论区留下你的想法！**
