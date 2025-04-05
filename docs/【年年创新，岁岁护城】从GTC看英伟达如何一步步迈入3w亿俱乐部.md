# 【年年创新，岁岁护城】从GTC看英伟达如何一步步迈入3w亿俱乐部
![](https://mmbiz.qpic.cn/mmbiz_jpg/614RnbPwb18k6rMjPUBl9mCfEsS6NbfEB36asKdxMnaR2lRqw4CZpzHOAG8GPrIEaNVT5UatStTk0js2p5jWPA/640?wx_fmt=jpeg)

GTC全称为GPU Technology Conference，是由英伟达举办的全球开发者大会。最初的主题仅限于GPU，后来扩展到深度学习和人工智能相关领域。首届GTC于2009年在加州圣何塞举行，每年举办次数不等，最少一次，通常在春季3月份召开。有时会在秋季再次举行，更新当年的进展。此外，会议地点也可能变更，除了美国有固定场次，欧洲、中国、日本等地都有过举办的记录。

GTC大会通常持续约2小时，主要由黄仁勋主讲，偶尔会邀请嘉宾助阵。这2小时的演讲充满技术干货，旨在向业界传达英伟达在软硬件方面的最新进展，以及与合作伙伴的最新动态。演讲涉及的技术细节丰富，非相关领域的开发者亦不太容易完全理解。然而，黑衣客老黄总是完整记住所有细节并逐一讲解，敬业精神可嘉。同时，他的演讲技巧娴熟，颇有乔布斯当年的风采。

不少投资机构，例如木头姐等，一直困惑于为什么英伟达没有如他们预期的开始走下坡路？为什么AMD不能成为有竞争力的第二名？为什么英伟达没有重蹈当年Cisco的覆辙？其实如果他们有仔细研究GTC大会的话，这些困惑是可以迎刃而解的。  

笔者因工作所需，自2016年起开始关注GTC大会，并于2017年参加了中国区的现场，之后每年都在线观看，收获颇丰。本文旨在梳理2016年起历届GTC大会中AI相关的亮点和趣闻，和读者一同了解这8年来英伟达如何一步步超越自我，跻身市值3万亿美元俱乐部的传奇历程。

（本文借助AIGC进行润色和配图，另外感谢@宝玉xp的Review，如果你能坚持看到最后，很大程度可能是得益于他的建议）

### \[GTC 2016\] 新一轮科技革命的种子：DGX-1

https://www.youtube.com/watch?v=npzRyTimcZo

本文之所以选择2016年Europe这一场的GTC作为起点，主要有几个原因：

1.  1. AlphaGo在2016年初打败了李世石，这是人工智能领域的一个重要里程碑，也是开启了之后的AI春天
    
2.  2. 从这一年开始，英伟达正式将GTC大会定义成为深度学习和人工智能的会议，重心开始完全迁移到人工智能上
    
3.  3\. 在本年度的GTC，英伟达推出了DGX-1（P100版本），并提到了捐献给OpenAI。这成为了历史的一段佳话，也为AI引领下一场科技革命的浪潮埋下了种子
    

所以这是AI非常重要一年，也是GTC开始变得有意思的一年。从2016年开始，GTC就开始成为AI专业人员的年度小众盛会。

1.  **1\. 支持NVLink的P100**
    

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jD4dCH0Vq5BGoIRmtlSddlCRnwtawZ99x6ZYCdCI0gscA47LCWOhNKg/640?wx_fmt=png)

  

在这一年，NVIDIA发布了的Pascal架构GPU，P100。这是第一款以100为后缀的训练系GPU，后面就一直沿用该命名风格（之前的是K80）。P100基于Cuda核心，支持混合精度和3D内存，其FP 16的性能是21.2 TFLOPS，虽然这在现在看来完全不够用，但是比上一代已经强很多了。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jVB7cwicbUhImwtzZYicWKN2kduwZVFJzWYibPuYaY1pmJgcRLMaW0fWtg/640?wx_fmt=png)

  

需要留意的是，从这一代的GPU开始正式支持NVLink，这是一个标志性的事件，它意味着英伟达的GPU开始正式迈入多机多卡的时代，并带来了DGX-1。

1.  **2\. 新科技革命的种子：DGX-1**
    

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jt37djibRKqQ9v1ibPyFUbQfRw9cSPxEIKgaTXxoONUOgr4FUwBZBBw4w/640?wx_fmt=png)

  

从P100开始，英伟达就开始推广对应的DGX，主打就是一个开箱即用 + 性能全开，当然价格也是顶级，适合土豪。第一代的DGX-1，配备了8个Tesla P100 GPU，性能达到170 TFLOPS。虽然现在看起来没什么，但是在当时可谓是顶配了。

DGX-1的初始合作伙伴是SAP，英伟达期望通过SAP来触达更多的数据科学家和算法工程师，可惜最终还是是错付了。还好，老黄没把鸡蛋放一个篮子里，在视频的46：57，他提到了DGX-1要交付给最好的科学家，也就是OpenAI的手里，于是也就有了下面这张经典的照片（Aug. 15， 2016），这成为了历史的一段佳话，也为AI引领下一场科技革命的浪潮埋下了种子。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jfgNgficvwXSKuZVLZribgE2icuAq6xIBLByBaqZJOpIeQmBUReIcplyYQ/640?wx_fmt=png)
在2017年，英伟达推出了新一代的DGX-1V，基于8块V100设计。这款性能更强，性能从170 TFLOPS提升到了960 TFLOPS，后来两者都叫DGX-1。需要注意的是，他送给OpenAI的是第一代DGX-1，也就是P100版本。![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jukWGAVibYmZVa9eN13J0HC1UniaF71jPlJAPl9WmPzVyRjliaShYmicbKw/640?wx_fmt=png)

> 从这一年开始，英伟达专注于AI和数据中心市场，其GPU被广泛用于深度学习和AI应用，提升了投资者的信心，股价大幅上涨。

