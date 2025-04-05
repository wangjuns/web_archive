# 英伟达在机器学习中的 CUDA 垄断如何破裂 - OpenAI Triton 和 PyTorch 2.0 --- How Nvidia’s CUDA Monopoly In Machine Learning Is Breaking - OpenAI Triton And PyTorch 2.0
[英伟达在机器学习中的 CUDA 垄断如何破裂 - OpenAI Triton 和 PyTorch 2.0 --- How Nvidia’s CUDA Monopoly In Machine Learning Is Breaking - OpenAI Triton And PyTorch 2.0](https://www.semianalysis.com/p/nvidiaopenaitritonpytorch) 

 Over the last decade, the landscape of machine learning software development has undergone significant changes. Many frameworks have come and gone, but most have relied heavily on leveraging Nvidia's CUDA and performed best on Nvidia GPUs. However, with the arrival of PyTorch 2.0 and OpenAI's Triton, Nvidia's dominant position in this field, mainly due to its software moat, is being disrupted.  
在过去十年中，机器学习软件开发的格局发生了重大变化。许多框架出现又消失，但大多数都严重依赖于 Nvidia 的 CUDA，并在 Nvidia 的 GPU 上表现最佳。然而，随着 PyTorch 2.0 和 OpenAI 的 Triton 的到来，Nvidia 在这一领域的主导地位，主要由于其软件护城河，正受到冲击。

This report will touch on topics such as why Google’s TensorFlow lost out to PyTorch, why Google hasn’t been able to capitalize publicly on its early leadership of AI, the major components of machine learning model training time, the memory capacity/bandwidth/cost wall, model optimization, why other AI hardware companies haven’t been able to make a dent in Nvidia’s dominance so far, why hardware will start to matter more, how Nvidia’s competitive advantage in CUDA is wiped away, and a major win one of Nvidia’s competitors has at a large cloud for training silicon.  
本报告将涉及以下主题：为什么谷歌的 TensorFlow 输给了 PyTorch，为什么谷歌未能在公众面前利用其在人工智能领域的早期领导地位，机器学习模型训练时间的主要组成部分，内存容量/带宽/成本壁垒，模型优化，为什么其他人工智能硬件公司迄今未能对英伟达的主导地位造成影响，为什么硬件将变得更加重要，英伟达在 CUDA 方面的竞争优势如何被消除，以及英伟达的一家竞争对手在大型云计算平台上获得的一个重大胜利，用于训练硅芯片。

The 1,000-foot summary is that the default software stack for machine learning models will no longer be Nvidia’s closed-source CUDA. The ball was in Nvidia’s court, and they let OpenAI and Meta take control of the software stack. That ecosystem built its own tools because of Nvidia’s failure with their proprietary tools, and now Nvidia’s moat will be permanently weakened.  
1000 英尺的总结是，机器学习模型的默认软件堆栈将不再是 Nvidia 的闭源 CUDA。球在 Nvidia 的场上，但他们让 OpenAI 和 Meta 掌控了软件堆栈。由于 Nvidia 在其专有工具上的失败，该生态系统构建了自己的工具，现在 Nvidia 的护城河将永久削弱。

A handful of years ago, the framework ecosystem was quite fragmented, but TensorFlow was the frontrunner. Google looked poised to control the machine learning industry. They had a first movers’ advantage with the most commonly used framework, TensorFlow, and by designing/deploying the only successful AI application-specific accelerator, TPU.  
几年前，框架生态系统相当分散，但 TensorFlow 是领跑者。谷歌似乎准备控制机器学习行业。他们凭借最常用的框架 TensorFlow 和设计/部署唯一成功的 AI 应用专用加速器 TPU，拥有了先发优势。

Instead, PyTorch won. Google failed to convert its first mover’s advantage into dominance of the nascent ML industry. Nowadays, Google is somewhat isolated within the machine learning community because of its lack of use of PyTorch and GPUs in favor of its own software stack and hardware. In typical Google fashion, they even have a 2nd framework called Jax that competes directly with TensorFlow.  
相反，PyTorch 胜出。谷歌未能将其先发优势转化为新兴机器学习行业的主导地位。如今，由于谷歌偏向于使用自己的软件堆栈和硬件，而不是 PyTorch 和 GPU，它在机器学习社区中显得有些孤立。按照谷歌的典型风格，他们甚至有一个名为 Jax 的第二框架，直接与 TensorFlow 竞争。

There’s even endless talk of Google’s dominance in search and natural language processing waning due to large language models, particularly those from OpenAI and the various startups that utilize OpenAI APIs or are building similar foundational models. While we believe this doom and gloom is overblown, that story is for another day. Despite these challenges, Google is still at the forefront of [the most advanced machine learning models](https://arxiv.org/abs/2212.13138). They invented transformers and remain state-of-the-art in many areas (PaLM, LaMBDA, Chinchilla, MUM, TPU).  
关于谷歌在搜索和自然语言处理领域的主导地位因大型语言模型而减弱的讨论不绝于耳，特别是来自 OpenAI 的模型以及利用 OpenAI API 或构建类似基础模型的各种初创公司。虽然我们认为这种悲观情绪被夸大了，但这个故事留待另日再说。尽管面临这些挑战，谷歌仍然处于最先进的机器学习模型的前沿。他们发明了变换器，并在许多领域保持着最先进的水平（PaLM、LaMBDA、Chinchilla、MUM、TPU）。

Back to why PyTorch won. While there was an element of wrestling control away from Google, it was primarily due to its increased flexibility and usability of PyTorch versus TensorFlow. If we boil it down to a first principal level, PyTorch differed from TensorFlow in using “**Eager mode**” rather than "**Graph Mode**."

Eager mode can be thought of as a standard scripting execution method. The deep learning framework executes each operation immediately, as it is called, line by line, like any other piece of Python code. This makes debugging and understanding your code more accessible, as you can see the results of intermediate operations and see how your model behaves.

In contrast, graph mode has two phases. The first phase is the definition of a computation graph representing the operations to perform. A computation graph is a series of interconnected nodes representing operations or variables, and the edges between nodes represent the data flow between them. The second phase is the deferred execution of an optimized version of the computation graph.

This two-phase approach makes it more challenging to understand and debug your code, as you cannot see what is happening until the end of the graph execution. This is analogous to "interpreted" vs. "compiled" languages, like python vs. C++. It's easier to debug Python, largely since it's interpreted.

While TensorFlow now has Eager mode by default, the research community and most large tech firms have settled around PyTorch. This is exemplified by the fact that nearly ever generative AI model that made the news, being based on PyTorch. The Google generative AI models are based on Jax, not TensorFlow.

Of course there is a long tail of image nets using other frameworks like TensorFlow and Keras, but the compute budgets for new model development is all flowing to PyTorch models. For a deeper explanation of why PyTorch won, see [here](https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/). In general, if you walk around the halls of NeurIPS (the main AI conference), all generative AI, the non-Google work is with PyTorch.

If we boil machine learning model training to its most simplistic form, there are two major time components in a machine learning model’s training time.

1.  Compute (FLOPS):  Running dense matrix multiplication within each layer
    
2.  Memory (Bandwidth): Waiting for data or layer weights to get to the compute resources. Common examples of bandwidth-constrained operations are various [normalizations](https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html), [pointwise operations](https://pytorch.org/docs/stable/torch.html), [SoftMax](https://pytorch.org/docs/stable/generated/torch.nn.Softmax.html), and [ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html).
    

In the past, the dominant factor in machine learning training time was compute time, waiting for matrix multiplies. As Nvidia’s GPUs continued to develop, this quickly faded away from being the primary concern.

Nvidia’s FLOPS have increased multiple orders of magnitude by leveraging Moore’s Law, but primarily architectural changes such as the tensor core and lower precision floating point formats. In contrast, [memory has not followed the same path](https://www.semianalysis.com/p/cxl-enables-microsoft-azure-to-cut).

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a422e2d-f2d2-404e-aad4-dec31f47ce77_1187x862.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3a422e2d-f2d2-404e-aad4-dec31f47ce77_1187x862.png)

If we go back to 2018, when the BERT model was state of the art, and the Nvidia V100 was the most advanced GPU, we could see that matrix multiplication was no longer the primary factor for improving a model’s performance. Since then, the most advanced models have grown 3 to 4 orders of magnitude in parameter count, and the fastest GPUs have grown an order of magnitude in FLOPS.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c718323-fd9c-4c6d-8ea3-815dea887386_1513x487.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c718323-fd9c-4c6d-8ea3-815dea887386_1513x487.png)

https://arxiv.org/pdf/2007.00072.pdf

Even in 2018, purely compute-bound workloads made up 99.8% of FLOPS but only 61% of the runtime. The normalization and pointwise ops achieve 250x less FLOPS and 700x less FLOPS than matrix multiplications, respectively, yet they consume nearly 40% of the model’s runtime.

As models continue to soar in size, large language models take 100s gigabytes, if not terabytes, for the model weights alone. Production recommendation networks deployed by Baidu and Meta require dozens of terabytes of memory for their massive embedding tables. A huge chunk of the time in large model training/inference is not spent computing matrix multiplies, but rather waiting for data to get to the compute resources. The obvious question is why don’t architects put more memory closer to the compute. The answer is $$$.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa62c2392-d588-4fdf-8872-e51ba3335250_704x513.jpeg)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa62c2392-d588-4fdf-8872-e51ba3335250_704x513.jpeg)

