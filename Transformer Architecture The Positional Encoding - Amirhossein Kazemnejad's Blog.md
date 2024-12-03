# Transformer Architecture: The Positional Encoding - Amirhossein Kazemnejad's Blog
[Transformer Architecture: The Positional Encoding - Amirhossein Kazemnejad's Blog](https://kazemnejad.com/blog/transformer_architecture_positional_encoding/) 

 Transformer architecture was introduced as a novel pure attention-only sequence-to-sequence architecture by Vaswani et al. Its ability for parallelizable training and its general performance improvement made it a popular option among NLP (and recently CV) researchers.

Thanks to the several implementations in common deep learning frameworks, it became an easy option to experiment with for many students (including myself). Even though making it more accessible is a great thing, but on the downside it may cause the details of the model to be ignored.

In this article, I don’t plan to explain its architecture in depth as there are currently several great tutorials on this topic ([here](http://nlp.seas.harvard.edu/2018/04/03/attention.html), [here](http://vandergoten.ai/2018-09-18-attention-is-all-you-need/), and [here](http://jalammar.github.io/illustrated-transformer/)), but alternatively, I want to discuss one specific part of the transformer’s architecture - the positional encoding.

When I read this part of the paper, it raised some questions in my head, which unfortunately the author had not provided sufficient information to answer them. So in this article, I want to try to break this module apart and look at how it works.

**NOTE:** To understand the rest of this post, I highly suggest you read one those tutorials to get familiar with the transformer architecture.

![](https://kazemnejad.com/img/transformer_architecture_positional_encoding/model_arc.jpg)
 Figure 1 - The Transformer Architecture

Header Photo by [Susan Yin](https://unsplash.com/@syinq?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/library?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

What is positional encoding and Why do we need it in the first place?
---------------------------------------------------------------------

Position and order of words are the essential parts of any language. They define the grammar and thus the actual semantics of a sentence. Recurrent Neural Networks (RNNs) inherently take the order of word into account; They parse a sentence word by word in a sequential manner. This will integrate the words’ order in the backbone of RNNs.

But the Transformer architecture ditched the recurrence mechanism in favor of multi-head self-attention mechanism. Avoiding the RNNs’ method of recurrence will result in massive speed-up in the training time. And theoretically, it can capture longer dependencies in a sentence.

As each word in a sentence simultaneously flows through the Transformer’s encoder/decoder stack, The model itself doesn’t have any sense of position/order for each word. Consequently, there’s still the need for a way to incorporate the order of the words into our model.

One possible solution to give the model some sense of order is to add a piece of information to each word about its position in the sentence. We call this “piece of information”, the positional encoding.

The first idea that might come to mind is to assign a number to each time-step within the \[0, 1\] range in which 0 means the first word and 1 is the last time-step. Could you figure out what kind of issues it would cause? One of the problems it will introduce is that you can’t figure out how many words are present within a specific range. In other words, time-step delta doesn’t have consistent meaning across different sentences.

Another idea is to assign a number to each time-step linearly. That is, the first word is given “1”, the second word is given “2”, and so on. The problem with this approach is that not only the values could get quite large, but also our model can face sentences longer than the ones in training. In addition, our model may not see any sample with one specific length which would hurt generalization of our model.

Ideally, the following criteria should be satisfied:

*   It should output a unique encoding for each time-step (word’s position in a sentence)
*   Distance between any two time-steps should be consistent across sentences with different lengths.
*   Our model should generalize to longer sentences without any efforts. Its values should be bounded.
*   It must be deterministic.

Proposed method
---------------

The encoding proposed by the authors is a simple yet genius technique which satisfies all of those criteria. First of all, it isn’t a single number. Instead, it’s a d\-dimensional vector that contains information about a specific position in a sentence. And secondly, this encoding is not integrated into the model itself. Instead, this vector is used to equip each word with information about its position in a sentence. In other words, we enhance the model’s input to inject the order of words.

Let t be the desired position in an input sentence, pt→∈Rd be its corresponding encoding, and d be the encoding dimension (where d≡20) Then f:N→Rd will be the function that produces the output vector pt→ and it is defined as follows:

pt→(i)\=f(t)(i):={sin⁡(ωk.t),ifi\=2kcos⁡(ωk.t),ifi\=2k+1

where

ωk\=1100002k/d

As it can be derived from the function definition, the frequencies are decreasing along the vector dimension. Thus it forms a geometric progression from 2π to 10000·2π on the wavelengths.

You can also imagine the positional embedding pt→ as a vector containing pairs of sines and cosines for each frequency (Note that d is divisble by 2):

pt→\=\[sin⁡(ω1.t)cos⁡(ω1.t)sin⁡(ω2.t)cos⁡(ω2.t)⋮sin⁡(ωd/2.t)cos⁡(ωd/2.t)\]d×1

The intuition
-------------

You may wonder how this combination of sines and cosines could ever represent a position/order? It is actually quite simple, Suppose you want to represent a number in binary format, how will that be?

0:00008:10001:00019:10012:001010:10103:001111:10114:010012:11005:010113:11016:011014:11107:011115:1111

You can spot the rate of change between different bits. The LSB bit is alternating on every number, the second-lowest bit is rotating on every two numbers, and so on.

But using binary values would be a waste of space in the world of floats. So instead, we can use their float continous counterparts - Sinusoidal functions. Indeed, they are the equivalent to alternating bits. Moreover, By decreasing their frequencies, we can go from red bits to orange ones.

![](https://kazemnejad.com/img/transformer_architecture_positional_encoding/positional_encoding.png)
 Figure 2 - The 128-dimensional positonal encoding for a sentence with the maximum lenght of 50. Each row represents the embedding vector pt→

Other details
-------------

Earlier in this post, I mentioned that positional embeddings are used to equip the input words with their positional information. But how is it done? In fact, the original paper added the positional encoding on top of the actual embeddings. That is for every word wt in a sentence \[w1,...wn\], Calculating the correspondent embedding which is fed to the model is as follows:

ψ′(wt)\=ψ(wt)+pt→

To make this summation possible, we keep the positional embedding’s dimension equal to the word embeddings’ dimension i.e. dword embedding\=dpostional embedding

Relative Positioning
--------------------

Another characteristic of sinusoidal positional encoding is that it allows the model to attend relative positions effortlessly. Here is a quote from the original paper:

> We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PEpos+k can be represented as a linear function of PEpos.

But why does this statement hold? To fully understand why, please refer to this great [article](https://timodenk.com/blog/linear-relationships-in-the-transformers-positional-encoding/) to read the detailed proof. However I’ve prepared a shorter version here.

For every sine-cosine pair corresponding to frequency ωk, there is a linear transformation M∈R2×2 (independent of t) where the following equation holds:

M.\[sin⁡(ωk.t)cos⁡(ωk.t)\]\=\[sin⁡(ωk.(t+ϕ))cos⁡(ωk.(t+ϕ))\]

**Proof:**

Let M be a 2×2 matrix, we want to find u1,v1,u2 and v2 so that:

\[u1v1u2v2\].\[sin⁡(ωk.t)cos⁡(ωk.t)\]\=\[sin⁡(ωk.(t+ϕ))cos⁡(ωk.(t+ϕ))\]

By applying the [addition theorem](https://timodenk.com/blog/trigonometric-functions-formulary/), we can expand the right hand side as follows:

\[u1v1u2v2\].\[sin⁡(ωk.t)cos⁡(ωk.t)\]\=\[sin⁡(ωk.t)cos⁡(ωk.ϕ)+cos⁡(ωk.t)sin⁡(ωk.ϕ)cos⁡(ωk.t)cos⁡(ωk.ϕ)−sin⁡(ωk.t)sin⁡(ωk.ϕ)\]

Which result in the following two equations:

(1)u1sin⁡(ωk.t)+v1cos⁡(ωk.t)\=cos⁡(ωk.ϕ)sin⁡(ωk.t)+sin⁡(ωk.ϕ)cos⁡(ωk.t)(2)u2sin⁡(ωk.t)+v2cos⁡(ωk.t)\=−sin⁡(ωk.ϕ)sin⁡(ωk.t)+cos⁡(ωk.ϕ)cos⁡(ωk.t)

By solving above equations, we get:

u1\=cos⁡(ωk.ϕ)v1\=sin⁡(ωk.ϕ)u2\=−sin⁡(ωk.ϕ)v2\=cos⁡(ωk.ϕ)

So the final transformation matrix M is:

Mϕ,k\=\[cos⁡(ωk.ϕ)sin⁡(ωk.ϕ)−sin⁡(ωk.ϕ)cos⁡(ωk.ϕ)\]

As you can see, the final transformation does not depend on t. Note that one can find the matrix M very similar to the [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix).

Similarly, we can find M for other sine-cosine pairs, which eventually allows us to represent pt+ϕ→ as a linear function of pt→ for any fixed offset ϕ. This property, makes it easy for the model to learn to attend by relative positions.

Another property of sinusoidal position encoding is that the distance between neighboring time-steps are symmetrical and decays nicely with time.

![](https://kazemnejad.com/img/transformer_architecture_positional_encoding/time-steps_dot_product.png)
 Figure 3 - Dot product of position embeddings for all time-steps

FAQ
---

### Why positional embeddings are summed with word embeddings instead of concatenation?

I couldn’t find any theoretical reason for this question. Since summation (in contrast to concatenation) saves the model’s parameters, it is reasonable to reform the initial question to “Does adding the positional embeddings to words have any disadvantages?”. I would say, not necessarily!

Initially, if we pay attention to the figure 2, we will find out that only the first few dimensions of the whole embedding are used to store the information about the positions (Note that the reported embedding dimension is 512 despite our small toy example). And since the embeddings in the Transfomer are trained from scratch, the parameters are probably set in a way that the semantic of words does not get stored in the first few dimensions to avoid interfering with the positional encoding.

With the same reason, I think the final Transformer can separate the semantic of words from their positional information. Moreover, there is no reason to consider the separability as an advantage. Maybe the summation provides a good source of feature for the model to learn from.

For more information, I recommend you to check these links: [link 1](https://github.com/tensorflow/tensor2tensor/issues/1591), [link 2](https://www.reddit.com/r/MachineLearning/comments/cttefo/d_positional_encoding_in_transformer/exs7d08/).

### Doesn't the position information get vanished once it reaches the upper layers?

Fortunately, the Transformer architecture is equipped with residual connections. Therefore the information from the input of the model (which contains positional embeddings) can efficiently propagate to further layers where the more complex interactions are handled.

### Why are both sine and cosine used?

Personally, I think, only by using both sine and cosine, we can express the sine(x+k) and cosine(x+k) as a linear transformation of sin(x) and cos(x). It seems that you can’t do the same thing with the single sine or cosine. If you can find a linear transformation for a single sine/cosine, please let me know in the comments section.

Summary
-------

Thank you for staying with me until the end of this article. I hope you’ve found this useful for answering your question. Please feel free to provide any corrections or feedbacks, the comment section is at your disposal.

Cited as

```
@article{kazemnejad2019:pencoding,
  title   = "Transformer Architecture: The Positional Encoding",
  author  = "Kazemnejad, Amirhossein",
  journal = "kazemnejad.com",
  year    = "2019",
  url     = "https://kazemnejad.com/blog/transformer_architecture_positional_encoding/"
} 
```

References
----------

*   [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
*   [Attention Is All You Need - The Transformer](http://vandergoten.ai/2018-09-18-attention-is-all-you-need/)
*   [Linear Relationships in the Transformer’s Positional Encoding](https://timodenk.com/blog/linear-relationships-in-the-transformers-positional-encoding/)
*   [position\_encoding.ipynb](https://github.com/tensorflow/examples/blob/master/community/en/position_encoding.ipynb)
*   [Tensor2Tensor Github issue #1591](https://github.com/tensorflow/tensor2tensor/issues/1591)
*   [Reddit thread - Positional Encoding in Transformer](https://www.reddit.com/r/MachineLearning/comments/cttefo/d_positional_encoding_in_transformer/)
*   [Reddit thread - Positional Encoding in Transformer model](https://www.reddit.com/r/learnmachinelearning/comments/9e4j4q/positional_encoding_in_transformer_model/)