> 2016年12月31日，NVIDIA股价为106.74美元，市值增长到630多亿美元，全年股价和市值上涨了233%

###  \[GTC 2017\] Tensor核心的V100，开拓AI新时代

https://www.youtube.com/watch?v=F3g7A4q0sO8

2017年的GTC是一个关键的转折点，AI变得炙手可热，老黄马不停蹄的开了4场GTC大会（可能还不止），包括在中国苏州，笔者也是在这一年首次线下参加GTC大会，现场感受到了浓厚的AI氛围和创新精神。

#### 1\. i am ai

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jduPo3ZPRlWrtUvKXibvEVn1IdibbzlHhEb2EIehV3rWk85ADGryMGFMw/640?wx_fmt=png)

  

从这一年开始，GTC大会开始引入“i am ai”作为开场视频，并一直沿用至今。该视频的音乐是由AIVA的人工智能AI作曲生成的。2017年-2020年，是由好莱坞交响乐团的Fox Studios所演奏；而从2021年到现在，则是由伦敦交响乐团演奏。而每年开场视频的内容细节，都会根据当年产品和技术的最新进展做Update，情怀满满。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jwKqyFc3OFl1KnO5oWWVUz6gW0hB0tbgL31x3x5yP3leqMHLVsFAhyw/640?wx_fmt=png)

  

#### 2\. 引入Tensor核心的V100

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jU4UCsIuUU1q5OpA5T90iapyshKGgMPhOfzwj06icbg3CYKHdPy1gsXrA/640?wx_fmt=png)

  

这是英伟达All in AI的关键点。Tensor（张量）是深度学习的核心基本元素（注意不是Vector，不是向量）。谷歌TensorFlow的成功，也在于其完全以Tensor为核心设计，英伟达也看到了这个本质。所以从V100开始，设计核心针对Tensor进行了相关优化，当然，还是保持Cuda兼容和支持。这在当时看来是非常大的一个冒险，A giant leap。因为这意味着如果不做AI，这些计算卡的性能优势就荡然无存了。但是多年后回头看，却发现这是一个无比正确的决定。

受益于核心的升级，V100的关键性能达到了120 TFLOPS，接近上一代的P100的6倍，NVLInk的带宽也达到了300GB。这是非常成熟的一张数据中心卡，直到2024年，它依然可以降级作为大模型的推理卡，部署SD大模型进行推理，生命周期非常长，相当能打。某种意义上，V100开拓了AI的一个新时代。

#### 3\. SXM接口

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jXBkR2ndop3cArYMkRsRuFWhouXCAOBHhOCypwiaxau22cWOBaTjtKrg/640?wx_fmt=png)

在这次大会上，你会发现，老黄手中展示的显卡不再像传统的显卡，而是如图片所示的样子（去年推出的P100也是这样，但未做实体演示）这是全新的SXM接口的V100，而不是PCIe接口。实际上，V100支持两种接口，SXM采用了更高带宽的NVLink 2.0互连，更适合服务器应用。但PCIe接口的卡依然保留，这可能是基于以下考量：

1.  1. **兼容性和灵活性：** PCIe是一个通用的行业标准，支持PCIe的主板和服务器非常普遍。提供PCIe版本可以让V100与更广泛的系统兼容，给用户更多的选择和灵活性。
    
2.  2. **升级现有系统：** 对于一些已经有PCIe基础设施的机构或企业，使用PCIe版本的V100，可以方便地升级现有系统，而无需更换主板或做大规模的硬件改造。
    
3.  3. **成本考虑：** 虽然SXM版本在性能上有优势，但其定制化的设计也可能带来更高的成本。对于一些对性能要求不是极高，但仍希望使用V100的用户，PCIe版本可能是一个更经济的选择。
    

所以，虽然SXM有更好的性能，英伟达还是保留了PCIe版本，一直到目前的H100。如果你的PC足够强大，功率足够，拆下一块PCIe的V100还能接上作为高性能显卡用。但是，如果是为了AI数据中心的多机多卡专用，SXM无疑是更好的选择。

#### 4\. The More You Buy，The More You Save

这个梗在2017年的GTC上，被老黄反复多次提到。一个Rack的DGX V100，可以抵得上一排的传统服务器的Rack，老黄对这个演示动画的商业效果很满意。2017年的多场GTC都就反复演示了。在2018年成就了这句经典，在场的观众都可以笑着帮他念完下一句了。老黄的商业销售技巧在这里得到了充分的体现。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jka9ToYybCUxdcPsZMibvyWfQWNSzE4GsnRoozOLRiboWgR9J0KsultAg/640?wx_fmt=png)

  

> AI需求的持续增长和V100的强大性能，进一步推动了2017年的股价上升。有趣的是，首发V100的当天，英伟达股价在一天内上涨约17%，成为最吸金的一次GTC。

> 2017年底（12月29日），NVIDIA股价上升至193.60美元，市值增长至1172.6亿美元，全年股价和市值上涨103.82%。

### \[GTC 2018\] 推理三利器：T4，TensorRT和Triton

https://www.youtube.com/watch?v=95nphvtVf34

如果说2017年的GTC重头戏是训练，那么2018年的重头戏就来到了推理，毕竟模型训练好了，就要上线部署推理了。所以在2018年的GTC大会上，无论硬件还是软件，都是针对推理进行优化的。

#### 1\. 推理专用卡T4

在推出V100之后，训练好的模型变大，之前的P40和P4很明显就不够用了，于是T4就应运而生了，它继承了 Vlota和Turing 的各种创新，包括 Tensor Core 和 RT Core，性能提升明显。和上一代P4只针对INT 8优化不同，它支持混合精度的计算，所以在FP 16和INT 4的表现也相当不错，整体而言是一张非常不错的推理卡。它配备 16 GB 的 GDDR6 显存，功率只有70w，只有PCIe接口，在数据中心和边缘侧都可以部署，也能稍做一张高级的显卡用。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb191vzuE64Fr2fy8zvPbJfwL1LFfGNzFUVh4V2ClKhiaTaOOfaFB2lOpibYnQg8TcaiaaCaT3tOibacUrg/640?wx_fmt=png)

  

