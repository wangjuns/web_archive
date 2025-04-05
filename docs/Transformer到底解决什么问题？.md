Transformer到底解决什么问题？
===============
                                                                          

             

  

![Image 1: cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuysYmI4oEicm7LgP14X4J0Iria5icZmfEpSO5gtGOEp9GJ60Zeal5AUms8w/0?wx_fmt=jpeg)

Transformer到底解决什么问题？
====================

Original 凉羽、青熙、纹路 [阿里云开发者](javascript:void(0);)

![Image 2: profile_qrcode](https://mp.weixin.qq.com/mp/qrcode?scene=10000005&size=102&__biz=MzIzOTU0NTQ0MA==&mid=2247547044&idx=1&sn=ee19716b65cec5e302bc1ff6fa6fddd7&send_time=)

阿里云开发者

阿里巴巴(中国)有限公司

阿里巴巴官方技术号，关于阿里的技术创新均呈现于此。

1572篇原创内容

_2025年03月10日 00:31_

![Image 3: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyjbpm1yUcUPjIu5vweMFyGPbnYbJYtgnc0EnXGicug1TKGPhOkEiasnEw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

阿里妹导读

本文希望围绕“Transformer到底是解决什么问题的”这个角度，阐述NLP发展以来遇到的关键问题和解法，通过这些问题引出Transformer实现原理，帮助初学者理解。

近期小组内发起AI技术的学习分享，单看 Transformer的相关资料太“干”了，很难较快的理解其中的设计思路，本文希望围绕“Transformer到底是解决什么问题的”这个角度，阐述NLP发展以来遇到的关键问题和解法，通过这些问题引出Transformer实现原理，帮助初学者理解。

一、人工智能的兴起

1950 年，计算机科学之父阿兰・图灵（Alan Turing）发表了一篇划时代的论文《计算机机械与智能》，文中预言了创造出具有真正智能的机器的可能性。由于注意到 “智能” 这一概念难以确切定义，他提出了一个模仿实验，有a、b、c 三个玩家，让c来根据a b 的回答猜测a、b的性别。a的工作是来迷惑c 让c尽可能错误，b的工作是来配合c 让c尽可能正确；现在将a换成电脑，如果回答能和之前一样，那么说明计算机a通过了图灵测试。

关于这个问题后来进一步演化，提出了著名的 “图灵测试”：如果一台机器能够与人类展开对话（通过电传设备），且不能被参与测试的 30% 以上的人类裁判辨别出其机器身份，那么则称这台机器具有人类智能。

二、NLP发展

如果让机器可以模仿人类，进行一些思考性的工作，那么理解人类自然语言，那就是第一步。所以NLP自然语言处理是至关重要的一步。

**规则模型**

最早期的相关研究都是针对规则定义的模型，这些规则的定义必须耗费大量的人力，需要由专业的人去精心定制，而且随着规则数的增加，不得不去处理一些冲突的问题。最重要的是它不能回答规则库里头没有的问题。但是它的优点是 由于规则都是专业的人去定义的，在某些特定的专业领域，它会表现的比较高效；花20%的人力就可以达到80%的成果。这种模型可以帮助我们解决很多重复性的工作，比如电商客服、电话机器人等。

![Image 4: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy7YBuNFHbYowCXdKaecxjCG60B7wLGJHECHjC47NkENSsXCQNGiaPybA/640?wx_fmt=other&from=appmsg)

但是如果我们想要一种通用模型，可以服务于各行各业呢？

**基于统计方法的模型**

在1980-1990这个年代，人们开始利用基于统计概率的模型。

基于马尔可夫假设，一个词语出现的概率，只和前面的n个词语有关 而与更早的词语或者往后的词语都无关。

马尔可夫假设原理:https://www.au92.com/post/markov-assumption/

因此自然就产生了二元模型（一个词语出现的概率只和它前面的一次词语有关） 和 n元模型（一个词语出现的概率跟它前n-1个词语有关），但是随着n的增大你所需要记录的概率分布就会呈现指数倍的增加，这导致了n不可能无限放大；放到模型上，就是说不能有一个很长的上下文，这个就是典型的长距离依赖问题；

![Image 5: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy3A4yv8MKnu6JEDJ0N5Hd9iczwEsM4f5Zv0a5MXaG7LXeEpJavobnG5w/640?wx_fmt=other&from=appmsg)

**基于神经网络的模型**

几乎在同一时期，出现了基于神经网络的NLP模型，比如我们熟知的CNN（卷积神经网络）RNN（循环神经网络），神经网络启发于我们人脑的工作逻辑，其中著名的hebbian理论阐述了人脑神经元的形态

![Image 6: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy4ys2oCDWRj6gcqzCCh7gLRu54b4wNzvV4lIeal99aG90gWg0xRONXw/640?wx_fmt=other&from=appmsg)

![Image 7: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyqJJ4zqsl9W6mFwRoYb9olBJzs9aBGoibV4Zm1oUDZrVd3QibicwynFCrQ/640?wx_fmt=other&from=appmsg)

又比如我们总习惯于顺序背诵古诗，根据赫布学习规则（Hebbian theory），"同时激活的神经元会强化彼此连接"。在顺序背诵时，前一个诗句对应的神经元集群激活会通过突触前增强（pre-synaptic facilitation）机制，促进后续诗句对应神经元的激活，形成链式神经回路。这种"预测-验证"的神经活动模式已被fMRI研究证实。

#### RNN（循环神经网络）

一个神经元的输出信号可能是另一个神经元的输入信号，得易于这种结构，人脑在处理序列化和结构化数据时非常高效，RNN受这种结构的启发，在序列化的数据处理方面获得了很大的成就，一定程度上缓解了n元模型长距离依赖的问题，但是并没有从根本上解决，同时它也带来了自己新的问题，那就是梯度消失-爆炸。

![Image 8: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyrhhp5GkzTA4Q5hqm7hvKWZBrqF2dVr2eyBib47RyDadLe1icLVMRGacg/640?wx_fmt=other&from=appmsg)

#### 什么是梯度消失-爆炸

梯度消失：误差信号在反向传播时越来越弱，导致模型学不会长期规律。简单来说，RNN的梯度消失就像“传话游戏越传越错”。

**反向传播**

反向传播（英语：Backpropagation，缩写为BP）是“误差反向传播”的简称，是一种与最优化方法（如梯度下降法）结合使用的，用来训练人工神经网络的常见方法。

举个例子：

正向传播：三个人在玩你画我猜游戏，第一个人描述物品信息传给第二个人，再由第二个人描述给第三个人，第三个人说出画的是什么？

反向传播：第三个人得知自己说和正确答案之间的误差，发现他们在传递时的问题差在哪里，向前面一个人说下次描述时可以怎么样更准确的传递信息，就这样一直向前一个人告知。

权重更新：在反向传播的过程中，三个人的默契一直在磨合，然后描述的更加准确。

**关键原因：RNN的“记忆链条”太长**

RNN（循环神经网络）像一条不断延长的锁链，每个时间步（时刻）都在链子上加一节。比如处理句子 \`我 昨天 吃了 一个 苹果\`，RNN会把每个词依次连起来分析。

问题出在反向传播：

当计算梯度时，RNN需要从最后一个词（苹果）一路回传到第一个词（我）。这个过程就像传话游戏：

\- 第5个人说：“苹果”（目标词）

\- 第4个人告诉第3个人：“误差要调整0.1”

\- 第3个人告诉第2个人：“误差变成0.1×0.9=0.09”

\- 第2个人告诉第1个人：“误差变成0.09×0.9=0.081”

\- ...

如果每一步传递的误差都在衰减（比如乘以0.9），经过多步后，开头的词（如“我”）收到的误差几乎为0，导致它无法被正确调整。

#### LSTM（长短期记忆网络）

简单说就是 **LSTM是给关键信息开了个绿色通道**。现有的翻译软件和语音助手很多也是使用了这个技术。

LSTM结构是专门为解决RNN在学习长的的上下文信息出现的梯度消失、爆炸问题而设计的，结构中加入了内存块。这些模块可以看作是计算机中的内存芯片——每个模块包含几个循环连接的内存单元和三个门(输入、输出和遗忘，相当于写入、读取和重置)。信息的输入只能通过每个门与神经元进行互动，因此这些门学会智能地打开和关闭，以防止梯度爆炸或消失。

![Image 9: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyKjcbpRj3iaCVbz4xRdCX7eician9LMn5RBicd9Hs9KhnD3qdKhfCkB3RsA/640?wx_fmt=other&from=appmsg)

但是基于RNN的变种都会存在一个问题，由于模型在学习训练过程中，依赖文本的输入顺序，必须按时间步顺序计算，无法并行处理序列。

那么我们可以做的更好吗？

三、Transformer

**引子**

Transformer这个概念来自于Google研究团队，在2017发表的一篇论文《Attention Is All You Need》，从发布的名称来看，这个理论将会统一NLP领域，从此以后只需Attention。。。

先讲下什么是 词嵌入（Word Embedding）

将单词向量化，映射为高维向量，使得单词之间的语义关系，可以在向量空间中得以体现。同一语境下的词语往往拥有相近的语义。

比如，可以把词嵌入比作字典里的每个词有一个独特的数字身份证，但这个身份证不是随机的，而是根据词的意思和用法生成的。相似的词在数字空间里位置相近。比如“猫”和“狗”都是宠物，它们的向量可能比较接近，而“猫”和“汽车”就离得远。而这个向量地图通过大量文本数据训练得到的，模型学习词语的上下文，比如Word2Vec、GloVe这些方法。例如，通过预测周围的词，模型调整词向量，让经常一起出现的词向量更接近。

![Image 10: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuykjABwjBiaxsOOqFUPkqiaY29xQvG4eHC7WeTPDw7mWUyJuoubk21HI4Q/640?wx_fmt=other&from=appmsg)

那么是不是每次将词语映射到向量空间都需要重新训练模型呢，当然不是；训练好的模型就像一个字典，比如猫狗鸡鸭这些词语无论在什么语境下都非常接近，我们只需要通过查表的方式去完成映射就可以。但是如果是具备多语义的词语我们该如何处理呢，那么就引出了 Transformer；

**什么是Transformer**

Transformer结构也是参考我们人脑的思维方式，我们人脑在获取信息时会选择性的划重点，忽略掉一些无关紧要的东西。比如“我是一个浙江杭州的程序员，我正在写一篇关于Transformer分享的文章”，人类在看到这句话时的反应都会是 我在写Transformer文章和浙江杭州有什么关系呢？因此我们自然而然的会把注意放在程序员和Transformer上。

Transformer经典架构图

![Image 11: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy1hVdUR8IyKQsLgTcZFSlictiaRmGEHqwibwcZAD7paNwuibvdpt1QlaEcw/640?wx_fmt=other&from=appmsg)

上图是论文中 Transformer 的内部结构图，左侧为 Encoder block，右侧为 Decoder block。红色圈中的部分为 **Multi-Head Attention**，是由多个 **Self-Attention**组成的，可以看到 Encoder block 包含一个 Multi-Head Attention，而 Decoder block 包含两个 Multi-Head Attention (其中有一个用到 Masked)。Multi-Head Attention 上方还包括一个 Add & Norm 层，Add 表示残差连接 (Residual Connection) 用于防止网络退化，Norm 表示 Layer Normalization，用于对每一层的激活值进行归一化。

**举例：用Transformer做中英翻译**

![Image 12: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy7a27jzHj8cAaWfiaFDbsIhasvWFply72YKqlp6BeZZfvRgdK2ohiba7A/640?wx_fmt=other&from=appmsg)

可以看到 **Transformer 由 Encoder 和 Decoder 两个部分组成**，Encoder 和 Decoder 都可以有多个。

训练一个模型的过程大体如下：

![Image 13: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyib1gTJTwstpZhBTTjrdER1axEEkbicw74CPYhHrEbulTcVK9VXWlSpzQ/640?wx_fmt=other&from=appmsg)

假设我们已经有一个训练好的模型，Transformer 的预测工作流程大体如下：

![Image 14: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy19QVagsPWOr1YC4zvibFcFLicjsjnAS6UzwetP6biaCKL1kFA1Dxiak6eA/640?wx_fmt=other&from=appmsg)

**Transformer工作原理**

#### Transformer的输入

![Image 15: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyibjPLsUc3BdkG0lD1srrXp01IJ4zEcIQPcNlMMfHE0YAlP7yYnauBIg/640?wx_fmt=other&from=appmsg)

##### **单词 Embedding**

单词的 Embedding 有很多种方式可以获取，例如可以采用 Word2Vec、Glove 等算法预训练得到，也可以在 Transformer 中训练得到。

##### **位置 Embedding**

因为 Transformer 不采用 RNN 的结构，而是使用全局信息，不能利用单词的顺序信息，位置信息对于 NLP 来说非常重要。计算公式如下：

![Image 16: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyA5bhQHp6Byu7ea8DePWKbxzT2Ahibg49WmvnpD9iaWw6ZKPaqlHolMbQ/640?wx_fmt=other&from=appmsg)

用这个公式的好处是：能够适应比训练集里面所有句子更长的句子、可以让模型容易地计算出相对位置；

#### Transformer的核心机制：自注意力（Self-Attention）

意思就是它不依赖额外输入的信息，即它只统计单词和其他单词之间的注意力（相关性）。

![Image 17: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyOqXiay1k2tk1rBvESjdfTmgNbwJIoufplFRibkianHbAFeMAkfGEKT6bA/640?wx_fmt=other&from=appmsg)

自注意力机制可以让模型在处理序列数据（比如一句话）时，动态关注不同位置的信息。它的实现可以简单理解为以下四步：

1.对每个输入词生成Q(query)、K(key)、V(value)向量。

![Image 18: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyrc2XROlibmZWeCib3FFwuYdbmcbCazaLT0Ul4A4JvOM8gfU6icIFLZdew/640?wx_fmt=other&from=appmsg)

2.计算每个Q与所有K的转置，缩放后得到注意力分数。

![Image 19: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyMXKShEKY9CSNAj7TxyOZkl8Ca5lQOQ3UfvXKEugAaXJR7bWc4vev9A/640?wx_fmt=other&from=appmsg)

3.用softmax归一化分数，，即每一行的和都变为 1，得到权重。

![Image 20: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyrWA9jDqicPtzILoibl2efGSibjmVPI7vZL9xMibIPoLOZDvkILV4mHiawPQ/640?wx_fmt=other&from=appmsg)

4.用权重对V加权求和，得到每个词的输出。

![Image 21: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyLAHEWeh0u64qPr0rcFBNDlsyrZwdWIacNXZyJmsribPrW3ZW42E8vjw/640?wx_fmt=other&from=appmsg)

![Image 22: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyX5B2S2pEEjMKWUGlMsNkbLzCxEnedWYduNfVfAicB28bGHK3kalY6AA/640?wx_fmt=other&from=appmsg)

##### **最终的公式：**

![Image 23: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyOCn5icjJq3YVgsd7TOQnR0PZKUF13ws0hoh1kaFc525etZsmicTlHGdw/640?wx_fmt=other&from=appmsg)

简单地来讲，假设我希望翻译的话就是前图的“我有一只猫”，“我”的query向量q1发出疑问，词“我”、“有”、“一只”、“猫”对翻译我都有什么贡献？这4个词的key向量k1、k2、k3、k4分别跟q1进行相似性匹配；

具体为，先跟q1乘，得到的结果除以![Image 24: Image](https://mmbiz.qpic.cn/mmbiz_png/Z6bicxIx5naKeun2fLND4HlY3iciaqE2SX3RqfXxGXAb6SjGvSDiaQPPAjt1yjtlpJLpwcPC9wIFpcU6HNyuNNu5dg/640?wx_fmt=png&from=appmsg)，再进softmax函数，得到权重值，假设为w1、w2、w3、w4，他们分别去跟v相乘后相加，得到最终的z1 =w1v1+w2v2+w3v3+w4v4，z2同理。

#### 多头注意力 Multi-Head Attention

在上一步，我们已经知道怎么通过 Self-Attention 计算得到输出矩阵 Z，而 Multi-Head Attention 是由多个 Self-Attention 组合形成的，下图是论文中 Multi-Head Attention 的结构图。

![Image 25: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyFTlBicib9ZR6aLWftaR3BNO9YOdqS0SOwRNgBCAtMVwTiaaj6tNPO8tew/640?wx_fmt=other&from=appmsg)

Multi-Head Attention

从上图可以看到 Multi-Head Attention 包含多个 Self-Attention 层，首先将输入X分别传递到 h 个不同的 Self-Attention 中，计算得到 h 个输出矩阵Z。下图是 h=8 时候的情况，此时会得到 8 个输出矩阵Z。换成人话来说就是我们矩阵图中的Wq，Wk和Wv分别初始化了多个进行训练；

![Image 26: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyss4Ha6gq7qKAWiaqUJE1dBm0PjajcVibYoZdOKiaqwhGAevxZdNtOiakTQ/640?wx_fmt=other&from=appmsg)

多个 Self-Attention

得到 8 个输出矩阵 Z1 到 Z8 之后，Multi-Head Attention 将它们拼接在一起 (Concat)，然后传入一个Linear层，得到 Multi-Head Attention 最终的输出Z。

![Image 27: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyyOBuruOiaia5xyzaoKqng4EYKpcPkcf45PxWRbKfvTRBsmCViaOiadk4JQ/640?wx_fmt=other&from=appmsg)

Multi-Head Attention 的输出

可以看到 Multi-Head Attention 输出的矩阵Z与其输入的矩阵X的维度是一样的。

![Image 28: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyu09IpDYjMTjeZicmnDpdI2KhPktIC764R72SLaJKUic5vicnwSJOZWcgw/640?wx_fmt=other&from=appmsg)

上图左为二头的着色结果，同样的”The animal didnt cross the street because it was too tired“这句话，我们想知道翻译it的时候这个词跟什么词有关，或者说哪个词对于翻译it更有效。

从二头的着色结果来说我们从橙色知道it指代了The animal，从绿色知道it的状态是tired，从五头的着色我们可以知道it的更多信息，这种关联性可以在翻译中给it更多的解释角度。

##### **举例**

![Image 29: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuylqEjHHviajA2iaehAETEOlVn6uJORFtmoACf0Gntibv5pyN1flgmfdHyQ/640?wx_fmt=other&from=appmsg)

在一句话中注意力往往要从多个角度进行分析，比如 “大学生“是考研这个单词的主体，”除了“表示考研在这个句子中的角色，”上班、创业“都是考研这个词替代；因此我们需要从不同的角度去进行学习，防止它们过度的相似。

我们可以给不同的注意力头选择不同的训练任务，比如一些注意力头去做完形填空，一些注意力头去预测下一个句子，不同的注意力头之间的训练是并行的，基于Transformer架构可以高效的训练超大规模的模型。

如下示例 每个头都会关注到不同的信息：https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello\_t2t.ipynb#scrollTo=OJKU36QAfqOC

![Image 30: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyNxhrDRmaibxNQufbOdSicSlnjezv4ibg4jia7SD0T63LlLQ9cmwuvkLhSg/640?wx_fmt=other&from=appmsg)

#### Add & Norm 层的作用

1.**残差连接**：缓解梯度消失问题，保留原始信息。

2.**层归一化：**加速训练，提高模型稳定性和泛化能力。在Transformer中，Add & Norm 层是模型能够高效训练和表现优异的关键组件之一。

#### Feed Forward的作用是

Feed Forward 层（也称为前馈神经网络）的作用是对自注意力机制输出的特征进行进一步的非线性变换和特征提取；

1.**非线性特征变换：**引入非线性激活函数，增强模型的表达能力。

2.**特征增强：**对自注意力机制的输出进行进一步处理，提取更丰富的特征。

3.**独立处理每个位置：**专注于每个位置的特征优化。

4.**增加模型容量：**通过额外的参数提高模型的拟合能力。

#### Encoder

Encoder block 接收输入矩阵 X(n×d) ，并输出一个矩阵 O(n×d) 。通过多个 Encoder block 叠加就可以组成 Encoder。

#### Decoder

![Image 31: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuyT036H4GcxpUUIfjdPcvbKLKPm2o5pYXfibcZLG6V5qia2kfJ0YrX689w/640?wx_fmt=other&from=appmsg)

*   包含两个 Multi-Head Attention 层。
    
*   第一个 Multi-Head Attention 层采用了 Masked 操作。通过 Masked 操作可以防止第 i 个单词知道 i+1 个单词之后的信息。
    

![Image 32: Image](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naJ35YiazaSniab217JvqoXFuy32UL8LRcawKNXLSYaXIxn7MeOtxeKa8FqPBPMhsVE42DwOYB6fTztA/640?wx_fmt=other&from=appmsg)

*   第二个 Multi-Head Attention 层的**K, V**矩阵使用 Encoder 的**编码信息矩阵****C**进行计算，而**Q**使用上一个 Decoder block 的输出计算。这样做的好处是在 Decoder 的时候，每一位单词都可以利用到 Encoder 所有单词的信息 (这些信息无需 **Mask**)。
    
*   最后有一个 Softmax 层计算下一个翻译单词的概率。
    

#### Transformer 总结

*   Transformer 与 RNN 不同，可以比较好地并行训练。
    
*   Transformer 本身是不能利用单词的顺序信息的，因此需要在输入中添加位置 Embedding，否则 Transformer 就是一个词袋模型了。
    
*   Transformer 的重点是 Self-Attention 结构，其中用到的 Q, K, V矩阵通过输出进行线性变换得到。
    
*   Transformer 中 Multi-Head Attention 中有多个 Self-Attention，可以捕获单词之间多种维度上的相关系数 attention score。
    

**参考：**
-------

*   ﻿https://github.com/datawhalechina/learn-nlp-with-transformers﻿
    
*   ﻿https://tech.dewu.com/article?id=109﻿
    
*   ﻿https://zhuanlan.zhihu.com/p/338817680﻿
    
*   ﻿https://arxiv.org/pdf/1706.03762﻿
    

**代码智能生成，AI编码助手搭建攻略**

随着人工智能技术的飞速发展，开发人员面临着代码编写效率和质量的双重挑战。为了提高编程效率、减少错误并加速创新，市场对智能编码助手的需求日益增长。本方案旨在介绍如何部署AI模型，构建一个基于私网的AI编码助手，以辅助开发者高效完成编程任务。

点击阅读原文查看详情。

预览时标签不可点

Close

更多

Name cleared

![Image 33: 赞赏二维码](https://mp.weixin.qq.com/s/BxpWFwXFbpur_gTuzSEsSA)**微信扫一扫赞赏作者**

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

[Read more](javascript:;)

Close

更多

搜索「」网络结果

[Read more](javascript:;)

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

![Image 34](https://mp.weixin.qq.com/mp/qrcode?scene=10000004&size=102&__biz=MzIzOTU0NTQ0MA==&mid=2247547044&idx=1&sn=ee19716b65cec5e302bc1ff6fa6fddd7&send_time=)Scan to Follow

继续滑动看下一个

轻触阅读原文

![Image 35](http://mmbiz.qpic.cn/mmbiz_png/Z6bicxIx5naI1jwOfnA1w4PL2LhwNia76vBRfzqaQVVVlqiaLjmWYQXHsn1FqBHhuGVcxEHjxE9tibBFBjcB352fhQ/0?wx_fmt=png)

阿里云开发者

向上滑动看下一个

当前内容可能存在未经审核的第三方商业营销信息，请确认是否继续访问。

[继续访问](javascript:)[Cancel](javascript:)

[微信公众平台广告规范指引](javacript:;)

[Got It](javascript:;)

 

![Image 36](https://mp.weixin.qq.com/s/BxpWFwXFbpur_gTuzSEsSA) Scan with Weixin to  
use this Mini Program

[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

× 分析

 : ， ， ， ， ， ， ， ， ， ， ， ， .   Video Mini Program Like ，轻点两下取消赞 Wow ，轻点两下取消在看 Share Comment Favorite 听过            

![Image 37](blob:https://mp.weixin.qq.com/fa93ed24361e9047225450ffd4582b71)

**阿里云开发者**

Transformer到底解决什么问题？

,

,

选择留言身份
