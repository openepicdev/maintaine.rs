# @raphael -- Raphaël Simon

> ![](https://github.com/raphael.png){ width=64px height=64px }  
> [github.com/raphael](https://github.com/raphael)  
> [maintaine.rs/raphael](https://maintaine.rs/raphael)

Hi, I’m Raphaël Simon, the creator of Goa, which you can find at [goa.design](https://goa.design/). It’s a design-first framework that helps with building APIs and microservices in Go.

Goa began as a personal project with the simple goal of streamlining my workday and ensuring that our APIs were built correctly from the outset. It wasn’t initially intended to be a community project.

Turns out, sometimes solving your own problems ends up helping a lot of other people too.

## **From one Rails app to fifty services**

At the time, I was working at RightScale, which is now part of Flexera. The platform was growing from a single Rails application into a distributed system with over 50 microservices, running on hundreds of virtual machines.

This scaling led to a pretty common issue: inconsistent APIs.

Each service had its own style and little quirks. Nothing major on its own, but all together, it made the whole system tough to understand, integrate, and change. Once an API was live, it was almost impossible to fix without causing problems for customers or other parts of the system.

We really needed a better approach: designing APIs first, making sure they were consistent, and letting teams move quickly without creating headaches later on.

In Ruby, we had built Praxis[^280] to help with that. But as we were moving towards Go, I wondered if we could do even better.

After some trial and error, two main ideas came to light:

- **Completely separate the design from the actual implementation.**
- **Describe the API using a simple, expressive DSL written in Go itself.**

That’s how Goa started. At first, it was just a solution for our team. I put it on GitHub mostly out of habit, not expecting much else.

## **The tweet that changed everything**

For a while, Goa just sat quietly on GitHub with a few stars.

Then one day, Brian Ketelsen, who co-founded Gopher Academy and organizes GopherCon, stumbled upon it. He tweeted, “I think I want to marry the guy who wrote Goa.”

I wasn’t even on Twitter at the time. A coworker had to show me the tweet. It made me laugh and made me realize that maybe Goa was resonating with people beyond just our immediate needs.

After that tweet, plus some blog posts and mentions on Go Time, Goa’s GitHub stars jumped from about 10 to over 1,000 in just a few days.

That momentum brought in new contributors, community interest, and eventually an invitation to present Goa at GopherCon 2016\.

Open Source has a way of surprising you, often when you least expect it.

## **Sharing work openly**

Publishing Goa was always about sharing something I thought was genuinely useful.

My early experience with Linux showed me how powerful it is to work with systems you can understand, modify, and improve yourself. I carried those lessons with me, and when Goa came together, it felt natural to share it. Not because it was perfect, but because it might help others.

Open sourcing Goa also made it better. Real users brought new ideas, edge cases, and improvements that our internal team never would have found on its own.

In Open Source, the project grows beyond its creator. And that’s exactly how it should be.

## **What made Goa different**

From the start, a few things were really important:

First, the generated code had to look natural, like something a human would write. Go developers really value clean, idiomatic code. If the generated code looked too mechanical or awkward, people wouldn’t use it.

Second, the DSL had to feel intuitive. Designing an API should be about describing real things — data structures, endpoints, payloads — without getting bogged down in technical details.

Finally, complexity needed to be hidden unless you wanted to dig deeper. Goa should make the hard stuff invisible most of the time, but still be understandable under the hood.

These early choices made a big difference and are still key to what makes Goa useful today.

## **Unexpected connections**

One of the best surprises has been Goa’s strong adoption in Japan.

The Japanese Go community picked up Goa early on, and some of the most important contributions came from developers like Taichi Sasaki and @ikawaha. They didn’t just use the framework — they helped shape it.

It’s a reminder that once you put something out there, you can’t predict where it will end up or how far it will go.

## **Where Goa is today**

Goa has come a long way since those early days.

Today, it generates complete scaffolding for HTTP and gRPC services, automatically creates OpenAPI documentation, and builds strongly typed client libraries that make working with APIs simpler and safer.

But the most important thing is that Goa is still evolving.

New features are constantly being added, driven by real-world needs from the community. Right now, for instance, we’re expanding support for Server-Sent Events (SSE), making it easier to build Model Context Protocol (MCP) servers using Goa.

Projects like this keep Goa growing naturally, one practical improvement at a time, without losing sight of the original goal: to help developers design and build reliable APIs more easily and with less hassle.

Goa isn’t just a framework you install once and forget. It’s something you can grow with and help grow as your services change.

## **Lessons from the journey**

Building and maintaining an Open Source project teaches you a lot more than you’d expect. Goa has taught me many things, including:

- Solve a real problem that you really understand.
- Make your project easy for people to get started with.
- Stay responsive, but also make sure it’s sustainable for you.
- Value every contributor, no matter how big or small their contribution is.

And maybe most importantly, **be ready for the unexpected.** Sometimes a random tweet can open doors you didn’t even know existed.

Building Goa has been one of the most rewarding experiences of my career. I’m thankful for everyone who found it, contributed to it, challenged it, and made it better.

I’m excited for what’s next and for the new ideas that Goa will continue to inspire.

\newpage


[^280]: https://praxis-framework.io/