借助T4，各个经典模型，例如ResNet-50，YOLO 等，推理的完整耗时可以轻松达到10ms以下，这对于线上服务来是一个关键可用指标，也是深度学习模型开始大规模应用于线上服务的一个分水岭。

#### 2\. TensorRT

推理的硬件有了，那必然需要推理的软件来优化。2016年，当时的几个开源框架，都是重训练而轻推理的。英伟达看到了这一点，所以就开发了TensorRT并开源。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb191vzuE64Fr2fy8zvPbJfwLukHxf8KdJUh6HjTibRcwyJvk6kNo44lVzmNBWPrsTuoGFYkA96ah6yw/640?wx_fmt=png)

  

TensorRT的定位是高性能的通用模型引擎，它可以对模型进行各种优化后加载，包括无损降低精度、层和张量融合、多流执行和时间融合……再把服务接口暴露给上层推理服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb191vzuE64Fr2fy8zvPbJfwLkN8icyXhHwR6zg2GjcTxibZ49fkrnYmwvkk0cxFrFZ5DEGHLXHianEJQQ/640?wx_fmt=png)

其实TensorFlow和PyTorch框架，后来也都开始重视推理了，各家都有自己的推理引擎和优化，但是一般只是针对自家模型。而TensorRT支持所有的模型格式，包括ONNX，所以对于不想绑定在具体框架上的用户来说，依然是个很好的选择。

#### 3\. Triton

其实，TensorRT一开始包含了更多复杂功能，包括推理的服务调度等。然而到了2018年，英伟达的工程师们意识到这样做架构设计很难做符合到KISS原则，于是他们将推理的服务功能分离出来，创建了Triton Inference Server。这一调整使得TensorRT可以专注于高性能模型优化，而Triton则专注于推理服务的管理和部署。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb191vzuE64Fr2fy8zvPbJfwLyhj3ic7A1vZYzNqzO1qibRNVuPokku3P0icoMknxnatE6P9lesk0zLysg/640?wx_fmt=png)

image.png

架构图如下，可以看出，它把TensorRT和其他深度学习框架的推理引擎放在了同等的位置，不需要强绑定。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb191vzuE64Fr2fy8zvPbJfwL74WiacZx1pP8YNKDKR9wrtSkU3mibwFezewOyrEicTrVjMF0zn6QFv6UQ/640?wx_fmt=png)

架构分离后，两个项目的目标设计变得更加清晰，各自也得到了更好的发展，吸引了不少专业开发者的关注和Star。它们成为中小企业友好的分布式推理开源解决方案。  

#### 4\. GPUs on K8s

K8s的成熟，对于英伟达的GPU是非常关键的，有实际GPU运维经验的同学都知道。在2018年之前，K8s对GPU的支持是有多不稳定，而日落西山的Yarn就更加不用说了，架构上就和GPU天然不搭。在2018年，K8s和GPU终于能够良好地搭配，为英伟达的GPU提供良好的虚拟化和用户隔离，这对云服务来说，是非常关键的一步。

借助K8s，GPU Cloud可以提供更加灵活的GPU服务，包括分时分片，多租户等等…… 从而可以将一个高端GPU，虚化成多个低价的GPU，对外提供推理服务，从而吸引到更多的用户。  

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jGXYu5MDmiaEbALXe439UUFniaqmfRPBnuCJhazzicF0poUrJH4t6BKY2g/640?wx_fmt=png)
到了2024年，TensorRT，Triton与GPU on K8s相融合，一起成为NIMs的一部分。这种整合进一步提升了它们的性能和易用性，为更多企业提供了高效的AI推理解决方案。

> 由于2018年10月份高估值的科技股的整体下调，虚拟货币市场崩盘和数据中心收入增长放缓，英伟达股价在2018年下滑。

> 2018年底（12月31日），英伟达的股价下跌至133.50美元，市值降至814.3亿美元，全年股价和市值下跌了30.55%。

### \[GTC 2019\] 成功收购Mellanox，补齐NVLink生态

https://www.youtube.com/watch?v=Z2XlNfCtxwI

2019年的GTC大会，说实话有点沉闷。AI领域暂未出现突破性的进展和应用，BERT虽然在2018年底发布，但当时的前景还不明朗。而英伟达没有推出新的服务器卡，发布重头戏是游戏端的RTX显卡和Ray Tracing，整体上显得乏善可陈。尽管如此，这一年英伟达还是做对一件非常关键的大事：

#### 1\. Mellanox

提到Mellanox，就要先了解一下NVLink的生态，作为NVIDIA的核心互联技术体系，大抵可以这样划分：

*   • **NVLink：** 用于单一计算节点（服务器）内部的高速 GPU 互连
    
*   • **NVSwitch：** 用于同一机架（Rack）内的计算节点之间的高速互连
    
*   • **InfiniBand：** 用于跨机架（Rack）和更大范围的数据中心内的高速互连
    

在2019年之前，用户在购买英伟达服务器时，通常需要搭配Mellanox的网卡，因为它是InfiniBand领域的领头羊。这一组合几乎是标配，成为了强依赖，老黄敏锐地意识到这一点，于是决定花重金（70亿美元）收购Mellanox。这笔交易在2019年3月份宣布，并于2020年4月份完成。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04j1gCL8fHPYbL8vSjcQhB569t7JmrTrMjCoS917h405Wge1wR5Mia5USw/640?wx_fmt=png)

image.png

在这届GTC大会上，老黄宣布了这一重大决定，并与Mellanox的CEO同台交流，展示了两家公司合作的友好氛围。Mellanox的收购，对于大规模的GPU机房建设非常关键，也是实现LLM的基础。

