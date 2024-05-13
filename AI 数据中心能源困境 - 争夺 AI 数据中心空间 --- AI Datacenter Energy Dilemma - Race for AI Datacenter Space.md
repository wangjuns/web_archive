# AI 数据中心能源困境 - 争夺 AI 数据中心空间 --- AI Datacenter Energy Dilemma - Race for AI Datacenter Space
The boom in demand for AI clusters has led to a surge in focus on datacenter capacity, with extreme stress on electricity grids, generation capacity, and the environment. The AI buildouts are heavily limited by the lack of datacenter capacity, especially with regard to training as GPUs need to be generally co-located for high-speed chip to chip networking. The deployment of inference is heavily limited by aggregate capacity in various regions as well as better models coming to market.  
对 AI 集群需求的激增导致对数据中心容量的关注激增，对电力网、发电能力和环境造成极大压力。由于缺乏数据中心容量，AI 建设受到严重限制，特别是在训练方面，因为 GPU 需要通常进行高速芯片对芯片的联网。推理的部署受到各个地区的总体容量限制以及更好的模型上市的影响。

There is plenty of discussion on where the bottlenecks will be – How large are the additional power needs? Where are GPUs being deployed? How is datacenter construction progressing by region including North America, Japan, Taiwan, Singapore, Malaysia, South Korea, China, Indonesia, Qatar, Saudi Arabia, and Kuwait? When will the accelerator ramp be constrained by physical infrastructure? will it be transformers, generators, grid capacity or one of the other 15 of the other datacenter component categories we track? How much capex is required? Which hyperscalers and large firms are racing to secure enough capacity and which will be constrained heavily because they were caught flat footed without datacenter capacity? Where will the Gigawatt and larger training clusters be built over the next few years? What is the mix of power generation types such as natural gas, solar, and wind? Is this even sustainable or will the AI buildout destroy the environment?  
对于瓶颈将出现在哪里有很多讨论 \- 额外的电力需求有多大？ GPU 在哪里部署？ 包括北美、日本、台湾、新加坡、马来西亚、韩国、中国、印度尼西亚、卡塔尔、沙特阿拉伯和科威特在内的各地区的数据中心建设进展如何？ 加速器的扩容将受到物理基础设施的限制吗？ 它将是变压器、发电机、电网容量还是我们跟踪的其他 15 种数据中心组件类别之一？ 需要多少资本支出？ 哪些超大规模云服务提供商和大型公司正在竞相确保足够的容量，哪些将受到严重限制，因为他们没有足够的数据中心容量？ 在未来几年内，将在哪里建造千兆瓦及更大规模的训练集群？ 电力发电类型的混合情况如天然气、太阳能和风能如何？ 这甚至可持续吗，还是人工智能的建设将破坏环境？

Today let’s answer these questions, with the first half of the report free, and the 2nd half is available to subscribers below.  
今天让我们回答这些问题，报告的前半部分免费，订阅者可以在下面获取第二半部分。

Many are opining with ridiculous assumptions about datacenter buildout pace. Even Elon Musk has chimed in to opine, but his assessment is not exactly accurate.  
许多人对数据中心建设速度做出了荒谬的假设。甚至埃隆·马斯克也发表了自己的看法，但他的评估并不完全准确。

> The artificial intelligence compute coming online appears to be increasing by a factor of 10 every six months… Then, it was very easy to predict that the next shortage will be voltage step-down transformers. You've got to feed the power to these things. If you've got 100-300 kilovolts coming out of a utility and it's got to step down all the way to six volts, that's a lot of stepping down. My not-that-funny joke is that you need transformers to run transformers... Then, the next shortage will be electricity. They won't be able to find enough electricity to run all the chips. I think next year, you'll see they just can't find enough electricity to run all the chips.  
> 看起来，人工智能计算能力每六个月就会增加 10 倍……然后，很容易预测下一个短缺将是电压降压变压器。你必须为这些设备供电。如果你从公用事业中得到 100-300 千伏的电压，它必须一直降到六伏，这需要大量的降压。我不是那么好笑的笑话是，你需要变压器来运行变压器……然后，下一个短缺将是电力。他们将无法找到足够的电力来运行所有的芯片。我认为明年，你会看到他们无法找到足够的电力来运行所有的芯片。
> 
> Bosch Connected World Conference  
> 博世全球互联大会

