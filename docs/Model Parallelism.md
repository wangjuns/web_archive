Title: Model Parallelism

URL Source: https://huggingface.co/docs/transformers/v4.13.0/parallelism

Markdown Content:
[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#parallelism-overview)Parallelism overview
---------------------------------------------------------------------------------------------------------

In the modern machine learning the various approaches to parallelism are used to:

1.  fit very large models onto limited hardware - e.g. t5-11b is 45GB in just model params
2.  significantly speed up training - finish training that would take a year in hours

We will first discuss in depth various 1D parallelism techniques and their pros and cons and then look at how they can be combined into 2D and 3D parallelism to enable an even faster training and to support even bigger models. Various other powerful alternative approaches will be presented.

While the main concepts most likely will apply to any other framework, this article is focused on PyTorch-based implementations.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#concepts)Concepts
---------------------------------------------------------------------------------

The following is the brief description of the main concepts that will be described later in depth in this document.

1.  DataParallel (DP) - the same setup is replicated multiple times, and each being fed a slice of the data. The processing is done in parallel and all setups are synchronized at the end of each training step.
2.  TensorParallel (TP) - each tensor is split up into multiple chunks, so instead of having the whole tensor reside on a single gpu, each shard of the tensor resides on its designated gpu. During processing each shard gets processed separately and in parallel on different GPUs and the results are synced at the end of the step. This is what one may call horizontal parallelism, as the splitting happens on horizontal level.
3.  PipelineParallel (PP) - the model is split up vertically (layer-level) across multiple GPUs, so that only one or several layers of the model are places on a single gpu. Each gpu processes in parallel different stages of the pipeline and working on a small chunk of the batch.
4.  Zero Redundancy Optimizer (ZeRO) - Also performs sharding of the tensors somewhat similar to TP, except the whole tensor gets reconstructed in time for a forward or backward computation, therefore the model doesn’t need to be modified. It also supports various offloading techniques to compensate for limited GPU memory.
5.  Sharded DDP - is another name for the foundational ZeRO concept as used by various other implementations of ZeRO.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#data-parallel)Data Parallel
-------------------------------------------------------------------------------------------

Most users with just 2 GPUs already enjoy the increased training speed up thanks to DataParallel (DP) and DistributedDataParallel (DDP) that are almost trivial to use. This is a built-in feature of Pytorch.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#zero-data-parallel)ZeRO Data Parallel
-----------------------------------------------------------------------------------------------------

ZeRO-powered data parallelism (ZeRO-DP) is described on the following diagram from this [blog post](https://www.microsoft.com/en-us/research/blog/zero-deepspeed-new-system-optimizations-enable-training-models-with-over-100-billion-parameters/) ![Image 1: DeepSpeed-Image-1](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-zero.png)

It can be difficult to wrap one’s head around it, but in reality the concept is quite simple. This is just the usual DataParallel (DP), except, instead of replicating the full model params, gradients and optimizer states, each GPU stores only a slice of it. And then at run-time when the full layer params are needed just for the given layer, all GPUs synchronize to give each other parts that they miss - this is it.

Consider this simple model with 3 layers, where each layer has 3 params:

La | Lb | Lc
---|\----|\---
a0 | b0 | c0
a1 | b1 | c1
a2 | b2 | c2

Layer La has weights a0, a1 and a2.

If we have 3 GPUs, the Sharded DDP (= Zero-DP) splits the model onto 3 GPUs like so:

GPU0:
La | Lb | Lc
---|\----|\---
a0 | b0 | c0

GPU1:
La | Lb | Lc
---|\----|\---
a1 | b1 | c1

GPU2:
La | Lb | Lc
---|\----|\---
a2 | b2 | c2

In a way this is the same horizontal slicing, as tensor parallelism, if you imagine the typical DNN diagram. Vertical slicing is where one puts whole layer-groups on different GPUs. But it’s just the starting point.

Now each of these GPUs will get the usual mini-batch as it works in DP:

x0 \=\> GPU0
x1 \=\> GPU1
x2 \=\> GPU2

The inputs are unmodified - they think they are going to be processed by the normal model.

First, the inputs hit the layer La.

Let’s focus just on GPU0: x0 needs a0, a1, a2 params to do its forward path, but GPU0 has only a0 - it gets sent a1 from GPU1 and a2 from GPU2, bringing all pieces of the model together.

In parallel, GPU1 gets mini-batch x1 and it only has a1, but needs a0 and a2 params, so it gets those from GPU0 and GPU2.

Same happens to GPU2 that gets input x2. It gets a0 and a1 from GPU0 and GPU1, and with its a2 it reconstructs the full tensor.

All 3 GPUs get the full tensors reconstructed and a forward happens.

As soon as the calculation is done, the data that is no longer needed gets dropped - it’s only used during the calculation. The reconstruction is done efficiently via a pre-fetch.

And the whole process is repeated for layer Lb, then Lc forward-wise, and then backward Lc -\> Lb -\> La.

To me this sounds like an efficient group backpacking weight distribution strategy:

1.  person A carries the tent
2.  person B carries the stove
3.  person C carries the axe

Now each night they all share what they have with others and get from others what they don’t have, and in the morning they pack up their allocated type of gear and continue on their way. This is Sharded DDP / Zero DP.

Compare this strategy to the simple one where each person has to carry their own tent, stove and axe, which would be far more inefficient. This is DataParallel (DP and DDP) in Pytorch.

While reading the literature on this topic you may encounter the following synonyms: Sharded, Partitioned.

If you pay close attention the way ZeRO partitions the model’s weights - it looks very similar to tensor parallelism which will be discussed later. This is because it partitions/shards each layer’s weights, unlike vertical model parallelism which is discussed next.

Implementations:

*   [DeepSpeed](https://www.deepspeed.ai/features/#the-zero-redundancy-optimizer) ZeRO-DP stages 1+2+3
*   [Fairscale](https://github.com/facebookresearch/fairscale/#optimizer-state-sharding-zero) ZeRO-DP stages 1+2+3
*   [`transformers` integration](https://huggingface.co/docs/transformers/v4.13.0/main_classes/trainer#trainer-integrations)

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#naive-model-parallel-vertical-and-pipeline-parallel)Naive Model Parallel (Vertical) and Pipeline Parallel
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Naive Model Parallel (MP) is where one spreads groups of model layers across multiple GPUs. The mechanism is relatively simple - switch the desired layers `.to()` the desired devices and now whenever the data goes in and out those layers switch the data to the same device as the layer and leave the rest unmodified.

We refer to it as Vertical MP, because if you remember how most models are drawn, we slice the layers vertically. For example, if the following diagram shows an 8-layer model:

\===================  ===================
|  0 | 1 | 2 | 3  |  |  4 | 5 | 6 | 7  |
===================  ===================
        gpu0                 gpu1

we just sliced it in 2 vertically, placing layers 0-3 onto GPU0 and 4-7 to GPU1.

Now while data travels from layer 0 to 1, 1 to 2 and 2 to 3 this is just the normal model. But when data needs to pass from layer 3 to layer 4 it needs to travel from GPU0 to GPU1 which introduces a communication overhead. If the participating GPUs are on the same compute node (e.g. same physical machine) this copying is pretty fast, but if the GPUs are located on different compute nodes (e.g. multiple machines) the communication overhead could be significantly larger.

Then layers 4 to 5 to 6 to 7 are as a normal model would have and when the 7th layer completes we often need to send the data back to layer 0 where the labels are (or alternatively send the labels to the last layer). Now the loss can be computed and the optimizer can do its work.

Problems:

*   the main deficiency and why this one is called “naive” MP, is that all but one GPU is idle at any given moment. So if 4 GPUs are used, it’s almost identical to quadrupling the amount of memory of a single GPU, and ignoring the rest of the hardware. Plus there is the overhead of copying the data between devices. So 4x 6GB cards will be able to accommodate the same size as 1x 24GB card using naive MP, except the latter will complete the training faster, since it doesn’t have the data copying overhead. But, say, if you have 40GB cards and need to fit a 45GB model you can with 4x 40GB cards (but barely because of the gradient and optimizer states)
*   shared embeddings may need to get copied back and forth between GPUs.

Pipeline Parallel (PP) is almost identical to a naive MP, but it solves the GPU idling problem, by chunking the incoming batch into micro-batches and artificially creating a pipeline, which allows different GPUs to concurrently participate in the computation process.

The following illustration from the [GPipe paper](https://ai.googleblog.com/2019/03/introducing-gpipe-open-source-library.html) shows the naive MP on the top, and PP on the bottom:

![Image 2: mp-pp](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-gpipe-bubble.png)

It’s easy to see from the bottom diagram how PP has less dead zones, where GPUs are idle. The idle parts are referred to as the “bubble”.

Both parts of the diagram show a parallelism that is of degree 4. That is 4 GPUs are participating in the pipeline. So there is the forward path of 4 pipe stages F0, F1, F2 and F3 and then the return reverse order backward path of B3, B2, B1 and B0.

PP introduces a new hyper-parameter to tune and it’s `chunks` which defines how many chunks of data are sent in a sequence through the same pipe stage. For example, in the bottomw diagram you can see that `chunks=4`. GPU0 performs the same forward path on chunk 0, 1, 2 and 3 (F0,0, F0,1, F0,2, F0,3) and then it waits for other GPUs to do their work and only when their work is starting to be complete, GPU0 starts to work again doing the backward path for chunks 3, 2, 1 and 0 (B0,3, B0,2, B0,1, B0,0).

Note that conceptually this is the same concept as gradient accumulation steps (GAS). Pytorch uses `chunks`, whereas DeepSpeed refers to the same hyper-parameter as GAS.

Because of the chunks, PP introduces the concept of micro-batches (MBS). DP splits the global data batch size into mini-batches, so if you have a DP degree of 4, a global batch size of 1024 gets split up into 4 mini-batches of 256 each (1024/4). And if the number of `chunks` (or GAS) is 32 we end up with a micro-batch size of 8 (256/32). Each Pipeline stage works with a single micro-batch at a time.

To calculate the global batch size of the DP + PP setup we then do: `mbs*chunks*dp_degree` (`8*32*4=1024`).

Let’s go back to the diagram.

With `chunks=1` you end up with the naive MP, which is very inefficient. With a very large `chunks` value you end up with tiny micro-batch sizes which could be not every efficient either. So one has to experiment to find the value that leads to the highest efficient utilization of the gpus.

While the diagram shows that there is a bubble of “dead” time that can’t be parallelized because the last `forward` stage has to wait for `backward` to complete the pipeline, the purpose of finding the best value for `chunks` is to enable a high concurrent GPU utilization across all participating GPUs which translates to minimizing the size of the bubble.

There are 2 groups of solutions - the traditional Pipeline API and the more modern solutions that make things much easier for the end user.

Traditional Pipeline API solutions:

*   PyTorch
*   FairScale
*   DeepSpeed
*   Megatron-LM

Modern solutions:

*   Varuna
*   Sagemaker

Problems with traditional Pipeline API solutions:

*   have to modify the model quite heavily, because Pipeline requires one to rewrite the normal flow of modules into a `nn.Sequential` sequence of the same, which may require changes to the design of the model.
*   currently the Pipeline API is very restricted. If you had a bunch of python variables being passed in the very first stage of the Pipeline, you will have to find a way around it. Currently, the pipeline interface requires either a single Tensor or a tuple of Tensors as the only input and output. These tensors must have a batch size as the very first dimension, since pipeline is going to chunk the mini batch into micro-batches. Possible improvements are being discussed here [https://github.com/pytorch/pytorch/pull/50693](https://github.com/pytorch/pytorch/pull/50693)
*   conditional control flow at the level of pipe stages is not possible - e.g., Encoder-Decoder models like T5 require special workarounds to handle a conditional encoder stage.
*   have to arrange each layer so that the output of one model becomes an input to the other model.

We are yet to experiment with Varuna and SageMaker but their papers report that they have overcome the list of problems mentioned above and that they require much smaller changes to the user’s model.

Implementations:

*   [Pytorch](https://pytorch.org/docs/stable/pipeline.html) (initial support in pytorch-1.8, and progressively getting improved in 1.9 and more so in 1.10). Some [examples](https://github.com/pytorch/pytorch/blob/master/benchmarks/distributed/pipeline/pipe.py)
*   [FairScale](https://fairscale.readthedocs.io/en/latest/tutorials/pipe.html)
*   [DeepSpeed](https://www.deepspeed.ai/tutorials/pipeline/)
*   [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) has an internal implementation - no API.
*   [Varuna](https://github.com/microsoft/varuna)
*   [SageMaker](https://arxiv.org/abs/2111.05972) - this is a proprietary solution that can only be used on AWS.

🤗 Transformers status: as of this writing none of the models supports full-PP. GPT2 and T5 models have naive PP support. The main obstacle is being unable to convert the models to `nn.Sequential` and have all the inputs to be Tensors. This is because currently the models include many features that make the conversion very complicated, and will need to be removed to accomplish that.

Other approaches:

DeepSpeed, Varuna and SageMaker use the concept of an [Interleaved Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-core-features.html) ![Image 3: interleaved-pipeline-execution](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-sagemaker-interleaved-pipeline.png)

Here the bubble (idle time) is further minimized by prioritizing backward passes.

Varuna further tries to improve the schedule by using simulations to discover the most efficient scheduling.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#tensor-parallelism)Tensor Parallelism
-----------------------------------------------------------------------------------------------------

In Tensor Parallelism each GPU processes only a slice of a tensor and only aggregates the full tensor for operations that require the whole thing.

In this section we use concepts and diagrams from the [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) paper: [Efficient Large-Scale Language Model Training on GPU Clusters](https://arxiv.org/abs/2104.04473).

The main building block of any transformer is a fully connected `nn.Linear` followed by a nonlinear activation `GeLU`.

Following the Megatron’s paper notation, we can write the dot-product part of it as `Y = GeLU(XA)`, where `X` and `Y` are the input and output vectors, and `A` is the weight matrix.

If we look at the computation in matrix form, it’s easy to see how the matrix multiplication can be split between multiple GPUs: ![Image 4: Parallel GEMM](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-tp-parallel_gemm.png)

If we split the weight matrix `A` column-wise across `N` GPUs and perform matrix multiplications `XA_1` through `XA_n` in parallel, then we will end up with `N` output vectors `Y_1, Y_2, ..., Y_n` which can be fed into `GeLU` independently: ![Image 5: independent GeLU](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-tp-independent-gelu.png)

Using this principle, we can update an MLP of arbitrary depth, without the need for any synchronization between GPUs until the very end, where we need to reconstruct the output vector from shards. The Megatron-LM paper authors provide a helpful illustration for that: ![Image 6: parallel shard processing](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-tp-parallel_shard_processing.png)

Parallelizing the multi-headed attention layers is even simpler, since they are already inherently parallel, due to having multiple independent heads! ![Image 7: parallel self-attention](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-tp-parallel_self_attention.png)

Special considerations: TP requires very fast network, and therefore it’s not advisable to do TP across more than one node. Practically, if a node has 4 GPUs, the highest TP degree is therefore 4. If you need a TP degree of 8, you need to use nodes that have at least 8 GPUs.

This section is based on the original much more [detailed TP overview](https://github.com/huggingface/transformers/issues/10321#issuecomment-783543530). by [@anton-l](https://github.com/anton-l).

SageMaker combines TP with DP for a more efficient processing.

Alternative names:

*   DeepSpeed calls it [tensor slicing](https://www.deepspeed.ai/features/#model-parallelism)

Implementations:

*   [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) has an internal implementation, as it’s very model-specific
*   [parallelformers](https://github.com/tunib-ai/parallelformers) (only inference at the moment)
*   [SageMaker](https://arxiv.org/abs/2111.05972) - this is a proprietary solution that can only be used on AWS.

🤗 Transformers status:

*   core: not yet implemented in the core
*   but if you want inference [parallelformers](https://github.com/tunib-ai/parallelformers) provides this support for most of our models. So until this is implemented in the core you can use theirs. And hopefully training mode will be supported too.
*   Deepspeed-Inference also supports our BERT, GPT-2, and GPT-Neo models in their super-fast CUDA-kernel-based inference mode, see more [here](https://www.deepspeed.ai/tutorials/inference-tutorial/)

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#dppp)DP+PP
--------------------------------------------------------------------------

The following diagram from the DeepSpeed [pipeline tutorial](https://www.deepspeed.ai/tutorials/pipeline/) demonstrates how one combines DP with PP.

![Image 8: dp-pp-2d](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-zero-dp-pp.png)

Here it’s important to see how DP rank 0 doesn’t see GPU2 and DP rank 1 doesn’t see GPU3. To DP there is just GPUs 0 and 1 where it feeds data as if there were just 2 GPUs. GPU0 “secretly” offloads some of its load to GPU2 using PP. And GPU1 does the same by enlisting GPU3 to its aid.

Since each dimension requires at least 2 GPUs, here you’d need at least 4 GPUs.

Implementations:

*   [DeepSpeed](https://github.com/microsoft/DeepSpeed)
*   [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
*   [Varuna](https://github.com/microsoft/varuna)
*   [SageMaker](https://arxiv.org/abs/2111.05972)

🤗 Transformers status: not yet implemented

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#dppptp)DP+PP+TP
-------------------------------------------------------------------------------

To get an even more efficient training a 3D parallelism is used where PP is combined with TP and DP. This can be seen in the following diagram.

![Image 9: dp-pp-tp-3d](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-deepspeed-3d.png)

This diagram is from a blog post [3D parallelism: Scaling to trillion-parameter models](https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/), which is a good read as well.

Since each dimension requires at least 2 GPUs, here you’d need at least 8 GPUs.

Implementations:

*   [DeepSpeed](https://github.com/microsoft/DeepSpeed) - DeepSpeed also includes an even more efficient DP, which they call ZeRO-DP.
*   [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
*   [Varuna](https://github.com/microsoft/varuna)
*   [SageMaker](https://arxiv.org/abs/2111.05972)

🤗 Transformers status: not yet implemented, since we have no PP and TP.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#dppptpzero)DP+PP+TP+ZeRO
----------------------------------------------------------------------------------------

One of the main features of DeepSpeed is ZeRO, which is a super-scalable extension of DP. It has already been discussed in [ZeRO Data Parallel](https://huggingface.co/docs/transformers/v4.13.0/parallelism#zero-data-parallel). Normally it’s a standalone feature that doesn’t require PP or TP. But it can be combined with PP and TP.

When ZeRO-DP is combined with PP (and optionally TP) it typically enables only ZeRO stage 1 (optimizer sharding).

While it’s theoretically possible to use ZeRO stage 2 (gradient sharding) with Pipeline Parallelism, it will have bad performance impacts. There would need to be an additional reduce-scatter collective for every micro-batch to aggregate the gradients before sharding, which adds a potentially significant communication overhead. By nature of Pipeline Parallelism, small micro-batches are used and instead the focus is on trying to balance arithmetic intensity (micro-batch size) with minimizing the Pipeline bubble (number of micro-batches). Therefore those communication costs are going to hurt.

In addition, There are already fewer layers than normal due to PP and so the memory savings won’t be huge. PP already reduces gradient size by `1/PP`, and so gradient sharding savings on top of that are less significant than pure DP.

ZeRO stage 3 is not a good choice either for the same reason - more inter-node communications required.

And since we have ZeRO, the other benefit is ZeRO-Offload. Since this is stage 1 optimizer states can be offloaded to CPU.

Implementations:

*   [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed)

🤗 Transformers status: not yet implemented, since we have no PP and TP.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#flexflow)FlexFlow
---------------------------------------------------------------------------------

[FlexFlow](https://github.com/flexflow/FlexFlow) also solves the parallelization problem in a slightly different approach.

Paper: [“Beyond Data and Model Parallelism for Deep Neural Networks” by Zhihao Jia, Matei Zaharia, Alex Aiken](https://arxiv.org/abs/1807.05358)

It performs a sort of 4D Parallelism over Sample-Operator-Attribute-Parameter.

1.  Sample = Data Parallelism (sample-wise parallel)
2.  Operator = Parallelize a single operation into several sub-operations
3.  Attribute = Data Parallelism (length-wise parallel)
4.  Parameter = Model Parallelism (regardless of dimension - horizontal or vertical)

Examples:

*   Sample

Let’s take 10 batches of sequence length 512. If we parallelize them by sample dimension into 2 devices, we get 10 x 512 which becomes be 5 x 2 x 512.

*   Operator

If we perform layer normalization, we compute std first and mean second, and then we can normalize data. Operator parallelism allows computing std and mean in parallel. So if we parallelize them by operator dimension into 2 devices (cuda:0, cuda:1), first we copy input data into both devices, and cuda:0 computes std, cuda:1 computes mean at the same time.

*   Attribute

We have 10 batches of 512 length. If we parallelize them by attribute dimension into 2 devices, 10 x 512 will be 10 x 2 x 256.

*   Parameter

It is similar with tensor model parallelism or naive layer-wise model parallelism.

![Image 10: flex-flow-soap](https://huggingface.co/docs/transformers/master/en/imgs/parallelism-flexflow.jpeg)

The significance of this framework is that it takes resources like (1) GPU/TPU/CPU vs. (2) RAM/DRAM vs. (3) fast-intra-connect/slow-inter-connect and it automatically optimizes all these algorithmically deciding which parallelisation to use where.

One very important aspect is that FlexFlow is designed for optimizing DNN parallelizations for models with static and fixed workloads, since models with dynamic behavior may prefer different parallelization strategies across iterations.

So the promise is very attractive - it runs a 30min simulation on the cluster of choice and it comes up with the best strategy to utilise this specific environment. If you add/remove/replace any parts it’ll run and re-optimize the plan for that. And then you can train. A different setup will have its own custom optimization.

🤗 Transformers status: not yet integrated. We already have our models FX-trace-able via [transformers.utils.fx](https://github.com/huggingface/transformers/blob/master/src/transformers/utils/fx.py), which is a prerequisite for FlexFlow, so someone needs to figure out what needs to be done to make FlexFlow work with our models.

[](https://huggingface.co/docs/transformers/v4.13.0/parallelism#which-strategy-to-use-when)Which Strategy To Use When
---------------------------------------------------------------------------------------------------------------------

Here is a very rough outline at which parallelism strategy to use when. The first on each list is typically faster.

**⇨ Single GPU**

*   Model fits onto a single GPU:
    
    1.  Normal use
*   Model doesn’t fit onto a single GPU:
    
    1.  ZeRO + Offload CPU and optionally NVMe
    2.  as above plus Memory Centric Tiling (see below for details) if the largest layer can’t fit into a single GPU
*   Largest Layer not fitting into a single GPU:
    

1.  ZeRO - Enable [Memory Centric Tiling](https://deepspeed.readthedocs.io/en/latest/zero3.html#memory-centric-tiling) (MCT). It allows you to run arbitrarily large layers by automatically splitting them and executing them sequentially. MCT reduces the number of parameters that are live on a GPU, but it does not affect the activation memory. As this need is very rare as of this writing a manual override of `torch.nn.Linear` needs to be done by the user.

**⇨ Single Node / Multi-GPU**

*   Model fits onto a single GPU:
    
    1.  DDP - Distributed DP
    2.  ZeRO - may or may not be faster depending on the situation and configuration used
*   Model doesn’t fit onto a single GPU:
    
    1.  PP
        
    2.  ZeRO
        
    3.  TP
        
        With very fast intra-node connectivity of NVLINK or NVSwitch all three should be mostly on par, without these PP will be faster than TP or ZeRO. The degree of TP may also make a difference. Best to experiment to find the winner on your particular setup.
        
        TP is almost always used within a single node. That is TP size <\= gpus per node.
        
*   Largest Layer not fitting into a single GPU:
    
    1.  If not using ZeRO - must use TP, as PP alone won’t be able to fit.
    2.  With ZeRO see the same entry for “Single GPU” above

**⇨ Multi-Node / Multi-GPU**

*   When you have fast inter-node connectivity:
    
    1.  ZeRO - as it requires close to no modifications to the model
    2.  PP+TP+DP - less communications, but requires massive changes to the model
*   when you have slow inter-node connectivity and still low on GPU memory:
    
    1.  DP+PP+TP+ZeRO-1
