Title: A Visual Guide to Reasoning LLMs

URL Source: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms

Published Time: 2025-02-03T15:41:35+00:00

Markdown Content:
##### Translations _- [Chinese](https://mp.weixin.qq.com/s/8DHjWUAIjfuIjqcoJYCotA) | [Korean](https://tulip-phalange-a1e.notion.site/Reasoning-LLMs-190c32470be2806d834ee0ad98aaa0b6)_

[DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1), [OpenAI o3-mini](https://openai.com/index/openai-o3-mini/), and [Google Gemini 2.0 Flash Thinking](https://deepmind.google/technologies/gemini/flash-thinking/) are prime examples of how LLMs can be scaled to new heights through “reasoning“ frameworks.

They mark the paradigm shift from scaling **train-time compute** to scaling **test-time compute**.

[![Image 109](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10912af1-1648-44e2-9cfc-af1c5b2a5aa8_1020x729.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10912af1-1648-44e2-9cfc-af1c5b2a5aa8_1020x729.png)

With over 40 custom visuals in this post, you will explore the field of reasoning LLMs, test-time compute, and deep dive into **DeepSeek-R1**. We explore concepts one by one to develop an intuition about this new paradigm shift.

_👈 click on the stack of lines on the left to see a **Table of Contents** (ToC),_

Check out the book we wrote on large language models for more visualizations related to LLMs and to support this newsletter!

_P.S. If you read the book, a **[quick review](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961)** would mean the world—it really helps us authors!_

Compared to regular LLMs, reasoning LLMs tend to break down a problem into smaller steps (often called reasoning steps or thought processes) before answering a given question.

[![Image 110](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2e82204-1a7d-43bb-b1f2-ce7d55122454_1668x1060.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2e82204-1a7d-43bb-b1f2-ce7d55122454_1668x1060.png)

So what does a “thought process”, “reasoning step”, or “Chain-of-Thought” actually mean?

Although we can philosophize whether LLMs are actually able to think like humans[1](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-1-153314921), these reasoning steps break down the process into smaller, structured inferences.

[![Image 111](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F302aecd1-eeec-45f6-8f21-97d9791ef67d_1284x960.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F302aecd1-eeec-45f6-8f21-97d9791ef67d_1284x960.png)

In other words, instead of having LLMs learn “what” to answer they learn “how” to answer!

To understand how reasoning LLMs are created, we first explore the paradigm shift from a focus on scaling training (**train**\-time compute) to inference (**test**\-time compute).

Until half of 2024, to increase the performance of LLMs during **pre-training**, developers often increase the **size** of the:

*   Model (# of **parameters**)
    
*   Dataset (# of **tokens**)
    
*   Compute (# of **FLOPs**)
    

Combined, this is called **train-time compute,** which refers to the idea that pretraining data is the “fossil fuel of AI”. Essentially, the larger your pretraining budget, the better the resulting model will be.

[![Image 112](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe91dc815-9210-4b10-abfb-efd631b30196_1384x588.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe91dc815-9210-4b10-abfb-efd631b30196_1384x588.png)

Train-time compute may include both the compute needed during training as well as during fine-tuning.

[![Image 113](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04fdfdaa-4ffe-440e-ada4-166cadd1f42a_1736x468.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F04fdfdaa-4ffe-440e-ada4-166cadd1f42a_1736x468.png)

Together, they have been a main focus on increasing the performance of LLMs.

How a model’s scale (through compute, dataset size, and model size) correlates with a model’s performance is researched through various scaling laws.

They are so-called “power laws” where an increase in one variable (e.g., compute) results in a proportional change in another variable (e.g., performance).

[![Image 114](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff028438e-4a6c-4398-87c6-5eacb617ad2c_1452x592.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff028438e-4a6c-4398-87c6-5eacb617ad2c_1452x592.png)

These are typically shown in a log-log scale (which results in a straight line) to showcase the large increase in compute.

Most well-known are the “Kaplan”[2](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-2-153314921) and “Chinchilla”[3](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-3-153314921) scaling laws. These laws more and less say that the performance of a model will increase with more compute, tokens, and parameters.

[![Image 115](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2a70247-3a21-4048-adb8-2ed2f9c15b01_1384x508.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2a70247-3a21-4048-adb8-2ed2f9c15b01_1384x508.png)

Annotated figure of the “[Scaling laws for neural language models](https://arxiv.org/abs/2001.08361)” paper. It shows how performance may increase with different measures of compute (longer training, dataset size, and parameter size).

They suggest that all three factors must be scaled up in tandem for optimal performance.

Kaplan’s Scaling Law states that scaling the model’s size is typically more effective than scaling data (given fixed compute). In contrast, the Chinchilla Scaling Law suggests that the model size and data are equally important.

However, throughout 2024, compute, dataset size and model parameters have steadily grown, yet the gains have shown diminishing returns.

[![Image 116](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd84d837-0b4f-4e91-9a84-d07976a72cfe_1452x592.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd84d837-0b4f-4e91-9a84-d07976a72cfe_1452x592.png)

As is with these power laws, there are diminishing returns as you scale up.

This raises the question:

“Have we reached a wall?”

The expensive nature of increasing train-time compute led to an interest in an alternative focus, namely **test-time compute**.

Instead of continuously increasing pre-training budgets, test-time compute allows modes to “_think longer_” during **inference**.

[![Image 117](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdc25691-a91b-4ab3-bd76-554b4233452e_1232x748.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdc25691-a91b-4ab3-bd76-554b4233452e_1232x748.png)

With non-reasoning models, it would normally only output the answer and skip any “reasoning” steps:

[![Image 118](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F833c7a1e-ce3c-4ff1-8796-97ca5cb67943_1384x776.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F833c7a1e-ce3c-4ff1-8796-97ca5cb67943_1384x776.png)

Reasoning models, however, would instead use more tokens to derive their answer through a systematic “**thinking**” process:

[![Image 119](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6392f3a1-4b9f-4eae-9e33-3b03d9a62dd6_1384x968.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6392f3a1-4b9f-4eae-9e33-3b03d9a62dd6_1384x968.png)

The idea is that the LLM has to spend resources (like VRAM compute) to create an answer. However, if all compute is spent generating the answer, then that is a bit inefficient!

Instead, by creating more tokens beforehand that contain additional information, relationships, and new thoughts, the model spent more compute generating the final answer.

[![Image 120](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0437cf25-8f58-47d4-b200-92f30829f3ab_1384x744.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0437cf25-8f58-47d4-b200-92f30829f3ab_1384x744.png)

Compared to train-time compute, scaling laws for test-time compute are relatively new. Of note are two interesting sources that relate test-time compute scaling to train-time compute.

First, is a [post by OpenAI](https://openai.com/index/learning-to-reason-with-llms/) showcasing that test-time compute might actually follow the same trend as scaling train-time compute.

[![Image 121](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff56b1b36-8e90-48cd-bc50-ab4d10522673_1384x884.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff56b1b36-8e90-48cd-bc50-ab4d10522673_1384x884.png)

Annotated figure from “[Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)”. The red dotted line was added to demonstrate how OpenAI suggests the new paradigm might be test-time compute.

As such, they claim that there might be a paradigm shift to scaling test-time compute as it is still a new field.

Second, an interesting paper called “Scaling Scaling Laws with Board Games”[4](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-4-153314921), explores **AlphaZero** and trains it to various degrees of compute to play Hex.

Their results show that train-time compute and test-time compute are tightly related. Each dotted line showcases the minimum compute needed for that particular ELO score.

With test-time compute scaling like train-time compute, a paradigm shift is happening toward “reasoning” models using more test-time compute.

Through this paradigm shift, instead of focusing purely on train-time compute (pre-training and fine-tuning), these “reasoning” models instead balance training with inference.

[![Image 122](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fe913b8-2210-4156-9bf6-ac1f489b0cec_1500x436.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fe913b8-2210-4156-9bf6-ac1f489b0cec_1500x436.png)

Test-time compute could even scale in length:

[![Image 123](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F574b4416-1903-4d19-8669-875f8ab45f92_1500x624.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F574b4416-1903-4d19-8669-875f8ab45f92_1500x624.png)

Scaling in length is something we will also explore when diving into DeepSeek-R1!

The incredible success of reasoning models like DeepSeek R-1 and OpenAI o1 showcase that there are more techniques than simply thinking “longer”.

As we will explore, test-time compute can be many different things, including Chain-of-Thought, revising answers, backtracking, sampling, and more.

These can be roughly put into two categories[5](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-5-153314921):

*   Search against Verifiers (sampling generations and selecting the best answer)
    
*   Modifying Proposal Distribution (trained “thinking” process)
    

[![Image 124](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbec64b2-53a6-4259-8a6c-6446281b4ee2_1668x1132.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbec64b2-53a6-4259-8a6c-6446281b4ee2_1668x1132.png)

Thus, search against verifiers is _output_\-focused whereas modifying the proposal distribution is _input_\-focused.

[![Image 125](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8afbaee-4d2d-4f5f-88dd-20ae58cdf806_1744x560.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8afbaee-4d2d-4f5f-88dd-20ae58cdf806_1744x560.png)

There are two types of verifiers that we will explore:

*   Outcome Reward Models (ORM)
    
*   Process Reward Models (PRM)
    

As their names imply, the ORM only judges the outcome and doesn’t care about the underlying process:

[![Image 126](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F036ff9da-db9f-4a01-8fc7-022bbc83dbcb_1156x808.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F036ff9da-db9f-4a01-8fc7-022bbc83dbcb_1156x808.png)

In contrast, the PRM also judges the process that leads to the outcome (the “reasoning”):

[![Image 127](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd3465b7-e01e-4c9f-835f-819f8a30214b_1156x732.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd3465b7-e01e-4c9f-835f-819f8a30214b_1156x732.png)

To make these reasoning steps a bit more explicit:

[![Image 128](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71760532-53a5-4953-8305-f0182954023c_1440x640.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71760532-53a5-4953-8305-f0182954023c_1440x640.png)

Note how step 2 is a poor reasoning step and is scored low by the PRM!

Now that you have a good grasp on ORMs vs. PRMs, let us explore how they can applied in various verification techniques!

The first major category of test-time compute is to search against verifiers. This generally involves two steps.

*   First, multiple samples of reasoning processes and answers are created.
    
*   Second, a verifier (Reward Model) scores the generated output
    

[![Image 129](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F822bfcc6-a0ab-4b90-b243-4d2f45195edb_1076x884.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F822bfcc6-a0ab-4b90-b243-4d2f45195edb_1076x884.png)

The verifier is typically a LLM, fine-tuned for either judging the outcome (ORM) or the process (PRM).

A major advantage of using verifiers is that there is no need to re-train or fine-tune the LLM that you use for answering the question.

The most straightforward method is actually not to use a reward model or verifier but instead, perform a majority vote.

We let the model generate multiple answers and the answer that is generated most often will be the final answer.

[![Image 130](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93f66577-0287-421f-b3e8-6bc2e5a47069_1480x744.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93f66577-0287-421f-b3e8-6bc2e5a47069_1480x744.png)

This method is also called _self-consistency_[6](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-6-153314921) as a way to emphasize the need for generating multiple answers and reasoning steps.

The first method that involves a verifier is called Best-of-N samples. This technique generates N samples and then uses a verifier (Outcome Reward Model) to judge each answer:

First, the LLM (often called the Proposer) generates multiple answers using either a high or varying temperature.

[![Image 131](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f674bc6-a20f-4e2c-9df1-ef288c169bcd_1776x676.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f674bc6-a20f-4e2c-9df1-ef288c169bcd_1776x676.png)

Second, each answer is put through an Output Reward Model (ORM) and scored on the quality of the answer. The answer with the highest score is selected:

[![Image 132](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f8cdfb5-7dd8-46d2-9cdd-192ca8e83728_1776x656.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f8cdfb5-7dd8-46d2-9cdd-192ca8e83728_1776x656.png)

Instead of judging the answer, the reasoning process might also be judged with a **Process Reward Model** (PRM) that judges the quality of each reasoning step. It will pick the candidate with the highest total weight.

[![Image 133](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3371566-e205-4240-8b6e-f2f0db9bd9a2_1776x960.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3371566-e205-4240-8b6e-f2f0db9bd9a2_1776x960.png)

With both verifier types, we can also weigh each answer candidate by the RM and pick the one with the highest total weight. This is called Weighted Best-of-N samples:

[![Image 134](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70c6c06f-5846-4888-b486-3b9e17ce753d_1480x1028.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70c6c06f-5846-4888-b486-3b9e17ce753d_1480x1028.png)

This process of generating answers and intermediate steps can be further extended with beam search. With beam search, multiple reasoning steps are sampled and each is judged by PRM (similar to Tree of Thought[7](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-7-153314921)). The top 3 “**beams**” (best-scoring paths) are tracked throughout the process.

[![Image 135](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d746daf-1f6f-4e0b-886d-a302ce826fb9_1416x1132.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d746daf-1f6f-4e0b-886d-a302ce826fb9_1416x1132.png)

This method allows for quickly stopping “reasoning” paths that do not end up to be fruitful (scored low by the PRM).

The resulting answers are then weighted using the Best-of-N approach we explored before.

A great technique for making the tree searches more efficient is called Monte Carlo Tree Search. It consists of four steps:

*   Selection (select a given leaf based on a pre-determined formulate)
    
*   Expand (create additional nodes)
    
*   Rollouts (randomly create new nodes until you reach the end)
    
*   Backprop (update parent node scores based on output)
    

The main goal of these steps is to keep expanding the best reasoning steps while also exploring other paths.

It is therefore a balance between **exploration** and **exploitation**. An example of how nodes are scored and selected is as follows:

[![Image 136](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F506b026c-709e-4fcc-b3d6-d2d96f0d1ca6_952x328.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F506b026c-709e-4fcc-b3d6-d2d96f0d1ca6_952x328.png)

Thus, when we select a new reasoning step to explore, it does not have to be the best-performing path thus far.

Using this type of formula, we start by **selecting** a node (reasoning step) and **expand** it by generating new reasoning steps. As before, this can be done with reasonably high and varying values of **temperature**:

[![Image 137](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F197ba7fc-e7ff-4d2b-9f3b-6cade4612e26_936x624.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F197ba7fc-e7ff-4d2b-9f3b-6cade4612e26_936x624.png)

One of the expanded reasoning steps is selected and rolled out multiple times until it reaches several answers.

These rollouts can be judged based on the reasoning steps (PRM), the rewards (ORM), or a combination of both.

The scores of the parent nodes are updated (backpropagated) and we can start the process again starting with selection.

[![Image 138](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69f0a6f4-d1a7-46ed-8346-2b466aef68d1_1476x1416.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69f0a6f4-d1a7-46ed-8346-2b466aef68d1_1476x1416.png)

The second category of making reasoning LLMs is called “Modifying Proposal Distribution”. Instead of searching for the correct reasoning steps with verifiers (_output_\-focused), the model is trained to create improved reasoning steps (_input_\-focused).

In other words, the distribution from which completions/thoughts/tokens are sampled is modified.

Imagine that we have a question and a distribution from which we can sample tokens. A common strategy would be to get the highest-scoring token:

[![Image 139](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53ff298a-d0d1-4704-92e7-9037e9cd26ba_1832x560.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53ff298a-d0d1-4704-92e7-9037e9cd26ba_1832x560.png)

However, note that some of the tokens are colored red in the image above. Those are the tokens that are more likely to lead to a reasoning process:

[![Image 140](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a17b874-c02e-4e71-83db-285618879928_1804x712.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a17b874-c02e-4e71-83db-285618879928_1804x712.png)

Although taking the greedy token is not necessarily wrong, selecting a token leading to a reasoning process tends to result in an improved answer.

When we modify the proposal distribution (the token probability distribution), we are essentially making it so that the model re-ranks the distribution such that “reasoning” tokens are selected more frequently:

[![Image 141](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c8886f6-da9f-4502-ae8d-180ac0e3cc23_1804x560.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c8886f6-da9f-4502-ae8d-180ac0e3cc23_1804x560.png)

There are various methods for modifying the proposal distribution but they can be generally put in two categories:

*   Updating the **prompt** through prompt engineering
    
*   **Training** the model to focus on reasoning tokens/processes
    

With prompt engineering, we are attempting to improve the output by updating the prompt. This process might also nudge the model to showcase some of the reasoning processes we saw before.

To change the proposal distribution with prompting, we can provide examples to the model (in-context learning) that it has to follow to generate reasoning-like behavior:

[![Image 142](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a80be6e-40c2-4d3b-bcd1-4fa6b4c30d3d_1804x680.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a80be6e-40c2-4d3b-bcd1-4fa6b4c30d3d_1804x680.png)

This process can be further simplified by simply stating “_Let’s think step-by-step_”[8](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-8-153314921). Likewise, this changes the proposal distribution in such a way that the LLM tends to break down the process before answering:

[![Image 143](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b013518-3af0-45e9-b684-79d88e4a44c4_1820x612.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b013518-3af0-45e9-b684-79d88e4a44c4_1820x612.png)

However, the model has not inherently learned to follow this process. Moreover, this is a static and linear process that inhibits self-refinement. If a model starts with an incorrect reasoning process it tends to keep it instead of revising it.

Aside from prompting, we can also have the model learn to “reason” by having it train so that it is rewarded for generating these reasoning steps. This typically involves a bunch of reasoning data and reinforcement learning to reward certain behaviors.

A much-debated technique is called STaR or Self-Taught Reasoner[9](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-9-153314921). STaR is a method that uses the LLM to generate its own reasoning data as the input for fine-tuning the model.

In the first step (1), it generates reasoning steps and an answer. If the answer is correct (2a), then add the reasoning and answer to a triplet training data set (3b). This data is used to perform **supervised fine-tuning** of the model (5):

[![Image 144](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4b352d1-2ed6-4b76-8696-4c7ca8df3c68_1640x1100.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4b352d1-2ed6-4b76-8696-4c7ca8df3c68_1640x1100.png)

If however, the model provides an incorrect answer (2b), then we provide a “hint” (the correct answer) and ask the model to reason why this answer would be correct (4b). The final reasoning step is to add to the same triplet training data which is used to perform **supervised fine-tuning** of the model (5):

[![Image 145](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4546442-c6ad-4119-99be-ee4edbfb0cd3_1640x1100.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4546442-c6ad-4119-99be-ee4edbfb0cd3_1640x1100.png)

A key element here (along with many other techniques for modifying the proposal distribution) is that we explicitly train the model to follow along with the reasoning processes we show it.

In other words, we decide how the reasoning process should be through **supervised fine-tuning**.

The full pipeline is quite interesting as it essentially generates **synthetic training** **examples**. Using synthetic training examples (as we will explore in DeepSeek R-1) is an incredible method of also **distilling** this reasoning process in other models.

A major release in reasoning models is **DeepSeek-R1**, an open-source model whose weights are available[10](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-10-153314921). Directly competing with the OpenAI o1 reasoning model, DeepSeek-R1 has had a major impact on the field.

DeepSeek has done a remarkable job at elegantly distilling reasoning into its base model (**DeepSeek-V3-Base**) through various techniques.

Interestingly, no verifiers were involved and instead of using supervised fine-tuning to distill reasoning behavior, a large focus was on reinforcement learning.

Let’s explore how they trained reasoning behavior in their models!

A major breakthrough leading to DeepSeek-R1 was an experimental model called **DeepSeek-R1 Zero**.

Starting with DeepSeek-V3-Base, instead of using supervised fine-tuning on a bunch of reasoning data, they only used reinforcement learning (RL) to enable reasoning behavior.

To do so, they start with a very straightforward prompt (similar to a system prompt) to be used in the pipeline:

[![Image 146](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f01d333-2976-41fc-8cc2-2180fb2e9c59_2604x918.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f01d333-2976-41fc-8cc2-2180fb2e9c59_2604x918.png)

Note how they explicitly mention that the reasoning process should go between **<think\>** tags but they do not specify what the reasoning process should look like.

During reinforcement learning, two specific rule-based rewards were created:

*   Accuracy rewards - Rewards the **answer** by testing it out.
    
*   Format rewards - Rewards using the **<thinking\>** and **<answer\>** tags.
    

The RL algorithm used in this process is called Group Relative Policy Optimization (GRPO)[11](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms#footnote-11-153314921). The intuition behind this algorithm is that it makes all choices that led to a correct or incorrect answer more or less likely. These choices can be both sets of tokens as well as reasoning steps.

[![Image 147](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf299252-386e-43f3-9875-238dd7d7e6fe_1628x1624.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf299252-386e-43f3-9875-238dd7d7e6fe_1628x1624.png)

Interestingly, no examples were given on how the <think\> process should look like. It merely states that it **should use <think\> tags**, and nothing more!

By providing these indirect rewards related to Chain-of-Thought behavior, the model learned by itself that the longer and more complex the reasoning process, the more likely the answer was correct.

This graph is especially important as it reinforces the **paradigm shift** from **train**\-time compute to **test**\-time compute. As these models generate longer sequences of thoughts, they focus on **test**\-time compute.

Using this training pipeline, they found that the model discovers on its own the most optimal Chain-of-Thought-like behavior, including advanced reasoning capabilities such as self-reflection and self-verification.

However, it still had a significant drawback. It had poor readability and tended to mix languages. Instead, they explored an alternative, the now well-known **DeepSeek R1**.

Let’s explore how they stabilized the reasoning process!

To create DeepSeek-R1, the authors followed five steps:

1.  Cold Start
    
2.  Reasoning-oriented Reinforcement Learning
    
3.  Rejection Sampling
    
4.  Supervised Fine-Tuning
    
5.  Reinforcement Learning for all Scenarios
    

In **step 1**, DeepSeek-V3-Base was fine-tuned with a small high-quality reasoning dataset (≈5.000 tokens). This was done to prevent the cold start problem resulting in poor readability.

[![Image 148](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa0c1e2c-b517-44bf-833a-36ae68aaa551_1628x836.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa0c1e2c-b517-44bf-833a-36ae68aaa551_1628x836.png)

In **step 2**, the resulting model was trained using a similar RL process as was used to train DeepSeek-R1-Zero. However, another reward measure was added to make sure the target language remained consistent.

[![Image 149](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F905ed035-f5bb-4b34-8351-c15f93e9b3c7_1628x1380.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F905ed035-f5bb-4b34-8351-c15f93e9b3c7_1628x1380.png)

In **step 3**, the resulting RL-trained model was used to generate synthetic reasoning data to be used for supervised fine-tuning in a later stage. Through rejecting sampling (rule-based rewards) and a reward model (DeepSeek-V3-Base), 600,000 high-quality reasoning samples were created.

Moreover, 200,000 non-reasoning samples were created by using DeepSeek-V3 and part of the data it was trained on.

[![Image 150](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd31892cd-e082-455c-96b0-3c209eca53ec_1712x1828.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd31892cd-e082-455c-96b0-3c209eca53ec_1712x1828.png)

In **step 4**, the resulting dataset of 800,000 samples was used to perform supervised fine-tuning of the DeepSeek-V3-Base model.

[![Image 151](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7facfbe9-de6d-4b6e-8372-64d79ef1eb9d_1628x836.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7facfbe9-de6d-4b6e-8372-64d79ef1eb9d_1628x836.png)

In **step 5**, RL-based training was performed on the resulting model using a similar approach used in DeepSeek-R1-Zero. However, to align with human preferences, additional reward signals were added focused on helpfulness and harmlessness.

The model was also asked to summarize the reasoning process to prevent readability issues.

[![Image 152](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d3517a-a3d6-4c56-a269-ac3dab6ba3ad_1628x1620.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d3517a-a3d6-4c56-a269-ac3dab6ba3ad_1628x1620.png)

And that’s it! This means that DeepSeek-R1 is actually a fine-tune of DeepSeek-V3-Base through supervised fine-tuning and reinforcement learning.

The bulk of the work is making sure that high-quality samples are generated!

DeepSeek-R1 is a huge model with 671B parameters. Unfortunately, this means running such a model is going to be difficult on consumer hardware.

Fortunately, the authors explored ways to distill the reasoning quality of DeepSeek-R1 into other models, such as Qwen-32B, which we can run on consumer hardware!

To do so, they use the DeepSeek-R1 as a **teacher** model and the smaller model as a **student**. Both models are presented with a prompt and have to generate a token probability distribution. During training, the **student** will attempt to closely follow the distribution of the **teacher**.

[![Image 153](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65aaf771-2030-4e4e-a273-fc8c517aef31_2332x1308.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65aaf771-2030-4e4e-a273-fc8c517aef31_2332x1308.png)

This process was done using the full 800,000 high-quality samples that we saw before:

[![Image 154](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0c9f75-03b8-493a-a5e3-ffb744153961_1888x820.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0c9f75-03b8-493a-a5e3-ffb744153961_1888x820.png)

The resulting distilled models are quite performant since they not just learned from the 800,000 samples but also the way the teacher (DeepSeek-R1) would answer them!

Remember when we talked about **Process Reward Models** (PRMs) and **Monte Carlo Tree Search** (MCTS)? It turns out that DeepSeek also tried those techniques to instill reasoning but was not successful in doing so.

With MCTS, they encountered issues with the large search space and had to limit the node expansions. Moreover, training a fine-grained Reward Model is inherently difficult.

With PRMs for Best-of-N techniques, they encountered issues with computational overhead to keep re-training the Reward Model to prevent reward-hacking.

This does not mean these are not valid techniques but it provides interesting insights into the limitations of these techniques!

This concludes our journey of reasoning LLMs. Hopefully, this post gives you a better understanding of the potential of scaling test-time compute.

To see more visualizations related to LLMs and to support this newsletter, check out the book I wrote on Large Language Models!

Hopefully, this was an accessible introduction to reasoning LLMs. If you want to go deeper, I would suggest the following resources:

*   [The Illustrated DeepSeek-R1](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1) is an amazing guide by Jay Alammar.
    
*   A great [Hugging Face post](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute) on scaling test-time compute with interesting experiments.
    
*   This video, [Speculations on Test-Time Scaling](https://www.youtube.com/watch?v=6PEJ96k1kiw), does a great job of going into the technical details of common test-time compute techniques.