从这件事情可以看出，老黄对产品细节的战略敏感度非常高。一旦发现自己的产品与其他厂商的产品经常紧密绑定，就会考虑要么自己做一个更好的，要么收购那个厂商。对于ARM的收购尝试也是出于同样的逻辑，可惜最终被英国的反垄断部门阻止了。

#### 2\. 自动驾驶

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jsMSCVLKzToColW6Jez9vxTUxquuSOdKcNATeAqiaZQrhUzutZTLsbCQ/640?wx_fmt=png)

  

英伟达其实从2017年的GTC大会就开始大力推广自动驾驶技术，并不遗余力地展示其硬件和软件解决方案，从上图来看，不可谓不丰富。然而，自动驾驶领域竞争异常激烈，许多技术公司都在开发自己的解决方案，包括特斯拉、谷歌和众多车企公司，它们在这个领域投入了大量资源，形成了激烈的竞争格局。

英伟达的车载方案，无论是硬件还是软件，都未能显著拉开与对手的差距，且价格偏高。在选择合作伙伴方面也存在不足，2017年的宝马和2019年的丰田，都未能在该领域成为佼佼者。而特斯拉选择了自动驾驶用自主开发的芯片，娱乐系统用AMD的Ryzen芯片，使得英伟达在这个领域显得非常尴尬。即便到了2024年，英伟达发布的惊艳四座的财报中，汽车芯片的收入和增速依然是垫底的（不算“OEM和其他收入”的话）

因此，在后来的GTC大会上，自动驾驶的介绍时间和篇幅逐渐减少。而老黄也意识到过度依赖合作伙伴的弊端，开始在机器人领域全力投资初创公司，例如Figure AI，以避免类似的困境再次发生。从这个事情也可以看出，英伟达所处的领域，竞争是多么激烈和残酷，很多客户实际上又是竞争对手，它需要保持高度的领先性，才能确保自己的生存。

> 得益于数据中心市场的复苏，以及战略性成功收购Mellanox技术公司，加上美股市场的整体上行，英伟达的股价得到了强劲反弹。

> 2019年底（12月31日），NVIDIA股价上涨至235.30美元，市值增至1440亿美元，全年股价和市值上涨了76.83%。

### \[GTC 2020\] 面向LLM的A100和Megatron

https://www.youtube.com/watch?v=bOf2S7OzFEg&list=PLZHnYvH1qtOZ2BSwG4CHmKSVHxC2lyIPL

众所周知，2020年是非常特殊的一年，GTC大会也从线下转到了线上，无论是春季还是秋季。虽然疫情影响严重，但它并未削减大家对新技术的热情。人们依然保持乐观，相信疫情终将很快过去…

因此，今年GTC的梗是厨房梗。这场大会是在黄仁勋家的厨房举办的，而当他介绍A100服务器时，转身从背后的烤箱中取出了一台DGX-A100服务器，效果还是挺酷的。如果不小心把烤箱开了，那这台价值19.9万美元的设备怕是要灰飞烟灭。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04j7GIulCtJL2mYI2gRbRyQQUlOUQaLr0pNWa4aMu7zwSJGCVibJhsQQKw/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jMhT1CxRwHLahiaserAiahC84hiav2Bs842DkC6CA8icI6ftf5gCY1ribS9g/640?wx_fmt=png)

  

1.  **1\. 面向LLM的A100**
    

言归正传，谈谈A100的设计。A100在核心架构上没有进行架构升级，仍然采用Tensor核心，但相比于V100进行了大幅度提升。2017年，《Attention is All You Need》带来了Transformer；而2018年，《Bidirectional Encoder Representations from Transformers》带来了BERT，对AI有高敏感度的英伟达，也该针对LLM进行硬件优化了。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jhQOp3x17fd8NGFfoeoOkTxJsoPJhWFj75K97x0vAxwSZIAAv4GA1iaA/640?wx_fmt=png)

  

A100的主要改进有：

1.  • **显存提升：** 上半年的显存已经提升了为40G，在下半年新增了80G的版本。
    
2.  • **Tensor Core：** 引入了32位和稀疏计算加速，更好地适配高精度的复杂训练场景。
    
3.  • **带宽提升：** NVLink 3.0的单条链路带宽达到了50 GB/s，而NVLink 2.0为25 GB/s。整体带宽提升了一倍，从而显著提高了GPU之间的数据传输速度。
    

得益于这些优化，A100的性能提升是巨大的，很多是10x-20x级别的，包括FP32（16->160->310），FP16（125->310->625）……拉开了和V100的距离。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jOLpBcS4bU5LBbszDj1Sd7iacJ7ToebCoLLkJqIP2HbLroAgqdRico6Og/640?wx_fmt=png)

  

而借助MIG的隔离技术，A100可以在物理层面上1虚7，每个的推理性能，都相当于一个V100，对云服务非常友好。在接下来的几年，英伟达都没有推过T4的继任。（直到2023的L40和L4）

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jHfmvA55OeZRCTbT8GDXVsat4zPa92CabjdhUUbXSzORzPQTqrcGgyg/640?wx_fmt=png)

  

即便到了2024年，A100依然是国内市面流通的香馍馍，因为凭借它可以方便的组成w卡级别的集群，进行LLM基座模型的预训练，虽然效率比下一代H100差一些，但是应对各种LLM还是游刃有余的。

#### 2\. 略微小众的Megatron

2020年，随着以BERT为代表的LLM的兴起，多机多卡的训练方案再次受到广泛关注。即便当时流行的V100，后面的A100显卡，也难以单机完成大规模模型的训练。而这一需求的变化促使了深度学习框架的转变，PyTorch逐渐兴起。

然而，原生PyTorch的多机多卡能力有限，各种基于PyTorch的分布式训练加速框架应运而生。其中，微软的DeepSpeed最为成功，但英伟达也推出了自己的通用解决方案——Megatron。如果没有DeepSpeed，Megatron可能会成为最受欢迎的PyTorch分布式加速框架之一。  

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jGv0VsVOYKqcPLCGM8lSUXMlWuuQrlIV6eWWmhKOrQZSFsMITKQ7ibDA/640?wx_fmt=png)

