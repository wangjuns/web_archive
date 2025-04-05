Title: Log/Trace/Metric 完成 APIServer 可观测覆盖

URL Source: https://mp.weixin.qq.com/s/jm5SSW6MfL8BhGC9Mkof-g

Markdown Content:
Log/Trace/Metric 完成 APIServer 可观测覆盖
Original 刘进步(石季) 阿里云云原生
 2025年02月25日 10:31



随着大模型的爆火，越来越多的企业期望将大模型融入现有业务，打造更具竞争力的产品与服务。API 与大模型的关系密不可分，API 作为桥梁，使得大模型的强大功能可以被广泛、便捷地应用于各种实际场景中。通过 API，开发者能够高效地集成和利用大模型的能力，推动技术创新和应用落地，同时也确保了模型的安全、可控和可维护性。

12 月 11 日，OpenAI 出现了全球范围的故障，影响了 ChatGPT/API/Sora/Playground/Labs 等服务，持续时间超过四个小时。究其背后原因，主要是新部署的服务产生大量的对 K8s APIServer 的请求，导致 APIServer 负载升高，最终导致 DNS 解析不能工作，影响了数据面业务的功能。面对 APIServer 这类公用基础组件，如何通过 Log/Trace/Metric 完成一套立体的覆盖体系，快速预警、定位根因，降低不可用时间变得非常重要。

时间序列（Metric）










Cloud Native

Prometheus 本身自带丰富的指标体系，可以解决大部分组件监控的问题。例如可以借助阿里云 Prometheus 可观测服务，开箱即有丰富的指标信息和默认大盘。


采集链路增强
在获得指标过程中，K8S APIServer 监控采集组件往往和集群同侧部署，当集群出现问题时，监控系统也会一并宕掉，不能起到观测异常现场的作用。阿里云通过建设“带外数据链路”（out-bound）来进一步提升可靠性：当集群本身异常时，只影响和集群内部环境相关的“带内链路”（in-bound），而不会影响这些“带外数据链路”（out-bound）。同时，集群关键组件的事件、能感知集群中的节点底层异常的主动运维事件，也通过“带外数据链路”（out-bound）采集至日志组件中。

访问日志（Log）










Cloud Native

APIServer 访问日志记录了访问请求的来源、状态、延时等数据，每一个请求可能源自不同的客户端（client）、访问不同的资源（resource），及不同请求类型（verb）。
I1219 15:30:45.123456 12345 audit.go:123] "Audit" verb="create" uri="/api/v1/namespaces/default/pods" user="system:serviceaccount:kube-system:default" srcIP="192.168.1.100:56789" userAgent="ilogtail/v0.0.0" response=201

如上访问日志会有众多组合，例如：

客户端（userAgent）：包括 ilogtail/v0.0.0，metrics-server/v0.0.0 和 cert-manager/v1.9.1 在内的超过 50 个左右不同的来源。

K8S 资源（uri）：包括 services，leases 和 ingresses 等等 100 个以上的不同资源。
不同方法（verb）：包含 GET，LIST，WATCH 等。

由于同一个时刻会有大量的操作，以如上的维度组合为例会非常大（50 x 100 x10 = 5W），在其中去找到源头好比大海捞针。有没有一些方法能够帮助快速定位呢？



从访问日志到时序指标
在丰富的指标和每秒几千条访问日志中去定位问题是非常困难的，我们把 userAgent + uri + verb 做一个组合，根据每分钟请求次数（QPS），能够看到 5W 条请求的序列曲线。排查问题就变成了，哪些组合引起了 APIServer 的超额请求？在这里，我们以 SPL 来演示通过日志生成时间序列指标 + AIOps 算法组合，定位根因的组合。
SPL（https://help.aliyun.com/zh/sls/user-guide/spl-overview/ SLS Processing Language），是针对数据查询、流式消费、数据加工、采集、Ingestion 等需要数据处理的场景，提供的统一的数据处理语法。SPL 能力已拓展至时间序列分析、AIOps 等场景上。以下我们通过 SPL 使用，来演示如何分析 APIServer 日志进行异常检测与定位。


日志转时序 + 异常检测

对于多维度指标的异常检测，我们给所有维度组合设置告警是不经济的。可以先聚合指标、从全局监控请求数序列的异常。例如我们忽略所有维度（userAgent=*，uri=*，verb=*），将所有数据聚合形成全局 QPS 指标，如下：

