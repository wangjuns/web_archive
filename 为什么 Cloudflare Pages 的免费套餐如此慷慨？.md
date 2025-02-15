Title: 为什么 Cloudflare Pages 的免费套餐如此慷慨？[译]

URL Source: https://baoyu.io/translations/why-does-cloudflare-pages-have-such-a-generous-free-tier

Markdown Content:
宝玉的分享
博客
翻译
Published on 2025-01-16
Translated on 2025-01-15
为什么 Cloudflare Pages 的免费套餐如此慷慨？[译]
原文：Why does Cloudflare Pages have such a generous Free tier?

这个网站使用 Cloudflare Pages 托管，我对此非常满意。在我研究如何在 2025 年搭建一个像我这样的网站时，我不禁好奇：如今为什么会有这么多免费且好用的托管服务。多年前，你_必须_付费才能拥有托管服务，但现在已经有了很多免费额度相当大的平台，比如 GitHub Pages、GitLab Pages、Netlify 等等。

但在免费方案之中，Cloudflare 一骑绝尘

这些平台会有各种各样的使用限制，但最值得担心的往往是带宽。如果你发现自己的网站突然火了，要么承担账单，要么让网站被“热情访问”拖垮，想想都会让人心跳加速。我收集了一些服务的限制如下：

服务

	

每月免费带宽限制

	

备注




Cloudflare Pages

	

无限

	

只要别托管 Netflix




GitHub Pages

	

软限制 100GB

	

“软限制”= 偶尔上 Reddit 热搜也应该没问题




GitLab Pages

	

X,000 次请求/分钟

	

具体细节较多，有点让人摸不着头脑




Netlify

	

100GB

	

超出需付费




AWS S3

	

100GB

	

需要绑定信用卡，以防万一……不过据说 Amazon 对意外超量很宽容

通常这些平台都会声明，你的网站大小应当不超过 ~1GB，文件数量也应低于数万。这个站点现在刚上线，大小大约 15MB，文件数少于 150。我也没打算上传 RAW 格式的照片库，所以如果我真达到了这些限制，请务必关心一下我的身心健康。

那么 Cloudflare Pages 为什么带宽是无限的？

确实为什么？从战略上来说，Cloudflare 为像我这样的小型静态网站提供无限带宽，和它的其他“慈善”服务——比如 1.1.1.1（这个域名笑死）以及免费的 DDoS 防护——是一以贯之的。

Cloudflare 在公司早期就决定要让安全工具尽可能广泛地被使用。这意味着我们会免费或以极低成本提供许多工具，以最大限度降低各类网络攻击的影响和破坏力。

——Matthew Prince，Cloudflare 联合创始人兼 CEO

但我还想谈点更实际的原因。首先，静态网站本身非常轻量，服务起来几乎不费什么劲。例如，你现在阅读的这一页差不多 2.2MB，而如今典型网页大小大约是 2.7MB。依托 Cloudflare 遍布全球的网络、缓存和优化方案，这点流量基本不值一提。我的网站跟 Netflix 完全不是一个量级。

第二，类似 Cloudflare 这样的公司会从一个快速、安全的互联网环境中受益。如果互联网速度快且安全，就会有更多人愿意使用它。使用者越多，就会有更多公司想在互联网上提供服务。更多公司提供服务，就越有可能需要购买相关的安全产品。而巧了，Cloudflare 恰好有一整套安全产品可供出售！这样一来就形成了一个良性循环。

第三，一旦我熟悉了 Cloudflare 一流的用户界面，如果有一天老板问我对它家产品的看法，我肯定会评价不错。我一开始的试用几乎没有任何风险，但如今我对它印象良好，还在这篇文章里免费为它做“口碑”宣传。此外，后台里还随处可见 “Upgrade to Pro” 升级按钮，这正是“免费增值”（Freemium）商业模式的体现。

Cloudflare 官方怎么说？

我已经想到了这些“实际原因”，但我也想看看 Cloudflare 官方是怎么说的。然而，我在 Cloudflare Pages 的文档或其他地方都没有找到专门的解释——无论是在 beta 发布公告还是 GA 正式发布公告里，都完全没有提到 “bandwidth” 这个关键词。

更新： shubhamjain 在 HN 提供了一段 Matt Prince 的精彩阐述；xd1936 也非常给力地找到了 官方评论 ，之前我搜半天都没找到。

我人微言轻，没法搞到官方声明，所以只能依赖我的直觉。所幸我也没有把所有鸡蛋都放在一个篮子里，因为我的网站也部分托管在 GitHub 上。如果哪天 Cloudflare 改变主意，我也还能有别的选择。

See all posts

Built by 宝玉. RSS . 本站原创内容，独家授权赛博禅心公众号发布。

Toggle theme