在2020年的GTC大会上，有一个专门介绍Megatron的在线演讲。Megatron通过融合数据并行和模型并行，混合精度训练和优化Transformer架构，对PyTorch做了些许的修改 （主要是加入少量通信操作），就在512个GPU上成功训练了一个8.3B大小的模型，这在当时是非常不错的成就。对Megatron感兴趣的同学可以查看这篇详细的论文《Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism》

但是因为DeepSpeed实在太成功了，所以后续Megatron后续重点转向了分布式多机推理，旨在解决大模型的推理瓶颈。这个项目至今仍然非常活跃，已经获得了近1万个Star。未来，Megatron有可能像TensorRT和Triton一样，成为一套完整解决方案中的重要一环，提供给用户。

通过这些技术，英伟达展示了其在软件方面的持续创新和贡献，并不仅仅是一家硬件公司，也不是仅仅有Cuda。

疫情期间，居家办公和娱乐需求激增，推动了游戏和远程工作解决方案的需求，其游戏显卡和数据中心产品在市场上表现优异，显著提升了英伟达的收入和股价。

> 2020年底（12月31日），NVIDIA股价飙升至522.20美元，市值增长至3232.4亿美元，全年股价和市值上涨了124.47%。

### \[GTC 2021\] 精彩的伏笔：Grace CPU

https://www.youtube.com/watch?v=eAn_oiZwUXA

这一年的GTC还是线上举行，老黄的头发变长了，也变白了，颇有披头士的风范。但是会议整体上显得有些沉闷，没有新的GPU发布，AI技术也整体上趋于平淡。不过老黄为未来的战略布局埋下了一个重要的伏笔，那就是Grace CPU。

#### 1\. GraceCPU

虽然GPU在高性能计算中扮演着重要角色，在并行计算任务上有着绝对的优势。但CPU的辅助作用同样不可忽视。一台服务器需要CPU来处理复杂逻辑和周边任务，例如I/O控制，内存管理，多GPU协调……而如果这些辅助任务处理不好，就会严重影响GPU的效率。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jHuBNQQUmzzbLft1JojkCOM7sZEGDaXII0hGiaTkYCHbzsYqP1dQgkgA/640?wx_fmt=png)

image.png

从上图可以看出，在之前的GPU服务器中，x86的CPU已经日渐成为CPU内存和GPU内存之间的带宽瓶颈。在2016年与IBM合作不太顺利之后，英伟达与竞争对手Intel的合作也遇到了一些阻碍。因此，在这一年，老黄终于推出了基于ARM架构的自家CPU芯片，即Grace CPU。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jAiagYv69Gq3GdCtIqNZDHn7XTmmh5g36jZ2hELLwH2Mjy4LHFPsib4icg/640?wx_fmt=png)

image.png

通过对比可以看出，通过引入新的内存和GRACE GPU，在同一块SXM卡上整合了CPU和GPU，通过高带宽和内存一致性的NVLink Chip-2-Chip (C2C)互连技术，实现更高效的数据处理和任务分配，解除通信效率和带宽的瓶颈，从而显著提升整体性能。这种设计允许多个GPU更紧密的协同工作，形成一个超大的GPU超级芯片。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jicVRmEYyOmvHD3Pwr9k0nibFCXtmpcSV22QZibDibQ7q9XOosMNqhGxavg/640?wx_fmt=png)

因为GraceCPU是ARM架构，参考Mellanox的成功Case，老黄试图收购ARM。然而，这笔交易遭到了英国的反垄断调查和反对，最终在第二年告吹。尽管如此，这并不影响英伟达开发自家的CPU，只是需要向ARM支付许可费用，而且也并且不能掌控ARM的未来发展方向。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jWUnA74owAKQpdx6dk6X6qopcgpDOiacib0q1hfDPUyKUKSH5vmB1RqcQ/640?wx_fmt=png)

  

在2023年的GTC大会上，在介绍Grace-Hopper时，老黄展示了Grace CPU全面战略。借助CX7和Grace CPU，CPU和GPU可以像乐高积木一样进行任意组合，不仅提升了整体性能，还提供了更高的灵活性和扩展性。

#### 2\. 虚拟数字人老黄

在这一年的GTC大会上，有15s的老黄是虚拟数字人代替的，在视频的1小时02分，开始有特效，分解厨房，然后切换场景，来到虚拟空间，这是的老黄切换成数字人了，从远处看，肢体语言和口型，确实都是有些不太自然的，没有太玄乎。SIGGRAPH 2021揭秘这个的时候，引起了不小的轰动，主要是有些媒体的标题党报道，让人们以为整个GTC 2021的演讲都是虚拟人，那效果就不要太震撼了。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jOTXHqCLs407SRqylWeiawdYg81Pp2BqicqQFVcmubN2wF37zHfhRuSkg/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibDkofH0UfokyWDmuXXp04jMXpzmzolF3jFibTiaWbkPfx6wjUDyKklHQoD4GhPnzDU6q9Dia2InKFJA/640?wx_fmt=png)

  

当然了，即便是短短的15秒，效果还是十分出色，而这都得益于Omniverse。由于在2022年对Omniverse的介绍更加详细，让我们将这部分内容留到了GTC 2022。

> 在这一年，受益于全球的数据中心需求激增，元宇宙、游戏和加密货币挖矿对显卡的需求持续旺盛以及美联储的宽松货币政策，英伟达的股价还是大幅提升。

> 2021年底（12月31日），NVIDIA股价上涨至294.35美元（1拆4后），市值增至7352.7亿美元，全年股价和市值上涨了127.47%。

### \[GTC 2022\] H100，进击的屠龙刀

https://www.youtube.com/watch?v=39ubNuxnrK8

