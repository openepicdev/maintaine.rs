# @martincostello -- Martin Costello

> ![](https://i0.wp.com/github.com/martincostello.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/martincostello](https://github.com/martincostello)  
> [maintaine.rs/martincostello](https://maintaine.rs/martincostello)

I'm Martin, I'm a software developer based in the UK, and I've been a contributor to
Open Source projects since 2013.

Open Source software is something that I have a lot of passion for, but it's not something that I've
actively sought out. Instead, it's something that's organically grown out of my time working in the
software industry. Incrementally as I've run into challenges, had ideas, or even just wanted to peek
under the covers of how something works, I've found myself contributing back to projects more and more.

It all started with this pull request: Glimpse/Glimpse#493[^276].

I'd been playing around with the Glimpse Open Source project, and ran into some difficulty configuring things
to work correctly with the project I was trying it out with. I took the opportunity to raise an issue asking
the maintainers how to resolve my problem. Once I got the information I needed to unblock my progress, I
suggested to the maintainers that the help messages in the project could be updated to include additional
information to help others who might run into the same problem in the future. They agreed, so I submitted my
first pull request on GitHub, and it was merged just two days later.

Looking back, this highlights some of the things that I think are great about Open Source software:

1. Anyone can propose a change to a project - you don't have to be a maintainer or have a support contract
   to be able to contribute to a project you're using.
2. You can solve your own problems - if you run into an edge case in some software where it might not otherwise
   be prioritised by the maintainers, you can give it your priority and make the change yourself.
3. You can make things better for those who follow you - if you run into a problem, there's a good chance that
   someone else will have the same experience at some point in the future. Sharing your solution for a difficulty
   back to the project means you can magnify the impact of your discovery and leave things better than you found them.
4. You don't just have to implement a big new feature to contribute - even a small change to some documentation can
   be invaluable to not only other users, but to the maintainers as well. Documentation is often the most neglected
   part of a project compared to the code itself.

Fast forward to today, and I'm a maintainer of multiple Open Source projects, some of which I started myself,
others I've inherited from collaborating with others. These projects include:

- Polly[^277] - a .NET resilience and transient fault handling library
- [Swashbuckle.AspNetCore](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) - OpenAPI tools for documenting APIs
  built with ASP.NET Core.
- HttpClient Interception[^278] - a library for intercepting and mocking HTTP requests for .NET applications
- xunit Logging[^279] - An logging library for xUnit.net to route application logs to the test output

I'm also a regular contributor to .NET, raising issues, improving documentation, fixing bugs, and (very) occasionally adding new features. I also help with issue triage for ASP.NET Core, routing issues to the right core team members where
necessary, or leaning on my own experience and knowledge to answer questions and troubleshoot users' problems myself.

But it's not just C# and .NET that I contribute to. I'm always happy to try and help out with projects written in other languages if they're a tool that I use and there's a problem I want to help out with (if I can). I've dabbled with Ruby,
Go and JavaScript too.

Open Source software is a great way to _be the change you want to see in the world_. If you find a bug in something,
rather than sit back and wait for someone else to fix it, you can take control of your own destiny and try to fix it yourself.
Not only will you learn something new, you'll help others, and contribute back to the community that you're part of
from consuming Open Source software in your own projects.

Over the last few years as I've got involved in more projects, especially as a maintainer of projects I've inherited,
there's a few things I've observed that seem to be common pain points for maintainers of Open Source projects that aren't
backed by a company or organisation. One of the major topics that should be a concern for consumers of Open Source software is that of burnout.

Many Open Source projects are ultimately run by a single person, and maintained in their spare time. When the popularity
of a project grows past a certain point, it can become overwhelming for the maintainer to keep up with the volume of issues and pull requests to their project to keep the project healthy and their users' concerns addressed. In some cases this can
lead to maintainers either being burned out by their experience, or having to abandon the project altogether due to a lack
of time to focus on it amongst the other commitments in their life.

Abandoned projects can then become a security risk to the users of the software - the maintainer may no longer be available to fix (or accept fixes) a security vulnerability, or to publish a new version containing a patch. This can lead to consuming projects with either an unpatched security vulnerability in their application, or having to expend time and
effort to find a suitable replacement for the dependency and migrate their projects to use the alternative.

If you're a consumer of Open Source software, then you should consider how you can help contribute back to the projects
you depend on to help keep them, and the wider ecosystem healthy. After all, the health of the projects you depend on
directly impacts the health of your own projects too.

1. Find a bug? Raise an issue. If you find an issue, raise an issue for visibility and attract help for a fix. But take a
   moment to check whether there's already an issue for your problem (open or closed).
1. If you've found a bug, consider whether you can try and fix it too. Maintainers love pull requests to solve bugs in their
   projects, as it often makes resolution quicker, and also helps avoid considerations over prioritisation of the issue
   compared to other issues in their backlog. Just be sure to check the contribution guidelines for the project first.
1. No contribution is too small. You don't just need to submit a cool new feature or fix a bug to contribute to an Open
   Source project. Documentation is often an overlooked part of a project, but it's just as important as the code itself
   to help users succeed. If you find a typo, or something that's unclear, consider raising an issue or submitting a pull request to fix it. Using the GitHub web interface is a great way to get started with small changes. You could be done within just a few minutes.
1. Sponsor a project. An increasing number of Open Source projects now accept donations via GitHub Sponsors, and these don't
   have to be a large amount of money, or even an ongoing commitment. If you get value from a project and are in a position
   to do so (especially if you're using it in a commercial project), consider sponsoring the project to help the maintainer
   prioritise the maintenance of the project amongst their other responsibilities and commitments. Even a small amount as a one-off sponsorship can go a long way to helping the maintainer feel appreciated for their work.

Open Source software is ultimately a large collaborative effort, with projects depending on each other to solve problems
in the best way they can to help users reach their goals, whether that's in industry, academia, charity, or just for fun.

I hope this post has inspired you to consider how you can contribute back to the Open Source projects you depend on.

\newpage


[^276]: https://github.com/Glimpse/Glimpse/pull/493
[^277]: https://github.com/App-vNext/Polly
[^278]: https://github.com/justeattakeaway/httpclient-interception
[^279]: https://github.com/martincostello/xunit-logging
