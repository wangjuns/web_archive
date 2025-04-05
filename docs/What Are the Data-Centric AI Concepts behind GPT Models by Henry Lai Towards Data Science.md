# What Are the Data-Centric AI Concepts behind GPT Models? | by Henry Lai | Towards Data Science
[What Are the Data-Centric AI Concepts behind GPT Models? | by Henry Lai | Towards Data Science](https://towardsdatascience.com/what-are-the-data-centric-ai-concepts-behind-gpt-models-a590071bb727) 

 Unpacking the data-centric AI techniques used in ChatGPT and GPT-4
------------------------------------------------------------------

[

![](https://miro.medium.com/v2/resize:fill:88:88/2*8ElEjOf9ImZ7RbZYsgMFtA.jpeg)










](https://medium.com/@a0987284901?source=post_page-----a590071bb727--------------------------------)[

![](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)












](https://towardsdatascience.com/?source=post_page-----a590071bb727--------------------------------)

![](https://miro.medium.com/v2/resize:fit:875/0*9FXXj9tfXGcX3ZZv.png)

[https://arxiv.org/abs/2303.10158](https://arxiv.org/abs/2303.10158). Image by the author.

Artificial Intelligence (AI) has made incredible strides in transforming the way we live, work, and interact with technology. Recently, that one area that has seen significant progress is the development of Large Language Models (LLMs), such as [GPT-3](https://arxiv.org/abs/2005.14165), [ChatGPT](https://openai.com/blog/chatgpt), and [GPT-4](https://cdn.openai.com/papers/gpt-4.pdf). These models are capable of performing tasks such as language translation, text summarization, and question-answering with impressive accuracy.

While it’s difficult to ignore the increasing model size of LLMs, it’s also important to recognize that their success is due largely to the large amount and high-quality data used to train them.

In this article, we will present an overview of the recent advancements in LLMs from a data-centric AI perspective, drawing upon insights from our recent survey papers \[1,2\] with corresponding technical resources on [GitHub](https://github.com/daochenzha/data-centric-AI). Particularly, we will take a closer look at GPT models through the lens of [data-centric AI](https://github.com/daochenzha/data-centric-AI), a growing concept in the data science community. We’ll unpack the data-centric AI concepts behind GPT models by discussing three data-centric AI goals: [training data development, inference data development, and data maintenance](https://arxiv.org/abs/2303.10158).

Large Language Models (LLMs) and GPT Models
-------------------------------------------

LLMs are a type of Natual Language Processing model that are trained to infer words within a context. For example, the most basic function of an LLM is to predict missing tokens given the context. To do this, LLMs are trained to predict the probability of each token candidate from massive data.

![](https://miro.medium.com/v2/resize:fit:875/1*0b-hv8CdhCQDtOJMoF-rkg.png)

An illustrative example of predicting the probabilities of missing tokens with an LLM within a context. Image by the author.

GPT models refer to a series of LLMs created by OpenAI, such as [GPT-1](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), [GPT-3](https://arxiv.org/abs/2005.14165), [InstructGPT](https://arxiv.org/abs/2203.02155), and [ChatGPT/GPT-4.](https://cdn.openai.com/papers/gpt-4.pdf) Just like other LLMs, GPT models’ architectures are largely based on [Transformers](https://arxiv.org/abs/1706.03762), which use text and positional embeddings as input, and attention layers to model tokens’ relationships.

![](https://miro.medium.com/v2/resize:fit:875/0*yJQHmOAp4l66uALw.png)

GPT-1 model architecture. Image from the paper [https://cdn.openai.com/research-covers/language-unsupervised/language\_understanding\_paper.pdf](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)

The later GPT models use similar architectures as GPT-1, except for using more model parameters with more layers, larger context length, hidden layer size, etc.

![](https://miro.medium.com/v2/resize:fit:875/1*TX1ytZFsV0JNBykpdlKPHQ.png)

Models size comparison of GPT models. Image by the author.

What is data-centric AI?
------------------------

[Data-centric AI](https://github.com/daochenzha/data-centric-AI) is an emerging new way of thinking about how to build AI systems. It has been advocated by Andrew Ng, an AI pioneer.

> _Data-centric AI is the discipline of systematically engineering the data used to build an AI system. — Andrew Ng_

In the past, we mainly focused on creating better models with data largely unchanged (model-centric AI). However, this approach can lead to problems in the real world because it doesn’t consider the different problems that may arise in the data, such as inaccurate labels, duplicates, and biases. As a result, “overfitting” a dataset may not necessarily lead to better model behaviors.

In contrast, data-centric AI focuses on improving the quality and quantity of data used to build AI systems. This means that the attention is on the data itself, and the models are relatively more fixed. Developing AI systems with a data-centric approach holds more potential in real-world scenarios, as the data used for training ultimately determines the maximum capability of a model.

It is important to note that “data-centric” differs fundamentally from “data-driven”, as the latter only emphasizes the use of data to guide AI development, which typically still centers on developing models rather than engineering data.

![](https://miro.medium.com/v2/resize:fit:875/0*9H17vC5k2hq9Agfc)

Comparison between data-centric AI and model-centric AI. [https://arxiv.org/abs/2301.04819](https://arxiv.org/abs/2301.04819) Image by the author.

The [data-centric AI framework](https://github.com/daochenzha/data-centric-AI) consists of three goals:

*   **Training data development** is to collect and produce rich and high-quality data to support the training of machine learning models.
*   **Inference data development** is to create novel evaluation sets that can provide more granular insights into the model or trigger a specific capability of the model with engineered data inputs.
*   **Data maintenance** is to ensure the quality and reliability of data in a dynamic environment. Data maintenance is critical as data in the real world is not created once but rather necessitates continuous maintenance.

![](https://miro.medium.com/v2/resize:fit:875/0*T-rVbW3xwLoNLoQI.png)

Data-centric AI framework. [https://arxiv.org/abs/2303.10158](https://arxiv.org/abs/2303.10158). Image by the author.

Why Data-centric AI Made GPT Models Successful
----------------------------------------------

Months earlier, Yann LeCun tweeted that ChatGPT was nothing new. Indeed, all techniques (transformer, reinforcement learning from human feedback, etc.) used in ChatGPT and GPT-4 are not new at all. However, they did achieve incredible results that previous models couldn’t. So, what is the driving force of their success?

**Training data development.** The quantity and quality of the data used for training GPT models have seen a significant increase through better data collection, data labeling, and data preparation strategies.

*   **GPT-1:** [BooksCorpus dataset](https://huggingface.co/datasets/bookcorpus) is used in training. This dataset contains 4629.00 MB of raw text, covering books from a range of genres such as Adventure, Fantasy, and Romance.  
    **\- _Data-centric AI strategies_:** None.  
    **\- _Result:_** Pertaining GPT-1 on this dataset can increase performances on downstream tasks with fine-tuning.
*   **GPT-2:** [WebText](https://paperswithcode.com/dataset/webtext) is used in training. This is an internal dataset in OpenAI created by scraping outbound links from Reddit.  
    **\- _Data-centric AI strategies:_** (1) Curate/filter data by only using the outbound links from Reddit, which received at least 3 karma. (2) Use tools [Dragnet](https://dl.acm.org/doi/abs/10.1145/2487788.2487828) and [Newspaper](https://github.com/codelucas/newspaper) to extract clean contents. (3) Adopt de-duplication and some other heuristic-based cleaning (details not mentioned in the paper)  
    **\- _Result:_** 40 GB of text is obtained after filtering. GPT-2 achieves strong zero-shot results without fine-tuning.
*   **GPT-3:** The training of GPT-3 is mainly based on [Common Crawl](https://commoncrawl.org/the-data/).  
    **\- _Data-centric AI strategies:_**  (1) Train a classifier to filter out low-quality documents based on the similarity of each document to WebText, a proxy for high-quality documents. (2) Use Spark’s MinHashLSH to fuzzily deduplicate documents. (3) Augment the data with WebText, books corpora, and Wikipedia.  
    **_\- Result:_** 570GB of text is obtained after filtering from 45TB of plaintext (only 1.27% of data is selected in this quality filtering). GPT-3 significantly outperforms GPT-2 in the zero-shot setting.
*   **InstructGPT:** Let humans evaluate the answer to tune GPT-3 so that it can better align with human expectations. They have designed tests for annotators, and only those who can pass the tests are eligible to annotate. They have even designed a survey to ensure that the annotators enjoy the annotating process.  
    **\- _Data-centric AI strategies:_**  (1) Use human-provided answers to prompts to tune the model with supervised training. (2) Collect comparison data to train a reward model and then use this reward model to tune GPT-3 with reinforcement learning from human feedback (RLHF).  
    **_\- Result:_** InstructGPT shows better truthfulness and less bias, i.e., better alignment.
*   **ChatGPT/GPT-4:** The details are not disclosed by OpenAI. But it is known that ChatGPT/GPT-4 largely follow the design of previous GPT models, and they still use RLHF to tune models (with potentially more and higher quality data/labels). It is commonly believed that GPT-4 used an even larger dataset, as the model weights have been increased.

**Inference data development.** As recent GPT models are already sufficiently powerful, we can achieve various goals by tuning prompts (or tuning inference data) with the model fixed. For example, we can conduct text summarization by offering the text to be summarized alongside an instruction like “summarize it” or “TL;DR” to steer the inference process.

![](https://miro.medium.com/v2/resize:fit:875/0*jj8QOR2NadXFgtj2.png)

Prompt tuning. [https://arxiv.org/abs/2303.10158](https://arxiv.org/abs/2303.10158). Image by the author.

Designing the proper prompts for inference is a challenging task. It heavily relies on heuristics. A nice [survey](https://arxiv.org/abs/2107.13586) has summarized different promoting methods. Sometimes, even semantically similar prompts can have very diverse outputs. In this case, [Soft Prompt-Based Calibration](https://arxiv.org/abs/2303.13035v1) may be required to reduce variance.

![](https://miro.medium.com/v2/resize:fit:875/0*AOGgxmPCe6NAQf8s.png)

Soft prompt-based calibration. Image from the paper [https://arxiv.org/abs/2303.13035v1](https://arxiv.org/abs/2303.13035v1) with original authors’ permission.

The research of inference data development for LLMs is still in its early stage. More [inference data development techniques that have been used in other tasks](https://arxiv.org/abs/2303.10158) could be applied in LLMs in the near future.

**Data maintenance.** ChatGPT/GPT-4, as a commercial product, is not only trained once but rather is updated continuously and maintained. Clearly, we can’t know how data maintenance is executed outside of OpenAI. So, we discuss some general data-centric AI strategies that are or will be very likely used for GPT models:  
**_\- Continuous data collection:_** When we use ChatGPT/GPT-4, our prompts/feedback could be, in turn, used by OpenAI to further advance their models. Quality metrics and assurance strategies may have been designed and implemented to collect high-quality data in this process.  
**_\- Data understanding tools:_** Various tools could have been developed to visualize and comprehend user data, facilitating a better understanding of users’ requirements and guiding the direction of future improvements.  
**_\- Efficient data processing:_** As the number of users of ChatGPT/GPT-4 grows rapidly, an efficient data administration system is required to enable fast data acquisition.

![](https://miro.medium.com/v2/resize:fit:875/0*wawvLcuefAO1aMDh.png)

ChatGPT/GPT-4 collects user feedback with “thumb up” and “thumb down” to further evolve their system. Screenshot from [https://chat.openai.com/chat](https://chat.openai.com/chat).

What Can the Data Science Community Learn from this Wave of LLMs?
-----------------------------------------------------------------

The success of LLMs has revolutionized AI. Looking forward, LLMs could further revolutionize the data science lifecycle. We make two predictions:

*   **Data-centric AI becomes even more important.** After years of research, the model design is already very mature, especially after Transformer. Engineering data becomes a crucial (or possibly the only) way to improve AI systems in the future. Also, when the model becomes sufficiently powerful, we don’t need to train models in our daily work. Instead, we only need to design the proper inference data (prompt engineering) to probe knowledge from the model. Thus, the research and development of data-centric AI will drive future advancements.
*   **LLMs will enable better data-centric AI solutions.** Many of the tedious data science works could be performed much more efficiently with the help of LLMs. For example, ChaGPT/GPT-4 can already write workable codes to process and clean data. Additionally, LLMs can even be used to create data for training. For example, [recent work](https://arxiv.org/abs/2303.04360) has shown that generating synthetic data with LLMs can boost model performance in clinical text mining.

![](https://miro.medium.com/v2/resize:fit:875/0*6PZfMcCsRMYLv0Xk.png)

Generating synthetic data with LLMs to train the model. Image from the paper [https://arxiv.org/abs/2303.04360](https://arxiv.org/abs/2303.04360) with the original authors’ permission.

Resources
---------

I hope this article can inspire you in your own work. You can learn more about the data-centric AI framework and how it benefits LLMs in the following papers:

*   \[1\] [Data-centric Artificial Intelligence: A Survey](https://arxiv.org/abs/2303.10158)
*   \[2\] [Data-centric AI: Perspectives and Challenges](https://arxiv.org/abs/2301.04819)

We have maintained a [GitHub repo](https://github.com/daochenzha/data-centric-AI), which will regularly update the relevant data-centric AI resources. Stay tuned!

In the later articles, I will delve into the three goals of data-centric AI (training data development, inference data development, and data maintenance) and introduce the representative methods.