Memory follows a hierarchy from close and fast to slow and cheap. The nearest shared memory pool is on the same chip and is generally made of SRAM. Some machine-learning ASICs attempt to utilize huge pools of SRAM to hold model weights, but there are issues with this approach. [Even Cerebras’ ~$2,500,000 wafer scale chips](https://www.semianalysis.com/p/gpt-model-training-competition-heats) only have 40GB of SRAM on the chip. There isn’t enough memory capacity to hold the weights of a 100B+ parameter model.

Nvidia’s architecture has always used a much smaller amount of memory on the die. The current generation A100 has 40MB, and the next generation H100 has 50MB. 1GB of SRAM on TSMC’s 5nm process node would require ~200mm^2 of silicon. Once the associated control logic/fabric are implemented, that would require over 400mm^2 of silicon, or about 50% of the total logic area of an Nvidia datacenter GPU. Given that an A100 GPU costs $10k+ and the H100 is more like $20k+, economically, this is infeasible. Even when you ignore Nvidia’s ~75% gross margin on datacenter GPUs (~4x markup), the cost per GB of SRAM memory would still be in the $100s for a fully yielded product.

Furthermore, the cost of on-chip SRAM memory will not decrease much through conventional Moore’s Law process technology shrinks. The same 1GB of memory actually costs more with the next-generation TSMC 3nm process technology. While 3D SRAM will help with SRAM costs to some degree, that is only a temporary bend of the curve.

[

TSMC’s 3nm Conundrum, Does It Even Make Sense? – N3 & N3E Process Technology & Cost Detailed

A couple of weeks ago, we were able to attend IEDM, where TSMC presented many details about their N3B and N3E, 3nm class process nodes. Furthermore, TSMC announced it would up its capital expenditure in Phoenix, Arizona, with a total of $40 Billion invested in Fab 21 phases 1 and 2. This fab would produce chips in the N5 and N3 families, respectively. This report will cover the process node transition, the excessive costs of TSMC’s most advanced technology, and how it will significantly accelerate changes in the industry towards…

Read more

2 years ago · 32 likes · 3 comments · Dylan Patel and Afzal Ahmad

](https://www.semianalysis.com/p/tsmcs-3nm-conundrum-does-it-even?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

The next step down in the memory hierarchy is tightly coupled off-chip memory, DRAM. DRAM has an order magnitude higher latency than SRAM (~>100 nanoseconds vs. ~10 nanoseconds), but it’s also much cheaper ($1s a GB vs. $100s GB.)

DRAM followed the path of Moore’s Law for many decades. When Gordon Moore coined the term, Intel’s primary business was DRAM. His economic prediction about density and cost of transistors generally held true until ~2009 for DRAM. Since ~2012 though, the cost of DRAM has barely improved.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f3c7f05-649b-4f02-91be-61c84a30888f_1697x883.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f3c7f05-649b-4f02-91be-61c84a30888f_1697x883.png)

The demands for memory have only increased. DRAM now [comprises 50% of the total server’s cost](https://www.semianalysis.com/p/cxl-enables-microsoft-azure-to-cut). This is the memory wall, and it has shown up in products. Comparing Nvidia’s 2016 P100 GPU to their 2022 H100 GPU that is just starting to ship, there is a 5x increase in memory capacity (16GB -> 80GB) but a 46x increase in FP16 performance (21.2 TFLOPS -> 989.5 TFLOPS).

While capacity is a significant bottleneck, it is intimately tied to the other major bottleneck, bandwidth. Increased memory bandwidth is generally obtained through parallelism. While standard DRAM is only a few dollars per GB today, to get the massive bandwidth machine learning requires, Nvidia uses HBM memory, a device comprised of [3D stacked layers of DRAM that requires more expensive packaging.](https://www.semianalysis.com/p/advanced-packaging-part-1-pad-limited) HBM is in the $10 to $20 a GB range, including packaging and yield costs.

The cost constraints of memory bandwidth and capacity show up in Nvidia’s A100 GPUs constantly. The A100 tends to have very low FLOPS utilization without heavy optimization. FLOPS utilization measures the total computed FLOPS required to train a model vs. the theoretical FLOPS the GPUs could compute in a model’s training time.

Even with heavy optimizations from leading researchers, 60% FLOPS utilization is considered a very high utilization rate for large language model training. The rest of the time is overhead, idle time spent waiting for data from another calculation/memory, or recomputing results just in time to reduce memory bottlenecks.

From the current generation A100 to the next generation H100, the FLOPS grow by more than 6X, but memory bandwidth only grows by 1.65x. This has led to many fears of low utilization for H100. The A100 [required many tricks](https://www.mosaicml.com/composer) to get around the memory wall, and more will need to be implemented with the H100.

The H100 brings [distributed shared memory and L2 multicast to Hopper](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/). The idea is that different SMs (think cores) can write directly to another SM’s SRAM (shared memory/L1 Cache). This [effectively increases the size of the cache and reduces the required bandwidth](https://www.nvidia.com/en-us/on-demand/session/gtcfall22-a41095/) of DRAM read/writes. Future architectures will rely on sending fewer operations to memory to minimize the impact of the memory wall. It should be noted that larger models tend to achieve higher utilization rates as FLOPS demands scale more exponentially whereas memory bandwidth and capacity demands tend to scale more linearly.

> Just like with training ML models, knowing what regime you're in allows you to narrow in on optimizations that matters. For example, if you're spending all of your time doing memory transfers (i.e. you are in a memory-bandwidth bound regime), then increasing the FLOPS of your GPU won't help. On the other hand, if you're spending all of your time performing big chonky matmuls (i.e. a compute-bound regime), then rewriting your model logic into C++ to reduce overhead won't help.
> 
> [https://horace.io/brrr\_intro.html](https://horace.io/brrr_intro.html)

Referring back to why PyTorch won, it was the increased flexibility and usability due to Eager mode, but moving to Eager mode isn’t all sunshine and rainbows. When executing in Eager mode, each operation is read from memory, computed, then sent to memory before the next operation is handled. This significantly increases the memory bandwidth demands if heavy optimizations aren’t done.

As such, one of the principal optimization methods for a model executed in Eager mode is called operator fusion. Instead of writing each intermediate result to memory, operations are fused, so multiple functions are computed in one pass to minimize memory reads/writes. Operator fusion improves operator dispatch, memory bandwidth, and memory size costs.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40995db9-3a8d-4917-8943-c313807d92b9_3420x1952.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40995db9-3a8d-4917-8943-c313807d92b9_3420x1952.png)

https://horace.io/brrr\_intro.html

This optimization often involves writing custom CUDA kernels, but that is much more difficult than using simple python scripts. As a built-in compromise, PyTorch steadily implemented more and more operators over time natively within PyTorch. Many of these operators were simply multiple commonly used operations fused into a single, more complex function.

The increase in operators made both creating the model within PyTorch easier and the performance of Eager mode faster due to having fewer memory read/writes. The downside was that PyTorch ballooned to over 2,000 operators over a few years.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F437175e3-1af1-451e-941e-5715858cff16_690x862.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F437175e3-1af1-451e-941e-5715858cff16_690x862.png)

We would say software developers are lazy, but let’s be honest, almost all people are lazy. If they get used to one of the new operators within PyTorch, they will continue to use that. The developer may not even recognize the performance improvement but instead, use that operator because it means writing less code.

Additionally, not all operations can be fused. A significant amount of time is often spent deciding which operations to fuse and which operations to assign to specific compute resources at the chip and cluster levels. The strategy of which operations to fuse where, although generally similar, does vary significantly depending on the architecture.

The growth in operators and position as the default has helped Nvidia as each operator was quickly optimized for their architecture but not for any other hardware. If an AI hardware startup wanted to fully implement PyTorch, that meant supporting the growing list of 2,000 operators natively with high performance.

The talent level required to train a massive model with high FLOPS utilization on a GPU grows increasingly higher because of all the tricks needed to extract maximum performance. Eager mode execution plus operator fusion means that software, techniques, and models that are developed are pushed to fit within the ratios of compute and memory that the current generation GPU has.

Everyone developing machine learning chips is beholden to the same memory wall. ASICs are beholden to supporting the most commonly used frameworks. ASICs are beholden to the default development methodology, GPU-optimized PyTorch code with a mix of Nvidia and external libraries. An architecture that eschews a GPU’s various non-compute baggage in favor of more FLOPS and a stiffer programming model makes very little sense in this context.

**Ease of use is king.  
易用性至关重要。** 

The only way to break the vicious cycle is for the software that runs models on Nvidia GPUs to transfer seamlessly to other hardware with as little effort as possible. As model architectures stabilize and abstractions from PyTorch 2.0, OpenAI Triton, [and MLOps firms such as MosaicML](https://www.mosaicml.com/composer) become the default, the architecture and economics of the chip solution starts to become the biggest driver of the purchase rather than the ease of use afforded to it by Nvidia’s superior software.  
打破恶性循环的唯一方法是让在 Nvidia GPU 上运行模型的软件能够尽可能无缝地转移到其他硬件上。随着模型架构的稳定以及 PyTorch 2.0、OpenAI Triton 和 MLOps 公司如 MosaicML 的抽象成为默认，芯片解决方案的架构和经济性开始成为购买的最大驱动因素，而不是 Nvidia 卓越软件所带来的易用性。

The [PyTorch Foundation was established and moved out from under the wings of Meta](https://ai.facebook.com/blog/pytorch-foundation/) just a few months ago. Alongside this change to an open development and governance model, 2.0 has been released for early testing with full availability in March. PyTorch 2.0 brings many changes, but the primary difference is that it adds a compiled solution that supports a graph execution model. This shift will make properly utilizing various hardware resources much easier.  
PyTorch 基金会在几个月前成立，并脱离了 Meta 的庇护。随着这一开放开发和治理模式的变化，2.0 版本已发布进行早期测试，并将在三月全面上线。PyTorch 2.0 带来了许多变化，但主要区别在于它增加了一个支持图执行模型的编译解决方案。这一转变将使得更好地利用各种硬件资源变得更加容易。

PyTorch 2.0 brings [an 86% performance improvement](https://www.youtube.com/watch?v=ppWKVg-VxmQ) for training on Nvidia’s A100 and [26% on CPUs for inference](https://www.youtube.com/watch?v=ppWKVg-VxmQ)! This dramatically reduces the compute time and cost required for training a model. These benefits could extend to other GPUs and accelerators from [AMD](https://www.semianalysis.com/p/amd-to-infinity-and-beyond), [Intel](https://www.semianalysis.com/p/intel-is-throwing-the-kitchen-sink), [Tenstorrent](https://www.semianalysis.com/p/tenstorrent-blackhole-grendel-and), Luminous Computing, [Tesla](https://www.semianalysis.com/p/tesla-dojo-unique-packaging-and-chip), Google, [Amazon](https://www.semianalysis.com/p/amazon-graviton-3-uses-chiplets-and), Microsoft, [Marvell](https://www.semianalysis.com/p/marvelldeepdive2022), [Meta](https://www.semianalysis.com/p/meta-discusses-ai-hardware-and-co), [Graphcore](https://www.semianalysis.com/p/graphcore-announces-worlds-first?s=w), [Cerebras](https://www.semianalysis.com/p/gpt-model-training-competition-heats), SambaNova, etc.  
PyTorch 2.0 在 Nvidia 的 A100 上训练性能提升了 86%，在 CPU 上推理性能提升了 26%！这大大减少了训练模型所需的计算时间和成本。这些好处可能会扩展到来自 AMD、Intel、Tenstorrent、Luminous Computing、Tesla、Google、Amazon、Microsoft、Marvell、Meta、Graphcore、Cerebras、SambaNova 等公司的其他 GPU 和加速器。

The performance improvements from PyTorch 2.0 will be larger for currently unoptimized hardware. Meta and other firms’ heavy contribution to PyTorch stems from the fact that they want to make it easier to achieve higher FLOPS utilization with less effort on their multi-billion-dollar training clusters made of GPUs. They are also motivated to make their software stacks more portable to other hardware to introduce competition to the machine learning space.  
PyTorch 2.0 的性能提升在当前未优化的硬件上将更为显著。Meta 和其他公司的大量贡献源于他们希望在其数十亿美元的 GPU 训练集群上，以更少的努力实现更高的 FLOPS 利用率。他们还希望使其软件栈更具可移植性，以便在机器学习领域引入竞争。

PyTorch 2.0 also brings [advancements to distributed training](https://www.youtube.com/watch?v=bGo-2xNvNAc) with better API support for data parallelism, [sharding](https://pytorch.org/blog/introducing-pytorch-fully-sharded-data-parallel-api/), [pipeline parallelism](https://github.com/pytorch/tau), and tensor parallelism. In addition, it supports dynamic shapes natively through the entire stack, which among many other examples, [makes varying sequence lengths for LLMs much easier to support.](https://www.youtube.com/watch?v=rn-kJQ-7JmQ) This is the first time a major compiler supports Dynamic Shapes from training to inference.  
PyTorch 2.0 还在分布式训练方面带来了进展，提供了更好的 API 支持数据并行、分片、管道并行和张量并行。此外，它在整个堆栈中原生支持动态形状，这使得支持 LLMs 的不同序列长度变得更加容易。这是主要编译器首次从训练到推理支持动态形状。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05aab965-a207-4d01-b680-6c0fb7bdcc8a_936x656.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05aab965-a207-4d01-b680-6c0fb7bdcc8a_936x656.png)

Writing a performant backend for PyTorch that fully supports all 2,000+ operators has been difficult for every machine learning ASIC except for Nvidia GPUs. PrimTorch brings the number of operators down to ~250 primitive operators while also keeping usability unchanged for end users of PyTorch. PrimTorch makes the implementation of different, non-Nvidia backends to PyTorch much simpler and more accessible. Custom hardware and system vendors can bring up their software stacks more easily.  
为 PyTorch 编写一个高性能的后端，完全支持所有 2000 多个操作符，对除了 Nvidia GPU 以外的每个机器学习 ASIC 来说都很困难。PrimTorch 将操作符的数量减少到约 250 个原始操作符，同时保持 PyTorch 最终用户的可用性不变。PrimTorch 使得为 PyTorch 实现不同的非 Nvidia 后端变得更加简单和可访问。定制硬件和系统供应商可以更轻松地搭建他们的软件栈。

Moving to graph mode requires a robust graph definition. Meta and PyTorch have been attempting to work on implementing this for ~5 years, but every solution they came up with had significant drawbacks. They finally cracked the puzzle with TorchDynamo. TorchDynamo will ingest any PyTorch user script, including those that call outside 3rd party libraries, and generate [an FX graph](https://arxiv.org/pdf/2112.08429.pdf).  
切换到图模式需要一个强大的图定义。Meta 和 PyTorch 已经尝试实现这一点大约 5 年，但他们提出的每个解决方案都有显著的缺陷。他们最终通过 TorchDynamo 解决了这个难题。TorchDynamo 将处理任何 PyTorch 用户脚本，包括那些调用外部第三方库的脚本，并生成一个 FX 图。

Dynamo lowers all complex operations to the ~250 primitive operations in PrimTorch. Once the graph is formed, unused operations are discarded, and the graph determines which intermediate operations need to be stored or written to memory and which can potentially be fused. This dramatically reduces the overhead within a model while also being seamless for the user.

TorchDynamo already works for [over 99% of the 7,000 PyTorch models tested](https://dev-discuss.pytorch.org/t/torchdynamo-update-8-torchdynamo-passed-correctness-check-on-7k-github-models/663), including those from OpenAI, HuggingFace, Meta, Nvidia, Stability.AI, and more, **without any changes to the original code**. The 7,000 models tested were indiscriminately chosen from the most popular projects using PyTorch on GitHub.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d458fdc-ae3c-406c-9ca2-16f011b7081a_1058x736.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d458fdc-ae3c-406c-9ca2-16f011b7081a_1058x736.png)

Google’s TensorFlow/Jax and other graph mode execution pipelines generally require the user to ensure their model fits into the compiler architecture so that the graph can be captured. Dynamo changes this by enabling partial graph capture, guarded graph capture, and just-in-time recapture.

*   Partial graph capture allows the model to include unsupported/non-python constructs. When a graph cannot be generated for that portion of the model, a graph break is inserted, and the unsupported constructs will be executed in eager mode between the partial graphs.
    
*   Guarded graph capture checks if the captured graph is valid for execution. A guard is a change that would require recompilation. This is important because running the same code multiple times won't recompile multiple times.
    
*   Just-in-time recapture allows the graph to be recaptured if the captured graph is invalid for execution.
    

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc42cb6d-5aaa-471b-b65f-fae82146fbd2_1920x966.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc42cb6d-5aaa-471b-b65f-fae82146fbd2_1920x966.png)

PyTorch’s goal is to create a unified front end with a smooth UX that leverages Dynamo to generate graphs. The user experience of this solution would be unchanged, but the performance can be significantly improved. Capturing the graph means execution can be parallelized more efficiently over a large base of compute resources.

Dynamo and [AOT Autograd](https://pytorch.org/functorch/stable/notebooks/aot_autograd_optimizations.html) then pass the optimized FX graphs to the PyTorch native compiler level, TorchInductor. Hardware companies can also take this graph and input it into their own backend compilers.

TorchInductor is a python native deep learning compiler that generates fast code for multiple accelerators and backends. Inductor will take the FX graphs, which have ~250 operators, and lowers them to ~50 operators. Inductor then moves to a scheduling phase where operators are fused, and memory planning is determined.

Inductor then goes to the “Wrapper Codegen,” which generates code that runs on the CPU, GPU, or other AI accelerators. The wrapper codegen replaces the interpreter part of a compiler stack and can call kernels and allocate memory. The backend code generation portion leverages OpenAI Triton for GPUs and outputs PTX code. For CPUs, an Intel compiler generates C++ (will work on non-Intel CPUs too).

More hardware will be supported going forward, but the key is that Inductor dramatically reduces the amount of work a compiler team must do when making a compiler for their AI hardware accelerator. Furthermore, the code is more optimized for performance. There are significant reductions in memory bandwidth and capacity requirements.

> We didn't want to build a compiler that only supported GPUs. We wanted something that could scale to support a wide variety of hardware back ends, and having a C++ as well as \[OpenAI\] Triton forces that generality.
> 
> [Jason Ansel – Meta AI](https://www.youtube.com/watch?v=ppWKVg-VxmQ)

OpenAI’s Triton is very disruptive angle to Nvidia’s closed-source software moat for machine learning. Triton takes in Python directly or feeds through the [PyTorch Inductor stack](https://github.com/pytorch/pytorch/blob/master/torch/_inductor/codegen/triton.py). The latter will be the most common use case. Triton then converts the input to an LLVM intermediate representation and then generates code. In the case of Nvidia GPUs, it directly generates PTX code, skipping Nvidia’s closed-source CUDA libraries, such as cuBLAS, in favor of open-source libraries, such as cutlass.

CUDA is commonly used by those specializing in accelerated computing, but it is less well-known among machine learning researchers and data scientists. It can be challenging to use efficiently and requires a deep understanding of the hardware architecture, which can slow down the development process. As a result, machine learning experts may rely on CUDA experts to modify, optimize, and parallelize their code.

Triton bridges the gap enabling higher-level languages to achieve performance comparable to those using lower-level languages. The Triton kernels themselves are quite legible to the typical ML researcher which is huge for usability. Triton automates memory coalescing, shared memory management, and scheduling within SMs. Triton is not particularly helpful for the element-wise matrix multiplies, which are already done very efficiently. Triton is incredibly useful for costly pointwise operations and [reducing overhead from more complex operations](https://github.com/HazyResearch/flash-attention/blob/main/flash_attn/flash_attn_triton.py) such as [Flash Attention](https://github.com/HazyResearch/flash-attention) that involve matrix multiplies as a portion of a larger fused operation.

[Share](https://www.semianalysis.com/p/nvidiaopenaitritonpytorch?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoxMDcwMTAwNDUsInBvc3RfaWQiOjk3MDA2MzA5LCJpYXQiOjE3MjYwMzM4ODYsImV4cCI6MTcyODYyNTg4NiwiaXNzIjoicHViLTMyOTI0MSIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.bv-tSxqRNLznXRbOocy6CUJJk6wX4sQNmX9b4fMqwnc)

OpenAI Triton only officially supports Nvidia GPUs today, but that is changing in the near future. Multiple other hardware vendors will be supported in the future, and this open-source project is gaining incredible steam. The ability for other hardware accelerators to integrate directly into the LLVM IR that is part of Triton dramatically reduces the time to build an AI compiler stack for a new piece of hardware.

Nvidia’s colossal software organization lacked the foresight to take their massive advantage in ML hardware and software and become the default compiler for machine learning. Their lack of focus on usability is what enabled outsiders at OpenAI and Meta to create a software stack that is portable to other hardware. Why aren’t they the one building a « simplified » CUDA like Triton for ML researchers? Stuff like [Flash Attention](https://github.com/HazyResearch/flash-attention), why does it come out of Ph.D. students and not Nvidia?

The rest of this report will point out the specific hardware accelerator that has a huge win at Microsoft, as well as multiple companies’ hardware that is quickly being integrated into the PyTorch 2.0/OpenAI Trion software stack. Furthermore, it will share the opposing view as a defense of Nvidia’s moat/strength in the AI training market.

[Get 20% off a group subscription](https://www.semianalysis.com/subscribe?group=true&coupon=fe141654)