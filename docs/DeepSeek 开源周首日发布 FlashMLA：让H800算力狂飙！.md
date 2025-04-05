Title: DeepSeek 开源周首日发布 FlashMLA：让H800算力狂飙！

URL Source: https://mp.weixin.qq.com/s/GN87C95lT2tHUkIf8lbnnw

Markdown Content:
![Image 1: 图片](https://mmbiz.qpic.cn/mmbiz_gif/u6UOjABnicbtCz6ryiaibXxklcGd6LqtORpX1aia788BnKm9TXI9E3oJvyOTwMTFFaguMCMGNVeT7R9H4TCswsa9gA/640?wx_fmt=gif&from=appmsg&retryload=1&wxfrom=5&wx_lazy=1&tp=webp)

2 月 24 日，DeepSeek 正式启动“开源周”，率先发布了首个开源项目FlashMLA（Flash Multi-Layer Attention），这是一款专为英伟达 Hopper 架构 GPU（如 H800）设计的高效多层注意力解码内核，旨在优化大语言模型（LLM）的推理性能，显著提升处理变长序列的效率。

![Image 2: Image](https://mmbiz.qpic.cn/sz_mmbiz_png/kfiaiar8iaaIIXnMyfCxzBygw3D2sPDZ4VTZpRCTXL3xThZWUc2ew8uicQ5NxPUIPXzCX35XbNxfKsbbUqUwVib4aVQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

DeepSeek的成本涉及两项关键的技术：一个是MoE，一个就是MLA（多层注意力机制）。

MLA 是一种改进的注意力机制，旨在提高Transformer模型在处理长序列时的效率和性能‌。MLA通过多个头（head）的并行计算，让模型能够同时关注文本中不同位置和不同语义层面的信息，从而更全面、更深入地捕捉长距离依赖关系和复杂语义结构‌。

![Image 3: Image](https://mmbiz.qpic.cn/sz_mmbiz_png/kfiaiar8iaaIIXnMyfCxzBygw3D2sPDZ4VTbqxtWbibjT82qtibkLPicloxVm6w49L2qYLOZXRw5xhZ8GibtY9a9b5Z9w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**技术突破：三大创新释放 GPU 潜能**

**1\. 分页 KV 缓存技术**

FlashMLA 引入了类似操作系统的分页内存管理机制，将键值对（KV 缓存）划分为固定大小的块（块大小为 64），按需动态分配显存。这一设计显著减少了显存碎片化问题，使 H800 GPU 的内存带宽利用率飙升至3000 GB/s，尤其适用于高并发推理场景。

**2\. BF16 精度支持**

采用 BF16（Bfloat16）精度格式，在保持 FP32 动态范围的同时，减少一半存储空间，平衡了计算效率与模型精度。这使得 FlashMLA 在计算密集型任务中实现了580 TFLOPS的单卡算力，较传统方案性能提升超 30%。

**3\. 低秩联合压缩**

受 LoRA 和 Stable Diffusion 启发，FlashMLA 对注意力机制中的键值矩阵进行低秩压缩，将 KV 缓存体积压缩至原始的 1/4，大幅降低显存需求。例如，原本需要 100GB 的中间结果，压缩后仅需 25GB。

**实际应用：加速 AI 商业化落地**

FlashMLA 已成功应用于生产环境，支持聊天机器人、长文本生成等实时任务。其动态处理变长序列的能力，解决了传统方法需填充（Padding）固定长度导致的算力浪费问题，使模型响应速度更快、用户体验更流畅。

DeepSeek 表示，FlashMLA 的普及有望推动 AI 推理进入“千元级硬件跑百亿模型”时代，降低企业部署成本。例如，企业可通过更少的 GPU 服务器完成同等任务量，直接节省硬件投入。

**打破算力垄断，推动技术普惠**

此前，高效解码内核多由科技巨头闭源垄断，而 FlashMLA 的开源使中小企业和开发者能免费获取“工业级优化方案”。这不仅降低了技术门槛，还为垂直领域的小模型创新提供了可能。

DeepSeek 强调，此次开源是构建“模型-开发者-软硬件”一体化生态的关键一步，后续还将陆续公开四个代码库。业界猜测，未来或涉及通用人工智能（AGI）相关技术，进一步推动技术标准化与商业化。

英伟达 CEO 黄仁勋近期评价称，DeepSeek 的技术进步“令人惊叹”，并认为其开源策略将加速 AI 应用普及，而非削弱对计算资源的需求。此前，DeepSeek 的 R1 开源模型曾引发英伟达股价剧烈波动，但市场逐渐回归理性，认可双方在软硬件协同优化上的互补性。

DeepSeek 通过 FlashMLA 的开源，展示了其在 AI 底层技术上的深厚积累。随着开源周的推进，更多技术细节的公开或将重塑行业格局，为全球开发者提供新的创新动力。

**快速开始**

![Image 4: Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kfiaiar8iaaIIXnMyfCxzBygw3D2sPDZ4VTbP7z2KWxibnDPR1WFjMwz7dk5WpuyLIYsYhKmTknGHicCejW5NUQAIBQ/640?wx_fmt=jpeg&from=appmsg)

相关链接：

FlashMLA GitHub：

https://github.com/deepseek-ai/FlashMLA

参考：

https://mp.weixin.qq.com/s/yX05DBbu\_BwE\_3aJVpSQzg

https://news.sina.cn/ai/2025-02-24/detail-inemqazs1041482.d.html?vt=4

* * *

【投稿】：[**SDNLAB原创文章奖励计划**](https://mp.weixin.qq.com/s?__biz=Mzg5NzY3NDUyMw==&mid=2247535856&idx=1&sn=62cc3fa2d19887c749c278fe55136ad8&scene=21#wechat_redirect)

【有奖】：[**常读文章有奖活动进行中**](https://mp.weixin.qq.com/s?__biz=Mzg5NzY3NDUyMw==&mid=2247536415&idx=1&sn=fcf766a4e7cd6f7f7a8ffeed1acd250e&scene=21#wechat_redirect)
