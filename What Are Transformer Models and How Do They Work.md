# What Are Transformer Models and How Do They Work?
[What Are Transformer Models and How Do They Work?](https://txt.cohere.com/what-are-transformer-models/?utm_source=pocket_reader) 

 ![](https://txt.cohere.com/content/images/size/w2000/2023/04/Fueling-Generative-Content-with-Keyword-Research--2-.jpg)

Share:

### TL;DR:

_Transformers are a new development in machine learning that have been making a lot of noise lately. They are incredibly good at keeping track of context, and this is why the text that they write makes sense. In this blog post, we will go over their architecture and how they work._

> _T_ry out the [Command model](https://dashboard.cohere.ai/playground/generate?ref=txt.cohere.com&{query}&__hstc=14363112.c3801ea446a572339a0e9de69112c296.1688435860231.1688435860231.1688435860231.1&__hssc=14363112.1.1688435860231&__hsfp=1456612391), Cohere’s latest generative transformer in this demo!

* * *

Transformer models are one of the most exciting new developments in machine learning. They were introduced in the paper [Attention is All You Need](https://arxiv.org/abs/1706.03762?ref=txt.cohere.com&{query}). Transformers can be used to write stories, essays, poems, answer questions, translate between languages, chat with humans, and they can even pass exams that are hard for humans! But what are they? You’ll be happy to know that the architecture of transformer models is not that complex, it simply is a concatenation of some very useful components, each of which has its own function. In this post, you will learn all of these components.

This blog post contains a simple conceptual introduction. For a much more detailed description of transformer models and how they work, please check out these two excellent articles by [Jay Alammar](https://jalammar.github.io/?ref=txt.cohere.com&{query}), also from [Cohere](https://www.cohere.ai/?ref=txt.cohere.com&{query}&__hstc=14363112.c3801ea446a572339a0e9de69112c296.1688435860231.1688435860231.1688435860231.1&__hssc=14363112.1.1688435860231&__hsfp=1456612391)!

*   [The illustrated transformer](https://jalammar.github.io/illustrated-transformer/?ref=txt.cohere.com&{query})
*   [How GPT3 works](https://jalammar.github.io/how-gpt3-works-visualizations-animations/?ref=txt.cohere.com&{query})

In a nutshell, what does a transformer do? Imagine that you’re writing a text message on your phone. After each word, you may get three words suggested to you. For example, if you type “Hello, how are”, the phone may suggest words such as “you”, or “your” as the next word. Of course, if you continue selecting the suggested word in your phone, you’ll quickly find that the message formed by these words makes no sense. If you look at each set of 3 or 4 consecutive words, it may make sense, but these words don’t concatenate to anything with a meaning. This is because the model used in the phone doesn’t carry the overall context of the message, it simply predicts which word is more likely to come up after the last few. Transformers, on the other hand, keep track of the context of what is being written, and this is why the text that they write makes sense.

![](https://lh4.googleusercontent.com/YMc1E2RFxD4ooeQTDZNWQWjptSLB-ZyFlQC6i5WkUcAA7Sb2BXNIzGqxiaXWGcCfernmocOJBaoxcxWFiWGePiJ__jW9d68VE1saGOrAODwjT7UFIay98vcjsyX8nzxio8wJ04sav2wEm9nVBKycT2U)

The phone can suggest the next word to use in a text message, but does not have the power to generate coherent text.

I have to be honest with you, the first time I found out that transformers build text one word at a time, I couldn’t believe it. First of all, this is not how humans form sentences and thoughts. We first form a basic thought, and then start refining it and adding words to it. This is also not how ML models do other things. For example, images are not built this way. Most neural network based graphical models form a rough version of the image, and slowly refine it or add detail until it is perfect. So why would a transformer model build text word by word? One answer is, because that works really well. A more satisfying one is that because transformers are so incredibly good at keeping track of the context, that the next word they pick is exactly what it needs to keep going with an idea.

And how are transformers trained? With a lot of data, all the data on the internet, in fact. So when you input the sentence “Hello, how are” into the transformer, it simply knows that, based on all the text in the internet, the best next word is “you”. If you were to give it a more complicated command, say, “Write a story.”, it may figure out that a good next word to use is “Once”. Then it adds this word to the command, and figures out that a good next word is “upon”, and so on. And word by word, it will continue until it writes a story.

**Command:** Write a story.  
**Response**: Once

**Next command:** Write a story. Once  
**Response**: upon

**Next command:** Write a story. Once upon  
**Response**: a

**Next command:** Write a story. Once upon a  
**Response**: time

**Next command:** Write a story. Once upon a time  
**Response**: there

etc.

![](https://txt.cohere.com/content/images/2023/05/image-7.png)

💡

If you enjoy this content, be sure to check out more in [LLM University](https://llm.university/?ref=txt.cohere.com&{query})!

Now that we know what transformers do,  let’s get to their architecture. If you’ve seen the architecture of a transformer model, you may have jumped in awe like I did the first time I saw it, it looks quite complicated! However, when you break it down into its most important parts, it’s not so bad. The transformer has 4 main parts:

1.  Tokenization
2.  Embedding
3.  Positional encoding
4.  Transformer block (several of these)
5.  Softmax

The fourth one, the transformer block, is the most complex of all. Many of these can be concatenated, and each one contains two main parts: The attention and the feedforward components.

![](https://txt.cohere.com/content/images/2023/04/image-3.png)

The architecture of a transformer model

Let’s study these parts one by one.

Tokenization is the most basic step. It consists of a large dataset of tokens, including all the words, punctuation signs, etc. The tokenization step takes every word, prefix, suffix, and punctuation signs, and sends them to a known token from the library.

![](https://lh6.googleusercontent.com/uGLtzKFP0qziISh_O7GY4xGmz8M6WSCWXa08dOu_svoBKTmGYY0p3XzgVAdXuJdDWe_rj2aLCQGalV9ddbW0r2BJKKelDzyidDClbQEqaI6CPvMq38uiDRH24mQwaqU6sqBbAjM2Y-iQpE5-c9W8J3U)

Tokenization: Turning words into tokens

For example, if the sentence is “Write a story”, then the 4 corresponding tokens will be <Write>, <a>, <story>, and <.>.

Once the input has been tokenized, it’s time to turn words into numbers. For this, we use an embedding. Embeddings are one of the most important parts of any large language model; it is where the rubber meets the road. The reason for this is that it is the bridge that turns text into numbers. As humans are good with text, and computers with numbers, the stronger this bridge is, the more powerful language models can be.

In short, text embeddings send every piece of text to a vector (a list) of numbers. If two pieces of text are similar, then the numbers in their corresponding vectors are similar to each other (componentwise, meaning each pair of numbers in the same position are similar). Otherwise, if two pieces of text are different, then the numbers in their corresponding vectors are different. If you’d like to learn more, check out this [post on text embeddings](https://txt.cohere.com/sentence-word-embeddings/?utm_source=pocket_reader), with its corresponding [video](https://www.youtube.com/watch?v=A8HEPBdKVMA&ref=txt.cohere.com&{query}).

Even though embeddings are numerical, I like to imagine them geometrically. Imagine for a moment that there is a very simple embedding which sends every word to a vector of length 2 (that is, a list of 2 numbers). If we were to locate each word in the coordinates given by these two numbers (imagine the number in a street and an avenue), then we have all the words standing on a big plane. In this plane, words that are similar, appear close to each other, and words that are different, appear far away from each other. For example, in the embedding below, the coordinates for cherry are \[6,4\], which are close to strawberry \[5,4\], but far from castle \[1,2\].

![](https://lh6.googleusercontent.com/NRTq1BnxHIBl2geH9pyvnrg8pZpeBYH293iBSu7Nt5fLsIOQP5JqFgvvXaLIHlHIlm-18JmgN_KvygzRHj5oWFSBQ-YfzZF5gHH6nNEmDczG2HPPV1YFNm5IF34nTkJM-N1_Q_mcZaAmKd71ECXpCxU)

Embedding: Turning words (tokens) into vectors (lists of numbers)

In the case of a much larger embedding, where each word gets sent to a longer vector (say, of length 4096), then the words no longer live in a 2-dimensional plane, but in a large 4096-dimensional space. However, even in that large space, we can think of words being close and far from each other, so the concept of embedding still makes sense.

Word embeddings generalize to text embeddings, in which the entire sentence, paragraph, or even longer piece of text, gets sent to a vector. However, in the case of transformers, we’ll be using a word embedding, meaning that every word in the sentence gets sent to a corresponding vector. More specifically, every token in the input text will be sent to its corresponding vector in the embedding.

For example, if the sentence we are considering is “Write a story.” and the tokens are <Write>, <a>, <story>, and <.>, then each one of these will be sent to a long vector, and we’ll have four vectors.  

![](https://lh6.googleusercontent.com/ssKSbm6mMRrjMOIEvqrVaMMK1QqAyNCjeSmWjXO5YiSoKBpCpmyHzhGwUfVRoumSxfDz_PwDDjGrveSvZf5QhO2AyOC47QTU68jgdRbGcV8jwoENkpL6a2wtZ1bhs-xgpF4h2eSqjOixaYY92zM1QQM)

In general embeddings send every word (token) to a long list of numbers

Once we have the vectors corresponding to each of the tokens in the sentence, the next step is to turn all these into one vector to process. The most common way to turn a bunch of vectors into one vector is to add them, componentwise. That means, we add each coordinate separately. For example, if the vectors (of length 2) are \[1,2\], and \[3,4\], their corresponding sum is \[1+3, 2+4\], which equals \[4, 6\]. This can work, but there’s a small caveat. Addition is commutative, meaning that if you add the same numbers in a different order, you get the same result. In that case, the sentence “I’m not sad, I’m happy” and the sentence “I’m not happy, I’m sad”, will result in the same vector, given that they have the same words, except in different order. This is not good. Therefore, we must come up with some method that will give us a different vector for the two sentences. Several methods work, and we’ll go with one of them: positional encoding. Positional encoding consists of adding a sequence of predefined vectors to the embedding vectors of the words. This ensures we get a unique vector for every sentence, and sentences with the same words in different order will be assigned different vectors. In the example below, the vectors corresponding to the words “Write”, “a”, “story”, and “.” become the modified vectors that carry information about their position, labeled “Write (1)”, “a (2)”, “story (3)”, and “. (4)”.

![](https://lh5.googleusercontent.com/cSu_BsO6anf8oRwx4so4Jwda9V__QDypOgPSLtPF1SanLXuqOBskNzLIkQOybFT1ZLGmWeA3yh3mxoxIWdzdhG70us3cWS_6UShl4XGow0AM6E_bwzWH69_iMo55LYutoDlL4QSVFuRdALbhRAbsCuA)

Positional encoding adds a positional vector to each word, in order to keep track of the positions of the words.

Now that we know we have a unique vector corresponding to the sentence, and that this vector carries the information on all the words in the sentence and their order, we can move to the next step.

Let’s recap what we have so far. The words come in and get turned into tokens (tokenization), then order gets taken into account (positional encoding). This gives us a vector for every token that we input to the model. Now, the next step is to predict the next word in this sentence. This is done with a really really large neural network, which is trained precisely with that goal, to predict the next word in a sentence.

We can train such a large network, but we can vastly improve it by adding a key step: the attention component. Introduced in the seminal paper [Attention is All you Need](https://arxiv.org/abs/1706.03762?ref=txt.cohere.com&{query}), it is one of the key ingredients in transformer models, and one of the reasons they work so well. Attention is explained in the following section, but for now, imagine it as a way to add context to each word in the text.

The attention component is added at every block of the feedforward network. Therefore, if you imagine a large feedforward neural network whose goal is to predict the next word, formed by several blocks of smaller neural networks, an attention component is added to each one of these blocks. Each component of the transformer, called a transformer block, is then formed by two main components:

*   The attention component.
*   The feedforward component.

The transformer is a concatenation of many transformer blocks.

![](https://lh5.googleusercontent.com/WD7P89qrdQ54LsSTsiTJP0CY-ENAAhujMJ6RD-arrTt3FXP4dXUD_VUlPsYVTq9NZD6z--Z6J6X61n6THrdzfGYZhow9VFDeeCV2tFBVv1g-feK6bWH6MkFuAFBnAhSdmAr8a1ca6oc2QtPviK9S_s0)

The transformer is a concatenation of many transformer blocks. Each one of these is composed by an attention component followed by a feedforward component (a neural network)

The attention step deals with a very important problem: the problem of context. Sometimes, as you know, the same word can be used with different meanings. This tends to confuse language models, since an embedding simply sends words to vectors, without knowing which definition of the word they’re using.

Attention is a very useful technique that helps language models understand the context. In order to understand how attention works, consider the following two sentences:

*   Sentence 1: The **bank** of the river.
*   Sentence 2: Money in the **bank.**

As you can see, the word ‘bank’ appears in both, but with different definitions. In sentence 1, we are referring to the land at the side of the river, and in the second one to the institution that holds money. The computer has no idea of this, so we need to somehow inject that knowledge into it. What can help us? Well, it seems that the other words in the sentence can come to our rescue. For the first sentence, the words ‘the’, and ‘of’ do us no good. But the word ‘river’ is the one that is letting us know that we’re talking about the land at the side of the river. Similarly, in sentence 2, the word ‘money’ is the one that is helping us understand that the word ‘bank’ is now referring to the institution that holds money.

![](https://lh4.googleusercontent.com/xr1VavwjFCoULSWQM7fPJGXvZvP-R8pu-DoUk0DwcQxE_bGBUZQeBg2zF6Z5hq9vipENzWay7IYIZvjytwK8ipuysQGn1Y92SwO7jaRwssxtuR6wOjTe-GspQfJiUciogPL-TEQBZLJ7PI_KjvNnnmU)

Attention helps give context to each word, based on the other words in the sentece (or text)

In short, what attention does is it moves the words in a sentence (or piece of text) closer in the word embedding. In that way, the word “bank” in the sentence “Money in the bank” will be moved closer to the word “money”. Equivalently, in the sentence “The bank of the river”, the word “bank” will be moved closer to the word “river”. That way, the modified word “bank” in each of the two sentences will carry some of the information of the neighboring words, adding context to it.

The attention step used in transformer models is actually much more powerful, and it’s called _multi-head attention_. In multi-head attention, several different embeddings are used to modify the vectors and add context to them. Multi-head attention has helped language models reach much higher levels of efficacy when processing and generating text. If you’d like to learn the attention mechanism more in detail, please check out this [blog post](https://txt.cohere.com/what-is-attention-in-language-models/?utm_source=pocket_reader) and its corresponding [video](https://www.youtube.com/watch?v=j10yrR6PPfg&pp=ygUoYXR0ZW50aW9uIG1lY2hhbmlzbXMgbHVpcyBzZXJyYW5vIGNvaGVyZQ%3D%3D&ref=txt.cohere.com&{query}).

Now that you know that a transformer is formed by many layers of transformer blocks, each containing an attention and a feedforward layer, you can think of it as a large neural network that predicts the next word in a sentence. The transformer outputs scores for all the words, where the highest scores are given to the words that are most likely to be next in the sentence.

The last step of a transformer is a softmax layer, which turns these scores into probabilities (that add to 1), where the highest scores correspond to the highest probabilities. Then, we can sample out of these probabilities for the next word. In the example below, the transformer gives the highest probability of 0.5 to “Once”, and probabilities of 0.3 and 0.2 to “Somewhere” and “There”. Once we sample, the word “once” is selected, and that’s the output of the transformer.  

![](https://lh4.googleusercontent.com/7PeFWif-WmUK6bi-3ocaoUpNYwEGzo-KCxMjU9wKS0D3qRpsgxek6fiYTo8HUhqgmnF7cijWpCT8Vhamb6aEkVbg7o9PadR9AWv0EDeS35_srSBgjM71vRnlm7kVky9uob7Y9tSmGsRWtkwHGUZuwSk)

The softmax layer turns the scores into probabilities, and these are used to pick the next word in the text.

Now what? Well, we repeat the step. We now input the text “Write a story. Once” into the model, and most likely, the output will be “upon”. Repeating this step again and again, the transformer will end up writing a story, such as “Once upon a time, there was a …”.

In this blog post you’ve learned how transformers work. They are formed by several blocks, each one with its own function, working together to understand text and generate the next word. These blocks are the following:

1.  **Tokenizer:** Turns words into tokens.
2.  **Embedding:** Turns tokens into numbers (vectors)
3.  **Positional encoding:** Adds order to the words in the text.
4.  **Transformer block:** Guesses the next word. It is formed by an attention block and a feedforward block.  
    **Attention:** Adds context to the text.  
    **Feedforward:** Is a block in the transformer neural network, which guesses the next word.
5.  **Softmax**: Turns the scores into probabilities in order to sample the next word.

The repetition of these steps is what writes the amazing text you’ve seen transformers create.

Now that you know how transformers work, we still have a bit of work to do. Imagine the following: You as the transformer “What is the capital of Algeria?”. We would love for it to answer “Algiers”, and move on. However, the transformer is trained on the entire internet. The internet is a big place, and it’s not necessarily the best question/answer repository. Many pages, for example, would have long lists of questions without answers. In this case, the next sentence after “What is the capital of Algeria?” could be another question, such as “What is the population of Algeria?”, or “What is the capital of Burkina Faso?”. The transformer is not a human who thinks about their responses, it simply mimics what it sees on the internet (or any dataset that has been provided). So how do we get the transformer to answer questions?

The answer is post-training. In the same way that you would teach a person to do certain tasks, you can get a transformer to perform tasks. Once a transformer is trained on the entire internet, then it is trained again on a large dataset which corresponds to lots of questions and their respective answers. Transformers (like humans), have a bias towards the last things they’ve learned, so post-training has proven a very useful step to help transformers succeed at the tasks they are asked to.

Post-training also helps with many other tasks. For example, one can post-train a transformer with large datasets of conversations, in order to help it perform well as a chatbot, or to help us write stories, poems, or even code.

As mentioned above, this is a conceptual introduction to give you an idea of how transformers generate text. If you'd like to open the hood and get a more detailed intuition of the mathematics behind a transformer, we invite you to check out the following video.

As you see, the architecture of a transformer is not that complicated. They are a concatenation of several blocks, each one of them with their own function. The main reason they work so well is because they have a huge amount of parameters that can capture many aspects of the context. We’re excited to see what you can build using transformer models!

[![](https://txt.cohere.com/content/images/2023/04/image-2.png)
](https://os.cohere.ai/?ref=txt.cohere.ai&{query}&__hstc=14363112.c3801ea446a572339a0e9de69112c296.1688435860231.1688435860231.1688435860231.1&__hssc=14363112.1.1688435860231&__hsfp=1456612391)