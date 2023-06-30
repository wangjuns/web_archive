# [必读] LLM 应用开发全栈指南 - 知乎
[[必读] LLM 应用开发全栈指南 - 知乎](https://zhuanlan.zhihu.com/p/629589593?utm_id=0&utm_oi=28589894402048&utm_psn=1641609936437141504&utm_source=pocket_saves) 

 [[必读] LLM 应用开发全栈指南 - 知乎](https://zhuanlan.zhihu.com/p/629589593?utm_id=0&utm_oi=28589894402048&utm_psn=1641609936437141504&utm_source=pocket_saves) 

 之前介绍过 [Full Stack Deep Learning](https://zhuanlan.zhihu.com/p/218468169) 这门课程，当之无愧是 Deep Learning 工程化产品化方面最好的课程（或许没有之一）。最近他们又顺应最近大模型领域的发展，推出了 [Full Stack LLM Bootcamp](https://link.zhihu.com/?target=https%3A//fullstackdeeplearning.com/llm-bootcamp/) 课程，同样也是非常的高质量。目前已经放出了大部分的视频，周末花了点时间快速看了一遍，记录一下相关收获，也强烈推荐从事 LLM 应用开发的同学关注学习。

## Launch an LLM App in One Hour

整个讲座的一个导论，信息量不大，先做个热身。

介绍了这波 AI 浪潮的一些背景，如大语言模型强大之处，一个模型就能搞定很多不同的任务。进而解锁了 Language User Interface 的很多可能。

回顾了下之前的 AI winter，主要原因是**期望过高，交付的产品远远无法兑现承诺**。而在当前这波浪潮中，已经有很多有价值的产品出现了，比如 ChatGPT，GitHub Copilot 等。自然引导到了基于 LLM 的应用的开发这个主题上来。

**开发 MVP 的方式**

-   先用各种 playground 或者 chat 界面来做原型。
-   利用开源框架来开发应用，优化 prompts。

Frye 举了个例子，比如先手动把 arxiv 上的 paper 摘要贴给模型，再给模型提问，就能拿到正确答案。接下来再在 notebook 里一步步把流程自动化，并加上更多的优化，如文档下载，分片，index 构建与搜索等。整个流程的确半小时就能搞定。

**部署 MVP 的方式**

-   使用云平台可以快速进行部署，不过要记得限制 API 开销。
-   使用简单的 UI，快速上线，收集用户反馈并迭代。

以他们的 discord bot app 为例，具体使用的 stack 包括：

-   模型：OpenAI
-   数据存储：MongoDB
-   向量存储：Pinecone
-   Serverless Backend：Modal
-   Discord Bot Server: AWS EC2

他提到要处理 300 多个 PDF，速度很慢。但利用像 [Modal](https://link.zhihu.com/?target=https%3A//modal.com/) 这样的云服务，可以同时启动上百个 container 来同步执行，速度一下子就快了很多。

![](https://pic1.zhimg.com/v2-50b584a8e9d3a762a00e4bfc7229018c_b.jpg)

一键并发载入 pdf

Twitter 上也有个类似的帖子讨论 [当下热门的 LLM 开发 stack 构成](https://link.zhihu.com/?target=https%3A//twitter.com/ompemi/status/1653032136193060865)，评论区也有很多信息可供参考。

## LLM Foundations

### 技术原理

前面介绍机器学习、深度学习的基础，transformer，embedding 等原理，model hub 等就不展开了，应该大多数同学都了解。作为一名 “老机器学习工程师”，看这段都有点恍如隔世的感觉 如果对于动手实现 transformer 有兴趣，推荐可以看下 Karpathy 的这个 [手把手实现 GPT 的教学视频](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1E14y1M75n/)。

作者也提到了为何 transformer 为何如此有效的一些想法，例如：

-   表达能力很强，feed forward + attention 的海量参数。
-   可优化，通过反向传播算法，而且相比 RNN 这类更容易优化一些？
-   高效，可以**有效地扩展利用并行计算资源**。这一点非常重要，也是 OpenAI 当年选择 transformer 的一个主要原因。

[大语言模型中的参数都用在哪了](https://link.zhihu.com/?target=https%3A//aizi.substack.com/p/how-does-gpt-3-spend-its-175b-parameters)？可以看到在百亿参数量以上，差不多三分之二的参数实际上是 FFN 参数，剩下的基本都是 attention 参数。所以虽然论文名叫 attention is all you need，但实际上 FFN 仍然起到了很重要的作用。

另外也提到了一篇来自 Anthropic 的文章 [In-context Learning and Induction Heads](https://link.zhihu.com/?target=https%3A//transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)，深入探索了大语言模型 in-context learning 能力的来源。从对 in-context learning 能力的定义，特定的评估方法，再到对各种规格的模型训练过程的细致观察与各种干预实验都非常有意思，很值得一读。

![](https://pic4.zhimg.com/v2-db6659696afa0f777621094f5776409b_b.jpg)

Induction Heads

### LLM 走马观花

作者依次介绍了一些值得一提的大语言模型，个人感觉当前应用 LLM 的热点主要在 prompting，而训练 LLM 最重要的可能就是**高质量数据集的构建**了。所以在回看这些模型论文时，可以更多关注一下他们使用了什么样的数据集，以及如何进行清洗和处理。

**BERT**

Pre-train + fine tune 的任务设计，强大的模型效果，也是当年在 NLP 界引起巨大轰动的一个模型。不过 BERT 是 encoder only 架构，从后续发展来看可能是 “刷分” 导向带歪了路。

**T5**

Encoder + decoder 架构。把各种 NLP 任务都统一成 text to text 的转换是一大创新。

**GPT/GPT-2**

Decoder only 的架构引领了现在的潮流，但在当初的影响力并不大。他们使用的 Byte Pair Encoding 值得关注，在使用词典和 UTF-8 字节码之间找到一个平衡。

![](https://pic4.zhimg.com/v2-0a4e240dfb4badd095f71230df3ea257_b.jpg)

Byte Pair Encoding

**GPT-3**

体现出了强大的 few-shot 和 zero-shot learning 能力，引领了 prompt engineering 风潮。另外有意思的是他们准备了 500B token 的训练数据，但实际只训练了 300B 就停止了。也就是**所有训练数据模型只看了一次**，跟他们分享中提到的 “无损压缩” 的思路一致。

![](https://pic3.zhimg.com/v2-21f3c9652a72bfb449e399a85f096b5e_b.jpg)

GPT-3 的训练数据

**Chinchilla**

探索了 scaling law，用 70B 参数加上**更多的训练数据**达到了 280B Gopher 模型的同等效果。

**LLaMA**

Chinchilla-optimal 模型，开源发布但不允许商用。最近的 RedPajama 项目中尝试 “复现” 了 [LLaMA 的训练数据集](https://link.zhihu.com/?target=https%3A//www.together.xyz/blog/redpajama)，可以说是功德无量了。

在这个讲座里还引用了很多 [Yao Fu 大佬的文章](https://link.zhihu.com/?target=https%3A//yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1) 内容，包括为何要在训练中包括代码数据，GPT 模型家族谱系图，alignment tax 等。

时下流行的 LLM 大多数也都在 pre-train 阶段之后做了 instruction fine tuning 以及 RLHF。作者也介绍了一下很多开源模型采用的 GPT 生成 instruction following 数据的方案，以及 23 年 4 月发布的 [Open Assistant 数据集](https://link.zhihu.com/?target=https%3A//huggingface.co/datasets/OpenAssistant/oasst1)。对于 RLHF，个人也额外推荐两个最近看过的资料，一个是 [John Schulman 分享的通过 RL 来实现 Truthfulness](https://link.zhihu.com/?target=https%3A//www.youtube.com/watch%3Fv%3DhhiLw5Q_UFg)，个人感觉还是比较能体现 RL 相对于 SFT 的优势的。另一个是 [Anthropic 的 Constitutional AI](https://link.zhihu.com/?target=https%3A//www.anthropic.com/index/claudes-constitution)，展现了或许可以不借助人工反馈也能实现价值观对齐。

![](https://pic4.zhimg.com/v2-bf874c83554cefe704100f1ed352ab1f_b.jpg)

Constitutional AI

### 训练与推理

如果看课程 ppt，可以看到最后还有一块讲大模型训练与推理方面的内容。其中提到了 [OPT 训练的血泪史](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2205.01068.pdf)，[模型 inference 优化的手段](https://link.zhihu.com/?target=https%3A//lilianweng.github.io/posts/2023-01-10-inference-optimization/) 等。不过对于应用开发话题来说的确目前这些可能都用不太上。

## Learn to Spell: Prompt Engineering

### Prompt 是一种魔法咒语

终于来到魔法学堂的主要课程了！Frye 把 prompt 魔法分成了三类，并使用一些比喻来让大家更好理解。

当应用于 pre-train 模型时，prompt 像是《瞬息全宇宙》中的传送器，能让模型瞬间拥有某个平行宇宙中的特殊能力。更多的 prompt 内容会更多限定模型后续输出的空间，从而达到了一种让模型进入到不同模式来实现不同任务的效果。

当应用于 instruction-tuned 模型时，prompt 就像对着阿拉丁神灯许愿。许愿的内容自然也是越精确清晰越好。作者引用了来自 [Reframing Instructional Prompts to GPTk’s Language](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2109.07830.pdf) 这篇文章中的一些建议：

-   使用**非常细节具体的 pattern 示例**，而不是需要背景知识的术语。比如 “复杂的”，“专业的” 这种形容就不如直接给一些具体句式效果更好。
-   将描述**通过 bullet point 的形式**逐项说明，如果放在一个长句里，模型很容易忽略后面的部分。如果有否定语句，转换成断言的形式。
-   尽可能将一个任务分解成多个简单的任务。这个分而治之的技巧在很多地方都有被提到。
-   添加明确的对于输出的约束条件说明。比如 ReAct，AutoGPT 中都对于模型的输出形式做了很具体的限定。
-   给出具体的指令。比如不要泛泛地说回答以下问题，而是根据你需要的输出，给出具体操作的建议。

还有一个比较有意思的思考原则是，当前很多模型在做 instruction tuning 时所采用的数据都是人工打标的，所以你可以想象着**在给一个新上手的打标人员描述你所需要完成的任务**，就能得到一个效果不错的 prompt。

![](https://pic4.zhimg.com/v2-d2874e2654419f76e48e8bbcc6ae1ba3_b.jpg)

可以把模型当作一个新手标记员

而在时下火热的 LLM agent 方向上，prompt 就像是能够创建一个有生命的机器人。最常见的例子是网上很多 prompt 的例子都有种让 LLM 做 “角色扮演” 的感觉。作者对于这种角色扮演所产出的效果质量给出了一个很好的总结：

![](https://pic1.zhimg.com/v2-2f5150a38f150889b20796bba4d7b250_b.jpg)

LLM 角色扮演的效果

对于那些没法很好 “模仿” 的场景，我们需要通过例如 chain-of-thought 提示，调用外部工具等方式来提升效果。

### Prompt 技术

Frye 表示，few-shot learning 很多时候可能并不是一个好主意。举了几篇论文中的例子：

-   [Prompt Programming for Large Language Models](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2102.07350) 中，设计良好的 zero-shot prompt 表现与 few-shot 相比同样出色。
-   [Rethinking the Role of Demonstrations](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2202.12837) 和 [Larger language models do in-context learning differently](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2303.03846) 中都尝试了将 few-shot 的例子 label 进行转换，但模型仍然主要按照其固有知识来做回答。所以模型可能只是学了任务形式，并没有把注意力放在 label 的具体信息上进行 “学习”。

前面提到了 GPT 的 BPE tokenization 方式也值得注意，模型可能因此不擅长做单词倒着拼写这类任务。一个 workaround 是在这种任务中**给每个字母前后加上空格，就会识别为单个 token**。包括在教 GPT 做长数字的加法时这个方法也有奇效

一些常见模式：

-   给出 “结构化” 的文本给模型操作。比如在 ReAct 中看到的 thought，action，action input，observation 这种固定结构的演示。
-   [Decomposed Prompting](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2210.02406) 等方法来拆解复杂任务，以及像 [self-ask](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2210.03350)，[ReAct](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2210.03629) 那样自动化这个过程。
-   [Chain-of-Thought prompting](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2201.11903)，[let's think step-by-step](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2205.11916)。这个应该已经人尽皆知了。
-   [Self-criticism](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2303.17491)，让模型不断自我审视与修正回答。
-   [Self-consistency](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2203.11171)，通过略微不同的 prompt 以及稍高一点的 temperature 设定，让模型多生成几个回答，最后投票来选择最终的回答。通过这种方式也能大大提升准确率。

![](https://pic2.zhimg.com/v2-c253d1ac93bbbb6b5e4964b650f0424d_b.jpg)

Self-consistency

这些模式还可以组合起来使用，以达到更好的效果。最后作者也总结了一下这些方法在速度和开销上的一些 trade-off 考量。

![](https://pic4.zhimg.com/v2-443f02c1af178c69bfa9aada09f96463_b.jpg)

Prompt 模式 trade-off

### 其它

在 ppt 的最后一部分，作者还讨论了一下当前的 LLM 是否拥有 theory of mind，感兴趣的同学可以阅读一下。

另外关于 prompt engineering 还有很多非常好的学习资料：

-   [OpenAI Cookbook](https://link.zhihu.com/?target=https%3A//github.com/openai/openai-cookbook)
-   [LangChain AI Handbook](https://link.zhihu.com/?target=https%3A//www.pinecone.io/learn/langchain/)
-   [Learn Prompting](https://link.zhihu.com/?target=https%3A//learnprompting.org/docs/intro)
-   [Prompt Engineering Guide](https://link.zhihu.com/?target=https%3A//github.com/dair-ai/Prompt-Engineering-Guide)
-   [Lilian Weng's blog](https://link.zhihu.com/?target=https%3A//lilianweng.github.io/posts/2023-03-15-prompt-engineering/)

## Augment Language Models

作者提出了一个很有意思的观点，**LLM 擅长于一般的语言理解与推理，而不是某个具体的知识点**。所以 OpenAI 也一直没有急着把 21 年以后的数据扔进去训练个 up to date 的 ChatGPT。

所以一个很自然的想法就是通过各种手段来 “增强”LLM，典型的方法包括信息获取，LLM Chains（通过 LLM 调用来增强 context），以及各类外部工具的使用。一眼看过去这不就是 LangChain 提供的核心功能嘛。

### Retrieval

常见的各类基于 LLM 做问答的应用都结合了 information retrieval 的方式来构建 context，从而让 LLM 能够很好地根据特定信息作出回答。作者很贴心地给大家做了下这块的科普，包括倒排索引，BM25 等经典方法。当然 AI 领域用的最多的还是基于 embedding 的 “语义搜索”。

Embedding 的技术原理大家应该都挺熟悉了。在具体选择 embedding 模型时，可以参考 [mteb 的 leaderboard](https://link.zhihu.com/?target=https%3A//huggingface.co/spaces/mteb/leaderboard)。其中 [sentence-transformers](https://link.zhihu.com/?target=https%3A//www.sbert.net/) 是一个非常不错的 baseline，使用也很方便。大多数情况下大家应该都是直接使用 OpenAI 的`text-embedding-ada-002`，效果好，便宜，直接一个 API 调用搞定。另外榜单上的第一名 [Instructor](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2212.09741) 也值得关注，其思想有点像经过 instruction tuning 的 embedding 模型。

![](https://pic1.zhimg.com/v2-a3d1ae37921e61676d985e88b9404610_b.jpg)

Instructor 模型

有了 embedding 模型之后，在做问答时的方式就是把 query 转换成向量，然后在文档向量库中做相似度搜索。在文档数量不超过百万量级时，其实**简单的 numpy 计算相似度来做搜索就足够用了**，不会跟那些近似搜索算法有多少体感上的差距。如果考虑到 LLM 本身调用的时间开销，这点差距可能就更不值一提了。

![](https://pic3.zhimg.com/v2-7e78bec238963110fa75789261c3b1ce_b.jpg)

numpy vs. hnsw

作者的建议是在做原型时直接用 numpy 就行，如果未来上生产环境，那么 IR 系统的选择会更加重要。比如选择一个整体的数据库解决方案，而不是重点考虑具体的 ANN 算法。

在数据库的选择上，作者也是非常的 practical，**直接选你现在用的数据库大概率就可以**，比如 pgvector，elasticsearch，redis 之类。看了下 LangChain 里的 vectorstores，这些也都已经支持了。

不过呢，一些复杂场景下，embedding 这块也是有不少挑战的，例如：

-   数据库本身的可扩展性和可靠性，以及如果引入向量数据库怎么保持多个系统之间的一致性
-   文档比较长怎么做 split
-   应该选择什么 embedding 方法，是否可以切换
-   是否能在相似度搜索基础上支持 metadata 条件查询
-   是否支持多种类型的用户 query，例如关键词搜索，文档总结，多个文档之间的对比等
-   是否能支持复杂的 index 结构，例如有层级关系的 index

为了解决这些问题，你可能需要考虑上个向量数据库，作者也给出了一个很贴心的对比图：

![](https://pic1.zhimg.com/v2-17a612baaabe07dc112edda885523ec8_b.jpg)

向量数据库对比

总结来说如果想快速验证，Pinecone 是个不错的选择。如果想拥有更灵活的查询方式，可以考虑 Vespa 或 Weaviate，如果需要更好的 scalability/reliability，那么经过大客户验证的 Vespa 或 Milvus 可能是不错的选择。

如果玩过 retrieval + LLM 组合的应用的同学，可能会碰到一些问题导致召回质量不理想，例如：

-   用户的问题往往很短且形式多样
-   而相应的文档很长
-   embedding 模型并不是在你的任务上训练的

针对这些问题，可以考虑自己 train embedding 模型，或者基于 OpenAI embedding 基础上 train 一个简单的转换模型。另外像 LangChain，LlamaIndex 项目里也有很多方案可以尝试，例如 [HyDE](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2212.10496)，[re-ranking](https://link.zhihu.com/?target=https%3A//blog.reachsumit.com/posts/2023/03/llm-for-text-ranking/)，以及各种复杂的 tree/keyword table index，query transformer，route retriever，compact and refine synthesize 等技术。如果对于这些细节内容感兴趣，也可以看一下我之前 [关于 LlamaIndex 的简单分享](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1Yk4y1L7Vh/)。

这部分的最后是个 case study，介绍了 GitHub Copilot 如何通过 retrieval 来增强 context。主要依据来自于 [这篇对 Copilot plugin 的逆向工程](https://link.zhihu.com/?target=https%3A//thakkarparth007.github.io/copilot-explorer/posts/copilot-internals)。具体做法是：

-   召回：编辑器中最近访问的 20 个同类型文件。可以看到有时候规则可能也足够了。
-   后处理：当前光标前后的代码片段，以及从前面召回中通过相似度搜索最相近的文件片段。
-   排序：通过一些规则来对这些信息排序，最后会根据 context size 限制按排序选取尽可能多的内容。

最后作者也展示了下目前最为广泛应用的 QA 场景中具体是如何结合 retrieval 的，也提到了通过不断 refine 的模式来突破 context size 限制，覆盖更多文档内容的方法。

![](https://pic3.zhimg.com/v2-23a0c185b37ee4de6638a38fa1b6bf92_b.jpg)

Retrieval 应用与问答场景

### Chains

从上一个话题自然延伸，有时候**最好的 context 信息并不直接存在于各种外部文档中，而是需要另一个 LLM 的输出来进行构建**。比如前面提到的 HyDE，就是先通过 LLM 来不依赖外部信息回答问题，然后再将回答内容和问题拿去做 embedding，相似度搜索，形成最终的 QA prompt。另外像 summary 场景中 “map-reduce” 的做法应该大家也都很熟悉了。

针对 Chain 这方面需求最典型的开源框架就是 LangChain 了，是一个超级火热更新速度超快的库。不过这部分的课程并没有展开介绍细节，感兴趣的同学也可以参考我之前的这个 [分享视频](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/BV1DY4y1Q7Te/)。

### Tools

很多人觉得 LLM 距离 AGI 的一大差距是没法与真实世界连接，但其实已经有很多工作（例如 Toolformer 等）在尝试让 LLM 自主使用外部工具了。作者以 SQL 工具为例展示了下 LLM 如何来利用外部工具。大致为以下几个步骤：

-   用户问了一个问题
-   将用户问题和数据库的 meta 信息放到 prompt 里，让 LLM 去生成 SQL
-   利用数据库来执行这个 SQL 查询，这就是工具的调用
-   将数据库查询结果与问题再扔给 LLM 做最终回答

当然这个步骤可以说是由 Chain 定义固定下来的，也可以采用类似 agent/plugin 的方式来让 LLM 自行决定在何时使用什么工具。用户只需要提供 API 的 spec 和描述，就可以快速接入到 plugin 体系中。

这两种方式主要的权衡在于**可靠性或者是流程的确定程度**。Chain 的运作流程是人工定义好的，流程不会出错，且对 LLM 来说生成具体的工具指令也会准确率更高。而 plugin 的优势在于极大的流程灵活度，可以用统一入口满足用户各类诉求。虽然可靠性会下降不少，但也可以考虑引入人工交互来弥补。

![](https://pic4.zhimg.com/v2-f93bab761db292049d1a80d9a6d07537_b.jpg)

两种应用工具的模式

最后还有一篇 [关于 augmented 语言模型的 survey 文章](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2302.07842) 可供参考学习。

## Project Walkthrough

带着大家过了一下 [askFSDL](https://link.zhihu.com/?target=https%3A//github.com/the-full-stack/ask-fsdl) 这个项目，live coding 的感觉很爽。

对于算法工程师来说，能学到不少 Python 工程方面的最佳实践，比如 pre-commit，makefile，用 [gradio](https://link.zhihu.com/?target=https%3A//gradio.app/) 来写简单的界面，通过 modal 来管理 infra 等。

对于软件工程师来说，可能数据接入这块之前接触的并不多，可以学习一下如何接入 markdown，PDF，Youtube transcript 等类型的文件，并尽可能多地保留原始信息。还有包括通过 [gantry](https://link.zhihu.com/?target=https%3A//gantry.io/) 来收集用户行为与反馈数据，并借助 LLM 来进行分析的方法应该也挺有启发。

## UX for Language User Interface

### UI Principles

开头介绍了 user interface 的历史，以及一些设计原则。其中提到的诸如**同理心，找真实用户进行测试**个人还是很有感触的。对这方面感兴趣的同学还可以参考我之前的这篇 [如何打造产品](https://zhuanlan.zhihu.com/p/574184394)。要知道 Sam Altman 最出名的可能就是他对于 PMF 的深刻理解了

具体到 AI 产品上，我们可以将 AI 能力以及决策错误的后果作为两个维度来进行分析：

![](https://pic2.zhimg.com/v2-9afa76a60cc4400f4477d90081dd993d_b.jpg)

不同情况下 AI 与用户的协作关系

设计良好的交互，不光能让用户用得更爽，还能很自然地收集到很多用户反馈信息，建立起**数据飞轮**。例如在 Midjourney 中，用户必须通过明确的点击来选定四个备选图像中的一张做 variation 或者 upscale 并下载。

### LUI Patterns

当前 Language User Interface 的几种常见 pattern 包括：

-   Click-to-complete，例如 OpenAI Playground。
-   Auto-complete，例如 GitHub Copilot。
-   Command palette，例如 Replit。
-   One-on-one chat，例如 ChatGPT。

作者进而提出一个框架来分析这几类 pattern 对于产品的要求，包括了几个角度。我们以 GitHub Copilot 为例来看下具体分析。

-   UI 的边界是什么。这一点 Copilot 非常自然，直接在 IDE 里提供补全，用户不需要做任何切换动作。
-   对于准确率的要求有多高。相对来说不高，因为用户完全可以不理会建议，或者接受后再做少量修改。
-   对于延迟要求有多高。要求比较高，大多数用户对于自动补全的习惯性期待肯定得在 1 秒以内。
-   是否鼓励用户给出反馈。这一点也比较好，如果用户接受了建议，是一个很强烈的反馈信号。

大家也可以用这个框架来审视一下自己的应用。尤其是第四点**如何鼓励用户给出反馈**，还是挺需要好好思考一下的。除了前面提到的 Midjourney 外，像 ChatGPT 里 regenerate response 和后面带的问题这种形式也很好，用户体验很流畅，同时又能拿到信号非常强烈的反馈。

![](https://pic3.zhimg.com/v2-be4c407d82d4f5a40e3321f5e66fc16a_b.jpg)

ChatGPT UI 中的设计亮点

### Case Studies

接下来一部分的 case study 个人感觉非常精彩，分享了对于 GitHub Copilot 和 Bing Chat 两个产品用户交互方面的分析。

**GitHub Copilot**

在训练了代码生成模型后，他们一开始在很多可能的产品方向进行了分析与探索，包括：

![](https://pic1.zhimg.com/v2-7299eec84c9ad9e9537f285e8d652ed8_b.jpg)

尝试各种 idea

很快他们就发现，当前的模型效果只能很好地支持 auto-complete 产品，而无法支持前两者。

选定方向后，他们针对用户界面和体验方面做了很多 ab 测试，主要依据的指标是用户对于代码提示的接受率以及 30 天后的用户留存率。获取到了很多有价值的信息，最终打造出了一款用户喜爱且能产生很多实际价值的产品。

**Bing Chat**

Bing Chat 相对来说在用户体验方面的考量就没有那么全面，更像是为了抢占市场而急忙推出的一个产品。网上也持续有关于 Bing Chat 出问题的各种负面反馈出现，例如回答不友好，会出现胡言乱语，没法理解用户意图，“泄漏”prompt，甚至出现威胁用户等。作者认为他们可能犯了几个错误：

-   急于推出产品，底层的模型可能没有经过 RLHF 做 alignment，导致了很多网上出现的很多有问题的回复案例。
-   没有注意到**潜在的反馈循环**。跟 ChatGPT 相比，Bing Chat 是 “联网” 的，所以每当它产生一些奇怪回复后，用户会贴到网上，然后搜索引擎又会很快索引这些信息，反过来不断增强出现这些奇怪回复的可能性。
-   **用户界面的 “引导” 与产品实际提供的能力不符**。很多做 AI 应用的同学可能都觉得为了让产品更酷炫，应该尽可能让交互界面像真人。比如生成一个真人头像，利用 D-ID，ElevenLabs 等技术让它能够像真人一样用非常流畅自然的语音回答。但是这会让用户的期望值拉得非常高，如果你的模型不能够达到真人交互的水平，那么用户的失望感就会非常强烈。

![](https://pic2.zhimg.com/v2-6496750b2087ad4c908aeb5cc2e37aad_b.jpg)

LUI 应该强调自己是个机器人

## LLMOps

这一节也非常有信息量，推荐观看。

### 选择基础模型

从几个维度来考虑选择哪个模型，包括**模型的效果，推理速度，价格开销，能否微调，数据安全，许可协议**等。

就 23 年 5 月这个时间节点来说，对于私有模型的建议：

-   绝大多数情况都可以直接选择 GPT-4 作为尝试的开始。后续如果有成本和速度的考量可以再切换到 GPT-3.5。
-   Claude 也是个不错的选择，无论是模型效果还是训练的完善程度上，再加上现在支持了超大的 context size，赶忙去申请了 wait-list。
-   如果需要做 fine tune，也可以考虑 Cohere 的 command 系列。

![](https://pic4.zhimg.com/v2-d64a8dd05af98f6fc3c6004bf01c2617_b.jpg)

私有模型对比一览

开源模型这块发展很快，最近几周都有新模型出来。这块的许可协议也很复杂，例如有些模型的不同版本因为用了特殊的数据就导致无法作为商业用途。在讲座的时间节点，作者的几个推荐是：

-   如果希望完全开放的使用，T5/Flan-T5 是个不错的选择，效果也还行。
-   开源可商用这块可以考虑最近的 Dolly，StableLM。
-   如果用于研究用途，LLaMA 系列是目前比较主流的。如果对于 2020 年的 GPT-3 复现与实验感兴趣，可以用 OPT。
-   其它基本不太用考虑，包括表上的 Bloom 和 GLM。不过这个表的更新迭代速度应该会很快。

![](https://pic1.zhimg.com/v2-03fd35ca0cbffe47d6c40cdd80e24bc8_b.jpg)

开源模型对比一览

总体来说在当前私有模型的能力大大超过了开源模型，对于应用开发来说估计 23 年的主流都是使用私有模型。

### Prompt 迭代开发

传统深度学习里对于实验追踪与记录有着非常完善的支持，但目前的 prompt 开发与迭代还在很早期的阶段，主要还是因为不同 prompt 产生的效果并不好自动化评估。

因此现阶段比较常见的做法就是通过 git 来管理 prompt 版本。如果有更复杂的需求，例如希望把 prompt 的应用逻辑解耦，或者引入业务人员来优化 prompt，以及通过单独的产品工具来快速评估管理不同的 prompt 甚至模型接口，那么就需要引入更加复杂的产品。这方面可以持续关注之前的 experiment tracking 产品，包括 WandB，MLFlow 等。

### 测试

LLM 的能力非常强大，能处理各种任务，这对其评估造成了很大的困难，比如我们很难判断一篇总结是否比另外一篇总结写得更好。对于不同的 prompt，模型甚至 fine tune 的效果，如何进行快速，低成本且准确的评估是一个大问题。目前的常见做法是：

-   构建一个针对你所需要完成任务的评估数据集，一开始可以完全人工生成，后续逐渐完善。
-   除了通过人工检验的方式，也可以**借助 LLM 来做评估**。可以参考 [auto-evaluator](https://link.zhihu.com/?target=https%3A//github.com/langchain-ai/auto-evaluator) 项目。
-   在添加新的评估数据时，需要考虑这条样本带来的 “额外价值”，比如是否是一个比较困难的问题，以及与已有评估数据是不是非常不一样。
-   思考 “AI 测试覆盖率”，你收集的评估数据集能多大程度上覆盖生产环境的所有情况？

通过 LLM 来做评估的具体方法包括：

-   如果有完全精确的答案判定，可以用传统指标，不需要借助 LLM。
-   如果你有标准答案，可以测试语义相似度，或者询问 LLM：两个回答是否一致？
-   如果有上一个版本的回答，可以询问 LLM：哪一个回答更好？
-   如果有用户填写的反馈信息，可以询问 LLM：用户的反馈是否已经包含在回答中了？
-   其它情况，可以通过外部工具来检查是否是个合法的格式，或者让 LLM 给回答做个打分。

![](https://pic4.zhimg.com/v2-11b8eebad9d57c9b1fd218373c01266f_b.jpg)

LLM 模型评估

### 部署

简单的应用可以直接从前端发起模型请求即可。如果业务逻辑复杂，再考虑单独开发个后端服务。这个示范 stack 也在前面有提到。

私有化部署 LLM 不在本课程讨论范围内……

一些提升 LLM 输出稳定性的手段：

-   Self-critique
-   多采样几次，选最好的那次
-   多采样几次，投票

可以参考这个比较新的 [guardrails](https://link.zhihu.com/?target=https%3A//github.com/ShreyaR/guardrails) 项目。

### 监控

这里应该也是一些标准做法了，可以结合前面的 UX 设计，主要思考如何系统性地获取并持续监控用户反馈。越是对用户来说没有什么负担的操作，越是信息含量高的操作，对于实际的业务监控越有效。

一些常见的可能出问题的点：

-   UI 问题，延迟太大。这也是出现最多的一类。
-   错误的回答，hallucinations。
-   冗长无用的回答。
-   拒绝回答。
-   Prompt injection。
-   违背价值观的回答。

### 持续优化与 fine tune

如果监控或者收集到上述问题的用户反馈，后续可以通过 prompt 优化或者 fine tune 的手段来持续改进。一般来说**优先选择前者**，尤其是当前开源模型，fine tune 技术都没有那么成熟的情况下。Slides 上有一些 fine tune 相关的内容介绍，不过作者认为当前应该多数情况下不需要，就跳过了 什么时候需要 fine tune 呢？

-   你需要节省成本，比如用更小的模型，不想每次都带一大段 prompt 之类。
-   你有大量的数据，且 retrieval 的方法表现不够理想。

大家如果有成功应用 fine tune 模式的例子，也欢迎交流分享。

![](https://pic4.zhimg.com/v2-138f578cc5f3b7286456bd2cc7366257_b.jpg)

LLM 应用迭代优化流程

## What's Next

最后一个 session，展望一下未来，也是笑点最多的一集。

### 大模型的下一步发展方向

作者认为一个很有希望的领域是多模态与机器人的结合。介绍了包括 ViT，PaLM-E，[MiniGPT-4](https://link.zhihu.com/?target=https%3A//github.com/Vision-CAIR/MiniGPT-4)，以及将 LLM 应用工具的思想拓展到机器人领域等工作。

### 大模型如何继续 scale

**Transformer 就是终极架构吗？**

之前看 RNN 相对来说很容易达到性能瓶颈，而且不能有效利用并行计算资源。不过看起来 [RWKV](https://link.zhihu.com/?target=https%3A//github.com/BlinkDL/RWKV-LM) 可能会是 RNN 的 “逆袭” 机会？

**钱，算力，数据哪个会成为大模型继续 scale 的瓶颈？**

总体来说最有可能成为瓶颈的是数据。比如 [Will we run out of data?](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2211.04325) 这篇文章认为我们在 2026 年之前就会碰到高质量数据增长跟不上算力提升的速度。而如果从 Chinchilla 论文中的 [scaling law 公式](https://link.zhihu.com/?target=https%3A//www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications) 来推算，在特定数据量下即使是**无限的参数量**都没法打败拥有更多数据量训练出来的有限参数量的模型。

![](https://pic3.zhimg.com/v2-71ed6b62ee977ad4aca5f644b698af96_b.jpg)

通过 scaling law 推算无限参数 / 数据情况下的模型性能

**小模型能够走多远？**

因为 retrieval 模式非常有效，所以大家自然会有想法说是不是不需要那么大的模型来记住各种知识点，而只需要一个**拥有推理能力的小模型**就可以？另外像 Alpaca 这些从 ChatGPT“蒸馏” 训练的方式目前看起来在简单场景上还挺有效的。小模型可以在手机端，机器人设备上直接部署使用，想象空间还是非常大的。

### AGI 已经到来了吗？

作者觉得有可能已经到了，只是我们还没有认识到。一些论点：

-   现有模型能做什么，还需要我们花很多时间去挖掘。一个很有名的例子是一开始以为 LLM 不能做推理，但后来发现加一个 let's think step by step 就把准确率从 17.7% 提升到了 78.7%。还有多少这样的现象是我们还没发现的？
-   模型已经可以自己探索和发现自己的能力了。比如在 [Large Language Models Are Human-Level Prompt Engineers](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2211.01910) 中，作者发现模型可以自己设计 prompt，甚至超过人类水平。
-   模型可能已经可以做到自我提升了。比如 Anthropic 的 Constitutional AI，再比如让模型自己学会写代码和 debug，是不是未来也可能自己写 GPT-X 的训练优化代码自己提升？还有像 AutoGPT，BabyAGI 这些赋予 agent 使用工具和长期记忆能力的尝试，也是一个可能的方向。

作者认为可以把 GPT-4 理解为一种新的 CPU，它的 context 相当于内存。我们现在的 prompt 还处在一个很原始的应用这种新型计算机的阶段（接近机器码？），还远没有出现更高阶的智能计算编程语言与框架。

![](https://pic3.zhimg.com/v2-a652ac90357c3218cfb807a36cf7533e_b.jpg)

GPT 是认知计算机的 CPU

### 安全问题

前面也看到了很多关于大模型应用的安全问题，包括 prompt 注入，“越狱” 让模型做一些原本不应该做的事情，连接上工具之后影响与操控真实世界。这一节也举了非常多的例子。

具体怎么做呢？这个应该也是各人都有不同的看法。或许 OpenAI 的逐渐发布更强大的模型让大家适应，同时密切关注安全，价值观对其等技术手段，并持续监控模型失控的信号算是目前看起来比较合理的方案。

最后一页 PPT 也是非常幽默，作为整个系列讲座的结尾送给大家。

![](https://pic3.zhimg.com/v2-8ef97853d02ea3050cc568d11f6aea8e_b.jpg)

想起 Dr. Strangelove
