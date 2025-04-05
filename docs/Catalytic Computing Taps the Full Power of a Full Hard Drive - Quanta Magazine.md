Title: Catalytic Computing Taps the Full Power of a Full Hard Drive

URL Source: https://www.quantamagazine.org/catalytic-computing-taps-the-full-power-of-a-full-hard-drive-20250218/

Published Time: 2025-02-18T15:15:12+00:00

Markdown Content:
Ten years ago, researchers proved that adding full memory can theoretically aid computation. They’re just now beginning to understand the implications.

![Image 1: A disk with a section highlighted](https://www.quantamagazine.org/wp-content/uploads/2025/02/Catalytic-Computing_crMark-Belan-Lede.jpg)

Mark Belan/ Quanta Magazine

Introduction
------------

“Obviously” is a dangerous word, even in scenarios that seem simple. Suppose, for instance, you need to do an important computation. You get to choose between two computers that are almost identical, except that one has an extra hard drive full of precious family photos. It’s natural to assume that the two options are equally good — that an extra drive with no space remaining won’t aid your computation.

“Obviously, it doesn’t help, right?” said [Bruno Loff](https://brunoloff.wordpress.com/), a computer scientist at the University of Lisbon.

Wrong. In 2014, Loff and four other researchers discovered that adding full storage space can in principle make computers more powerful. Their theoretical framework, called [catalytic computing](https://dl.acm.org/doi/10.1145/2591796.2591874), has become an object of study in its own right. And recently, it also helped researchers prove a [startling result](https://eccc.weizmann.ac.il/report/2023/174/) in a related area of computer science: The standard approach to resolving a major open question about the role of memory in computation is most likely a dead end.

“It’s quite a feat,” said [Pierre McKenzie](https://diro.umontreal.ca/repertoire-departement/professeurs/professeur/in/in14154/sg/Pierre%20McKenzie/), a complexity theorist at the University of Montreal. “I really appreciate these results.”

**Almost No Memory**
--------------------

Catalytic computing grew out of work in computational complexity theory, the branch of computer science focused on the resources needed to solve different problems. All the problems that complexity theorists consider can be solved with step-by-step procedures called algorithms. But all algorithms are not created equal — some run faster than others or demand less space in a computer’s memory. Complexity theorists sort problems into [different classes](https://www.quantamagazine.org/a-short-guide-to-hard-problems-20180716/) based on the behavior of the best algorithms known to solve them.

The most famous class, dubbed “P,” contains all problems known to have fast algorithms, such as finding the smallest number in a list or finding the shortest path between two points in a network. Another class, called “L,” sets a higher bar for membership: Problems in L must have algorithms that not only are fast, but also use barely any memory. The “smallest number in a list” problem is one example. By definition, every problem in L is also in P, but researchers have long wondered if the reverse is also true.

“The basic question is: Can I take any problem in P and solve it using very, very little memory?” McKenzie said.

Most researchers suspect the answer is no. To prove it, they’ll need to choose a specific problem in P and show that it’s impossible to solve with any clever memory-saving trick.

![Image 2: Stephen Cook in a blue shirt and black sweater types at a keyboard in front of bookshelves](https://www.quantamagazine.org/wp-content/uploads/2025/02/StephenCook_cr-BBVA-FOundation-1.jpg)

Stephen Cook devised a computational task, called the tree evaluation problem, that seemed impossible for any algorithm with limited memory.

BBVA Foundation

In the late 2000s, McKenzie and the pioneering complexity theorist [Stephen Cook](https://www.cs.toronto.edu/~sacook/) devised a problem that seemed like a promising candidate. Called the tree evaluation problem, it involves repeatedly solving a simpler math problem that turns a pair of input numbers into a single output. Copies of this math problem are arranged in layers like the matches in a tournament bracket: The outputs of each layer become the inputs to the next layer until there’s just one output remaining. Different tree evaluation algorithms represent different strategies for calculating this final output from the initial inputs — they might perform the calculations in a different order, or record the results of intermediate steps in a different way.

Many algorithms can solve the tree evaluation problem quickly, putting it in the class P. But every such algorithm must devote some memory to the numbers it’s working with, while also storing numbers it’s already calculated for use in later steps. That’s why Cook and McKenzie suspected that the problem was impossible to solve using limited memory. They formalized this intuition in a [2010 paper](http://arxiv.org/abs/1005.2642) co-authored with three other researchers, and proved that every ordinary algorithm for solving the tree evaluation problem required too much memory to qualify for membership in L.

But their work didn’t rule out the possibility of bizarre algorithms that could somehow use the same piece of memory for storage and calculations simultaneously — the computing equivalent of using a page filled with important notes as scratch paper. Cook and McKenzie thought such outlandish algorithms couldn’t exist, and they were confident enough to put money on it: Anyone who could prove them wrong would win a cool $100.

**Catalytic Conversion**
------------------------

[Michal Koucký](https://iuuk.mff.cuni.cz/~koucky/), a complexity theorist at Charles University in Prague, learned about the tree evaluation result from Cook during a 2011 sabbatical in Toronto. He grew determined to finish what Cook and McKenzie had started, by proving that there’s no way to do additional computations using memory that’s saving data for later. Koucký’s quest would lead him on an unexpected detour to the discovery of catalytic computing. Nearly a decade later, that discovery would inspire two young researchers to return to tree evaluation and settle Cook and McKenzie’s bet once and for all.

But back to the story of catalytic computing. It all started when Koucký visited colleagues in Amsterdam and posed the question that had been preoccupying him in simpler terms: What can you do with memory that’s already full?

“Nothing” was the obvious answer. “I thought, ‘OK, this is of course very useless, and we’re going to prove it,’” said [Harry Buhrman](https://www.cwi.nl/en/people/harry-buhrman/), the leader of the Amsterdam group. “And then we couldn’t prove it.”

![Image 3: Michal Koucký in a blue sweater in front of a chalkboard. Harry Bhurman in a black shirt and coat in front of a glass wall](https://www.quantamagazine.org/wp-content/uploads/2025/02/Burhman-Koucky-Diptych-1-scaled.jpg)

Using an approach called catalytic computing, Harry Buhrman and Michal Koucký showed that even full memory could theoretically aid computation.

From left: Bob Bronshoff, Tomas Rubin

The breakthrough came months later, when Buhrman was visiting his frequent collaborator [Richard Cleve](https://uwaterloo.ca/institute-for-quantum-computing/profiles/richard-cleve) at the University of Waterloo. They decided to focus on an extreme scenario, one where the full memory is very large. If a computer with little free memory can access this massive full memory, would that enable it to solve problems that would be impossible with the free memory alone? It’s like the “hard drive full of family photos” question, but with a hard drive the size of a data center.

If that extra data is untouchable — you can’t interact with it at all — then it definitely doesn’t help. But what if you’re allowed to tweak some of the bits encoding this data, as long as you promise to reset them when you’re done? You can’t simply keep a record of your changes, since that would take up even more space, so instead you’ll have to ensure that your changes are easily reversible. What’s more, you don’t get to choose the content of the extra data, so whatever you do must work for any possible initial configuration of bits.

Those are pretty stringent constraints, so it wasn’t obvious that the extra memory could ever prove useful. But to their surprise, Buhrman and Cleve showed that, if you tweak bits in just the right way, you really can get extra computational oomph out of a full memory.

“That was a shocker for everyone,” said Loff, who was a graduate student in Buhrman’s group at the time, working on the memory question with his fellow student [Florian Speelman](https://www.cwi.nl/en/people/florian-speelman/). The team soon extended the result to an even larger class of problems, and published [their combined results](https://dl.acm.org/doi/10.1145/2591796.2591874) in 2014.

They named the new framework catalytic computing, borrowing a term from chemistry. “Without the catalyst, the reaction would not have proceeded,” said [Raghunath Tewari](https://www.cse.iitk.ac.in/users/rtewari/), a complexity theorist at the Indian Institute of Technology, Kanpur. “But the catalyst itself remains unchanged.”

**Not Far From the Tree**
-------------------------

A small band of researchers continued to develop catalytic computing further, but no one even tried to apply it to the tree evaluation problem that had initially inspired Koucký’s quest. For that problem, the remaining open question was whether a small amount of memory could be used for storage and computation simultaneously. But the techniques of catalytic computing relied on the extra, full memory being very large. Shrink that memory, and the techniques no longer work.

Still, one young researcher couldn’t help wondering whether there was a way to adapt those techniques to reuse memory in a tree evaluation algorithm. His name was [James Cook](https://www.falsifian.org/), and for him the tree evaluation problem was personal: Stephen Cook, the legendary complexity theorist who invented it, is his father. James had even worked on it in graduate school, though he mostly focused on [completely unrelated subjects](https://digicoll.lib.berkeley.edu/record/138671). By the time he encountered the original catalytic computing paper in 2014, James was about to graduate and leave academia for software engineering. But even as he settled into his new job, he kept thinking about catalytic computing.

“I had to understand it and see what could be done,” he said.

For years, James Cook tinkered with a catalytic approach to the tree evaluation problem in his spare time. He gave a talk about his progress at a 2019 symposium in honor of his father’s [groundbreaking work](https://www.quantamagazine.org/complexity-theorys-50-year-journey-to-the-limits-of-knowledge-20230817/) in complexity theory. After the talk, he was approached by a graduate student named [Ian Mertz](https://iuuk.mff.cuni.cz/~iwmertz/), who’d fallen in love with catalytic computing five years earlier after learning about it as an impressionable young undergrad.

“It was like a baby bird imprinting scenario,” Mertz said.

![Image 4: James Cook in a blue coat standing in a snowy field. Ian Mertz in a green T-shirt leaning against a wooden fence.](https://www.quantamagazine.org/wp-content/uploads/2025/02/Cook-Mertz-Diptych.jpg)

James Cook and Ian Mertz adapted catalytic computing techniques to design a low-memory algorithm for the tree evaluation problem.

From left: Colin Morris, Stefan Grosser

Cook and Mertz joined forces, and their efforts soon paid off. In 2020, they devised [an algorithm](https://dl.acm.org/doi/10.1145/3357713.3384316) that solved the tree evaluation problem with less memory than a necessary minimum conjectured by the elder Cook and McKenzie — though it was just barely below that threshold. Still, that was enough to collect on the $100 bet; conveniently for the Cooks, half of it stayed in the family.

But there was still work to do. Researchers had started studying tree evaluation because it seemed as if it might finally provide an example of a problem in P that’s not in L — in other words, a relatively easy problem that can’t be solved using very little memory. Cook and Mertz’s new method used less memory than any other tree evaluation algorithm, but it still used significantly more than any algorithm for a problem in L. Tree evaluation was down, but not out.

In 2023, Cook and Mertz came out with an [improved algorithm](https://eccc.weizmann.ac.il/report/2023/174/) that used much less memory — barely more than the maximum allowed for problems in L. Many researchers now suspect that tree evaluation is in L after all, and that a proof is only a matter of time. Complexity theorists may need a different approach to the P versus L problem.

Meanwhile, Cook and Mertz’s results have galvanized interest in catalytic computing, with new works exploring [connections to randomness](https://eccc.weizmann.ac.il/report/2024/106/) and the effects of allowing a [few](http://arxiv.org/abs/2408.14670) [mistakes](http://arxiv.org/abs/2409.05046) in resetting the full memory to its original state.

“We’ve not finished exploring what we can do with these new techniques,” McKenzie said. “We can expect even more surprises.”

The Quanta Newsletter

_Get highlights of the most important news delivered to your email inbox_

Also in Computer Science
------------------------

Comment on this article
-----------------------

![Image 5](https://www.quantamagazine.org/wp-content/uploads/2025/02/Moving-sofas_crTommy-Parker-HP-1720x728.webp)

Next article
------------

The Largest Sofa You Can Move Around a Corner
