# @andreashappe -- Andreas Happe

> ![](https://github.com/andreashappe.png){ width=64px height=64px }  
> [github.com/andreashappe](https://github.com/andreashappe)  
> [maintaine.rs/andreashappe](https://maintaine.rs/andreashappe)

Hi, I am Andreas, living in Vienna, Austria. I'm a developer gone penetration-tester gone PhD student focusing on how to use LLMs for offensive security. People tell me, that I breathe security.

**What Projects are you currently involved in?**

Currently I work on hackingBuddyGPT[^170] and cochise[^169]: both are research projects that use LLMs to hack real systems. These projects enable security practitioners to experiment with using LLMs in very few lines of code. In the long term, I believe that LLMs will democratize access to security testing.

I am also one of the leaders for two OWASP[^168] projects: the Top 10 Proactive Controls[^167] and the upcoming OT Top 10[^166]. The Proactive Top 10s describe common security measures and techniques that software developers should be aware of. I am not happy that we typically only highlight how to attack systems and not show how to better protect ourselves.

The OT Top 10 are currently under development. OT stands for Operational Technology, typically this is technology that controls some sort of physical process. Think factory floors, power networks, etc. We need to improve the security of these critical infrastructure systems.

## Why Open Source?

I don't understand the question.

I was learning to code in the late 90s, living in Austria's country-side. People were talking about this new thing, Linux, and I became intrigued. Online, I found my tribe and have been a proponent of FOSS since. David Roe's awesome [firstcommit.js](https://firstcommit.js) gives my first commit as a documentation/configuration fix for the linux kernel in 2000[^165] (although I believe that this commit happened around 2003/2004).

How do I feel about Open Source? How does a fish feel about water? Open Source and its community has been a big influence on my life. This is true for most of us, some of us might just not know that yet.

I work in the security domain. In my opinion, Open Source security (and FOSS security tooling) raises the collective security for all of us.

## What do you think are the biggest security challenges facing Open Source today?

I see two two challenges:

1. Maintaining Trust

   Sophisticated attacks[^164] against OSS maintainers erode the trust that is fundamental for online collaboration. Collaboration is the life blood of OSS, so we have to take this threat very seriously. If you think about it, other hyped security problems such as Supply-Chain Attacks (attacks against your dependencies) also boil down to trusting your dependencies' maintainers. Getting to know them (including face-to-face contact) is thus becoming more and more important.

2. Making Security invisible and unobtrusive

   I believe in making it easy to do the right thing, especially when it comes to security. Developers should not have to explicitly think about how to make things secure, the "normal" way of solving a problem should already be the secure way. Frameworks that offer sane secure defaults have had a great positive impact on web application security.

And a bonus one: Don't use Security to Shame People

Typically people can only keep a few things on their mind (3-4 things). Imagine, you're a developer. Those four things are quickly used up: one or two functional requirements, performance, food & coffe, and maybe there's something going on in your personal life. Now, imagine a pen-tester gets to work on the same projects. What's on their mind? security, security, security, coffee. Of course, they will find issues.. and that's okay. We're here to help. An audit is just an opportunity to learn and fix problems before real attackers find them.

## What’s the impact of AI on Open Source development?

It's gonna be an interesting ride. On one hand, I believe that AI will allow many more people to create code. This is a big enabler.

But once there's the code, you have to maintain it and keep it secure. For this, you need a deep level of understanding of how code works and be social with your contributors. "Just" depending upon AI and ignoring both education and social dynamics will not be the perfect solution in the long-term.

\newpage


[^164]: https://en.wikipedia.org/wiki/XZ_Utils_backdoor
[^165]: https://firstcommit.is/andreashappe
[^166]: https://ot.owasp.org/
[^167]: https://top10proactive.owasp.org/
[^168]: https://owasp.org/
[^169]: https://github.com/andreashappe/cochise/
[^170]: https://github.com/ipa-lab/hackingBuddyGPT