* 
| extend ts= second_to_nano(date_trunc(60, __time__))
| stats request_count=count(1) by ts
| make-series request_count_arr = request_count on ts

从全局 QPS 请求数（下图）能够看到，在 12-17 09:20 ~ 12-17 09:35 之间存在明显的请求数量异常上升：

在该时间序列上，我们可以使用异常检测算子（series_decompose_anomalies）识别序列中的异常：

....
| extend ret = series_decompose_anomalies(ts, request_count_arr)
| extend anomalies_score_series = ret.anomalies_score_series
| project ts, request_count_arr, anomalies_score_series
通过异常检测算法（series_decompose_anomalies），可以看到在 [1734398340, 1734399120] 之间指标的异常分数较高，可能是真正的异常。
异常区间开始时间（s）
	
异常区间结束时间（s）
	
异常分数


1734345480
	
1734345480
	
0.01


1734398220
	
1734398220
	
0.07


1734398340
	
1734399120
	
0.85


1734399840
	
1734399840
	
0.03


1734482880
	
1734482880
	
0.13


1734526740
	
1734526740
	
0.04

对应全局 QPS 曲线图，也能够验证这一点：



时序数据根因分析（定位组合维度）

在获取异常和时间段后，我们继续使用根因下探算子（series_drilldown）分析导致异常的维度组合，在如下的例子中，我们针对（userAgent, verb, resource）这 3 个维度组合进行根因定位。

*
| extend resource = json_extract_scalar(objectRef, '$.resource') 
| extend ts= second_to_nano(date_trunc(60, __time__))
| stats request_count=count(1) by ts, userAgent, verb, resource
| make-series   request_count_arr = request_count
                on ts
                by userAgent, verb, resource
| stats userAgent_arr = array_agg(userAgent), verb_arr = array_agg(verb), resource_arr = array_agg(resource),ts_arr = array_agg(ts), metrics_arr = array_agg(latency_arr)
| extend ret = series_drilldown(userAgent_arr, verb_arr,resource_arr, ts_arr, metrics_arr, 1734398340000000000, 1734399120000000000)
| project ret
从算法返回结果可以看到，导致异常的维度组合可能是 verb=GET and resource=leases，即读取 leases 资源的请求数量异常上升。
{
  # 异常根因对应的维度组合
  "attrs": [{ 
    "verb": "GET",
    "resource": "leases" 
  }],
  # 异常根因的评价指标
  "statistics": {
    "relative_ratio": 0.84611478200,
    "relative_unexpected_difference": 0.73918632088300926,
    "difference": -293.23809523809524,
    "predict": 53.33333333333331,
    "real": 346.57142857142856,
    "support": 117
  }
}

为了验证该维度组合是否为根因，首先我们聚合与该维度组合相匹配的请求数序列，如下:

由于 leases 一般是保存在 etcd 中，主要用于节点的心跳检测和选主。如果 leases 相关的请求数量异常上升，可能需要进一步检测 etcd 性能、网络延时，或者检查节点和 pod 数量是否正常等等。

链路追踪（Trace）










Cloud Native

除 Log/Metric 外，我们还可以借助链路追踪（Trace）对重点操作做进一步诊断。APIServer 内置了基于 OpenTelemetry 的链路追踪能力：它会为传入的 HTTP 请求、webhook 调用、etcd 操作以及重入请求生成链路数据。通过这些追踪数据，开发者和运维人员可以深入理解 Kubernetes 内部的运行机制，快速定位性能瓶颈，有效进行故障排查。
阿里云容器服务为开发者提供了开箱即用 APIServer 链路追踪方案，支持将集群管控面的链路自动上报至可观测链路 OpenTelemetry 版。以下是一些步骤：

1. 在 ACK 组件管理中为 APIServer 中开启链路追踪。

2. 开启链路追踪后，可在调用链分析查看 APIServer 链路数据。

3. 从链路追踪角度，获得 Deployment API 完整处理过程，包含认证、访问 etcd 查询数据、对象序列化返回操作。

欢迎体验

通过上述例子可以看到，我们可以通过 Log/Trace/Metric 对 APIServer 等关键组件提供立体化的可观测覆盖，帮助我们加快故障分析处理的速度，提升系统稳定性。欢迎来可观测案例中心尝试：https://sls.aliyun.com/doc/

Read more