这是AI非常沉闷的一年，疫情的走向在3月份尚未明朗，全球经济依然处于半困顿的状态。AI也来到了迷茫期，缺乏Killer App，Web 3大行其道，AI的热点变成了毫无吸引力的MLOps 和Data Centric，令人尴尬。

当然这一切，都会改变于2022年底ChatGPT的横空出世，可3月份，那时候ChatGPT连比尔盖茨都没见过呢（应该是8月份奥特曼才去演示）老黄还是坚持召开了线上的GTC大会，但是今年的笑容明显少了许多，头发也更白了，整个Keynote的色调也是较灰暗，也没有玩梗了……但是，没关系，一把比A100更强的屠龙刀问世了。

**1\. 基于Transformer核心的H100**

2021年，李飞飞团队发表了著名论文《Learning Transferable Visual Models From Natural Language Supervision》，开启了基于大模型的新篇章。而大模型的基础之一就是Transformer。因此这一代的H100，开始引入了Transformer核心，专门优化大模型的性能，这比起V100的Tensor核心是更加彻底的All in。

所以不得不佩服老黄的魄力，在2021就能够做出引入Transformer为新一代芯片核心的决策，并在2022年推出产品，这是非常难得的眼界和执行力。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzEKB6ymnm2Yh5dP31k61Uw0KkzXWgVbJ8PpA92icVI6oBcea3A1EmCZA/640?wx_fmt=png)

  

作为Hopper架构的新一代GPU，除了配备Transformer核心，H100起步80GB HBM3内存，FP16性能高达2000 TFLOPS。它还引入了更高带宽的NVLink 4.0，在多级多卡上性能更佳……总之，它就是为了LLM而生的最佳方案。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzWFuMbjDKzicj9Xia9nJqRZictzaWhraMy32XLkY3lcJ1y6LYVWdlUb16w/640?wx_fmt=png)

  

从上图比较数据就可以看出H100的强悍了，需要留意的是，H100的PCIe版本把光栅单元阉割了，这意味着无法像A100一样把它当成一块高端显卡使用了。极客湾出过一期视频专门评测这个版本的显卡，提到过这个问题。光栅单元阉割后，基本上没法愉快的玩游戏了，他们当时还拿了4张H100组多卡阵列，真是土豪（虽然也是借的...）

但是说实话，2022年很多公司不知道买这么强的GPU有什么用，它确实非常强，但是无论是LLM还是Stable Disfusion，都处于不成熟的阶段，所以，H100虽然拥有逆天的性能，但它像是一把暂时无用的屠龙刀。真正识货的，恐怕只有OpenAI和微软。

1.  **2. **全**新升级的Omniverse和Digital Twin**
    

在2019年的GTC上，英伟达正式推出Omniverse。一开始它的定位是：开放的3D设计协作平台。简单来说是可以让不同阶段的设计师，用不同的3D设计工具进行设计，但是可以在一个地方看到协作的3D成果。它的初衷是One Share World。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzcibicpZT7nxib8syKHP8Ov1P36nfmRg0D0xYf1t4LZnfC5vKwlWhFYQRw/640?wx_fmt=png)

image.png

但如果一直只是这样，这个产品就太工具化了。还好，Omniverse的产品概念的非常灵活，在2022年，它引入了虚拟世界仿真平台的理念，变成一个协作的平行世界，也就是Digital Twin（数字孪生）的概念，在其中可以进行多个自主系统的模拟而不影响物理世界，变成元宇宙平台的承载。

### ![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzKjO2Oic48JhNbM06k57Hhic3IWE54fVW0fu9cE09oBQB1koUrr2aXR1Q/640?wx_fmt=png)

《奇异博士2：疯狂多元宇宙》就是2022年上映的，这里明显也做了一点致敬。![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzRUXmaHVo0IeuY6punE0sbbNgb3hEXsubN6j9TQXpzbXmZOUnAtJfsA/640?wx_fmt=png)

而到了2024年，Omniverse又化身为具身智能（AI Agent）平台，融合了AI和元宇宙，AI的智能体可以在高仿真的虚拟宇宙里面进行演化，验证大模型能力，这个就更有想象力了。

  

需要注意的是，英伟达并不是生硬的把流行概念套上去，而确确实实是根据时代的趋势，对产品和技术做了相应的改进和升级，从而使它能够承载相应的产品心智和功能，紧跟时代发展的潮流。

由于全球经济受疫情影响，处于半困顿状态，而美联储的加息政策导致美股，尤其是科技股一路走低，另外8月份以太坊合并对矿业和显卡市场带来了重大利空，导致英伟达的股价下行。

> 2022年底，英伟达的市值跌到了3641亿美元，少有的出现了50%的年度跌幅，最低时一度股价接近110美元

### \[GTC 2023\] 屠龙刀迎来了群龙乱舞，引发新一轮科技革命

https://www.youtube.com/watch?v=a0soRIiqT1Q&list=PL5B692fm6--tKaj1zUmjQANTQT31O5pAB

人逢喜事精神爽，2023年，新冠的阴霾终于过去，而作为给人类补偿的礼物：ChatGPT，到3月份的时候已经取得举世瞩目的成功。这意味着GAI时代的到来，也代表AI的春天再次归来。当然，这也是英伟达的春天，老黄给出的定义是：**iPhone Moment of AI**。今年的GTC，也用上了鲜绿色的主题色，一扫去年的灰暗色调。这也是GTC最后一年线上召开。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtz9A2gF4eAdflbGsDQ2slmiaJ3ZSWkuon3qp0V90PsUfVU5bc2uO8gRzw/640?wx_fmt=png)

image.png

**1\. Chat With Ilya Sutskever**

GTC大会其实不止有老黄的Keynote精彩，还有众多的Talk和Presentation。而今年最有意思的Talk，就莫过于老黄和OpenAI的首席科学家Ilya Sutskever的这场炉边对话了。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzDyV8t6Q6gfQxiccAByD8At3CaXObdrrWMZ25ib88h0TOVbFDwJrtJSxQ/640?wx_fmt=png)