To be clear he is mostly right on these limitations of physical infrastructure, but compute is not up 10x every six months – we track the [CoWoS, HBM, and server supply chains of all major hyperscale and merchant silicon firms](https://www.semianalysis.com/p/accelerator-model) and see total AI compute capacity measured in peak theoretical FP8 FLOPS has been growing at a still rapid 50-60% quarter on quarter pace since 1Q23. I.E. nowhere close to 10x in six months. CoWoS and HBM is simply not growing fast enough.  
要明确的是，他在对物理基础设施的限制方面大多是正确的，但计算并不是每六个月就增长 10 倍——我们追踪所有主要超大规模和商业硅公司的 CoWoS、HBM 和服务器供应链，看到峰值理论 FP8 FLOPS 的总 AI 计算能力自 1Q23 以来仍以 50-60%的季度增长速度快速增长。即在六个月内远未达到 10 倍。CoWoS 和 HBM 的增长速度根本不够快。

The boom in generative AI, powered by transformers, will indeed need a lot of transformers, generators and a myriad of other electrical and cooling widgets.  
基于变压器的生成式人工智能的繁荣确实需要大量的变压器、发电机和各种其他电气和冷却小部件。

A lot of back of the envelope guesstimates or straight up alarmist narratives are based on outdated research. The IEA’s recent [Electricity 2024 report](https://www.iea.org/reports/electricity-2024) suggests 90 terawatt-hours (TWh) of power demand from AI Datacenters by 2026, which is equivalent to about 10 Gigawatts (GW) of Datacenter Critical IT Power Capacity, or the equivalent of 7.3M H100s. We estimate that Nvidia alone will have shipped accelerators with the power needs of 5M+ H100s (mostly shipments of H100s, in fact) from 2021 through the end of 2024, and we see AI Datacenter capacity demand crossing above 10 GW by early 2025.  
许多草稿估计或纯粹的危言耸听的叙述都是基于过时的研究。 国际能源署最近的《2024 年电力》报告指出，到 2026 年，人工智能数据中心将需要 90 太瓦时（TWh）的电力需求，相当于约 10 吉瓦（GW）的数据中心关键 IT 功率容量，或相当于 730 万个 H100。 我们估计，仅 Nvidia 在 2021 年至 2024 年底将已经发货的加速器的功率需求相当于 5 百万个 H100（事实上主要是 H100 的发货），而我们预计到 2025 年初，人工智能数据中心的容量需求将超过 10 吉瓦。

The above report is an underestimation of datacenter power demand, but there are plenty of overestimates too – some from the alarmist camp have recycled [old paper](https://www.mdpi.com/2078-1547/6/1/117)s written before the widespread adoption of accelerated compute that point to a worst-case scenario with datacenters consuming a whopping 7,933 TWh or 24% of global electricity generation by 2030!  
上述报告低估了数据中心的电力需求，但也有很多高估 \- 一些来自危言耸听的阵营的人回收了在广泛采用加速计算之前撰写的旧论文，指出数据中心到 2030 年可能消耗惊人的 7,933 TWh，占全球电力发电量的 24%！

Here come the datacenter locusts, Dyson spheres, Matrioshka brains!  
数据中心蝗虫来了，戴森球，马特里奥什卡大脑！

Many of these back of the envelope estimates are based on a function of growth estimates for global internet protocol traffic, and estimates for power used per unit of traffic dampened by efficiency gains – all figures that are extremely hard to estimate, while others utilize top down datacenter power consumption estimates created in the pre-AI era. Mckinsey also has laughably bad estimates, which pretty much amount to putting their finger on a random CAGR and repeating it with fancy graphics.  
这些草稿估计中的许多是基于全球互联网协议流量增长估计的函数，以及每单位流量使用的功率估计，受效率提高的影响 \- 所有这些数字都极难估计，而其他人则利用了在人工智能时代之前创建的数据中心功耗的自上而下估计。麦肯锡也有令人发笑的糟糕估计，基本上相当于把他们的手指放在一个随机的复合年增长率上，并用花哨的图形重复它。

**Let’s correct the narrative here and quantify the datacenter power crunch with empirical data.  
让我们在这里纠正叙述，并用经验数据量化数据中心的电力危机。** 

Our approach forecasts AI Datacenter demand and supply through [our analysis of over 1,100 datacenters in North America across existing colocation and hyperscale datacenters](https://www.semianalysis.com/p/datacenter-model), including construction progress forecasts for datacenters under development, and for the first time ever for a study of its type, we combine this database with AI Accelerator power demand derived from [our AI Accelerator Model](https://www.semianalysis.com/p/accelerator-model) to estimate AI and non-AI Datacenter Critical IT Power demand and supply. We also combine this analysis with regional aggregate estimates for geographies outside North America (Asia Pacific, China, EMEA, Latin America) collated by [Structure Research](https://www.structureresearch.net/) to provide a holistic global view of datacenter trends. We supplement the regional estimates by tracking individual clusters and build outs of note with satellite imagery and construction progress, for example the up to 1,000 MW development pipeline in Johor Bahru, Malaysia (primarily by Chinese firms) – just a few miles north of Singapore.  
我们的方法通过分析北美地区超过 1,100 个数据中心（包括现有的合作数据中心和超大规模数据中心）来预测人工智能数据中心的需求和供应情况，还包括对正在建设中的数据中心的建设进展进行预测。这是该类型研究中首次将这一数据库与我们的人工智能加速器模型推导出的人工智能加速器功率需求相结合，以估算人工智能和非人工智能数据中心的关键 IT 功率需求和供应。我们还将这一分析与 Structure Research 整理的北美以外地区（亚太地区、中国、欧洲、中东和非洲、拉丁美洲）的区域总体估计相结合，以提供数据中心趋势的全球综合视图。我们通过卫星图像和建设进展追踪个别集群和值得注意的建设项目，例如马来西亚柔佛新山高达 1,000 兆瓦的开发管线（主要由中国公司开发），该地距新加坡仅几英里。

This tracking is done by hyperscaler, and it’s clear some of the largest players in AI will lag behind others in deployable AI compute over the medium term.  
这种追踪是由超大规模数据中心进行的，很明显，在中期内，一些人工智能领域最大的参与者在可部署的人工智能计算方面将落后于其他公司。

The AI boom will indeed rapidly accelerate datacenter power consumption growth, but global datacenter power usage will remain well below the doomsday scenario of 24% of total energy generation in the near term. We believe AI will propel datacenters to use 4.5% of global energy generation by 2030.  
AI 繁荣确实会迅速加速数据中心的能耗增长，但全球数据中心的能耗在短期内仍将远低于总能源发电量的 24%的末日场景。我们相信到 2030 年，AI 将推动数据中心使用全球能源发电量的 4.5%。

Datacenter power capacity growth will accelerate from a 12-15% CAGR to a 25% CAGR over the next few years. Global Datacenter Critical IT power demand will surge from 49 Gigawatts (GW) in 2023 to 96 GW by 2026, of which AI will consume ~40 GW. In reality the buildout is not this smooth and there is a real power crunch coming soon.  
数据中心的电力容量增长将从每年 12-15%的复合年增长率加速到未来几年的 25%的复合年增长率。全球数据中心关键 IT 电力需求将从 2023 年的 49 千兆瓦（GW）激增至 2026 年的 96 GW，其中人工智能将消耗约 40 GW。实际上，建设并不会如此顺利，真正的电力危机即将来临。

The need for abundant, inexpensive power, and to quickly add electrical grid capacity while still meeting hyperscalers’ carbon emissions commitments, coupled with chip export restrictions, will limit the regions and countries that can meet the surge in demand from AI Datacenters.  
对丰富、廉价的电力需求，以及在满足超大规模数据中心碳排放承诺的同时迅速增加电网容量的需求，再加上芯片出口限制，将限制能够满足 AI 数据中心需求激增的地区和国家。

Some countries and regions such as the US will be able to respond flexibly with a low electrical grid carbon intensity, low-cost fuel sources with supply stability, while others such as Europe will be effectively handcuffed by geopolitical realities and structural regulatory constraints on power. Others will simply grow capacity without care for environmental impact.  
一些国家和地区，如美国，能够灵活应对低电网碳强度、低成本燃料来源和供应稳定性，而其他地区，如欧洲，将受到地缘政治现实和结构性监管限制的影响。其他地区将简单地扩大产能，而不考虑环境影响。

AI Training workloads have unique requirements that are very dissimilar to those of typical hardware deployed in existing datacenters.  
AI 训练工作负载具有独特的要求，这些要求与现有数据中心中部署的典型硬件非常不同。

First, models train for weeks or months, with network connectivity requirements being relativity limited to training data ingress. Training is latency insensitive and does not need to be near any major population centers. AI Training clusters can be deployed essentially anywhere in the world that makes economic sense, subject to data residency and compliance regulations.  
首先，模型需要进行数周甚至数月的训练，网络连接要求相对较低，只需训练数据输入。训练对延迟不敏感，不需要靠近任何主要人口中心。人工智能训练集群可以部署在世界上任何经济上合理的地方，但需遵守数据驻留和合规法规。

The second major difference to keep in mind is also somewhat obvious – AI Training workloads are extremely power hungry and tend to run AI hardware at power levels closer to their Thermal Design Power (TDP) than would a traditional non-accelerated hyperscale or enterprise workload. Additionally, while CPU and storage servers consume on the order of 1kW, each AI server is now eclipsing 10kW. Coupled with the insensitivity towards latency and decreased importance of proximity to population centers, this means that the availability of abundant quantities of inexpensive electricity (and in the future – access to any grid supply at all) is of much higher relative importance for AI Training workloads vs traditional workloads. Incidentally, some of these are requirements shared by useless crypto mining operations, sans the scaling benefits of >100 megawatt in singular sites.  
请注意的第二个主要区别也显而易见——AI 训练工作负载极度耗电，并倾向于以接近其热设计功率（TDP）的功率水平运行 AI 硬件，而非传统的非加速超大规模或企业工作负载。此外，虽然 CPU 和存储服务器的功耗约为 1 千瓦，但每台 AI 服务器现在已超过 10 千瓦。再加上对延迟的不敏感和与人口中心的距离降低的重要性，这意味着对于 AI 训练工作负载而言，大量廉价电力的可用性（以及未来——对任何电网供应的访问）相对更为重要，与传统工作负载相比。顺便说一句，其中一些要求与无用的加密挖矿操作共享，只是缺少单一站点超过 100 兆瓦的规模化好处。

Inference on the other hand is eventually a larger workload than training, but it can also be quite distributed. The chips don’t need to be centrally located, but the sheer volume will be outstanding.  
推理，另一方面，最终比训练工作量更大，但也可以相当分散。芯片不需要集中放置，但数量之多将是惊人的。

AI Accelerators achieve relatively high utilization rates (in terms of power usage, not MFU). The expected average power (EAP) from normal operation per DGX H100 server is ~10,200 W, which works out to be 1,275W for each of the 8 GPUs per server. This incorporates the 700W Thermal Design Power (TDP) of the H100 itself, along with about 575W (allocated per GPU) for the Dual Intel Xeon Platinum 8480C processors and 2TB of DDR5 memory, NVSwitches, NVLink, NICs, retimers, network transceivers, etc. Adding the power needs for storage and management servers as well as various networking switches for an entire SuperPOD gets us to an effective power requirement of 11,112W per DGX server or 1,389W per H100 GPU. The DGX H100 configuration is somewhat overprovisioned with respect to storage and other items when compared to the HGX H100, which we account for. Companies like Meta have released enough information about their full configuration to estimate system level power consumption.  
AI 加速器实现了相对较高的利用率（以功耗而非 MFU 为单位）。每台 DGX H100 服务器的预期平均功耗（EAP）约为 10,200 瓦特，这意味着每台服务器的 8 个 GPU 的功耗为 1,275 瓦特。这包括 H100 本身的 700 瓦特热设计功耗（TDP），以及每个 GPU 分配的约 575 瓦特（用于双 Intel Xeon Platinum 8480C 处理器和 2TB DDR5 内存，NVSwitches，NVLink，NICs，再生器，网络收发器等）。将存储和管理服务器的功耗需求以及整个 SuperPOD 的各种网络交换机的功耗需求相加，我们得到每台 DGX 服务器的有效功耗需求为 11,112 瓦特，每个 H100 GPU 的功耗需求为 1,389 瓦特。与 HGX H100 相比，DGX H100 配置在存储和其他项目方面有些过度配置，我们已经考虑到了这一点。像 Meta 这样的公司已经发布了关于其完整配置的足够信息，以估算系统级功耗。

Critical IT Power is defined as the usable electrical capacity at the datacenter floor available to compute, servers and networking equipment housed within the server racks. It excludes the power needed to run cooling, power delivery and other facility related systems in the datacenter. To calculate the Critical IT Power capacity that needs to be built or purchased in this example, add up the total expected power load of the IT equipment deployed. In our example below, 20,480 GPUs at 1,389W per GPU equates to 28.4 MW of Critical IT Power Required.  
临界 IT 电力被定义为数据中心地板上可用的电力容量，可用于计算、服务器和网络设备，这些设备存放在服务器机架内。它不包括运行冷却、电力传输和数据中心其他设施相关系统所需的电力。要计算在本示例中需要建造或购买的临界 IT 电力容量，需要将部署的 IT 设备的总预期功率负载相加。在我们的示例中，20,480 个 GPU，每个 GPU 的功率为 1,389W，相当于需要 28.4MW 的临界 IT 电力。

To get to the total power that the IT equipment is expected to consume (Critical IT Power Consumed), we need to apply a likely utilization rate relative to Critical IT Power Required. This factor accounts for the fact that the IT equipment typically does not run at 100% of its design capability and may not be utilized to the same degree over a 24-hour period. This ratio is set to 80% in the example.  
要获得 IT 设备预计消耗的总功率（临界 IT 电力消耗），我们需要将一个可能的利用率应用于所需的临界 IT 电力。这个因素考虑到 IT 设备通常不会以其设计能力的 100% 运行，并且在 24 小时内可能不会以相同程度被利用。在本示例中，这个比率设置为 80%。

On top of the Critical IT Power Consumed, operators must also supply power for cooling, to cover power distribution losses, lighting and other non-IT facility equipment. The industry measures Power Usage Effectiveness (PUE) to measure the energy efficiency of data centers. It's calculated by dividing the total amount of power entering a data center by the power used to run the IT equipment within it. It of course is a very flawed metric, because cooling within the server is considered “IT equipment”. We account for this by multiplying the Critical IT Power Consumed by the Power Usage Effectiveness (PUE). A lower PUE indicates a more power efficient datacenter, with a PUE of 1.0 representing a perfectly efficient datacenter, with no power consumption for cooling or any non-IT equipment. A typical enterprise colocation PUE is around 1.5-1.6, while most hyperscale datacenters are below 1.4 PUE, with some purpose build facilities (such as Google’s) claim to achieve PUEs of below 1.10. Most AI Datacenter specs aim for lower than 1.3 PUE. The decline in industry-wide average PUE over the last 10 years, from 2.20 in 2010 to an estimated 1.55 by 2022 has been one of the largest drivers of power savings and has helped avoid runaway growth in datacenter power consumption.  
在关键的 IT 能耗之外，运营商还必须为冷却提供电力，以覆盖电力分配损失、照明和其他非 IT 设施设备。该行业使用电力使用效率（PUE）来衡量数据中心的能源效率。它是通过将进入数据中心的总电力量除以其中用于运行 IT 设备的电力来计算的。当然，这是一个非常有缺陷的指标，因为服务器内的冷却被视为“IT 设备”。我们通过将关键 IT 能耗乘以电力使用效率（PUE）来考虑这一点。较低的 PUE 表示数据中心更具电力效率，PUE 为 1.0 表示一个完全高效的数据中心，冷却或任何非 IT 设备都不消耗电力。典型的企业共用 PUE 约为 1.5-1.6，而大多数超大规模数据中心的 PUE 低于 1.4，一些专门建造的设施（如谷歌的）声称实现了低于 1.10 的 PUE。大多数人工智能数据中心的规格目标是低于 1.3 的 PUE。在过去 10 年中，行业平均 PUE 从 2010 年的 2.20 下降到估计的 1.到 2022 年，55%的节能已成为数据中心电力消耗的最大驱动力之一，并帮助避免了数据中心电力消耗的失控增长。

For example at 80% utilization rate and a PUE of 1.25, the theoretical datacenter with a cluster of 20,480 GPUs would on average draw 28-29MW of power from the grid, adding up to 249,185 Megawatt-hours per year, which would cost $20.7M USD per year in electricity based on average US power tariffs of $0.083 per kilowatt-hour.  
例如，在 80% 利用率和 PUE 为 1.25 的情况下，具有 20,480 个 GPU 群集的理论数据中心平均每年从电网吸取 28-29MW 的电力，累计为 249,185 兆瓦时，根据平均美国电力 tariffs 为每千瓦时 0.083 美元，这将导致每年电费为 2070 万美元。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ae3573-7fc5-4ed1-a1f4-359e0f41187b_1126x943.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92ae3573-7fc5-4ed1-a1f4-359e0f41187b_1126x943.png)

While the DGX H100 server requires 10.2 kilowatts (kW) of IT Power, most colocation datacenters can still only support a power capacity of ~12 kW per rack, though a typical Hyperscale datacenter can deliver higher power capacity.  
DGX H100 服务器需要 10.2 千瓦（kW）的 IT 功率，大多数共用数据中心仍然只能支持每个机架约 12 千瓦的功率容量，尽管典型的超大规模数据中心可以提供更高的功率容量。

Server deployments will therefore vary depending on the power supply and cooling capacity available, with only 2-3 DGX H100 servers deployed where power/cooling constrained, and entire rows rack space sitting empty to double the power delivery density from 12 kW to 24 kW in colocation datacenters. This spacing is implemented to resolve cooling oversubscription aswell.  
服务器部署因此会根据可用的电源和冷却容量而有所不同，只有在电源/冷却受限的情况下才部署 2-3 台 DGX H100 服务器，并且整个机架空间处于空置状态，以将功率传输密度从 12 kW 提高到 24 kW，以解决共同数据中心中的冷却过度订阅问题。

As datacenters are increasingly designed with AI workloads in mind, racks will be able to achieve power densities of 30-40kW+ using air cooling by using specialized equipment to increase airflow. The future use of direct to chip liquid cooling opens the door to even higher power density by [potentially reducing per rack power usage](https://www.supermicro.com/white_paper/white_paper_Liquid-Cooling-Solutions.pdf) by 10% by eliminating the use of fan power, and lowering PUE by 0.2-0.3 by reducing or eliminating the need for ambient air cooling, though with PUEs already at 1.25 or so, this will be the last wave of meaningful PUE gains to be had.  
随着数据中心越来越多地考虑到人工智能工作负载的设计，机架将能够通过使用专门的设备增加空气流量，实现 30-40kW+的功率密度。未来使用直接对芯片进行液冷可以进一步提高功率密度，通过可能减少每个机架的功耗 10%，消除风扇功率的使用，并通过减少或消除环境空气冷却的需求，降低 PUE 0.2-0.3。尽管 PUE 已经达到 1.25 左右，这将是最后一波有意义的 PUE 增益。

Another important consideration that many operators raise is that individual GPU server nodes are best positioned near each other to achieve acceptable cost and latency. A rule of thumb used is that racks from the same cluster should be at most 30 meters from the network core. The short reach enables lower cost multimode optical transceivers as opposed to expensive single mode, which can often reach multiple km of reach. The specific multimode optical transceiver typically used by Nvidia to connect GPUs to leaf switches has a short range of up to 50m. Using longer optical cables and longer reach transceivers to accommodate more distant GPU racks will add costs with much more expensive transceivers needed. Future GPU clusters utilizing other scale-up network technology will also require very short cable runs to work properly. For instance, in [Nvidia’s yet to be deployed NVLink scale-up network for H100 clusters](https://www.semianalysis.com/p/nvidias-optical-ascent-1b-revenue),  which supports clusters of up to 256 GPUs across 32 nodes and can deliver 57.6 TB/s of all-to-all bandwidth, the maximum switch-to-switch cable length will be 20 meters.  
许多运营商提出的另一个重要考虑因素是，最好将单个 GPU 服务器节点放置在彼此附近，以实现可接受的成本和延迟。一个经常使用的经验法则是，来自同一集群的机架与网络核心之间的距离最多应为 30 米。短距离可以使用成本更低的多模光收发器，而不是昂贵的单模光收发器，后者通常可以达到数公里的距离。Nvidia 通常用于将 GPU 连接到叶子交换机的特定多模光收发器的短距离范围为 50 米。使用更长的光缆和更远的收发器来容纳更远的 GPU 机架将增加成本，需要更昂贵的收发器。未来利用其他规模扩展网络技术的 GPU 集群也将需要非常短的电缆跑来正常工作。例如，在 Nvidia 尚未部署的 H100 集群的 NVLink 规模扩展网络中，支持最多 256 个 GPU 跨越 32 个节点的集群，并且可以提供 57.6 TB/s 的全互连带宽，最大交换机到交换机的电缆长度将为 20 米。

The trend towards higher power density per rack is driven more by networking, compute efficiency and cost per compute considerations – with regards to datacenter planning, as the cost of floor space and data hall space efficiency is an generally an afterthought. Roughly 90% of colocation datacenter costs are from power and 10% is from physical space.  
机柜功率密度不断增加的趋势更多地受到网络、计算效率和每计算成本的驱动 \- 关于数据中心规划，地板空间成本和数据大厅空间效率通常是事后考虑的问题。大约 90%的托管数据中心成本来自电力，10%来自物理空间。

The data hall where IT equipment is installed is typically only about 30-40% of a datacenter’s total gross floor area, so designing a data hall that is 30% larger will only require 10% more gross floor area for the entire datacenter. Considering that [80% of the GPU cost of ownership is from capital costs](https://www.semianalysis.com/p/gpu-cloud-economics-explained-the), with [20% related to hosting (which bakes in the colocation datacenter costs) the cost of additional space is a mere 2-3% of total cost of ownership for an AI Cluster](https://www.semianalysis.com/p/gpu-cloud-economics-explained-the).  
安装 IT 设备的数据大厅通常只占数据中心总毛地板面积的 30-40%，因此设计一个比原来大 30%的数据大厅只需要整个数据中心多 10%的毛地板面积。考虑到 80%的 GPU 所有权成本来自资本成本，而 20%与托管相关（其中包括托管数据中心成本），额外空间的成本仅占 AI 集群总拥有成本的 2-3%。

Most existing colocation datacenters are not ready for rack densities above 20kW per rack. Chip production constraints will meaningfully improve in 2024, but certain hyperscalers and colos run straight into a datacenter capacity bottleneck, because they were flat footed with AI – most notably within colocation datacenters, as well as a power density mismatch – where the limits of 12-15kW power in traditional colocation will be an obstacle to achieving ideal physical density of AI super clusters.  
大多数现有的托管数据中心无法承受每个机架超过 20 千瓦的功率密度。芯片生产限制将在 2024 年得到显著改善，但某些超大规模数据中心和托管数据中心因为在人工智能方面措手不及而陷入数据中心容量瓶颈，尤其是在托管数据中心内，以及功率密度不匹配的情况下——传统托管中 12-15 千瓦功率的限制将成为实现理想的人工智能超级集群物理密度的障碍。

Rear door heat exchangers and direct to chip liquid cooling solutions can be deployed in newly built datacenters to solve the power density problem. However, it is much easier to design a new facility from the ground up incorporating these solutions than it is to retrofit existing facilities – realizing this, Meta has [halted development of planned datacenter projects](https://www.datacenterdynamics.com/en/news/exclusive-after-meta-cancels-odense-data-center-expansion-other-projects-are-being-rescoped/) to rescope them into datacenters [catering specifically to AI workloads](https://www.datacenterdynamics.com/en/analysis/how-meta-redesigned-its-data-centers-for-the-ai-era/).  
后门热交换器和直接到芯片液冷解决方案可以部署在新建的数据中心中，以解决功率密度问题。然而，相比于改造现有设施，从头开始设计一个新的设施并将这些解决方案纳入其中要容易得多——意识到这一点，Meta 已经停止了计划中的数据中心项目的开发，将其重新规划为专门为 AI 工作负载提供服务的数据中心。

Meta had the worst datacenter design in terms of power density of all the hyperscalers, but they woke up and shifted very quickly. Retrofitting an existing datacenter is costly, time consuming, and in some cases may not even be possible – there may not be the physical space to install additional units of 2-3 MW generators, Uninterruptable Power Supplies (UPSs), switching gear or additional transformers, and redoing plumbing to accommodate the Cooling Distribution Units (CDUs) needed for direct to chip liquid cooling is hardly ideal.  
Meta 在所有超大规模数据中心中的功率密度设计最差，但他们醒悟过来并迅速转变。对现有数据中心进行改造成本高昂、耗时且在某些情况下甚至不可能——可能没有物理空间安装额外的 2-3 兆瓦发电机组、不间断电源系统（UPS）、开关设备或额外的变压器，并重新布置管道以适应直接冷却芯片所需的冷却分配单元（CDU）几乎不理想。

Using a line-by-line unit shipment forecasts by accelerator chip based on our [AI Accelerator Model](https://www.semianalysis.com/p/ai-capacity-constraints-cowos-and) together with our estimated chip specifications and modeled ancillary equipment power requirements, we calculate total AI Datacenter Critical IT Power needs for the next few years.  
利用我们的 AI 加速器模型基于加速器芯片的逐行出货预测，结合我们估计的芯片规格和建模的辅助设备功耗需求，我们计算未来几年 AI 数据中心关键 IT 功耗总需求。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd411a4d-2b02-4f43-a20b-888a04a64de2_1553x987.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd411a4d-2b02-4f43-a20b-888a04a64de2_1553x987.png)

SemiAnalysis EstimatesSemiAnalysis 估计

As mentioned above, total Datacenter Critical IT Power demand will double from about 49 GW in 2023 to 96 GW by 2026, with 90% of the growth coming from AI-related demand. This is purely from chip demand, but [physical datacenters](https://www.semianalysis.com/p/datacenter-model) tell a different story.  
如上所述，到 2026 年，总数据中心关键 IT 功率需求将从 2023 年的约 49 吉瓦增加到 96 吉瓦，其中 90% 的增长来自 AI 相关需求。这纯粹是来自芯片需求，但物理数据中心讲述了一个不同的故事。

Nowhere will the impact be felt more than in the United States, where our satellite data shows the majority of AI Clusters are being deployed and planned, meaning Datacenter Critical IT Capacity in the US will need to triple from 2023 to 2027.  
在美国，AI 集群的部署和规划占据绝大部分，我们的卫星数据显示，这将对美国产生的影响最为显著，这意味着美国的数据中心关键 IT 容量需要从 2023 年到 2027 年增加两倍。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f8168e8-e7ca-4006-bab6-e93b55151e83_1698x514.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f8168e8-e7ca-4006-bab6-e93b55151e83_1698x514.png)

SemiAnalysis EstimatesSemiAnalysis 估计

Aggressive plans by major AI Clouds to roll out accelerator chips highlight this point. OpenAI has [plans to deploy hundreds of thousands of GPUs](https://www.semianalysis.com/p/microsoft-swallows-openais-core-team) in their largest multi-site training cluster, which requires hundreds of megawatts of Critical IT Power. [We can track their cluster size quite accurately by looking at the buildout of the physical infrastructure, generators, and evaporation towers](https://www.semianalysis.com/p/datacenter-model). Meta discusses an installed base of 650,000 H100 equivalent by the end of the year. GPU Cloud provider CoreWeave has [big plans to invest $1.6B in a Plano, Texas facility](https://www.datacenterdynamics.com/en/news/coreweave-plans-16bn-ai-cloud-data-center-in-plano-texas/), implying plans to spend for construction up to 50MW of Critical IT Power and install 30,000-40,000 GPUs in that facility alone, with a clear pathway to a whole company 250MW datacenter footprint (equivalent to 180k H100s), and they have plans for multiple hundreds of MW in a single site in planning.  
主要 AI 云计划推出加速器芯片的积极计划突显了这一点。OpenAI 计划在其最大的多地点培训集群中部署数十万个 GPU，这需要数百兆瓦的关键 IT 功率。我们可以通过观察物理基础设施、发电机和蒸发塔的建设情况来相当准确地追踪他们的集群规模。Meta 讨论了到年底将安装的 65 万个 H100 等效设备。GPU 云服务提供商 CoreWeave 计划在德克萨斯州普莱诺投资 16 亿美元，意味着计划在该设施的建设上花费高达 50 兆瓦的关键 IT 功率，并在该设施单独安装 3 万至 4 万个 GPU，明确规划了整个公司 2.5 亿瓦特的数据中心足迹（相当于 18 万个 H100s），并且他们计划在一个地点规划多达数百兆瓦。

Microsoft has the largest pipeline of datacenter buildouts pre-AI era (see January 2023 data below), and [our data shows its skyrocketed since](https://www.semianalysis.com/p/datacenter-model). They have been gobbling any and all colocation space they can as well aggressively increasing their datacenter buildouts[. AI laggers like Amazon](https://www.semianalysis.com/p/amazons-cloud-crisis-how-aws-will) have made press releases about nuclear powered datacenters totaling 1,000MW, but to be clear they are lagging materially on real near term buildouts as they were [the last of the hyperscalers to wake up to AI](https://www.semianalysis.com/p/amazons-cloud-crisis-how-aws-will). Google, and Microsoft/OpenAI both have plans for larger than Gigawatt class training clusters in the works.  
微软在人工智能时代之前拥有最大规模的数据中心建设项目（请参阅下面的 2023 年 1 月数据），我们的数据显示自那时以来规模急剧扩大。他们一直在积极地扩大数据中心建设，并不断吞并任何和所有的共用空间。亚马逊等人工智能后来者发布了关于核能数据中心总容量达到 1,000 兆瓦的新闻稿，但明确指出他们在近期实际建设方面明显滞后，因为他们是最后一批意识到人工智能重要性的超大规模数据中心运营商。谷歌和微软/OpenAI 都计划建设超过千兆瓦级别的训练集群。

From a supply perspective, sell side consensus estimates of 3M+ GPUs shipped by Nvidia in calendar year 2024 would correspond to over 4,200 MW of datacenter needs, nearly 10% of current global datacenter capacity, just for one year’s GPU shipments. The consensus estimates for Nvidia’s shipments are also very wrong of course. Ignoring that, AI is only going to grow in subsequent years, and Nvidia’s GPUs are [slated to get even more power hungry](https://www.semianalysis.com/p/nvidias-plans-to-crush-competition), with 1,000W, 1,200W, and 1,500W GPUs on the roadmap. Nvidia is not the only company producing accelerators, with [Google ramping custom accelerator production rapidly](https://www.semianalysis.com/p/broadcoms-google-tpu-revenue-explosion). Going forward, Meta and Amazon will also ramp their in house accelerators.  
从供应角度来看，Nvidia 在 2024 年的日历年出货的 3M+ GPU 的卖方共识估计将对应于超过 4,200 兆瓦的数据中心需求，几乎占据了当前全球数据中心容量的 10%，仅仅是一年的 GPU 出货量。当然，Nvidia 的出货量的共识估计也是非常错误的。忽略这一点，人工智能在随后的几年中只会增长，Nvidia 的 GPU 预计将变得更加耗电，路线图上有 1,000W、1,200W 和 1,500W 的 GPU。Nvidia 并不是唯一一家生产加速器的公司，Google 正在快速推进定制加速器的生产。未来，Meta 和亚马逊也将加速他们内部的加速器。

This reality is not lost on the top global hyperscalers – who are rapidly ramping up datacenter construction and colocation leasing. AWS literally bought a 1000MW [nuclear-powered datacenter campus](https://www.datacenterdynamics.com/en/news/aws-acquires-talens-nuclear-data-center-campus-in-pennsylvania/) for $650M USD. Though only the very first building with 48MW of capacity is likely to be online in the near term, this provides a valuable pipeline of datacenter capacity for AWS without being held up waiting for power generation or grid transmission capacity. We think a campus of such mammoth proportions will take many years to fully ramp to the promised 1,000 MW of Critical IT Power.  
这个现实并没有被全球顶级超大规模数据中心运营商忽视 \- 他们正在快速扩建数据中心和租赁机房。AWS 实际上以 6.5 亿美元购买了一个 1000MW 核动力数据中心园区。尽管在短期内可能只有 48MW 容量的第一栋建筑有望上线，但这为 AWS 提供了一个宝贵的数据中心容量管道，而不必等待发电或电网传输能力。我们认为这样规模庞大的园区将需要多年时间才能完全达到承诺的 1000MW 临界 IT 功率。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe94eed35-8a5b-44c1-a02e-6aeae001a145_1886x1078.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe94eed35-8a5b-44c1-a02e-6aeae001a145_1886x1078.png)

Datacenter Dynamics数据中心动态

Understanding power requirements for training popular models can help gauge power needs as well as understand carbon emissions generated by the AI industry. [ Estimating the Carbon Footprint of BLOOM, a 175B Parameter Language Model](https://arxiv.org/abs/2211.02001) examines the power usage of training the BLOOM model at the Jean Zay computer cluster at IDRIS, a part of France’s CNRS. The paper provides empirical observations of the relationship of an AI Chip’s TDP to total cluster power usage including storage, networking and other IT equipment, all the way through the actual power draw from the grid.  
了解培训流行模型的功率需求可以帮助评估功率需求，以及了解人工智能行业产生的碳排放。估算 BLOOM，一个 175B 参数语言模型的碳足迹，研究了在法国国家科学研究中心（CNRS）的 Jean Zay 计算机集群上训练 BLOOM 模型的功耗。该论文提供了关于 AI 芯片的 TDP 与总集群功耗之间关系的经验观察，包括存储、网络和其他 IT 设备，一直到实际从电网中吸取的电力。

Another paper, [Carbon Emissions and Large Neural Network Training](https://arxiv.org/abs/2104.10350), reports on the training time, configuration and power consumption of training for a few other models. Power needs for training can vary depending on the efficiency of models and training algorithms (optimizing for Model FLOPs Utilization – MFU) as well as overall networking and server power efficiency and usage, but the results as reproduced below are a helpful yardstick  
另一篇论文《碳排放和大型神经网络训练》报告了几种其他模型的训练时间、配置和功耗。训练的功耗可以根据模型和训练算法的效率（优化模型 FLOPs 利用率 - MFU）以及整体网络和服务器功耗效率和使用情况而变化，但下面复制的结果是一个有用的标准。

The papers estimate the carbon emissions from training these models by multiplying the total power consumption in kWh by the [carbon intensity of the power grid](https://www.epa.gov/egrid/data-explorer) that the datacenter is running on. Eagle eyed readers will note the very low carbon intensity of 0.057 kg CO2e/kWh for training the BLOOM model in France, which sources 60% its electricity from nuclear power, far lower than the [0.387 kg CO2e/kWh average for the US](https://www.epa.gov/egrid/data-explorer). We provide an additional set of calculations assuming the training jobs are run on datacenters connected to a power grid in Arizona, one of the leading states for datacenter buildouts currently.  
这些论文通过将总耗电量（以千瓦时为单位）乘以数据中心所在电网的碳强度来估算这些模型的碳排放量。敏锐的读者会注意到在法国训练 BLOOM 模型的碳强度非常低，为 0.057 公斤 CO2e/kWh，该国电力的 60% 来自核能，远低于美国的平均值 0.387 公斤 CO2e/kWh。我们还提供了一组额外的计算，假设训练作业在目前数据中心建设的领先州之一的亚利桑那州的电网上运行。

The last piece of the emissions puzzle to consider is embodied emissions, defined as the total carbon emissions involved in manufacturing and transporting a given device, in this case the accelerator chip and related IT equipment. Solid data on embodied emissions for AI Accelerator Chips is scarce, but some have roughly estimated the figure at 150kg of CO2e per A100 GPU and 2,500kg of CO2e for a server hosting 8 GPUs. Embodied emissions work out to be about 8-10% of total emissions for a training run.  
考虑的排放谜题的最后一块是体现排放，定义为制造和运输给定设备所涉及的总碳排放，本例中是加速器芯片和相关的 IT 设备。对于 AI 加速器芯片的体现排放的实际数据很少，但一些人粗略估计为每个 A100 GPU 的 CO2e 为 150 公斤，8 个 GPU 的服务器的 CO2e 为 2,500 公斤。体现排放约占训练运行总排放的 8-10%。

The carbon emissions from these training runs are significant, with one GPT-3 training run generating 588.9 metric tons of CO2e, equivalent to the [annual emissions of 128 passenger vehicles](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle). Complaining about GPT-3 training emissions is like recycling plastic water bottles but then taking a flight every few months. Literally irrelevant virtue signaling.  
这些训练运行产生的碳排放量相当可观，其中一个 GPT-3 训练运行产生了 588.9 公吨 CO2e，相当于 128 辆乘用车的年排放量。抱怨 GPT-3 训练排放就像回收塑料水瓶，然后每隔几个月就乘飞机一样。完全无关的虚伪信号。

On the flip side, it is a safe bet that there were many iterations of training runs before settling down on the final model. In 2022, [Google emitted a total of 8,045,800 metric tons of CO2e](https://sustainability.google/reports/google-2023-environmental-report/) from its facilities including datacenters, before factoring in any offsets from renewable energy projects. All this means is GPT-3 is not effecting carbon output of the world, but with the FLOPS of GPT-4 multiple orders of magnitude more, and the current OpenAI training run, more than an magnitude above that, the carbon emissions of training are going to start to become sizeable in a few years.  
反过来说，可以肯定在最终模型确定之前进行了许多次训练运行。2022 年，谷歌在其设施（包括数据中心）排放了总共 8,045,800 公吨 CO2e，未考虑任何来自可再生能源项目的抵消。所有这些意味着 GPT-3 并未影响世界的碳排放，但随着 GPT-4 的 FLOPS 数量级增加，以及当前 OpenAI 的训练运行，超过了一个数量级，训练的碳排放将在未来几年开始变得可观。

For inference, we have detailed the economics of AI Cloud hosting in our posts on [GPU Cloud Economics](https://www.semianalysis.com/p/gpu-cloud-economics-explained-the) and on [Groq Inference Tokenomics](https://www.semianalysis.com/p/groq-inference-tokenomics-speed-but). A typical H100 server with 8 GPUs will emit about 2,450 kg of CO2e per month and require 10,200 W of IT Power – a cost of $648 per month assuming $0.087 per kilowatt-hour (KWh).    
对于推理，我们在我们的 GPU 云经济学和 Groq 推理代币经济学的帖子中详细介绍了 AI 云托管的经济情况。一个典型的带有 8 个 GPU 的 H100 服务器每月将排放约 2,450 公斤的 CO2e，并需要 10,200 瓦的 IT 功率-假设每千瓦时（KWh）0.087 美元，每月成本为 648 美元。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb6ee4a0-5d69-466b-965f-fc42ebd93924_1912x1365.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb6ee4a0-5d69-466b-965f-fc42ebd93924_1912x1365.png)

SemiAnalysis EstimatesSemiAnalysis 估计

The AI Datacenter industry is going to need the following:  
AI 数据中心行业将需要以下内容：

*   Inexpensive electricity costs given the immense amount of power to be consumed on an ongoing basis, particularly since inference needs will only compound over time.  
    由于需要消耗大量电力，尤其是随着时间推移，推断需求只会不断增加，因此需要低廉的电力成本。
    
*   Stability and robustness of energy supply chain against geopolitical and weather disturbances to decrease likelihood of energy price volatility, as well as the ability to quickly ramp up fuel production and thus rapidly provision power generation at great scale.  
    能源供应链的稳定性和健壮性，以抵御地缘政治和天气干扰，降低能源价格波动的可能性，以及快速增加燃料生产能力，从而迅速提供大规模的发电能力。
    
*   Power generation with a low carbon intensity power mix overall, and that suitable to stand up massive quantities of renewable energy that can produce at reasonable economics.  
    具有低碳强度电力混合的发电，适合承载大量可以以合理经济方式产生的可再生能源。
    

Countries that can step up to the plate and tick off those boxes are contenders to be Real AI Superpowers.  
能够胜任并勾选这些方面的国家有望成为真正的人工智能超级大国。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fec2a9c-7a44-4eaa-83c3-55049d3174c6_2446x1464.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fec2a9c-7a44-4eaa-83c3-55049d3174c6_2446x1464.png)

US EIA, Various National and Regional Electrical Distribution Organizations  
美国能源信息署，各种国家和地区的电力分配组织

Comparing global electricity tariffs, the US has among the lowest power prices in the world at $0.083 USD/kWh on average. Natural gas production in the US is abundant and has surged since the [shale gas revolution of the early 2000s](https://www.strausscenter.org/energy-and-security-project/the-u-s-shale-revolution/), which made the US the world’s largest producer of natural gas. Almost 40% of the electricity generation in the US is fueled by natural gas, with low power generation prices chiefly driven by the abundance of dry natural gas production from shale formations. Natural gas prices will remain depressed in the US due to fracking for oil and the increasing percentage of gas coming from wells, and so natural gas bulls that ping us every few weeks about datacenter power consumption should probably calm down.  
比较全球的电力价格，美国的平均电价为 0.083 美元/千瓦时，属于世界上最低的之一。美国的天然气产量丰富，并自从 21 世纪初页岩气革命以来一直在激增，使美国成为世界上最大的天然气生产国。美国近 40%的电力发电来自天然气，低电力价格主要受益于页岩层干天然气产量的丰富。由于对石油的水力压裂和天然气来自井口的比例不断增加，美国的天然气价格将保持低迷，因此那些每隔几周就会询问我们数据中心电力消耗的天然气支持者可能应该冷静下来。

The fact that the US is energy independent in natural gas adds geopolitical stability to prices, and the widespread distribution of gas fields across the US adds supply chain robustness, while a [proven reserve of 20 years of consumption](https://www.eia.gov/energyexplained/natural-gas/how-much-gas-is-left.php) adds longevity to energy supply, though these reserve estimates have increased over the years, doubling since 2015 and up 32% in 2021 alone.  
美国在天然气方面的能源独立事实为价格增添了地缘政治稳定性，美国境内天然气田的广泛分布增加了供应链的稳健性，而 20 年的消耗储备为能源供应增添了长久性，尽管这些储备估计多年来一直在增加，自 2015 年以来翻了一番，在 2021 年仅增加了 32%。

In addition, the US has a far greener energy mix than most of the other contenders, having reduced its coal mix of power generation from 37% in 2012 to 20% by 2022 with the coal mix forecast to reach 8% by 2030 as natural gas and renewables step in to fill the gap. This compares to India at a 75% coal mix, China at a 61% coal mix, and even Japan still at a 34% coal mix in 2022. This difference is very impactful as coal power plants have a [carbon intensity of 1.025 kg/kWh CO2e, over double that of natural gas plants at 0.443 kg/kWh CO2e](https://www.eia.gov/todayinenergy/detail.php?id=48296). Datacenters built in the US will therefore rely on a far cleaner fuel mix for necessary baseload and overnight power generation than in many other countries.  
此外，美国的能源组合比大多数其他竞争对手更加环保，自 2012 年以来，其发电煤炭比例已从 37%降至 2022 年的 20%，预计到 2030 年，煤炭比例将降至 8%，因为天然气和可再生能源将填补缺口。与 2022 年印度的 75%煤炭比例、中国的 61%煤炭比例以及甚至日本仍然保持 34%煤炭比例相比，这种差异非常重要，因为燃煤发电厂的碳强度为 1.025 千克/千瓦时 CO2e，是天然气发电厂的 0.443 千克/千瓦时 CO2e 的两倍多。因此，在美国建造的数据中心将依赖于比许多其他国家更清洁的燃料组合进行必要的基础负荷和夜间发电。

The energy supply situation in the US stands in stark contrast to East Asia and Western Europe, which host about 15% and 18% of global datacenter capacity respectively. While the US is self-sufficient in natural gas, countries such as Japan, Taiwan, Singapore, and Korea import well over 90% of their gas and coal needs.  
美国的能源供应情况与东亚和西欧形成鲜明对比，东亚和西欧分别拥有全球数据中心容量的约 15%和 18%。美国在天然气方面基本自给自足，而日本、台湾、新加坡和韩国等国家的天然气和煤炭需求超过 90%依赖进口。

Japan’s power mix is tilted towards these imported fuel types, with 35% natural gas, 34% coal, 7% hydro and 5% nuclear, resulting in average industrial electricity tariffs of $0.152 USD/kWh in 2022, 82% higher than the US at $0.083 USD/kWh. Taiwan and Korea have similar power mixes dominated by natural gas imports and have electricity tariffs of about $0.10 to $0.12 USD/kWh, though this is after $0.03 to $0.04 of effective subsidies given the state owned electric companies have been running massive losses, with Korea’s [KEPCO losing $24B in 2022](https://www.ft.com/content/3533347c-cd50-4e42-bd15-e48173b003d7) and Taiwan’s Taipower [losing $0.04 USD per kWh](https://www.taiwannews.com.tw/en/news/4839443) sold.  
日本的能源结构偏向这些进口燃料类型，天然气占 35%，煤炭占 34%，水电占 7%，核能占 5%，导致 2022 年工业用电平均电价为 0.152 美元/千瓦时，比美国的 0.083 美元/千瓦时高出 82%。台湾和韩国的能源结构也以天然气进口为主导，电价约为 0.10 至 0.12 美元/千瓦时，尽管这是在国有电力公司运营巨额亏损的情况下，通过有效补贴后的价格，韩国的 KEPCO 在 2022 年亏损了 240 亿美元，台湾的台电每卖出一千瓦时电力亏损 0.04 美元。

In ASEAN, Singapore is another datacenter hub that has a heavy reliance on imported natural gas at 90% of its power generation mix, resulting in a high electricity tariff of $0.23 USD/kWh in 2022. The 900MW of Critical IT Power that Singapore hosts is large relative to its power generation capacity and consumes over 10% of Singapore’s national power generation. For this reason, Singapore had placed a four-year moratorium on new datacenter builds which only lifted in July 2023 with approval of a mere 80MW of new capacity. This constraint has spawned an enormous development pipeline of up to 1,000 MW of capacity in Johor Bahru, Malaysia, just a few miles north of Singapore, with much of it being driven by Chinese companies trying to "internationalize" and increasingly distancing themselves from their mothership parent companes in China. Indonesia also has a significant pipeline.

China’s industrial electricity tariff of $0.092 USD/kWh is on the low end of the range for electricity tariffs, but like many other emerging markets, China has a very dirty power generation mix, with 61% of generation from coal. This is a significant disadvantage from an emissions perspective, and new coal power plants are still being approved despite China significantly leading the world in renewable power installation. Any hyperscale or AI company that has a net-zero emissions commitment will be fighting an uphill battle with respect to that goal given coal’s [carbon intensity of 1.025 kg/kWh CO2e vs natural gas at 0.443 kg/kWh CO2e](https://www.eia.gov/todayinenergy/detail.php?id=48296).

China is largely self-reliant on coal used for power generation, but it imports the vast majority of its other energy needs, with over 70% of its petroleum and LNG exports shipped through the Strait of Malacca, and therefore subject to the so-called “[Malacca Dilemma](https://gjia.georgetown.edu/2023/03/22/chinas-economic-security-challenge-difficulties-overcoming-the-malacca-dilemma/)”, meaning that for strategic reasons China cannot pivot towards natural gas and will have to rely on adding coal and nuclear for baseload generation.  China does lead the world in adding renewable capacity, however, the huge existing base of fossil fuel-based power plants and continued reliance on adding coal power to grow overall capacity means that in 2022 only 13.5% of total power generation was from renewables.

To be clear, China is the best country at building new power generation, and they would likely lead in the construction of gigawatt scale datacenters if they were enabled to, but they cannot, so the US is dominating here.

And this is all before looking the elephant in the room squarely in the eyes, specifically, [the ongoing AI Semiconductor export controls](https://www.semianalysis.com/p/wafer-wars-deciphering-latest-restrictions) put into place by the US’s Bureau of Industry and Security, which has the intent of almost entirely denying China from obtaining any form of AI chips. In this respect, the exports control whack-a-mole game is ongoing, with Nvidia tweaking its chips to [comply with the latest changes](https://www.semianalysis.com/p/nvidias-new-china-ai-chips-circumvent) to the controls. The H20 has a huge ramp in Q2 and on for China, but this is still nowhere close to the 35% to 40% of AI chips China would import if they were allowed to.

In Western Europe, electricity generation has been slowly declining, with a 5% drop cumulatively over the past five years. One reason for the drop is that nuclear power has become a political non-starter, causing nuclear power generation to decline massively, for example declining 75% in Germany from 2007 to 2021. A strong focus on the “environment” has led to dirty fuel sources such as coal also declining dramatically over the same time, although the cleanest power in the world nuclear has been replaced with coal and natural gas in some instances. Renewable energy is increasing within Europe’s power mix, but not fast enough, leaving many Europeans countries to scramble to pivot more towards natural gas, which now stands at 35-45% of the power generation mix for major Western European countries.

Given Europe’s energy situation, the EU average industrial tariff reached $0.18 USD/kWh in 2022, with the UK at $0.235 USD/kWh and datacenter heavyweight Ireland at $0.211 USD/kWh, nearly triple the electricity cost in the US. Like Asia, Europe imports over 90% of its gas in the form of LNG, mainly sourced from the Middle East (and also still [from Russia](https://www.reuters.com/business/energy/lng-imports-russia-rise-despite-cuts-pipeline-gas-2023-08-30/), despite the ongoing war), so their entire industrial base, not just Datacenters, is subject to geopolitical risk, as most readers will vividly remember from the onset of the war in Ukraine. Given the political and geopolitical realities, adding a massive amount of power generation capacity to host the AI Datacenter boom in Europe would be very challenging.

Furthermore, Europe is allergic to building as proven by many regulations and restrictions on the datacenter and manufacturing industries already in place. While small projects and pipelines for datacenters are in progress, especially in France who at least has somewhat realized the geopolitical necessity, no one is planning to build Gigawatt class clusters in Europe. Europe has less than 4% of globally deployed AI Accelerator FLOPs based on our estimates.

As discussed, electricity pricing will matter considerably given the scale of AI clusters to be deployed, amounting to hundreds of millions of dollars of cost difference depending where the clusters are deployed. Locating AI Datacenters in Europe or Asia would easily double or triple the power costs vs building datacenters in the US. Furthermore construction costs are also higher due to the lack of skills.

The Middle East is another location that is racing to start datacenter construction and they scores very high among the Real AI Superpower criteria in some metrics, with some of the lowest electricity tariffs globally, and very high viability for the use of Solar power. Indeed, the Middle East has a very strong pipeline with the UAE expected to nearly triple Datacenter Critical IT Power from 115MW in 2022 to 330MW by 2026.

Saudi Arabia has already gotten involved with [the purchase of a measily 3,000 H100s](https://www.ft.com/content/c93d2a76-16f3-4585-af61-86667c5090ba) so far for its research institution, with plans to build its own LLM. Microsoft also announced plans to establish a datacenter in Saudi Arabia, following on the [launch of its Qatar datacenter](https://news.microsoft.com/en-xm/2022/08/31/microsoft-opens-first-global-datacenter-region-in-qatar-bringing-new-opportunities-for-a-cloud-first-economy/) in 2022. Saudi Arabia leads the pack however, with a current Critical IT Power of 67MW, but with plans to leapfrog the UAE and reach 530MW in the next few years.

Meanwhile, AI startup Omniva, which has just barely exited from stealth mode, purportedly aims to build low-cost AI Datacenter facilities in the Middle East with significant backing from a Kuwaiti royal family member. It boasts ex AWS, Meta and Microsoft staff among key personnel. They are the only one with real traction on the ground movement and have the most impressive talent / pedigree, but they also have a legal battle with Meta having sued an employee who allegedly stole documents and recruited 8 former employees to join.

**Below we are going to quantify the power price differences, transformer infrastructure, power generation capabilities, and a breakdown of global datacenter capex requirements by UPS, Generator, Switch Gear, Power Distribution, CRAH/CRAC, Chillers, Cooling towers, Valves/pipes/pumps, Project Management Facility Engineering, Lighting, Management, Security, IT Enclosures and containment, raised floors/dropped ceilings, and Fire protection.**

**We will also dive deeper into Meta’s buildouts specifically. We will also discuss the merits of solar versus wind on the renewable side and regional differences for deploying this type of power. Power storage capabilities, and carbon emissions are also touched on.**

[Get 20% off a group subscription](https://www.semianalysis.com/subscribe?group=true&coupon=fe141654)

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d2bade3-4a05-402f-9ee6-c45e4a3403cb_970x1060.png)


](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d2bade3-4a05-402f-9ee6-c45e4a3403cb_970x1060.png)

US EIA, Various National and Regional Electrical Distribution Organizations