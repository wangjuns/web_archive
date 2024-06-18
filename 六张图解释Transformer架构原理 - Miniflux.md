# 六张图解释Transformer架构原理 - Miniflux
 #六张图解释Transformer架构原理##模型时代#  
 
很多AI创新公司的专家，也包括一些高校学者，都很喜欢做AI的知识普及工作。  
现在分享的是LightningAI的首席数据科学家Akshay（x.com/akshay_pachaar）所做的六张图解释Transformer，相当清晰明了。

1、图一：在我们开始之前，让我们简要介绍一下 tokenization！  
原始文本 → 分词 → 嵌入 → 模型  
嵌入是使用一堆数字对每个token（大约一个词）进行有意义的表示。  
这个嵌入是我们提供给语言模型作为输入的。

2、图二：语言建模的核心思想是理解语言中的结构和模式。  
通过对句子中的单词（tokens）建模，我们可以捕捉文本的上下文和含义。

3、图三：现在自我关注是一种帮助建立这些关系的通信机制，表达为概率分数。  
每个token都会给自己最高分，并根据它们的相关性给其他tokens分数。  
您可以将其视为一个有向图（Directed Graph）。

4、图四：了解这些概率/注意力分数是如何获得的：  
我们必须理解 3 个关键术语：  
\- 查询向量  
\- 关键向量  
价值向量  
这些向量是通过将输入嵌入乘以三个可训练的权重矩阵而创建的。

5、图五：现在让我们更全面地了解输入嵌入是如何与键、查询和数值结合以获得实际的注意力分数的。  
获取密钥、查询和值后，我们将它们合并以创建一组新的上下文感知嵌入。

6、图六：使用 PyTorch 实现自注意力，再也不会更简单了！ 🚀 这非常直观！ 💡

[![](https://rss.tsinling.workers.dev/image/wx2.sinaimg.cn/large/49858279gy1hqo1l3l43lj235s2l4am0.jpg)
](https://rss.tsinling.workers.dev/image/wx2.sinaimg.cn/large/49858279gy1hqo1l3l43lj235s2l4am0.jpg)

[![](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1l5xxvpj235s25vk0i.jpg)
](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1l5xxvpj235s25vk0i.jpg)

[![](https://rss.tsinling.workers.dev/image/wx1.sinaimg.cn/large/49858279gy1hqo1kznj05j235s209gyo.jpg)
](https://rss.tsinling.workers.dev/image/wx1.sinaimg.cn/large/49858279gy1hqo1kznj05j235s209gyo.jpg)

[![](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1lcoy3nj235s2e212k.jpg)
](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1lcoy3nj235s2e212k.jpg)

[![](https://rss.tsinling.workers.dev/image/wx3.sinaimg.cn/large/49858279gy1hqo1lekl94j235s2cpwq8.jpg)
](https://rss.tsinling.workers.dev/image/wx3.sinaimg.cn/large/49858279gy1hqo1lekl94j235s2cpwq8.jpg)

[![](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1m0tr8hj235s2m9h13.jpg)
](https://rss.tsinling.workers.dev/image/wx4.sinaimg.cn/large/49858279gy1hqo1m0tr8hj235s2m9h13.jpg)