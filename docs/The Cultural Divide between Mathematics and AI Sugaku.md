# The Cultural Divide between Mathematics and AI | Sugaku
By [Ralph Furman](https://www.linkedin.com/in/ralphfurman/). [HackerNews Discussion](https://news.ycombinator.com/item?id=43344703)

This January, I attended the Joint Mathematics Meeting (JMM), themed "We Decide Our Future: Mathematics in the Age of AI." It was a veritable buffet of talks and connections, and I found myself rushing across the convention hall to go between sessions in fields I'm close to (eg: modular forms), new areas I was delighted to dig into (eg: knowledge graphs), and the many talks on AI for math.

Jointly organized by the American Mathematical Society (AMS) and the Mathematical Association of America (MAA), the JMM is the largest gathering of mathematicians in the U.S. described as a "family reunion for the mathematical community" (Saxe, 2019). Having attended since 2009, I've always enjoyed this sense of community. This year however I was struck with a palpable cultural divide between mathematics researchers and those working on AI in industry. To be clear, this isn't a judgment call—I've spent time in both worlds and deeply respect the work happening in each. But these communities have been shaped by different forces and realities, leading to distinct perspectives, values, and approaches.

As excitement builds around AI's potential contributions to mathematics, I worry that this enthusiasm doesn't always come with a nuanced understanding of what mathematics truly is and isn't. This is my attempt to articulate these differences and hopefully build a bridge for better collaboration. I'm also building tools to [help make research more deterministic](https://sugaku.net/).

Observations from JMM 2025
--------------------------

The 2025 JMM featured over 6,000 attendees and more than 2,500 presentations according to the official program statistics, with approximately 15% explicitly focused on AI-related topics—a significant increase from just five years ago when such sessions comprised less than 3% of the program.

The 2025 JMM was, in many ways, a study in contrasts. Traditional mathematics sessions proceeded with their usual rigor and depth, while newer AI-focused tracks buzzed with speculation and possibility. Throughout the conference, I noticed a subtle pressure on presenters to incorporate AI themes into their talks, regardless of relevance. Some embraced this challenge creatively, while others politely sidestepped it to focus on their core research.

Throughout the conference, I overheard jokes about mathematicians being "spammed with offers to solve math problems for money" to help train AI models.

One senior professor's comment captured the essence of the divide: "Their incentives aren't ours." In this simple statement lies a profound truth about the different motivations driving academic mathematics and AI research in industry. While mathematicians traditionally pursue understanding for its own sake, industry researchers must ultimately deliver products, features, or capabilities that create value for their organizations.

Concerns were openly expressed about various aspects of AI development: potential military applications, lack of transparency in research, enormous energy consumption, and the growing elitism as research becomes concentrated in well-funded private labs. Many drew parallels to how artists have responded to AI's incursion into their creative domain—with a mixture of fascination, adaptation, and resistance.

Perhaps most telling was the sadness expressed by several mathematicians regarding the increasing secrecy in AI research. Mathematics has long prided itself on openness and transparency, with results freely shared and discussed. The closing off of research at major AI labs—and the inability of collaborating mathematicians to discuss their work—represents a significant cultural clash with mathematical traditions. This tension recalls Michael Atiyah's warning against secrecy in research: "Mathematics thrives on openness; secrecy is anathema to its progress" (Atiyah, 1984).

The tension between openness and secrecy was particularly evident in discussions about collaboration with industry. William Thurston, in his seminal paper "On proof and progress in mathematics" (1994), emphasized that "mathematics is a communal effort," yet multiple attendees expressed dismay at the increasing secrecy in AI research labs and the inability of collaborating mathematicians to discuss their work openly.

The Nature of Mathematics
-------------------------

### What Mathematics Is

To understand the cultural divide, we must first understand what mathematics truly is. Paul Halmos captured this beautifully in _I Want to Be a Mathematician_ (1985): "The youngster who is presented with a proof of a difficult theorem admires the achievement and is left wondering: How was this proof found? How could I invent something like this? No hints are given in the books." This gets at a fundamental truth: mathematics isn't primarily about finding proofs; it's about building understanding.

Richard Feynman, in _Surely You're Joking, Mr. Feynman!_ (1985), shared a humorous observation about mathematicians that actually reveals a profound truth about mathematical culture:

> "At the Princeton graduate school, the physics department and the math department shared a common lounge... I still remember a guy sitting on the couch, thinking very hard, and another guy standing in front of him, saying, 'And therefore such-and-such is true.' 'Why is that?' the guy on the couch asks. 'It's trivial! It's trivial!' the standing guy says, and he rapidly reels off a series of logical steps... which goes on at high speed for about fifteen minutes! Finally the standing guy comes out the other end, and the guy on the couch says, 'Yeah, yeah. It's trivial.'
> 
> "We physicists were laughing, trying to figure them out. We decided that 'trivial' means 'proved.' So we joked with the mathematicians: 'We have a new theorem—that mathematicians can prove only trivial theorems, because every theorem that's proved is trivial.'"

Yet in the mathematical community, this notion of "triviality" actually reflects the highest aspiration: to understand a concept so deeply that what initially seemed complex becomes obvious. This is how solutions to Hilbert's problems—once considered the most challenging questions in mathematics—can eventually be taught as quick corollaries in undergraduate courses.

This prioritization of understanding explains why black-box proofs, while occasionally accepted, are rarely considered satisfying. A proof's value typically lies in its ability to illuminate why a result is true, not merely that it is true. Consider Apéry's proof of the irrationality of ζ(3): initially mysterious, it eventually led to Beukers integrals and other developments that fit into a broader theoretical framework.

This quest for deep understanding also explains a common experience for mathematics graduate students: asking an advisor a question, only to be told, "Read these books and come back in a few months." Sometimes there is a quick answer, but it might not foster the right way of thinking about the problem. I've even heard professors warn that reading the wrong book can "cause brain damage" - a colorful way of saying that premature or misaligned explanations can impede deeper understanding. As Gauss famously said, there is "no royal road" to mathematical mastery.

### Mathematical Culture and Values

Mathematics places tremendous value on elegance. G.H. Hardy, in "A Mathematician's Apology," famously argued for mathematics as an aesthetic pursuit, comparable to poetry or painting. This focus on beauty and elegance isn't merely stylistic preference—it often leads to deeper insights and more powerful generalizations.

The culture is also marked by a profound humility, encapsulated in Newton's phrase about "standing on the shoulders of giants." Young mathematicians quickly learn that despite their talent and ambition, they must first thoroughly understand what has come before them. Those who skip this step, believing they can revolutionize a field without mastering its foundations, often find themselves labeled as "cranks" within the community.

Mathematics is inherently open and transparent. Results are shared freely, methods are discussed openly, and the community collectively verifies and builds upon established work. This transparency isn't just philosophical - it's practical, allowing mathematicians to learn from each other and collaboratively advance the field.

The human element in mathematics is crucial and often underappreciated. While mathematical truths may be objective, the process of discovering them is deeply human, relying on intuition, creativity, and collaboration. Despite the theoretical possibility that anyone could participate in mathematical research (given its open and definite nature), the mentorship provided by advisors and the community fostered by universities remain invaluable. Advisors don't merely direct research; they help students develop taste, intuition, and the ability to navigate the vast landscape of mathematical literature. _The Princeton Companion to Mathematics_ (2008) includes a section titled "Advice to a Young Mathematician" with contributions from Sir Michael Atiyah, Béla Bollobás, Alain Connes, Dusa McDuff, and Peter Sarnak, all emphasizing the importance of mentorship and community in mathematical development.

Attribution in mathematics highlights this human dimension. Results are often named after people rather than described functionally, from results like "Tate's Thesis", research areas like "the Langlands program,", or collaborative works like CFKRS (Conrey, Farmer, Keating, Rubinstein, and Snaith). These names aren't usually self-assigned but emerge organically from the community. There's a famous anecdote, recounted in Constance Reid's _Hilbert_ (1970), of Hilbert once asking after a lecture, "What are Hilbert spaces, exactly?"

One striking feature of mathematical culture that came up was the norm of alphabetical authorship. Unlike many scientific fields, mathematics has no concept of "first author" or "senior author"; contributors are simply listed alphabetically. As documented in Ludo Waltman's "An empirical analysis of the use of alphabetical authorship in scientific publishing" (2012), over 75% of mathematical papers use alphabetical ordering, compared to less than 4% in medicine and biology. There are some exceptions, like Adleman insisting on being last in the RSA paper.

This reflects deeper cultural values in mathematics. Several speakers noted the stark contrast between mathematics and other fields regarding advisor-student publications. While many disciplines expect advisors to be co-authors on their students' papers, the American Mathematical Society's guidelines are that intellectual contributions should be reflected through authorship rather than through role or position. A young mathematician described being shocked when colleagues in another department assumed her advisor would be a co-author on her thesis work, quoting her advisor's response: "If I contributed enough to be a co-author, you wouldn't have much of a thesis, would you?" As Peter Sarnak notes in "Advice to a Young Mathematician" (2008): "Ph.D. students in mathematics are expected to work quite independently, and they often do."

### The Mathematical Process

Mathematics requires extreme patience. Terence Tao, in his blog post "Be patient" (2007), advises young mathematicians that "it can take years to get from the first basic insight into a problem to the complete solution." Many mathematicians report that they can only manage about two hours of truly productive research time per day because of the intense concentration required. In Jacques Hadamard's _The Psychology of Invention in the Mathematical Field_ (1945), he documents how mathematical thinking often requires long periods of unconscious processing, punctuated by moments of insight.

Reading a mathematical paper is similarly demanding, sometimes requiring a full day to process a single page. This isn't passive reading but active engagement: testing claims, working through examples, and connecting new ideas to established knowledge. Some of my most productive days have involved staring at a blank page for hours, writing down a single equation, and feeling genuinely excited about that modest progress.

Andrew Wiles, who spent seven years working on Fermat's Last Theorem, reflected on problem-solving: "Perhaps I can best describe my experience of doing mathematics in terms of a journey through a dark unexplored mansion" (PBS Nova, _The Proof_, 1997). The ongoing effort to formalize this proof illustrates just how complex and resource-intensive mathematical formalization can be, and ambitious efforts like mathlib in Lean (a formal proof verification system) are estimated to contain only about 1% of known mathematical definitions and proofs.

The scale of mathematical knowledge is staggering. The best undergraduate programs typically only bring students to the mid-20th century in terms of mathematical development. The last mathematicians considered to have a comprehensive view of the field were Hilbert and Poincaré, over a century ago.

The precision and density of mathematical language often comes as a shock to those from other disciplines. As Norman Steenrod observed in _How to Write Mathematics_ (1973), mathematical writing aims for "maximum information for minimum reading time"—an efficiency that necessarily produces dense text requiring careful unpacking. James Kaput's research on "Mathematics and Learning" (1987) demonstrates how mathematical notation serves as a cognitive tool that compresses complex concepts into manageable symbols. During my PhD, I experienced this culture shock firsthand when taking courses in other departments. Engineering and computer science courses typically spent the first few sessions motivating the material and explaining potential applications. In contrast, my graduate mathematics seminars operated more like apprenticeships—diving immediately into dense material with the understanding that mastery would gradually reveal both the underlying structures and their applications.

One of the most valuable insights from my experience as a teaching assistant at Stanford was recognizing how students fundamentally misunderstand the difficulty of mathematics. Many arrive with the expectation that sufficient studying and memorization will enable them to solve any test problem algorithmically. They're often shocked to discover that even instructors must engage in substantial problem-solving, trying multiple approaches and experiencing failures before finding solutions. As Alan Schoenfeld documented in his landmark work _Mathematical Problem Solving_ (1985), expertise in mathematics is characterized not by memorization but by strategic thinking, heuristic approaches, and metacognitive awareness of one's problem-solving process.

AI and Mathematics
------------------

At JMM, there was considerable discussion about how AI might contribute to mathematics. Interestingly, most mathematicians expressed interest not in AI creating new mathematics, but in processing and organizing existing knowledge—helping connect fields, translate notation between subdomains, and automate routine calculations.

Yann LeCun's presentation discussed limitations of Large Language Models based on next-token prediction for mathematical reasoning, while highlighting more promising approaches like JEMA. Several speakers noted that AI tools might be particularly valuable for searching and organizing the rapidly expanding mathematical literature—a challenge that many identified as increasingly unmanageable through traditional methods.

### The Different Value Systems

A revealing anecdote shared at one panel highlighted the cultural divide: when AI systems reproduced known mathematical results, mathematicians were excited (seeing this as validation of the system's capabilities), while AI researchers were disappointed (having hoped for novel discoveries). This reflects fundamentally different goals: mathematicians seek deeper understanding of established truths, while AI researchers often prioritize novel results. The mathematicians saw this as validation of the system's capabilities and potential for understanding existing mathematics, while the AI researchers had hoped for novel discoveries.

Several speakers discussed the challenge of mathematical relevance: out of the infinitude of true statements one could prove, which ones matter? Mathematics values results that are not just True and Provable, but also ones "We Care" about—a judgment that requires mathematical taste, context, and community values.

There was genuine enthusiasm about AI's potential to assist with day-to-day mathematical work. Robert Ghrist's experience using AI to accelerate textbook writing (detailed in "Practical AI for the working mathematician") generated particular interest as a pragmatic application that supports rather than replaces mathematical thinking.

The debate between formal methods and natural language approaches reflected another tension. Some mathematicians championed formal proof systems like Lean, which offer rigorous verification but require translation into specific formal languages. Others advocated for natural language approaches more aligned with how mathematicians typically communicate. Both approaches have merits, but they reflect different priorities and values.

Perhaps the most fundamental difference between AI research and mathematics lies in their approaches to knowledge generation. AI research—particularly in deep learning—has been overwhelmingly empirical. As noted in several talks, this empirical focus often contradicts traditional theoretical frameworks. Vladimir Vapnik, whose _Statistical Learning Theory_ underpins much of classical machine learning, famously expressed skepticism about neural networks in his 1998 work, arguing they should be theoretically untrainable for many complex tasks. Zhang et al.'s influential 2017 paper "Understanding deep learning requires rethinking generalization" directly confronted this disconnect, documenting how deep learning empirically succeeds despite theoretical reasons suggesting it shouldn't.

### Future Implications and Concerns

One question generated particular concern: what would happen if an AI system produced a proof of a major conjecture like the Riemann Hypothesis, but the proof was too complex for humans to understand? Would such a result be satisfying? Would it advance mathematical understanding? The consensus seemed to be that while such a proof might technically resolve the conjecture, it would fail to deliver the deeper understanding that mathematicians truly seek.

Some AI researchers confidently predicted that AI would solve a substantial open problem within five years—a claim that many mathematicians viewed with skepticism, not necessarily about AI's capabilities but about what constitutes meaningful mathematical progress. Technical achievement without conceptual advancement would be considered incomplete by most mathematicians.

Bridging the Divide
-------------------

The special issue of the _Bulletin of the American Mathematical Society_ on AI and mathematics (2023) provided an excellent foundation for understanding these different perspectives. Jeremy Avigad, in his article "Mathematics and the Formal Turn," wrote: "Mathematics has always been about coming up with abstractions that enable us to think more efficiently, communicate precisely, solve hard problems, and reach a stable consensus as to whether our claims are justified... We can use technology to do lots of things, but if we are not using it to do those things, then we are probably not doing mathematics."

Akshay Venkatesh proposed an interesting Bayesian model for how mathematicians assign importance to results: when one conjecture implies another, we update our estimates of the difficulty of both; when a mathematician proves a challenging result, we update our assessment of both the mathematician and the result. This framework, presented in his talk "Value and Difficulty in Mathematics," suggests that AI systems might dramatically change these calculations, but many problems will likely remain out of reach, preserving the value of human insight.

### Potential Collaborative Frameworks

The most promising areas for AI-mathematics collaboration emerged from honest assessments of mathematical needs:

1.  **Literature management**: AI could help mathematicians navigate the overwhelming volume of published work, identifying relevant papers and connections between seemingly disparate fields.
    
2.  **Theorem verification**: Formal verification systems enhanced by AI could help check proofs and identify subtle errors or gaps.
    
3.  **Refactoring proofs**: AI might help restate existing results in more general or elegant forms, revealing underlying patterns.
    
4.  **Teaching and accessibility**: AI tools could make mathematics more accessible to students and those without traditional institutional access.
    
5.  **Counterexample generation**: AI systems might excel at finding counterexamples to false conjectures, saving mathematicians from pursuing unproductive paths.
    

### Maintaining Mathematical Culture in an AI Era

Throughout the discussions, a consistent theme emerged: the importance of preserving mathematics' human, open, and understanding-centered culture while embracing technological advances.

Several speakers suggested frameworks for collaboration that respect mathematical values: open research sharing, focus on explanation rather than just results, and maintaining human oversight and interpretation. The consensus was that AI should serve as a tool for expanding human mathematical capability rather than replacing human mathematicians.

Conclusion
----------

The cultural divide between mathematics and AI isn't an insurmountable barrier but rather an opportunity for mutual learning and growth. Both communities bring valuable perspectives: mathematics offers deep traditions of rigor, patience, and beauty, while AI research brings energy, resources, and new computational approaches.

Bridging this divide requires mutual respect and understanding. Albert Einstein famously said, "The grand aim of all science is to cover the greatest number of empirical facts by logical deduction from the smallest number of hypotheses or axioms" (quoted in Dyson, 2006). This pursuit unites both mathematicians and AI researchers, though they may approach it from different angles.

As someone who has spent time in both worlds, I see tremendous potential in collaboration that honors the best of both traditions, and I'm trying to build tools to enable this at [Sugaku](https://sugaku.net/). AI won't "solve" mathematics, nor should we want it to, but it might help us explore mathematical landscapes more efficiently, connect disparate areas of knowledge, and perhaps even suggest new directions for human creativity and insight.

Mathematics has evolved over thousands of years, absorbing new tools and methods while maintaining its essential character. I'm confident it will continue to do so in the age of AI—not by resisting change, but by thoughtfully incorporating these new capabilities into its rich intellectual tradition.

References and Resources
------------------------

### Bulletin of the American Mathematical Society special issues on AI and mathematic

*   [Mathematics, word problems, common sense, and artificial intelligence](https://sugaku.net/oa/W4391836239/)
*   [Mathematical reasoning and the computer](https://sugaku.net/oa/W4391839001/)
*   [Abstraction boundaries and spec driven development in pure mathematics](https://sugaku.net/oa/W4391839082/)
*   [Mathematics and the formal turn](https://sugaku.net/oa/W4391839106/)
*   [Is deep learning a useful tool for the pure mathematician?](https://sugaku.net/oa/W4391839309/)
*   [Some thoughts on automation and mathematical research](https://sugaku.net/oa/W4391885377/)
*   [How machines can make mathematics more congressive](https://sugaku.net/oa/W4391958675/)
*   [Automated mathematics and the reconfiguration of proof and labor](https://sugaku.net/oa/W4398767253/)
*   [Machine Learning and Information Theory Concepts towards an AI Mathematician](https://sugaku.net/oa/W4398767262/)
*   [Compositional sparsity of learnable functions](https://sugaku.net/oa/W4398776577/)
*   [Poincaré on the value of reasoning machines](https://sugaku.net/oa/W4398776588/)
*   [Proofs for a price: Tomorrow’s ultra-rigorous mathematical culture](https://sugaku.net/oa/W4398782068/)

### Terence Tao's blog posts

*   ["What is good mathematics"](https://arxiv.org/pdf/math/0702396)
*   ["Don't base career decisions on glamour or fame"](https://terrytao.wordpress.com/career-advice/don%E2%80%99t-base-career-decisions-on-glamour-or-fame/)
*   ["Be professional in your work"](https://terrytao.wordpress.com/career-advice/be-professional-in-your-work/)
*   ["Enjoy Your Work"](https://terrytao.wordpress.com/career-advice/enjoy-your-work/)
*   ["Career advice"](https://terrytao.wordpress.com/career-advice/)
*   ["Learn and Relearn your field"](https://terrytao.wordpress.com/career-advice/learn-and-relearn-your-field/)
*   ["Continually aim just beyond your current range"](https://terrytao.wordpress.com/career-advice/continually-aim-just-beyond-your-current-range/)
*   ["Be flexible"](https://terrytao.wordpress.com/career-advice/be-flexible/)
*   ["Don't prematurely obsess on a single 'big problem' or 'big theory'"](https://terrytao.wordpress.com/career-advice/dont-prematurely-obsess-on-a-single-big-problem-or-big-theory/)
*   ["Be patient"](https://terrytao.wordpress.com/career-advice/be-patient/)
*   ["Be sceptical of your own work"](https://terrytao.wordpress.com/career-advice/be-sceptical-of-your-own-work/)

### Additional Perspectives on Mathematics

*   G.H. Hardy, ["A Mathematician's Apology"](https://en.wikipedia.org/wiki/A_Mathematician%27s_Apology) (1940)
*   Henri Poincaré, _Science and Method_ (1908)
*   Paul Halmos, ["I Want to Be a Mathematician"](https://sugaku.net/oa/W2801698030/) (1985)
*   Edward Frenkel, ["Love and Math: The Heart of Hidden Reality"](https://www.edwardfrenkel.com/lovemath/)
*   Paul Lockhart, ["A Mathematician's Lament"](https://worrydream.com/refs/Lockhart_2002_-_A_Mathematician's_Lament.pdf)
*   Imre Lakatos, ["Proofs and Refutations"](https://sugaku.net/oa/W4244520098/)
*   Jacques Hadamard, ["The Psychology of Invention in the Mathematical Field"](https://sugaku.net/oa/W2027049501/)
*   André Weil, ["The Apprenticeship of a Mathematician"](https://sugaku.net/oa/W4300859058/)
*   John Littlewood, ["A Mathematician's Miscellany"](https://sugaku.net/oa/W4231831983/)
*   Richard Courant, ["What is Mathematics?"](https://sugaku.net/oa/W1539883774/)
*   Cédric Villani, ["The Birth of a Theorem"](https://sugaku.net/oa/W826091870/)
*   Ian Stewart, ["Letters to a Young Mathematician"](https://en.wikipedia.org/wiki/Letters_to_a_Young_Mathematician)
*   Davis & Hersh, ["The Mathematical Experience"](https://sugaku.net/oa/W2072405721/)
*   ["Practical AI for the working mathematician"](https://www.youtube.com/watch?v=DkQyUta5CAw) (Ghrist interview)
*   Thurston's ["On proof and progress in mathematics"](https://arxiv.org/abs/math/9404236)
*   Princeton Companion's ["Advice to a Young Mathematician"](https://assets.press.princeton.edu/releases/gowers/gowers_VIII_6.pdf)
*   _Mathematical People_ (interviews with leading mathematicians)
*   ["Mathematician's Delight"](https://sugaku.net/oa/W2795539731/) by W. W. Sawyer
*   Matt Might's ["The Illustrated Guide to a PhD"](https://matt.might.net/articles/phd-school-in-pictures/)
*   [XKCD purity](https://xkcd.com/435/)