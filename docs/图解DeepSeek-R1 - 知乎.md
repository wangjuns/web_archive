# 图解DeepSeek-R1 - 知乎
[图解DeepSeek-R1 - 知乎](https://zhuanlan.zhihu.com/p/21175143007) 

 前言
--

DeepSeek最近爆火，相信将来回首时，其将是AI发展过程中的里程碑式工作。对于机器学习研发领域而言，它的发布意义重大，原因主要有两点：

*   它是一个开放权重模型，还拥有规模更小的蒸馏版本；
*   它分享并深入探讨了一种训练方法，有望复刻像 [OpenAI O1](https://zhida.zhihu.com/search?content_id=253257464&content_type=Article&match_order=1&q=OpenAI+O1&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDEzMzU3NjIsInEiOiJPcGVuQUkgTzEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTMyNTc0NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.KqeFpd2BdbyU4ANxnj2INLhgMxfubY8JckfRPzpeP4Q&zhida_source=entity) 这样的推理模型（且使用的算力更小）。

在这篇文章中，我们将一同探寻DeepSeek-R1是如何构建的。

回顾：大语言模型的训练方式
-------------

和大多数已有的大语言模型一样，DeepSeek-R1 也是每次生成一个token。不过，它在解决数学和推理问题方面表现卓越，因为它会花更多时间处理问题，时间花在哪里了呢？即通过产生能够解释其思维链的thinking tokens（即生成思考过程的token）来更好的处理数学和推理问题。

![](assets/9/4/9408bd0611e72724fba5cc5bc5a0978f.jpg)

给出答案前先思考

如下图所示，创建一个高质量大语言模型通常需要三个步骤：

![](assets/1/d/1d4f5d1f8f5255ec1d62dcf10ba2acf7.jpg)

1.  **语言建模阶段**：使用海量网络数据训练模型，让它预测下一个单词，这个阶段会产生一个基础模型。
2.  **监督微调阶段**：使模型在遵循指令和回答问题方面具备更好的表现，该阶段会产生一个经过指令调整的模型，即监督微调（SFT）模型。
3.  **偏好微调阶段**：进一步优化模型行为，使其符合人类偏好，最终得到可供用户在各种平台和应用中交互使用的偏好微调大语言模型。

DeepSeek-R1 的训练方法
-----------------

DeepSeek-R1 遵循上述基本流程。第一步的具体细节源自之前关于 [DeepSeek-V3 模型的论文](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2412.19437v1)。R1 采用那篇论文中的基础模型（并非最终的 DeepSeek-v3 模型），同样要经过监督微调和偏好微调步骤，但具体实施方式有所不同。从base model到R1的过程图解如下：

![](assets/4/7/4788a9a0063d2af2291c95761c1645fb.jpg)

在 R1 的创建过程中，有三个特别之处值得关注，下文将分别围绕这三个方面展开：

*   长链推理 SFT 数据
*   一个临时的高质量推理语言模型（但在非推理任务上表现较差）
*   使用大规模强化学习创建推理模型

长推理链监督微调（SFT）数据
---------------

![](assets/7/e/7ec0fc284694cccea140babcec98fc20.jpg)

基于base model的SFT

基于base model做SFT用到大量的长思维链推理数据（60 万条）。在这种规模下，这些数据很难获得，并且用人类进行标注非常昂贵。这就是为什么创建它们的过程是要强调的第一个特别之处。如上图所示，SFT数据即是图中的"Reasoning data Long chain-of-thought examples"。

为了获取这些数据，DeepSeek团队使用了一个"临时的推理模型"，这样数据来源有了。为了提高数据质量，就要求“临时模型”的推理效果要足够好。详见下一小节。

一个临时的高质量推理大语言模型
---------------

这些用于做SFT的数据由 R1 的一个前身模型生成（**注意不是R1-Zero**），这是一个未命名的同类模型，专门用于推理。它的灵感来源于另一个名为 R1-Zero 的模型（稍后会详细介绍）。这个模型的重要意义不在于它本身是一个多么出色的大语言模型，而在于它的创建过程。在大规模强化学习的辅助下，仅需少量标注数据，就能训练出一个擅长解决推理问题的模型。这个模型可以在非推理任务上表现欠佳。

这个未命名的专业推理模型的输出结果，可用于训练一个更通用的模型，使其在非推理任务上也能达到用户对大语言模型的预期水平。

上述过程图解如下，其中的"Interim reasoning model"就是临时的推理模型：

![](assets/6/6/6607da005f54484666b3c125b70f185f.jpg)

SFT数据来自Interim reasoning model

通过大规模强化学习创建推理模型
---------------

临时的高质量推理模型如何训练呢？答案是：大规模的推理导向的强化学习 (Large-Scale Reasoning-Oriented Reinforcement Learning)，即下图中的"Reasoning-Oriented Reinforcement Learning"。

![](assets/5/7/5765ad09ff6018e2f886352aa57aab66.jpg)

临时推理模型的主要技术-推理导向的强化学习

### 大规模推理导向强化学习（R1-Zero）

这里强化学习被用于创建“临时推理模型”（注意临时推理模型不是R1-Zero），之后该模型会生成推理数据，进而用于微调。而能够成功创建这个模型，得益于之前训练 [DeepSeek-R1-Zero](https://zhida.zhihu.com/search?content_id=253257464&content_type=Article&match_order=1&q=DeepSeek-R1-Zero&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDEzMzU3NjIsInEiOiJEZWVwU2Vlay1SMS1aZXJvIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjUzMjU3NDY0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.YYBNsKJPIozFkag88pqsUpXoVwhCzaCfH4eGj-4elJs&zhida_source=entity) 模型的实验。

![](assets/b/f/bf69a50af983a61ea05a833180443836.jpg)

R1-Zero与OpenAI-o1的推理效果对比

R1-Zero 的独特之处在于，它无需在监督微调训练集上做SFT，就能在推理任务中表现出色。它直接从预训练基础模型开始进行强化学习训练（未做SFT），且效果显著，能与 OpenAI o1 模型相媲美。

![](assets/4/4/448e29ce4c2654191ca470bde8943125.jpg)

R1-Zero直接强化学习、无SFT

这一成果意义非凡，因为数据一直是机器学习模型能力提升的关键要素。这个模型却打破了常规，这背后主要有两个原因：

1.  现代基础模型在质量和能力上有了质的飞跃（此基础模型基于 14.8 万亿高质量token进行训练）。
2.  与一般的聊天或写作请求不同，推理问题可以实现自动验证或标注。下面通过一个例子来说明。

**推理问题的自动验证示例**：在强化学习训练步骤中，可能会出现这样一个提示或问题：_编写一段 Python 代码，要求输入一个数字列表，将其排序后，在开头添加 42 再返回_。

这类问题有多种自动验证方法。假设将这个问题交给正在训练的模型，它生成了如下内容：

*   软件代码检查工具可以判断生成内容是否为正确的 Python 代码。
*   我们可以运行这段 Python 代码，看它能否正常执行。
*   其他现代代码生成大语言模型可以创建单元测试，来验证代码是否符合预期功能（即便这些模型本身并非推理专家）。
*   我们甚至可以进一步测量代码执行时间，在训练过程中，让模型更倾向于选择性能更优的解决方案，哪怕其他正确的 Python 程序也能解决问题。

我们可以在训练步骤中向模型提出类似的问题，并生成多种可能的解决方案。一图胜千言，上图：

![](assets/0/0/0001b562593ce101eba9a1857bc2323d.jpg)

上述训练过程中生成结果，可以自动检查（无需人工干预）：发现第一个生成内容甚至不是代码；第二个是代码，但不是 Python 代码；第三个是一个可能的解决方案，但未通过单元测试；而第四个是正确的解决方案。

![](assets/8/d/8db7713886b9a153847d62750c77c2b8.jpg)

基于规则的自动验证

这些反馈信号可直接用于改进模型。当然，这一过程会基于大量示例（以小批量的形式），并在连续的训练步骤中不断进行。

![](assets/f/0/f00ff8029f1379846f5d9a4b28824d4b.jpg)

这些奖励信号和模型更新机制，推动着模型在强化学习训练过程中不断提升任务处理能力，如下图所示：

![](assets/6/0/60e893bfee84079003f854915c41f594.jpg)

随着模型推理能力的提升，模型生成的响应长度也在增加，它会生成更多思考token来处理问题。如下图所示：

![](assets/0/3/03f525beb1ad856f224713cc277e305a.jpg)

随着模型推理能力的增强，生成的响应长度也在增加

这一过程虽然有效，但 R1-Zero 模型尽管在推理问题上得分很高，却存在一些问题，导致其可用性不如预期。

> Although DeepSeek-R1-Zero exhibits strong reasoning capabilities and autonomously develops unexpected and powerful reasoning behaviors, it faces several issues. For instance, DeepSeek-R1-Zero struggles with challenges like poor readability, and language mixing.  
> 尽管 DeepSeek-R1-Zero 展现出强大的推理能力，还自主发展出一些意想不到的强大推理方式，但它也面临不少挑战，比如生成内容可读性差、语言混杂等问题。

R1 旨在成为一个更实用的模型。因此，它并非完全依赖强化学习过程。正如我们在本节前面提到的，强化学习过程主要应用在两个方面：

*   创建一个临时推理模型，用于生成监督微调数据点；
*   训练 R1 模型，提升其在推理和非推理问题上的表现（借助其他类型的验证器）。

![](assets/5/7/5765ad09ff6018e2f886352aa57aab66.jpg)

强化学习在R1训练过程中的应用

### 利用临时推理模型创建监督微调推理数据

为了让临时推理模型发挥更大作用，会在几千个推理问题示例上对其进行监督微调训练（部分示例由 R1-Zero 生成并筛选而来），论文中将这些数据称为 “冷启动数据”。

> **2.3.1. Cold Start**  
> Unlike DeepSeek-R1-Zero, to prevent the early unstable cold start phase of RL training from the base model, for DeepSeek-R1 we construct and collect a small amount of long CoT data to fine-tune the model as the initial RL actor. To collect such data, we have explored several approaches: using few-shot prompting with a long CoT as an example, directly prompting models to generate detailed answers with reflection and verification, gathering DeepSeek-R1- Zero outputs in a readable format, and refining the results through post-processing by human annotators.

![](assets/f/a/fa67b77c8321b3ee3ef4c4dd9d6b8fb0.jpg)

临时推理模型的训练过程

或许你会疑惑，如果已经有了这些数据，为什么还需要强化学习过程呢？这是因为数据规模的问题。这个数据集可能只有 5000 条（获取相对容易），但训练R1却需要 60 万条数据。这个临时模型就起到了填补数据缺口的作用，能够合成生成极为宝贵的数据。

![](assets/9/c/9c050349ed6bfe5be9710282a18cb7cf.jpg)

R1训练数据的生成过程

如果您对监督微调（SFT）的概念不太熟悉，简单来说，就是向模型提供由提示和正确输出结果构成的训练示例。下图展示了几个监督微调训练示例：

![](assets/c/3/c37b4e7ea0316315f71c026869a33fac.jpg)

### 通用强化学习训练阶段

这一阶段让 R1 不仅在推理任务上表现出色，在其他非推理任务上也能有良好表现。该过程与前面介绍的强化学习过程类似，但由于涉及非推理应用，它采用了一个基于有用性和安全性的奖励模型（与 [Llama 模型](https://zhida.zhihu.com/search?content_id=253257464&content_type=Article&match_order=1&q=Llama+%E6%A8%A1%E5%9E%8B&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDEzMzU3NjIsInEiOiJMbGFtYSDmqKHlnosiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyNTMyNTc0NjQsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.5V3_09v5gnpn2K6MtlDHaa9Z-Fi1zPQ3XKUlhNeMy1U&zhida_source=entity)类似），用于处理这类应用中的提示信息。

![](assets/6/2/621615c071bb253eeffe4b4fef7036dc.jpg)

架构
--

和 GPT2、GPT 3 诞生初期的模型一样，DeepSeek-R1 由一系列 Transformer 解码器模块堆叠而成，共有 61 个。前三个模块是密集连接层，其余的是混合专家层

![](assets/b/a/ba0e94a19d9f5b289ced1d40c28a7043.jpg)

在模型维度大小和其他超参数方面，具体如下：

*   **分词器**：词汇表大小约 130,000
*   **模型维度**：7,168
*   **Transformer 模块 1 - FFNN 维度**：18,432
*   **共享专家（始终路由到）**：1
*   **MoE Transformer 模块 4 - 路由专家**：256
*   **每个token的激活专家数**：8

![](assets/3/9/39e9f595097667e3968c2094a7e04087.jpg)

总结
--

R1的训练过程如下图所示：

![](assets/3/f/3ffad917d6d5ba4cd53ca6ba8654b353.jpg)

附录
--

*   [DeepSeek-V3 Technical Report](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2412.19437v1)
*   [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2401.06066)
*   原文地址：