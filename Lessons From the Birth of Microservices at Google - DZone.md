# Lessons From the Birth of Microservices at Google - DZone
[Lessons From the Birth of Microservices at Google - DZone](https://dzone.com/articles/lessons-from-the-birth-of-microservices-at-google) 

 _[This article is featured in the new DZone Guide to Microservices. Get your free copy for insightful articles, industry stats, and more!](https://dzone.com/guides/microservices-3)_

Our story begins in the early 2000s when Google's Search and Ads products were really taking off. At the time, the conventional wisdom suggested that building a reliable internet service meant buying reliable — and expensive — servers. To keep costs down, Google engineering teams switched to commodity hardware. While this approach saved on cost, these servers were (as you might expect) highly unreliable. As hardware failure became the common case rather than the exception, Google engineers needed to design accordingly.

Today, we might start by going to GitHub to look for code that others have developed to tackle similar problems, but in 2001 this simply wasn't an option. While there were strong communities around projects like Linux and the Apache Web Server, these projects were mostly focused on the software running on a single machine. As a result, Google had no choice but to build things from scratch.

What followed was an explosion of now-legendary infrastructure projects, including GFS, BigTable, and MapReduce. These systems, along with widely used products like Google Search and Ads, had several characteristics that we now associate with microservice architectures:

*   Horizontal scale points that enabled the software to scale across thousands of physical machines.
    
*   Reusable code for RPC, service discovery, load balancing, distributed tracing, and authentication.
    
*   Frequent and independent releases.
    

However, even if Google arrived at the results we are hoping to achieve with microservices, should we follow the same path?

The Lessons
-----------

### Lesson 1: Know Why (You're Adopting Microservices)

The most important reason to adopt microservices has nothing to do with how your software scales: microservices are useful because they address engineering management challenges. Specifically, by defining service boundaries between teams and letting them work independently, teams will need to communicate less and can move more quickly.

The architecture developed for Google Search and Ads, while superficially similar to microservices, was really there to support the scale needed to index and search the web while serving billions of requests every second. This scale came at a cost in terms of features, and there were hundreds of other smaller teams at Google who needed tools that were easy to use, and who didn't care about the planetary scale or tiny gains in efficiency.

As you are designing your infrastructure, consider the scale of what you need to build. Does it need to support billions of requests per second... or "just" millions?

### Lesson 2: Serverless Still Runs on Servers

Many organizations are considering skipping microservices and moving straight to a "serverless" architecture. Of course, serverless still runs on servers, and that has important consequences for performance. As Google built out its infrastructure, measuring performance was critical. Among the many things that Google engineers measured and used are two that are still relevant to serverless:

*   A main memory reference is about 100 nanoseconds.
    
*   A roundtrip RPC (even within a single data center) is about 500,000 nanoseconds.
    

This means that a function call within a process is roughly 5,000 times faster than a remote procedure call to another process. Stateless services can be a great opportunity to use serverless, but even stateless functions need access to data as part of their implementation. If some of this data must be fetched from other services (which almost goes without saying for something that's stateless!), that performance difference can quickly add up. The solution to this problem is (of course) a cache, but caching isn't compatible with a serverless model.

Serverless has its place, especially for offline processing where latency is less of a concern, but often a small amount of context (in the form of a cache) can make all the difference. "Skipping" right to a serverless-based architecture might leave you in a situation where you need to step back to a more performant, services-based one. 

### Lesson 3: What Independence Should Mean

Above, I argued that organizations should adopt microservices to enable teams to work more independently. But how much independence should we give teams? Can they be too independent? The answer is definitely yes, they can.

In adopting microservices, many organizations allow each team to make every decision independently. However, the right way to adopt microservices is to establish organization-wide solutions for common needs like authentication, load balancing, CI/CD, and monitoring. Failing to do so will result in lots of redundant work, as each team evaluates or even builds tools to solve these problems. Worse, without standards, it will become impossible to measure or reason about the performance or security of the application as a whole.

Google got this one right. They had a small number of approved languages and a single RPC framework, and all of these supported standard solutions in the areas listed above. As a result, product teams got the benefits of shared infrastructure, and infrastructure teams could quickly roll out new tools that would benefit the entire organization.

### Lesson 4: Beware of Giant Dashboards

Time series data is great for determining when there is a regression but it's nearly impossible to use it to determine which service was the cause of the problem. It's tempting to build dashboards with dozens or even hundreds of graphs, one for each possible root cause. You aren't going to be able to enumerate all possible root causes, however — let alone build graphs to measure them.

The best practice is to choose fewer than a dozen metrics that will give you the best signal that something has gone wrong. Even products as large as Google Search were able to identify a small number of signals that really mattered to their users. In this case, perhaps unlike others, what worked for Google Search can work for you.

Ultimately, observability boils down to two activities: measuring these critical signals and then refining the search space of possible root causes. I use the word "refining" because root cause analysis is usually an iterative process: establishing a theory for what went wrong, then digging in more to validate or refute that theory. With microservices, the search space can be huge: it must encompass not only any changes in the behavior of individual services but also the connections between them. To reduce the size of the search space effectively, you'll need tools to help test these theories, including tracing, as described next.

### Lesson 5: You Can't Trace Everything... or Can You?

Like anyone who has tried to understand a large distributed system, Google engineers needed tools that would cut across service boundaries and give them a view of performance centered around end-to-end transactions. They built Dapper, Google's distributed tracing system, to measure the time it takes to handle a single transaction and to break down and assign that time to each of the services that played a role in that transaction. Using Dapper, engineers can quickly rule out which services aren't relevant and focus on those that are.

Tracing, like logging, grows in cost as the volume of data increases. When this volume increases because of an increased number of business transactions, that's fine — as presumably, you can justify additional costs as your business grows. The volume of tracing data also increases combinatorially with the number of microservices, however, so new microservices mean your margins will take a hit.

Google's solution to this problem was simple: 99.99% of traces were discarded before they were recorded in long-term durable storage. While this may seem like a lot to throw out, at the scale of services like Google Search, even as few as 0.01% of requests can provide ample data for understanding latency. To keep things simple, the choice about which traces to keep was made at the very beginning of the request. Subsequent work, like Zipkin, copied this technique.

Unfortunately, this approach misses many rare yet interesting transactions. And for most organizations, it's not necessary to take such a simplistic view of trace selection. They can use additional signals that are available until after the request has been completed as part of the selection. This means we can put more — and more meaningful — traces in front of developers without increasing costs. To do so will require rethinking the data collection and analysis architecture, but the payoff, in terms of reducing mean time-to-resolution and improved performance, is well worth the investment.

Conclusion
----------

While Google built systems that share many characteristics with microservices as they exist today (as well as a powerful infrastructure that has since been replicated by a number of open-source projects), not every design choice that Google engineers made should be duplicated. It's critical to understand what led Google engineers down these paths — and what's changed in the last 15 years — so you can make the best choices for your own organizations.

_[This article is featured in the new DZone Guide to Microservices. Get your free copy for insightful articles, industry stats, and more!](https://dzone.com/guides/microservices-3)_

Opinions expressed by DZone contributors are their own.