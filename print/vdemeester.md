# @vdemeester -- Vincent Demeester

> ![](https://github.com/vdemeester.png){ width=64px height=64px }  
> [github.com/vdemeester](https://github.com/vdemeester)  
> [maintaine.rs/vdemeester](https://maintaine.rs/vdemeester)

I've always wanted to do Open Source, since I discovered it around 1999. The first Linux distribution I used was Red Hat Linux, and that was also my first encounter with Linux and Open Source. Little did I know that 20 years later I would work for the company that kind of introduced me to it!

I initially started looking into small projects I would need in my first startup job, like `fog/fog`, but what really got me started was the Docker project. Docker organized those "contribute meetups" in different places around their "birthday" and so, I made my first pull-request to the project that way. And from that point on, I was hooked. I also got involved a bit in the Archlinux User Repository when I was using it and now in NixOS.

## **What’s Open Source to you?**

For me, Open Source is "the way" to do things. I truly believe in sharing commons and the fact that we do better when we work together, in the open. And Open Source embodies that.

## **What projects are you involved in?**

I am involved in a bunch of projects, some more than the others, but the highlights are:

- The TektonCD project[^149], where I am one of the main contributors and a governance member. I am also the architect of our product based on top, OpenShift Pipelines[^150].
- The Moby project[^151] and the Docker project[^152]. I have been a main contributor for years, and I am now a little less active.
- The Traefik project[^153], where I was one of the first contributors—well, the second.
- The NixOS project[^154], where I am maintaining a bunch of packages.

## Nurturing Communities and Overcoming Hurdles

**How do you grow your community?**

This is a hard question, but essentially, to help a community grow, you need to make it welcoming to anyone, no matter what their background or interest is. And then you need to keep it alive. You need to make sure the goal(s) of the community are clear and drive the community to draw a path towards those goals. There are always some ups and downs during the life of a community—people leaving, new people coming—so you need to ensure that the community is standing for itself.

**What are the main challenges you face as a maintainer?**

I guess time management is one. As a maintainer, you need to triage user requests and proposals. You need to make sure you treat everyone equally. It can be a challenge to figure out what the priorities are.

Another challenge is around process. To be functioning, a community needs some process in place, but there is a balance to find. Too much process can become a burden and kill motivation and creativity. Not enough can make it very hard to make decisions. Also, maintaining those processes and making them evolve as the community evolves can be overlooked.

**What are some ways contributors can better support maintainers?**

Even seemingly minor contributions can be incredibly impactful. For instance, submitting pull requests that are unambiguous and thoroughly documented is a massive help. Likewise, ensuring changes are tested beforehand, contributing to documentation—whether by writing new material or updating existing content—and assisting with the initial review and categorization of issues are all activities of immense value.

Beyond individual code submissions, ongoing engagement from contributors is also key. When someone takes responsibility for a specific area, like a plugin or a particular feature, diligently acts on feedback, or offers support to other community members, it significantly eases the burden on maintainers. Ultimately, Open Source thrives on teamwork and a sense of collective ownership, which is vital for its long-term health.

## Security in the Open Source Realm

**What are some of the key security practices you’ve implemented in your project(s)?**

In most projects I have been involved in, we are trying to apply all the security best practices we can find that make sense. That goes from linting and code scanning to automating dependency security fixes updates. But aside from tooling, these days, one area of focus for me is to look for ways to reduce dependencies in our project. Fewer dependencies usually mean fewer problems.

**What do you think are the biggest security challenges facing Open Source today?**

One of the primary difficulties arises from how extensively Open Source is now used. It's not uncommon for a project maintained by a very small team, sometimes just a few volunteers, to be a critical component in thousands of live production systems. This mismatch places enormous pressure on maintainers to deliver high-level security, often with insufficient resources.

Furthermore, the way we handle software dependencies presents another significant area of concern. A single security flaw in an upstream library can cascade through the ecosystem, impacting hundreds or even thousands of projects that depend on it. To effectively manage this interconnectedness and its risks, we really need to see advancements in tooling, the establishment of more rigorous processes, and a much stronger emphasis on collaboration between different ecosystems.

## The Horizon: AI and Open Source

**What’s the impact of Artificial Intelligence on Open Source development?**

I am not sure it is clear yet what impact Artificial Intelligence (AI) will have on Open Source development. I feel it can help tremendously maintainers, for example for triaging issues, reviewing code. But it also feels like a double-edged sword, and we already saw some AI-generated spam issues and pull-requests on some of our projects. With the "vibe" coding trend and agents, it feels there could be some enhancement in productivity, but I am a bit concerned about quality, and thus it's definitely something to be careful about.

\newpage


[^149]: https://github.com/tektoncd
[^150]: https://github.com/openshift-pipelines
[^151]: https://github.com/moby
[^152]: https://github.com/docker
[^153]: https://github.com/traefik/
[^154]: https://github.com/NixOS
