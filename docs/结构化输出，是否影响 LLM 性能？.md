# 结构化输出，是否影响 LLM 性能？
[结构化输出，是否影响 LLM 性能？](https://mp.weixin.qq.com/s/UyX2xlf0XBKi8zR6Wh5J4g) 

 本文作者：Will Kurt，翻译：宝玉　

https://blog.dottxt.co/say-what-you-mean.html　

**本文反驳**：构化生成，显著影响了 LLM 的性能。

关于结构化输出，我之前还写了一篇：  

《[看完这篇，你也能做 AI 搜索：论「结构化输出」](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247490254&idx=1&sn=f49e6ad20fe3be90f563f565dfab4bac&scene=21#wechat_redirect)》  

最近，Appier 研究团队发表了一篇论文 《让我自由表达？关于格式限制对大语言模型性能影响的研究》（https://arxiv.org/abs/2408.02442），对大语言模型（LLM）在执行结构化生成任务时的评估结果质量提出了严重质疑。论文的最终结论是：　

我们的研究表明，结构化生成限制显著影响了 LLM 在各种任务上的性能。　

论文基于三组评估结果得出这一结论，这些结果表明，与非结构化生成（图表中的“自然语言”/NL）相比，结构化生成（图表中的“JSON 模式”）表现更差。下图（根据原图表重绘并重新调整比例）展示了令人担忧的性能表现：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzuAIyH0jAKCy5v8gf9Aic3brafgQFXXiaPBFLAmAUuqHjw0c9dvK05Gxw/640?wx_fmt=png&from=appmsg)

图 1：《让我自由表达？》的原始发现　

我们 .txt 团队在以往的实验中发现 结构化生成优于非结构化生成。我们的实验聚焦于具有清晰、适合 LLM 处理的结构化问题，而 Tam 等人研究的任务也是如此（实际上，我们早已用不同的模型对 GSM8K 进行了 类似实验：https://blog.dottxt.co/performance-gsm8k.html）。因此，Tam 等人的研究结果既令人惊讶又令人担忧。　

在使用相同模型（Llama-3-8B-instruct）重新测试上述任务后，我们发现我们的结果与论文中的结果不一致，而是反映了我们此前的发现。深入研究论文的数据和源代码后，我们发现存在几个关键问题，导致论文得出了根本错误的结论。　

这篇文章的目的不仅仅是反驳，而是分享我们在日常使用结构化生成中积累的经验。我们将展示 Tam 等人犯下的错误，同时提供结构化生成提示技巧，即使在您 未使用结构化生成 的情况下，也能改善 LLM 的响应效果。　

简单反驳：结构化生成提升了性能
---------------

对于急需答案的读者，**关于结构化生成是否会降低性能的简短回答是：明确不会**。下图显示了我们针对论文中提到的所有问题进行了快速 JSON 生成实现后的结果。　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzvbuCsqmGibt5HwrypU8Kgia9XIgHtumVHZmW2yDVk0Ds3GJW3ia8xK7gQ/640?wx_fmt=png&from=appmsg)

图 2：重新实现相关评估的结果　

虽然我们的非结构化生成结果与论文一致，但我们的结构化生成结果直接驳斥了论文的发现，显示结构化生成在所有方面都有所改善。复现这些结果的代码可在 GitHub 上找到：

https://github.com/dottxt-ai/demos/tree/main/say-what-you-mean  

以下是我们在论文中发现的主要问题：　

1.  论文本身发现结构化生成在一些分类任务上的表现优于非结构化生成。
    
2.  用于非结构化（NL）生成的提示与用于结构化生成的提示明显 不同，因此无法进行公平比较。
    
3.  结构化生成提示未向模型提供足够信息来完成任务，这导致“JSON 模式”示例的性能尤其差。
    
4.  论文的核心实际上是利用另一个 LLM 解析一个 LLM 的结果。作者将其称为“完美文本解析器”，我们称之为“AI 解析器”（原因稍后解释）。
    
5.  论文混淆了结构化生成与 JSON 模式，但独立运行这些评估显示，“JSON 模式”优于非结构化生成。
    

一个合适的比喻是编程语言的基准测试：如果用糟糕的 Rust 代码和精心优化的 Python 代码进行比较，很容易得出 Rust 性能不如 Python 的结论。然而，任何有理智的读者都会意识到，这些结果更多反映了作者的技能水平，而不是工具的能力。优化性能的代码本身是一项挑战，就像确保评估真实反映任务一样。　

尽管如此，这篇论文为我们深入研究结构化生成的意义和如何提升其性能提供了绝佳机会。　

任务概述 - 最后一个字母
-------------