在这场对话中，ChatGPT才刚推出不久，其技术细节也处于严格保密中，外界对此也有不少猜测和臆想，甚至在某种程度上被神话了。老黄的访谈，很大程度上是想解惑，但是Ilya的嘴那可不是一般的严，基本上全场听下来就一个意思：“Predict the next character”。至于怎么做到的？不告诉你。（注意，这时连Token都基本没提到）直到后面Andrej的演讲，才揭开了面纱。而后面Llama的开源，算是彻底的祛魅和解密。

**2\. Grace Hopper架构的GH200**

在3月份的GTC上，实际上老黄并没有推出新的芯片，但是在6月份的Computex上，老黄推出了GH200。将H100 GPU和Grace CPU，焊到了同一块板上，组形成了一套更强的组合。这也彰显了英伟达的技术布局能力，先是单独的SXM接口的GPU卡，再是Grace CPU，然后再组合，而不是一味的简单做大GPU面积，挑战Die Size，很有战略思维。  
![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzDTXAsWmo2ubmC1RWAsWAGiaXSNYTia4fbIhaZqx4FVT4ysic2qNkibqZ6A/640?wx_fmt=png)

image.png

而同样的，由于接口的兼容性，这样的卡，能够很好的替代之前的旧卡，无缝衔接，继续通过NVLink，组合成Pod，到Rack，再到机房……

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzuMV0siaXD8NiaMqclR6ibU5PqibpTZgEtMnskk6sKHLgOPOFiayAHVDynPg/640?wx_fmt=png)

image.png

微软的机房看起来就是这样的，一排排的Rack，填充满了H100，形成了电力怪兽，也是计算怪兽，ChatGPT就是借助微软这些Super AI Factory，用英伟达的GPU训练出GPT-3.5，GPT-4……

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzyKFqdm2QjPGJBcicUClh62LZtr4DeTpOxibwp1bJEKibrMsnSugasdbpw/640?wx_fmt=png)

胜利的雪球一旦滚动，就很难停下。2023年，各大公司开始纷纷加入这场GAI的竞赛，争夺人工智能时代的船票，而关键之一，就是算力。无论是ChatGPT，Bard，Llama，都需要庞大的算力作为支撑，谁抢到了算力，谁就有了先发优势。于是到了2023年底，就有了这样的一个统计图。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1ibpiaB8ejUE4L5sXeASlELtzK0cBOaGQOupltCDHuqQqempsSicRQlmkX3gVhHIBRs7GFiaw4Za79eAQ/640?wx_fmt=png)

H100，作为一把预先打造好的屠龙刀，终于迎来了群龙乱舞的时代。而2023年，也被公认为开启新一轮科技革命的AI元年。英伟达和老黄的坚持和远见，终于开始得到又一轮回报。

> 受益于与ChatGPT和GAI的兴起，A100和H100大卖，英伟达的5月份财报爆表，开启了全新的周期

> 2023年底，英伟达的市值达到了1.2w亿美元，年度涨幅235.88%

### \[GTC 2024\] 小众的AI开发者大会，终成AI工业界的盛会

https://www.youtube.com/watch?v=f8DKD78BrQA&t=228s

2024年3月18日，伴随着人工智能的兴起和英伟达的成功，GTC大会成为了万众瞩目的盛会。本届GTC是时隔五年后第一次线下举办，从全球各地涌来的AI专业开发者、创业者和投资人，挤满了加州的圣何塞会议中心，创下了有史以来参会人数最多的记录。GTC已经成为全球AI开发者的顶级工业盛会，其影响力甚至开始超越苹果的WWDC和谷歌的I/O大会。

![](https://mmbiz.qpic.cn/mmbiz_jpg/614RnbPwb1icVyQjVVzklq7jexLUnOro06x75GiasibQ4JuJ2unFYEnARjHOiciaic88OrNJ8IQHoiaknemmztib9HEWsQ/640?wx_fmt=jpeg)
1\. B200和GB200这次的主角之一是B200芯片和GB200，性能毫无悬念地强劲。当然还有NVL72，将液冷技术应用带到一个新台阶。![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0sWjApzkEC9SeDnYLXTL8YoJpwoYsgC5YNB3N4sajPtzZTYSU7CRCLg/640?wx_fmt=png)

  

GB200将Grace-n的优势提升到一个新台阶，1拖2达到了惊人的40 PFLOPS。也许下一款X100发布，GX200就是1拖4的设计了，届时性能又是一个全新的境界。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0LpzYRKbAKGicsiazDcEphMg8z3rpcibYPOHkvHiceMOPTVXHUDBickuEdRQ/640?wx_fmt=png)
得益于之前发布的Sora，业界和学术界不再质疑如此强大的芯片的用途，不像H100刚发布时无龙可屠的“屠龙刀”。

#### 2\. NIMs

NIMs（NVIDIA Inference Microservices）是老黄今年主推的一个新产品，其实是一套完整的模型推理微服务，旨在简化和加速GAI模型的部署和推理，吸引用户使用GPU Cloud的模式，来部署自己的服务。

不难发现，其实NIMs是之前多种技术的组合，稍微再复习一下：

*   • **Triton：** 提供模型的网关和微服务，对推理请求进行优化，实现了模型的灵活部署和高效管理
    
*   • **TensorRT：** 提供模型的推理引擎，提升模型的推理速度和效率
    
*   • **K8s on GPU：** 提供GPU的虚拟化，实现了对GPU资源的容器化，充分利用GPU的计算能力
    

这些分布式技术由上至下，提供了基于GPU Cloud的一体化大模型推理解决方案。只要将大模型交给NIMs，就可以快速对外提供高性能的API服务，这对中小企业来说无疑非常有吸引力。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0wyeatiburHdMs84sUD8VlYGgn0go0SibbMFubsbYicLL64kkUOFalHGPQ/640?wx_fmt=png)

  

