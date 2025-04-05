Title: 英伟达RTX 5090揭秘：集成RISC-V处理器

URL Source: https://mp.weixin.qq.com/s/ng9yG2ydJ7RTF8Q4HF42iw

Markdown Content:
![Image 1](https://mmbiz.qpic.cn/mmbiz_jpg/CB90MLwUv2dlSOw0Zeq8bxDDb9at7uFb5MI56wyliabMPeGVJDphicsoGTAVFYnsicCjx9D4ediabGpxjbtVUgfpDg/640?wx_fmt=jpeg&from=appmsg)

👆如果您希望可以时常见面，欢迎标星🌟收藏哦~

来源：本文编译自forbe，谢谢。

当 Nvidia 在 2025 年 CES 上首次发布 RTX 5000 系列显卡时，很明显该公司将通过这些产品进一步向 AI 靠拢。任何关注企业技术的人都知道，Nvidia 是 AI 领域的主要参与者——也许是最重要的参与者——因此它在利用 AI 加速游戏方面取得重大进展也就不足为奇了。

虽然很多人会关注 GPU 内部的 CUDA 核心和 Tensor 核心，但新的 DLSS 4 软件也带来了许多改进，其中包括新的transformer模型和 4x 帧生成。RTX 50 系列是 Nvidia 唯一能够同时实现这两个功能的产品系列，尽管前代 RTX 40 系列确实可以实现 1x 帧生成并将利用transformer模型。

**Nvidia GB202 GPU**

RTX 5090 的核心是 GB202 GPU，基于 Nvidia 的新 Blackwell 架构。完整的 GB202 GPU 具有 24,575 个 CUDA 核心、192 个光线追踪核心、768 个 Tensor 核心和 768 个纹理单元。基于台积电 4N 工艺节点的 GB202 芯片的当前版本具有 21,760 个 CUDA 核心、680 个第五代 Tensor 核心和 170 个第四代光线追踪核心，此外它还具有 512 位内存接口。未来，随着产量的提高，我们可能会看到启用所有核心的 RTX 5090 Ti。对于内存，RTX 5090 具有 32GB GDDR7，使用 PAM3 脉冲幅度调制信号，以获得更好的频率和电压。这使得内存达到 28 Gbps，内存带宽达到 1,792 GB/s。

与 4090 相比，5090 拥有下一代 CUDA、Tensor Core 和光线追踪核心。它的 CUDA 核心数量也比 RTX 4090 多出近 33%，Tensor Core、RT 核心和 RT 性能也有类似的升级。5090 还拥有 575 瓦的 GPU，而 4090 的 GPU 为 450 瓦，同时使用相同的 TSMC 4nm 4N 工艺节点和升级的 PCIe Gen 5 接口。Nvidia 已将 Tensor Core 升级到 FP4 功能，据称其 FP8 吞吐量是 4090 内 Ada Tensor Core 的两倍。RT 核心在射线三角相交测试和大量其他光线追踪和路径追踪功能中的性能也得到了巨大提升。

![Image 2](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7XsgBoR53icjfbeiaX0pWHfnECZdgeToB7gxsibPr4qHBMK5rHkuqrTyZQ/640?wx_fmt=png&from=appmsg)

RTX 5090 GPU 的一个新特性是 AI 管理处理器 (AMP)，这是一个完全可编程的上下文调度程序。它旨在减少 GPU 将任务调度到不同核心的开销；它就像是 GPU 上同时运行的所有不同工作负载的交通警察。这是一个专用的 RISC-V 处理器，位于 GPU 管道的前端，与 CPU 驱动的方法相比，它可以实现低得多的决策延迟。AMP 还兼容 Windows 10 中引入的 Microsoft 硬件加速 GPU 调度，因此它不会给开发人员带来任何新的挑战，并且在同时在 GPU 上执行多个任务时应该可以提高 CPU 利用率和延迟。总而言之，这意味着在同时执行图形和 AI 工作负载时可以获得更好的体验，随着 DLSS 等功能变得如此重要，这种情况在 Nvidia GPU 上越来越常见。

除了 AI 和图形之外，RTX 5090 上的新 GPU 还带来了增强的 4:2:2 H.265 和 HEVC 视频编码功能。这提高了以 4:2:2 色彩拍摄的 4K 内容的编码能力，这对内容创作者来说正变得越来越标准，并且支持新的 AV1 和 HEVC 编码。Nvidia 的第九代 NVENC 编码器还增加了一种新的 AV1 超高质量模式，其质量甚至比标准 AV1 质量更高。Nvidia 还在 5090 中添加了第三个编码器，与（已经非常快的）4090 相比，它可以将编码时间缩短多达 50%。Nvidia 甚至表示它比 RTX 3090 快 4 倍；我从未测试过该型号，所以我们只能依靠其他评测人员来测试。

GB202 GPU 的显示管道支持 DisplayPort 2.1b，利用 UHBR 20 可实现高达 80 Gbps 的带宽。这意味着以 60 赫兹运行高达 16K，以 120 赫兹运行 8K，以高达 240 赫兹运行 4K。

![Image 3](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7DE2enAHRrZ89SF8PxC6aDicDsFjHbETwwRibcibmHLu4mbSqDB2kLREicg/640?wx_fmt=png&from=appmsg)

**DLSS 4 多帧生成**

RTX 50 系列最重要的功能是 DLSS 4 的多帧生成。此功能可有效地将一个渲染像素转换为最多 16 个总像素。虽然 40 系列提供帧生成，但上限为 1 倍，这可以提高图形性能，但远不及 4 倍的水平。下表列出了不同系列 Nvidia 显卡的 DLSS 功能；该公司表示，未来可能会在 RTX 30 系列上提供帧生成功能，但目前还不确定。

![Image 4](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7OxqNb1uvuF8FLJkq7T3kLfXBn7ibSiagPXFlzJYZCLPADSZreBJa7Hng/640?wx_fmt=png&from=appmsg)

DLSS 多帧生成与新的变换器模型协同提升了性能，它使用变换器模型在升级的同时提高图像质量。这是 Nvidia 五年来首次改变其用于 DLSS 的模型类型，此前它使用的是卷积神经网络模型。DLSS 的基本功能之一是以较低的分辨率渲染游戏以实现更高的帧速率，然后将其升级到可玩的分辨率，这会影响图像质量。通过使用变换器模型，Nvidia 提高了升级质量，可以说让 DLSS 感觉无损，即使事实并非如此。Nvidia 还将变换器模型用于其射线重建功能，从而带来类似的图像质量改进。

![Image 5](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7coruay1vuEJ0gmyjYPaqgS4AsfNEONZyrM6iaEcYA6aVx8r7pQ5UTLw/640?wx_fmt=png&from=appmsg)

**测试平台和方法**

为了测试 RTX 5090，我使用 AMD Ryzen 9800X3D 处理器和 ASUS X870E Hero 游戏主板（由 AMD 寄给我）搭建了一个新的测试台，并由 360mm ASUS ROG RYUO III CPU 冷却器冷却。它还搭配了 Patriot Memory 寄给我的 64GB Patriot Viper DDR5 6000 MT/s RAM、2TB Crucial Memory T705 Gen 5 SSD 和 Corsair 7000X 机箱以及 Corsair 寄给我的 1 千瓦 Corsair RM1000x 电源。显示器是 Alienware AW3225QF，我去年评测过；这款显示器能够进行 4K 240 赫兹游戏，而这正是 RTX 5090 的亮点所在。所有这些组件都用于使 RTX 5090 相对于 4090 获得最佳的基准测试数字。

![Image 6](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7kcwVoyNXnuOhtM7Gz4MOpKJWEM5KpDcgniaxuFvZlAUunYG5NgSqlXw/640?wx_fmt=png&from=appmsg)

由于 AMD 在这一世代的高端市场上并不一定与 Nvidia 竞争，因此将 5090 与 4090 进行比较似乎要容易得多；这种方法也考虑到了我搭建系统和测试新卡的时间，大约三天。由于需要将自己限制在几个基准测试中，我选择了 Blender、3Dmark 和三款相关游戏，这些游戏可以展示 DLSS 4 和帧生成功能的实际效果。这三款游戏分别是《漫威对手》、《星球大战：法外狂徒》和《赛博朋克 2077》。Nvidia 表示，当 1 月 30 日开始零售时，将有 75 款游戏支持 DLSS 4。赛博朋克 2077用于解决这一代版本的“但它能运行Crysis吗？”测试。Nvidia 和赛博朋克的制造商 CD Projekt RED 投入了大量的时间和金钱来让这款游戏看起来非常出色。

**与 RTX 4090 的基准测试结果**

首先是 Blender，它已成为 3D 艺术家最喜爱的创作工具之一。最新版本 4.3 可在 Blender Benchmark 中找到，我用它来比较 5090 和 4090。它由三个不同的测试组成，比较两款显卡的原始 3D 渲染能力。

![Image 7](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7WTbcf5fJxb5UfQosEiacWWdpmpqH5P91vLgyxd2mL7nmTYKdkM3lHPA/640?wx_fmt=png&from=appmsg)

如上图所示，RTX 5090 在所有三项测试中都取得了明显的胜利；与 RTX 4090 相比，它在 Monster 中提升了 33%，在 Junkshop 中提升了 45%，在 Classroom 中提升了 31%。这是一个可观的提升，任何 3D 创作者都会喜欢，尤其是如果他们使用的是更老的显卡的话。

接下来，3Dmark 是一个综合基准测试，包含两个 DX12 测试，不利用 GPU 的 AI 功能，主要侧重于光栅化。Steel Nomad 是一个 4K 基准测试，具有 DX12 和 HDR，使用先进的渲染技术，而 Speed Way 使用较低的分辨率 (1440P) 和光线追踪，提供一点光线追踪和光栅化，尽管仍然没有像 DLSS 那样的功能。3Dmark 仍然是行业标准基准测试，也是测试理论性能的好方法。

![Image 8](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7fxrgr79ot1zhI64NAQzOlj8Ssq86QaRAgeLLq0fMibp1ZelbibeOeUfg/640?wx_fmt=png&from=appmsg)

正如这些基准测试所示，RTX 5090 的性能再次远高于 4090。具体来说，RTX 5090 在 Speed Way 中快 42%，在 Steel Nomad 中快 50%，如果考虑到增加的 CUDA 和 RT 核心，这是有道理的。话虽如此，我可能会认为这些是不使用 DLSS 的游戏中的最佳情况；在没有 AI 的现实世界中，许多游戏的表现可能会低于这些数字。

**真实游戏基准**

测试的所有三款游戏都是 Nvidia 在其 DLSS 4 抢先体验列表中确定的游戏。我之所以选择这三款游戏，是因为它们也代表了游戏的多样性，并且是了解 Nvidia 在 AI 方面取得多大进步的绝佳方式。同样，Nvidia 表示，75 款游戏将在零售时支持 DLSS 4，但 700 款游戏已经在某种程度上支持 DLSS，并且随着 Nvidia App 中的 DLSS 覆盖，我们可以看到更多游戏支持 DLSS 4。Nvidia 拥有让行业采用 DLSS 的市场份额，并且随着Marvel Rivals等热门游戏在发布时采用并支持 DLSS 4，我们可以期待它从一开始就产生重大影响。

![Image 9](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7vJQ25M5Adwgz4icJcLTYAndzu4oTID0EViaxcJ4jpuwYxzqBrCzkSXdQ/640?wx_fmt=png&from=appmsg)

对于《漫威宿敌》，我使用两张显卡开启了帧生成功能，这会自动开启低延迟和 DLSS。游戏还设置为以 4K 分辨率运行，同时使用 Nvidia FrameView 来跟踪帧速率。对于那些不熟悉的人来说，1% 低帧率是在玩游戏时 1% 的时间内遇到的最低帧速率；这是最坏情况（不是最坏情况），可以为简单的平均帧速率提供更多背景信息。

当我进行这项测试时，RTX 4090 的 1% 最低帧率为 84 FPS，仍然非常可玩，平均帧率为 160，而 PC 延迟为 31 毫秒。然而，RTX 5090 的 1% 最低帧率为 115 FPS，平均帧率为 258 FPS，这完全超出了我的预期，这实际上超出了我 240 赫兹显示器的刷新率——对于如此具有竞争力的游戏来说，这非常棒。PC 延迟也降低了 30%，降至 21 毫秒，这对于像Marvel Rivals这样的竞争性游戏来说，可能会产生很大的不同。

![Image 10](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7vOoNt3m9pbkXOeSsFfbCUXhWfP7G1tKlf2j4nbSCgaFaLIIjlOpMQg/640?wx_fmt=png&from=appmsg)

对于《星球大战：法外狂徒》，Nvidia 为我提供了一个抢先体验版本，用于测试 DLSS 4。然而，在此之前，我在 RTX 5090 上以 4K 分辨率玩了这款游戏，完全启用了光线追踪，但没有启用帧生成；在这种配置下，平均帧速率只有 40 到 50 FPS。打开 DLSS 和 4 倍帧生成后，我的帧速率平均提高到了 180，这让游戏玩起来完全不同，但看起来仍然同样令人惊叹。RTX 4090 也有帧生成功能，平均为 96 FPS，但这基本上是 RTX 5090 性能的一半。

![Image 11](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7UppsQJr7AztGjMZUhwTfuXoyU47400a6zO9HAYl4h4H0JP3LX4P0tg/640?wx_fmt=png&from=appmsg)

最后，我为Cyberpunk 2077开启了两款显卡的几乎所有功能，包括光线追踪、帧生成和光线重建。我在 4K 分辨率下运行Cyberpunk游戏内基准测试时执行了此操作，该基准测试显示了低、中和高 FPS。在这三种情况下，RTX 5090 的性能都是 RTX 4090 的两倍多，这再次表明最新的 AI 使 RTX 5090 的速度提高了多少。

**功率和散热**

RTX 5090 是一款耗电猛兽。据纸面数据，它的 GPU 功率为 575 瓦，而 RTX 4090 的 GPU 功率为 450 瓦。Nvidia 建议为 5090 使用 1 千瓦的电源，这对许多人来说是一个升级。在我测试期间，GPU 监控应用程序 GPU-Z 报告称，GPU 的热设计功率达到 555 瓦，峰值板功率达到 523 瓦；这些数字可能不是 100% 准确，但它们确实表明该卡已几乎发挥出其全部潜力。

![Image 12](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2c2scrnevddXp9802V3SWw7icwZjFeMpTTldAqykrBC1j5TXFNg4hKYaOHRv4K1iaiczx9PBaibKeibEZA/640?wx_fmt=png&from=appmsg)

从散热方面来看，这张卡非常出色，尤其是考虑到 RTX 4090 是一张三插槽卡，上面有一个巨大的冷却器。RTX 5090 要小得多，PCB 更小，可以实现直通。根据我的 Flir 热像仪，在我测试的峰值时，这张卡的温度达到了 77 摄氏度，外部温度从未超过 62.1 摄氏度。这张卡在我的机箱中任何时候都没有发出很大的声音，而且说实话，它似乎比我预期的更好地处理了热负荷，考虑到它是一种双插槽卡设计，冷却器比 4090 更小——同时 TDP 也高出 100 多瓦。

**我们的新神经渲染时代**

总而言之，当启用最新的 AI 功能时，RTX 5090 无疑是世界上最快的显卡。即使没有 AI 功能，它仍然是最快的。虽然我没有时间测试 Premiere Pro 或 DaVinci Resolve 等创意应用程序，但我对增加第三个编码器和改进的 HEVC 和 AV1 编码感到兴奋。虽然这些编码器对创作者来说很棒，可以大大加快速度，但它们也可以并且很可能在流式传输时进一步降低 GPU 的开销。RTX 5090 是一款强大的游戏、内容创作和 AI GPU，在这三个方面都具有令人难以置信的性能。

尽管如此，这仍然是一张售价 2,000 美元的显卡，而且一段时间内供应可能会非常紧张。不幸的是，即使标价为 2,000 美元，我们也可能看到 GPU 抢购潮的回归。请注意，这比 RTX 4090 的首发价要高，后者的首发价为 1,600 美元，尽管它确实为 1,500 美元的 RTX 5080 Ti 留出了空间，后者的配置几乎一样好，因为性能较弱的 RTX 5080 零售价为 999 美元。我认为 RTX 50 系列其他产品的定价旨在挤压 AMD，而 RTX 5090 本身看起来就像一个毫无歉意的光环。虽然我确实认为 RTX 5090 对于那些预算充足且渴望顶级性能的人来说值得 2,000 美元，但我还想说，很多人可能会从启用帧生成功能的 RTX 5080 中受益。

RTX 5090 整合了 CUDA、RT 和 Tensor Cores 以及管理芯片的最佳技术，以确保更好的延迟并最大限度地提高效率。我很想知道这些性能改进如何转化为 RTX 5080 和 RTX 5070，以及它们与 Nvidia 的 RTX 4080 和 4070 相比如何——甚至可能是 AMD 即将推出的 Radeon RX 9070。在这方面，我很好奇 AMD 将如何应对多帧生成等功能以及 Nvidia 对光线追踪性能的持续改进。在支持 Nvidia 和 AMD 技术（如 FidelityFX Super Resolution）的游戏中测试这些功能非常重要。我担心，如果 AMD 不能提供与 Nvidia 在 DLSS 4 上所做的相媲美的产品，我们可能永远看不到 AMD 迎头赶上。

_**END**_

**👇半导体精品公众号推荐👇**

▲点击上方名片即可关注

专注半导体领域更多原创内容

▲点击上方名片即可关注

关注全球半导体产业动向与趋势

\*免责声明：本文由作者原创。文章内容系作者个人观点，半导体行业观察转载仅为了传达一种不同的观点，不代表半导体行业观察对该观点赞同或支持，如果有任何异议，欢迎联系半导体行业观察。

![Image 13](https://mmbiz.qpic.cn/mmbiz_jpg/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUuDk7BHibzliciaibdYCIhf1mqRA2MmBiaTWaD5ibeicNlAFlNsibkd1f2pmeDOg/640?wx_fmt=jpeg&from=appmsg)

**今天是《半导体行业观察》为您分享的第4029期内容，欢迎关注。**

**推荐阅读**

★[一颗改变了世界的芯片](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247732748&idx=1&sn=2ba19055f90ac8ab5512098d039ef391&chksm=ce6e4cfbf919c5eddc8b3af5a147990afc3c7227f59c332d15ed5f8b8a100a4dcb97f59d05d1&scene=21#wechat_redirect)

★[美国商务部长：华为的芯片没那么先进](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247735441&idx=6&sn=786b62b5f4edbac37b66f91ff36d0f49&chksm=ce6e5a66f919d37052778a97f49442c77529699f08f3dcf599c99347dcf35da064528aab5222&scene=21#wechat_redirect)

★[“ASML新光刻机，太贵了！”](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247738477&idx=1&sn=636a6387c4e83b7e47e6377aba07f8d4&chksm=ce6e269af919af8cc2bfddf1dff60566bfd0169eb1c31d97413c6f97abe8d307cda0b58cc795&scene=21#wechat_redirect)

★[悄然崛起的英伟达新对手](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247741738&idx=1&sn=860c31832b6c6e03b152300b991be5f9&scene=21#wechat_redirect)

★[芯片暴跌，全怪特朗普](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247746259&idx=1&sn=f9a5a82f84e598d0f2d8b8d2cb1d371e&chksm=ce6e0024f919893285b3069f01821e6bd47cb772c890cacf88874707e1576ecc3d7673290afb&scene=21#wechat_redirect)

[★](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247709689&idx=2&sn=d77e02ac93f0b0e490744945d550f269&chksm=ce6eb10ef919381813abb86c6dee73b999b8c8ccbdeb9af8b47b7dde46b05e15e13be81cb704&token=1171908126&lang=zh_CN&scene=21#wechat_redirect)[替代EUV光刻，新方案公布！](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247741646&idx=1&sn=aa71a43b134a613453f29ddc8cfdb32c&chksm=ce6e3239f919bb2f75efc5a7b90c48944655808f6fc901dd146eec31f73340cf1f663b31cced&scene=21#wechat_redirect)

★[半导体设备巨头，工资暴涨40%](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247723271&idx=7&sn=1e4f5124fa7d3f029e4c212823633e1e&scene=21#wechat_redirect)

★[外媒：美国将提议禁止中国制造的汽车软件和硬件](https://mp.weixin.qq.com/s?__biz=Mzg2NDgzNTQ4MA==&mid=2247756729&idx=8&sn=7763455e2146a96c6c5945c7092c9c90&scene=21#wechat_redirect)

![Image 14](https://mmbiz.qpic.cn/mmbiz_gif/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUu1TXpDFVTuWPIxHJktS4KxvLHbBdANu82pWXFucbIVric6M3Cn7WuJQA/640?wx_fmt=gif&from=appmsg)

![Image 15](https://mmbiz.qpic.cn/mmbiz_gif/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUuCG4MLz2oyuIZMqcgS0cC9tfaiavhootjOTmg6loyqbjb1EHlNxsKgtw/640?wx_fmt=gif&from=appmsg)

![Image 16](https://mmbiz.qpic.cn/mmbiz_jpg/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUuoAoO1fpqEjmy1OPQpiagH2XnYgibDaXTwibchog92XXY3z0AUt5m6klGw/640?wx_fmt=jpeg&from=appmsg)

『半导体第一垂直媒体』

**实时 专业 原创 深度**

公众号ID：icbank

喜欢我们的内容就点**“在看”**分享给小伙伴哦![Image 17](https://mmbiz.qpic.cn/mmbiz_gif/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUuhbJFmFI0FmXdAOGSJU6V1ibAveWWFVjtJf5mH7n0ib7BUhbC0naFWyoQ/640?wx_fmt=gif&from=appmsg)

![Image 18](https://mmbiz.qpic.cn/mmbiz_png/CB90MLwUv2dVQxuwN8gBNHd4YoTAibOUuPwZbdic1dGW2ibmrg50pT5BGZUMw0jE1StKR4D8guBwSalq28F6ZcQcw/640?wx_fmt=png&from=appmsg)