我们将聚焦于《让我自由表达？》声称结构化生成表现最差的任务之一：最后一个字母（https://paperswithcode.com/dataset/lastletterconcat）。　

在此任务中，模型需要处理如下输入：一个包含 4 个名字的列表，例如：　

```
Ian Peter Bernard Stephen
```

然后模型必须将每个名字的 最后一个字母 串联起来。例如，答案为：NRDN。　

测试集包含 150 个问题，训练集包含 350 个问题。论文仅使用了测试集中的 150 个问题，我们也将遵循这一做法（尽管所有发现也适用于完整数据集）。　

为什么需要结构化生成？解析结果！
----------------

论文方法中一个有趣的部分（实际上应该是其重点）是用所谓的“完美文本解析器”从初始模型响应中提取答案。通常，大多数评估框架会使用简单、明确的正则表达式解析响应，但 Tam 等人使用了 claude-3-haiku-20240307 来解析生成的输出。换言之，每个答案实际上使用了两个模型。在论文中，他们称之为“完美文本解析器”，我们将其称为“AI 解析器”。　

必须注意这一非常规的方法，因为使用结构化生成的主要原因之一是 保证响应格式便于解析。解析和结构化生成密切相关。尽管论文存在许多问题，但 AI 解析器的使用是一个值得探讨的有趣点。我们将深入研究 AI 解析与结构化生成的对比，以更深入地了解结构化生成的强大功能。　

### 问题 1：AI 解析器的影响

为了更好地理解 AI 解析器的影响，我们深入研究了论文记录的一个示例。幸运的是，Tam 等人提供了详尽的数据集（12GB！https://drive.google.com/file/d/1HIh6BydZjxBkqm1oAxR5zSHzMG3M1nPC/view?usp=sharing）。这些实验数据按模型和提示模板分类。我们将重点分析 lastletter-t3-f3 提示模板，并专注于 meta-llama/Meta-Llama-3-8B-Instruct 的单样本示例。　

让我们先看一下提示如何指导模型完成自然语言（NL）格式下的任务：　

按照指示完成任务： 字符串操作任务： • 已知：一串单词 • 要求：生成一个新字符串，由每个单词的最后一个字母组成 • 过程：逐步思考，解决此问题 注意：开始前请确保已经仔细阅读问题。　

指示：请按以下文本格式提供输出： 答案：<逐步思考>。The final answer is <答案>　

可以注意到，提示中明确描述了响应格式：The final answer is <答案>。这意味着，如果模型遵循提示，我们应该能够使用如下简单的正则表达式解析所有答案：　

```
answer_regex = r'answer is ([A-Za-z]{4})'
```

通过遍历实验数据的记录结果，我们很快发现严格正则解析与 AI 解析结果之间存在差异：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzVVsRNsbrHj73cEHypc0ywX9Fzp3AvzgY6s1VcwKuiccheIsKLIXZQibg/640?wx_fmt=png&from=appmsg)

图 3：严格正则解析与 AI 解析的对比　

事实证明，AI 解析器在自然语言格式的解析中承担了大量工作。检查实验结果后，我们发现严格的正则表达式未能捕捉到的部分模型响应示例如下：　

*   The answer is e-S-S-E. → ESSE
    
*   The answer is AAA R. → AAAR
    
*   The answer is "reye". → REYE
    
*   The final answer is: YOOI → YOOI
    

扩展正则表达式可以解决这些问题。以下是经过调整的正则表达式组合：　

```
alt_regex_1 = r'answer is ([A-Za-z]-[A-Za-z]-[A-Za-z]-[A-Za-z])'alt_regex_2 = r'answer is:? "?([A-Za-z] ?[A-Za-z] ?[A-Za-z] ?[A-Za-z])"?'alt_regex_3 = r'Concatenating them is "([A-Za-z]{4})"'alt_regex_4 = r"answer is:? ([A-Za-z]'?[A-Za-z]'?[A-Za-z]'?[A-Za-z])"
```

结果表明，这些正则表达式组合可以覆盖我们错过的所有情况，无需额外调用更强大的模型。使用这些灵活的正则表达式组合解析后，我们得到以下结果：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzhAZSImTVTgmUkP84owWql2z7bAfXPLklZhVLPL7cqftMMRW5GZX2hA/640?wx_fmt=png&from=appmsg)

图 4：严格正则解析、AI 解析和灵活正则解析的比较　

令人惊讶的是，我们手工设计的正则表达式列表（花费时间并不多）在此数据集上的表现优于 AI 解析器！需要强调的是，使用结构化生成的主要目的之一就是避免解析输出时的复杂性。然而，这一探索表明，AI 解析器并非“完美”的文本解析器：灵活的正则解析在性能上超过了调用 Claude 模型（同时更快、更便宜！）。　