如果NIMs能成气候，不仅会为英伟达带来更广阔的盈利和市值增长空间，还会让它具备与云厂商一较高下的实力。

3\. Robotics & Isaac 

英伟达在机器人领域其实布局已经久，技术核心是Isaac和Jetson。Isaac平台提供一整套开发工具和模拟环境，帮助开发者设计、测试和部署机器人系统。Jetson平台则通过强大的计算能力，支持复杂的AI和边缘计算任务。结合Omniverse，开发者可以在虚拟环境中进行高保真训练，极大地提升了机器人开发的效率和效果。这是第一次老黄把机器人带上台进行展示。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0pN4UmqUtkOzaicqhBKbhdHiaib2NpSeU5qrJ5ygA1emaBRzWZLHF7YA8Q/640?wx_fmt=png)

image.png

整个环节很明显在致敬钢铁侠。但很可惜，目前的机器人技术成熟度还不够，这9台机器人只能充当背景，真正能稍微互动的是2台像Walle的小机器人，互动过程也有些尴尬。因此，这个环节在今年更多的像是一个Show，希望明年这9台机器人都能够真正和老黄在台上互动起来。这或许要靠Figure AI公司的技术突破，而这也将是下一个精彩的故事和浪潮。

#### 4\. Transforming AI Panel

在这次GTC大会上，有许多精彩的Panel，其中最火热的莫过于老黄与《Attention is all you need》论文的7位作者的圆桌会议（作者共8位，有1位因事缺席），这7位作者中有6位已经是创业公司的CEO，很多都是大家耳熟能详的公司，例如Cohere、Character.ai等

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0TTJaibPUAvUiaiaStIFecNBu4vU2cyGXicRkw22ActsiaicjlJcHcc4kKzAA/640?wx_fmt=png)

image.png

从这张Model Size的曲线图可以看出，如果没有Transformer，就不会有大模型，没有大模型，就不会有如此陡峭的算力新曲线（绿色这一条也证实了GPT-MOE的模型大小），自然也不会有H100的热卖。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0khpPibjjBL9QPKBv7ensJeUbLraToKYYG0uyFEzm5OZrCsibCD9lSGRg/640?wx_fmt=png)

会议的主题非常有趣和开放，讨论了当时这篇论文的名字由来，为什么命名模型为Transformer，下一个可能的颠覆性Model，各个CEO现在公司的方向……等话题。例如Transformer的由来是，他们认为这个模型应该是非常通用的，可以支持世界中所有文本、图像、语音、视频等之间的通用转换（Universe Transforming），所以叫Transformer。

Transformer的创始人们不仅有卓越的技术能力，还有深刻的洞察力和远见。看到这7个神采飞扬而又风格各异的人，也就不奇怪他们能写出如此精彩的论文。而老黄饮水不忘挖井人，把他们聚集在一起，为这届GTC大会多添了一笔靓丽的色彩。

> 立于人工智能的浪潮之巅，借助3月份GTC大会、5月份财报和拆股，6月份的Computex连续加持，2024年，NVIDIA的股价成为了美股村里的希望和支柱

> 2024年中（6月18日），NVIDIA股价上涨至135.58美元（1拆10后），市值增至33340亿美元，年度涨幅173.13%，全球市值第一

* * *

  
![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0jtWW3Bx806dp1ib4IJ6iaUafYyAdQCRFwxMCyqz5gDn430MzRoIWdqrg/640?wx_fmt=png)

这张8年芯片算力进化图，某种程度上和英伟达的市值不谋而合，如出一辙地冲上天际。1000倍的算力，150倍的股价。这是时代的馈赠，也是给勇者的礼物。

![](https://mmbiz.qpic.cn/mmbiz_png/614RnbPwb1icVyQjVVzklq7jexLUnOro0N2pTR5Bcm4BLIVHSPLdfWdyVQEPQAf9gtz44QiacCsLK4NpmFehFhvw/640?wx_fmt=png)

纵观这8年来的GTC大会，英伟达不仅不断推出了性能接近10倍提升的硬件，还在软件和生态领域深耕，打造了自己的护城河。一些早期不显眼的软件如TensorRT和Triton，后来组合成NIMs；而Omniverse则不断演进和完善……这些领域都是英伟达近5-10年深耕细作的成果，并非一朝一夕可突破，更不是几个公司成立联盟就能攻破的。这正是技术的魅力所在，无限可能但又真实不虚，不是急功近利和夸夸其谈就能实现的。

伴随着AI的时代浪潮，英伟达市值一路水涨船高，而GTC大会也不断改进，变得愈发丰富精彩，和日渐乏味且挤牙膏的苹果发布会相比，它开始吸引了越来越多的受众，包括投资机构。如果他们能早点参加GTC，就会发现这家3w人的公司，不仅仅是一家硬件公司，而是在强大的危机感驱动下，打造了了众多护城河的一家全方位的AI公司，包括硬件、软件、产品和生态。更重要的是，从8年前开始，它就已经真的All In AI了。

英伟达不仅是AI浪潮的受益者，也是这波浪潮的缔造者。没有它的贡献，就没有2012年开始的深度学习革命，也不会有2022年ChatGPT的横空出世。真正的英雄不仅顺应时代，也造就时代。老黄作为公司的创始人和CEO，一直保持虚怀若谷的心态和勤勉的工作态度，不断进取和创新，在GTC大会上10年如一日地坚持做2个小时的全程演讲，传播技术和理念，为AI领域开疆拓土，并且善待公司的员工。这样的CEO和公司，值得我们学习和尊敬，也担得起这3万多亿的全球前三市值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/614RnbPwb1icVyQjVVzklq7jexLUnOro02XLh1oVPCbaFQaoA3slu4Mh48VicTKukdFGp2rT8Lak6mDVj8YlwDsg/640?wx_fmt=jpeg)