# 我们的 IP 是怎么来的——从本地路由 DHCP 到 IANA 的 “公网” IP 分配 | Nova Kwok's Awesome Blog
`curl ip.sb` 一下，你就可以看到自己的 IP，但是这个 IP 是怎么来的，这个问题在多年前困扰了我好久，最近由于自己有 ASN 和一小段 IP，所以便有了整理本文的想法，一来可以分享一些可能大家少关注的信息，另一个方面也是增强一下自己对于知识的理解，因为：

> 在【理想情况】下，如果你已经对某个领域某个分支达到【完全掌握】的程度，那么你就可以比较轻松地写出该领域某个分支的【通俗性读物】，并且确实能让【外行人】看懂，反之，如果你的掌握程度还不够。
> 
> ——如何【系统性学习】——从“媒介形态”聊到“DIKW 模型”

IP 地址分类
-------

首先我们介绍一个简单的概念，IP 地址有哪些分类，这个我们在各类计算机网络的书上都见过，由于我本人一直没能背下来，所以这里再贴一下相关的表格：

| Prefix | Designation and Explanation | IPv4 Equivalent |
| --- | --- | --- |
| ::1/128 | Loopback  
This address is used when a host talks to itself over IPv6. This often happens when one program sends data to another. | 127.0.0.1 |
| fc00::/7  
Example: fdf8:f53b:82e4::53 | Unique Local Addresses (ULAs)  
These addresses are reserved for local use in home and enterprise environments and are not public address space.These addresses might not be unique, and there is no formal address registration. Packets with these addresses in the source or destination fields are not intended to be routed on the public Internet but are intended to be routed within the enterprise or organisation.See RFC 4193 for more details. | Private, or RFC 1918 address space:  
10.0.0.0/8  
172.16.0.0/12  
192.168.0.0/16 |
| fe80::/10  
Example: fe80::200:5aee:feaa:20a2 | Link-Local Addresses  
These addresses are used on a single link or a non-routed common access network, such as an Ethernet LAN. They do not need to be unique outside of that link.Link-local addresses may appear as the source or destination of an IPv6 packet. Routers must not forward IPv6 packets if the source or destination contains a link-local address.Link-local addresses may appear as the source or destination of an IPv6 packet. Routers must not forward IPv6 packets if the source or destination contains a link-local address. | 169.254.0.0/16（可以参考 [关于 169.254.0.0/16 地址的一点笔记](https://nova.moe/note-on-169-254-ip-addresses/) ） |
| 2000::/3 | Global Unicast  
Other than the exceptions documented in this table, the operators of networks using these addresses can be found using the Whois servers of the RIRs listed in the registry at:http://www.iana.org/assignments/ipv6-unicast-address-assignments | No equivalent single block |
| ff00::/8  
Example: ff01:0:0:0:0:0:0:2 | Multicast  
These addresses are used to identify multicast groups. They should only be used as destination addresses, never as source addresses | 224.0.0.0/4 |

IP 是如何分配的
---------

我们要探寻的第一个问题在于，IP 是怎么来的，这个时候如果你使用的是 Windows，那么你的第一反应应该是 `ipconfig` ，作为 BSD 用户，可能第一反应是 `ip addr`，这个时候如果你在家中的话，可能就会看到非常常见的 `172.16.xxx.xxx`，好了，这个时候参考上表，我们可以知道这个 IP 是一个：Unique Local Addresses，或者也就是我们所谓的保留地址，或者私有地址，这个 IP 地址是如何来的？

DHCP！（大声）

没错，DHCP 全称 Dynamic Host Configuration Protocol，简单来说，你连接上家里路由器，然后 DHCP 就会开始工作，如果要说的详细一点的话，DHCP 是走的 UDP，且分为一下四个步骤：

*   Server discovery（这网络中有 DHCP 服务器嘛？此时会有一个 DHCPDISCOVER 包）
*   IP lease offer（有！太有了，我就是，我收到了你的 DHCPDISCOVER，这里是 DHCPOFFER 包，包含了给你分的 IP 地址，子网掩码，还有我们的 DNS 服务器信息）
*   IP lease request（客户端收到并接受一个 DHCPOFFER 之后进行确认，好，我就要这个 IP 了，此时发送一个 DHCPREQUEST 包）
*   IP lease acknowledgement（服务器接受到 DHCPREQUEST 包之后会返回一个 DHCPACK 包，了解自己已经成功分配地址给客户端）

这个时候我们已经获得了一个所谓的内网 IP 了，且由于 NAT 的存在，我们可以一个家庭共享一个「公网 IP」（如果你家有的话，如果没有的话，可以打电话给 ISP 要求开通，是免费的）来上网了，那我们这个「公网 IP」又是如何得到的呢？

还是 DHCP，不过底层一般还有一个 PPPoE 的封装，也就是所谓的宽带拨号，如果你不熟悉原理的话，可以参考[Point-to-Point Protocol over Ethernet](https://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_Ethernet)。

在一个简单的模型下，你的「内网 IP」为 `172.16.0.1/24`，你的「公网 IP 」为 `123.19.98.2/32`，那么你的运营商一定是因为拥有包含了你的「公网 IP」的段才可以这么分配，那么运营商是如何获得这个段的呢？

IP 是如何来的
--------

我们知道在一个隔离的局域网下，在可以用的私有地址中我们可以随意指定设备的 IP，比如路由器（或者叫网关）指定一个 `172.16.0.1`，然后每个客户端上分配 `172.16.0.1/24` 段中的地址，但是在一个公网环境下，事情就没有那么简单了。

### IP 是谁在管理

是 IANA，Wiki 描述如下：

> The Internet Assigned Numbers Authority is a function of ICANN, a nonprofit private American corporation that oversees global IP address allocation, autonomous system number allocation, root zone management in the Domain Name System, media types, and other Internet Protocol-related symbols and Internet numbers.

一般来说，你的 IP 可能会属于一个 ASN，也就是 Autonomous System Number，以 Cloudflare 之前得手的 `1.1.1.1` 为例，从 `https://bgp.he.net/ip/1.1.1.1` 上可以看到，这个 IP 属于 AS13335 Cloudflare，他甚至拥有 `1.1.1.0/24` 整个段，所以 Cloudflare 可以自由地使用自己的 IP 地址。

接下来一个问题就显而易见了，我们如何拥有一个自己的 IP 地址，或者说，怎么证明自己拥有了 IP 地址呢？

### 如何证明自己对于 IP 地址的所有权

假设你有了，对，就是你有了，别说怎么来的，那么如何证明你有了？

首先我们知道一个 IP 是包含在一个 ASN 中的，所以给定一个 IP 或 ASN，一定可以查询到关于 ASN 的所有信息，例如上文中的 AS13335 的 WHOIS 信息如下（可以在 `https://apps.db.ripe.net/db-web-ui/lookup?source=ripe-nonauth&key=AS13335&type=aut-num` 看到）：

```
    aut-num:         AS13335
    as-name:         CLOUDFLARENET-AS
    descr:           Cloudflare, Inc.
    descr:           101 Townsend Street, San Francisco, CA 94107, US
    status:          OTHER
    mnt-by:          MNT-CLOUDFLARE
    org:             ORG-CI40-RIPE
    notify:          rir@cloudflare.com
    admin-c:         CAC80-RIPE
    tech-c:          CTC6-RIPE
    remarks:         See ARIN database for complete information
    created:         2015-10-08T16:51:14Z
    last-modified:   2019-03-19T21:30:09Z
    source:          RIPE-NONAUTH

```

其中 mnt-by 表示这个 ASN 的 Maintainer，也就是 `MNT-CLOUDFLARE`，相关 WHOIS 如下：

```
    mntner:          MNT-CLOUDFLARE
    descr:           Cloudflare, Inc.
    descr:           101 Townsend Street, San Francisco, CA 94107, US
    admin-c:         ML18637-RIPE
    admin-c:         SR11544-RIPE
    admin-c:         TP5485-RIPE
    upd-to:          ripe@cloudflare.com
    auth:            MD5-PW# Filtered
    auth:            SSO# Filtered
    auth:            SSO# Filtered
    auth:            SSO# Filtered
    mnt-by:          MNT-CLOUDFLARE
    notify:          ripe@cloudflare.com
    mnt-nfy:         ripe@cloudflare.com
    created:         2012-08-10T03:29:42Z
    last-modified:   2019-03-14T22:25:52Z
    source:          RIPE# Filtered

```

这样你就可以知道这个段的 IP 属于谁了，所以我们理一下关系：一个 IP 一定属于某一个段（比如 `1.1.1.1` 属于 `1.1.1.0/24` 段），这个 IP 段一定属于某一个 AS ，IP 段的所有者信息其实是 AS 的所有者信息，那么，如果你想有一个属于自己的 IP 的话，其实就很明确了，需要有一个 AS。

### 如何获得一个 ASN/IP 段

对于想获得自己 IP 段或者 ASN 的同学，有以下两个方式：

*   自己成为 LIR，这样可以获得很多个 ASN，但是这样的价格非常高
*   找一个 LIR 来赞助你申请一个 ASN，普遍费用比较低

当自己有了 ASN 之后我们就可以购买一个 IP 段了，如上文所说，IP 和 ASN 存在对应关系，所以当你购买了 IP 之后就会出现在你的 ASN 下，然后，由于在 mnt-by 上标记了你的邮件地址，这个时候你通过这个邮件地址发出的邮件就具有证明效益了，为什么如此，见下文。

### 如何使用 IP 地址

现在我们有了 ASN 和 IP 地址，我们要如何使用到自己的 IP 地址呢？我们需要对自己的 IP 进行 IP 宣告（IP Announcement）：

> IP Announcement (IPAN) enables you (if you have your own AS (Autonomous System) and IP Ranges) to have your IP addresses announced by Leaseweb. This allows you to use a larger amount of IPs on a rack or server (than the standard allocation of Leaseweb) and keep the IPs when moving to another provider.

如果使用了一些机房的网络，或者需要使用 HE 的 Tunnel Broker，我们需要先发送一个被称为 LOA 的文件，比如 Leaseweb 就有如下要求：

> If the organization and/or individual does not own the IP prefix that needs to be advertised, we will require a Letter Of Authorization (LOA) from actual owner of the IP prefix.

LOA 的内容可以类似如下：

```
AUTHORIZATION LETTER

2020/02/18

To whom it may concern,

This letter serves as authorization for Hurricane Electric, AS6939 to announce the following netblocks:

2xxx:xxxx:xxxx::/48

As a representative of the company XXXX that is the owner of the subnet and/or ASN, I hereby declare that I'm authorized to represent and sign for this LOA.

Should you have questions about this request, email me at XXXX@XXXX.XXX.

From,

XXXX

```

当然，形式不拘一格，差不多是那么回事就可以，然后注意，需要用上面 MNT 的邮件地址发送以证明所有权。

### 如何宣告 IP

这里推荐几个不错的实践教程：

*   [IP 广播: 使用bird广播(组播)ipv6](https://blog.ni-co.moe/public/560.html)
*   偷 IP 实况：[IP 广播：使用 bird 广播 ipv4](https://blog.ni-co.moe/public/561.html)

出于篇幅考虑，本文就不再继续讨论 IP 宣告的背后原理了，有兴趣的读者可以先自行探索一下，现在你已经有了自己的 IP 和 ASN 了，为什么不去玩玩看 Anycast 呢？比如可以[搭建 Cloudflare 背后的 IPv6 AnyCast 网络](https://nova.moe/simulate-argo-using-anycast-network-behind-cloudflare/)。

Reference
---------

1.  [IPv6 Address Types](https://www.ripe.net/participate/member-support/lir-basics/ipv6_reference_card.pdf)
2.  [Dynamic Host Configuration Protocol](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
3.  [Point-to-Point Protocol over Ethernet](https://en.wikipedia.org/wiki/Point-to-Point_Protocol_over_Ethernet)
4.  [How are IP addresses actually assigned?](https://serverfault.com/questions/275675/how-are-ip-addresses-actually-assigned)