### 重现这些结果——非结构化

接下来，我们将使用 outlines.generate.text 方法重新运行相同提示，观察结果如何。我们对单样本提示进行了一点修改：Tam 等人的示例中仅使用了两个名字，但所有问题实际上包含四个名字。根据我们的经验，即使在未使用结构化生成的情况下，示例格式与实际问题保持一致也非常重要。因此，我们将提示示例修改为包含四个名字。　

运行 outlines.generate.text 后，我们得到以下结果，与论文中记录的结果进行比较：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJz2to4uOBClhnujItud1y8VfkRtWiaCKQQvb9DYoYJicWbQhibazAYfut3A/640?wx_fmt=png&from=appmsg)

图 5：复现原始自然语言（NL）结果　

可以看出，尽管结果稍有提升，但整体上与记录的结果一致。我们并非追求完全一致的复现，而是验证我们的结果是否与原始结果在同一水平上。　

在改进单样本提示后，不同解析方法之间的差距也缩小了。根据我们以往的研究（https://blog.dottxt.co/prompt-efficiency.html），模型似乎主要从示例中学习问题的结构。因此，提供更好的结构示例有助于提高对结构的遵从性。　

现在，我们可以真正测试结构化生成对性能的影响。　

### 任何可以解析的内容都可以生成

讨论 AI 解析器的原因在于，理解如何解析 LLM 的响应是深入理解结构化生成的关键。一个常见误解是（论文中也存在）将结构化生成简单等同于 JSON 模式（或 YAML 模式、XML 模式等）。更好的理解方式是：将我们的响应解析器作为生成器运行。　

为说明这一点，我们在运行结构化生成时，将对提示的推理步骤增加结构，然后将我们定义的答案正则表达式附加到提示中。这种方法统一了提示、解析器和生成器。这正是结构化生成之所以强大的秘诀所在。　

以下是我们定义的结构和结果分析：　

*   定义回答的推理结构的正则表达式：
    

```
cot_regex = r'Answer: T[\w \\",\\.]{30,250}. The '
```

*   此正则表达式允许模型在 30 到 250 个字符内进行推理，然后给出答案。
    
*   将此结构与之前的答案正则表达式组合：
    

```
struct_strict = outlines.generate.regex(    model,    cot_regex + answer_regex,    sampler=greedy())
```

完成后，我们通过运行上述生成器来测试结构化生成结果，结果如下：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzdgFGVRwicWujrMlVhtIuTudrqiaIgUjWeGic7Wic8KpLBhwYUYicZDWiaWiaA/640?wx_fmt=png&from=appmsg)

图 6：使用结构化生成复现自然语言（NL）结果　

与我们过往的发现一致，结构化生成的表现 **优于** 非结构化生成。　

### JSON 的问题在哪里？

通过对如何正确实施结构化生成的深入了解，我们可以进一步分析论文中 JSON 结果的问题。下图是论文中关于 JSON 模式表现的图表：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJz89ibicD5SosPLMmyjibd73jZ4d3ibmD3bW8gFlDFXuV6A5BelYvvRQ9ezw/640?wx_fmt=png&from=appmsg)

图 7：原始图表显示 JSON 模式在“最后一个字母”任务中的糟糕表现　

在上图中，结构化生成（JSON 模式）的准确率低于 10%，而非结构化生成（自然语言）的准确率接近 70%。尽管我们已成功复现非结构化结果，但 JSON 模式的表现显然不合理。问题可能出在模型被要求以 JSON 格式响应时的提示设计上。　

### 问题 2：提示设计中的问题

正如我们所提到的，论文的主要问题之一是用于结构化生成和非结构化生成的提示设计不同。在我们的分析中，只有使用相同的提示模板才能进行公正的比较。　

因此，我们首先查看了论文中用于 JSON 模式评估的提示。根据记录的数据（文件 lastletter-t2-structure/struct\_llama-3-8b-instruct\_shots\_0.jsonl），以下是 JSON 模式评估中使用的提示：　

```
按照指示完成任务：\仔细阅读每个问题，并逐步思考后作答。给定一串单词，取出每个单词的最后一个字母并将它们串联起来。指示：您必须使用工具。问题：取出 “Britt Tamara Elvis Nayeli” 的每个单词的最后一个字母并将它们串联起来。
```

显然，这个提示需要显著改进才能正确评估此任务！在编写提示时，建议反问自己：“这个提示是否包含足够信息，让一个经验丰富的人类能够正确回答问题？” 从提示中我们无法明确以下几点：　

1.  回答必须是 JSON 格式（提示中完全没有提到 JSON）。
    
2.  即使假设回答需要 JSON 格式，也没有提供具体的 JSON 格式或结构。
    

虽然提示提到需要使用“工具”，但并未说明需要使用什么工具，或者工具的输出应该是什么样的格式。结构化生成并不能“魔术般”地让模型理解您的意图，就如同在自家庭院中铺设铁路并不会让火车停靠一样。　

### JSON 的正确提示设计

我们之前讨论过，结构化生成并不等同于 JSON 模式，但在某些情况下，我们确实需要 JSON 格式的输出。为了理解《让我自由表达？》论文中的错误，我们可以通过以下方式正确实施结构化生成。首先，使用如下的指令式提示：　

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>你是一位擅长通过推理步骤解决简单单词谜题的专家。你的具体任务是接受一个包含 4 个名字的列表，分析每个名字的最后一个字母，然后将这些字母拼接成一个单词。用户的问题将以纯文本形式呈现，您的回答需要以以下 JSON 格式呈现：{"reasoning": <对答案的推理>, "answer": <最终答案>}<|eot_id|><|start_header_id|>user<|end_header_id|>问题：取出 'Ian Peter Bernard Stephen' 的每个名字的最后一个字母并将它们拼接起来。<|eot_id|><|start_header_id|>assistant<|end_header_id|>{"reasoning": "'Ian' 的最后一个字母是 'N'，'Peter' 的最后一个字母是 'R'，'Bernard' 的最后一个字母是 'D'，'Stephen' 的最后一个字母是 'N'。因此，答案是 'NRDN'。", "answer": "NRDN"}<|eot_id|><|start_header_id|>user<|end_header_id|>问题：取出 'Britt Tamara Elvis Nayeli' 的每个名字的最后一个字母并将它们拼接起来。<|eot_id|><|start_header_id|>assistant<|end_header_id|><|eot_id|>
```

这种提示的特点如下：　

1.  明确的格式：清楚说明了回答需要采用 JSON 格式。
    
2.  具体的示例：示例既匹配问题格式，也明确了答案的结构。
    
3.  逻辑清晰：通过示例演示推理步骤，模型更易遵循。
    

### 定义我们的结构

接下来，我们需要定义结构（实际上，这应与提示同步进行）。针对该任务，我们将使用一个简单的 Pydantic 模型：　

```
class Response(BaseModel):    reasoning: constr(max_length=250)    answer: str = Field(pattern=r'[A-Z]{4}')
```

*   这里将推理步骤限制为 250 个字符，确保模型不会花费过长时间进行推理。
    
*   将答案限制为仅包含 4 个大写字母的有效响应。
    

#### 验证提示是否包含我们的结构

验证提示是否与我们定义的结构相符，是确保模型输出正确格式的关键步骤。以下代码用于验证：　

```
from outlines.fsm.json_schema import build_regex_from_schemaschema_regex = build_regex_from_schema(Response.schema_json())example_prompt = create_prompt(all_evals[5]['question'], tokenizer)re.search(schema_regex, example_prompt)
```

验证完成后，我们就可以进行下一步了！值得注意的是，这些准备工作同样可以显著改善非结构化生成的效果。　

### 重新运行 JSON 评估

在上述改进提示的基础上，我们重新运行了 JSON 模式的生成任务。以下是最终结果的比较：　

![](https://mmbiz.qpic.cn/mmbiz_png/2icSMc1VBIYr71pE6OFE9AOC8ykgnzwJzsK9xdFgkwJOxu80ds1CZXgpWh263kAJfXZokNaDqJUo3GfeB4sIeCA/640?wx_fmt=png&from=appmsg)

图 8：使用改进的提示对比结构化和非结构化 JSON 生成结果（与自然语言生成结果比较）　

正如所见，结构化生成再次优于非结构化生成。此外，结构化 JSON 的准确率最高，为 77%。这清楚地表明，正确的提示设计对结果的准确性有显著影响。　

### 结论

我们 .txt 团队对结构化生成充满热情，并深信其能彻底改变使用 LLM 的方式。正因如此，我们对结构化生成有负面影响的任何说法都非常关注，并愿意通过研究和实践帮助澄清误解。　

但令人遗憾的是，当某些研究人员未能充分理解问题而发表误导性结论时，社区就需要花费额外的时间和精力来纠正错误。如果您有关于结构化生成的任何疑问或问题，请随时联系我们，我们乐于分享经验。　

正如《火线》中的 Omar Little 所说：　

"向国王出手时，必须全力以赴，否则后果自负。"