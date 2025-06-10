# @darccio -- Dario Castañé

> ![](https://i0.wp.com/github.com/darccio.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/darccio](https://github.com/darccio)  
> [maintaine.rs/darccio](https://maintaine.rs/darccio)

Hola\! I’m [Dario Castañé](https://dario.cat), a software engineer and lifelong Open Source enthusiast based in Catalonia. In my career I’ve worn many hats – from full-stack developer to engineering manager – but a constant through it all has been my love for Free/Libre Open Source Software (FLOSS). I’m now a Senior Software Engineer at Datadog, where I work on Open Source client libraries (specifically the Go APM tracer). My journey into Open Source began with a simple desire to share solutions to problems I encountered.

## Some of my projects

Over the years, I’ve created and maintained several Open Source projects that reflect my diverse interests:

- [**Mergo**](https://github.com/darccio/mergo) – a tiny Go library for merging structs and maps. I released Mergo back in 2013 to help configure default values in Go applications, and it took on a life of its own. Incredibly, Mergo is now used by over 60,000 repositories on GitHub and has been adopted by major projects like Docker, running my code millions of times in production.

- [**Asembleo**](https://github.com/coopanio/asembleo) – a pseudo-anonymous voting system for general assemblies and organizations. I built Asembleo inspired by my interest in civic tech and grassroots democracy. As a former city councilor in my hometown, I wanted a secure Open Source tool to help communities make collective decisions. Asembleo combines my political passion with coding, enabling transparent votes in a way that protects privacy. It’s an example of how Open Source can strengthen democratic participation.

- [**Zas**](https://github.com/darccio/zas) – the simplest static site generator you can imagine, written in Go. Zas powers my personal website and blog. Rather than use a big framework, I created Zas to generate my site with just the features I needed. It’s minimalistic by design – the joy was in building something from scratch and sharing it. Zas embodies the “indie hacker” spirit I love: if the tool you want doesn’t exist, why not create it and Open Source it for others?

These projects (and a few others in my GitHub) each started as a personal itch to scratch. By releasing them openly, I discovered the joy of seeing others benefit from my code. Each repository became a little community of its own, where I could collaborate with users and other contributors.

## Reflections on impact and community Contributions

When I look back, I’m humbled by the impact some of my work has had. For instance, I never imagined that a small utility like Mergo would become part of fundamental systems. Knowing that my code runs in data centers worldwide is both exciting and a little daunting. It really underscored for me how **a single Open Source contribution can ripple out to millions of users**. This realization has been one of the most motivating aspects of being a maintainer.

Beyond code, I’ve tried to give back to the community in other ways. I’m an active advocate for Open Source, open access, and free culture, frequently speaking at meetups and conferences about the importance of sharing knowledge. I’ve organized local tech meetups, and I also volunteered in grassroots initiatives campaigning for fair legislation around copyright laws and Open Source. For me, Open Source is not just about code – it’s about a set of values: **collaboration, transparency, and empowerment** of individuals and communities.

## Maintaining Datadog’s dd-trace-go

In my professional role at Datadog, I’m part of the team maintaining [**dd-trace-go**](https://github.com/DataDog/dd-trace-go), Datadog’s Go client library for APM (tracing, profiling, etc.). This has been a unique experience because it sits at the intersection of corporate software and Open Source. On one hand, dd-trace-go is critical to many companies’ infrastructure (including our own product), and on the other hand it’s Open Source on GitHub, with a community of users and contributors just like any other OSS project.

Maintaining dd-trace-go has reinforced a few key lessons for me:

- **Consistency and reliability are paramount:** When thousands of businesses rely on your library for monitoring their systems, you can’t afford to break things. We are extremely careful with backward compatibility and thoroughly test every change. I apply the same rigor in dd-trace-go that I do in my personal projects: writing extensive tests and using linters to catch issues early. This discipline was something I cultivated through Open Source, and it pays off hugely at enterprise scale.

- **Community feedback is gold:** Being an Open Source maintainer at a company means we get constant feedback from external users – bug reports, feature requests, even occasional pull requests from the community. I’ve learned to embrace this feedback loop. Users of dd-trace-go often surface use-cases we hadn’t thought of. By listening and engaging with them, we improve the library in ways that benefit everyone. It’s a virtuous cycle: an Open Source ethos inside a commercial product.

- **Collaboration and mentorship:** Within our team, we treat dd-trace-go as a shared responsibility. We review each other’s code, collaborate on design decisions, and mentor newer engineers in Go best practices. I’ve found that my experience in Open Source – where code review and knowledge sharing are the norm – prepared me well for this. A healthy maintainer team functions much like an Open Source community, where respect and continuous learning are key.

## The importance of Open Source supply chain management

One aspect of Open Source that has really hit home for me is the importance of the **software supply chain** – the network of dependencies and libraries that modern applications rely on. As maintainers, we are not just writing code for ourselves; we’re effectively stewards of a supply chain that others trust. I learned this dramatically through Mergo. At one point, because of one teeny-tiny mistake in an update, [I inadvertently _broke a released version of Docker_](https://www.youtube.com/watch?v=kx1ycW4YGqQ). It was an “oops” moment that taught me how even a minor change in a widely used library can have far-reaching consequences, even when you have an extensive test suite in place.

That incident turned into a story I now share with fellow developers: always consider the downstream impact of your changes. I was fortunate – the Docker community and maintainers were understanding, and we worked together to fix the issue quickly. But it highlighted the **responsibility maintainers carry**. Since then, I pay extra attention to semantic versioning, changelogs, and testing against real-world scenarios. It’s crucial to communicate breaking changes clearly (or avoid them when possible). In Open Source supply chains, trust is everything – users trust that our component will function as expected and not compromise their systems.

Security is another big part of supply chain management. I’ve become much more proactive about addressing security reports and keeping dependencies up to date. In the wake of high-profile supply-chain attacks and vulnerabilities in recent years, I feel it’s part of my duty as a maintainer to ensure my projects don’t become weak links. This means embracing tools and best practices for dependency management, auditing, and incident response, like [the ones championed by OpenSSF](https://openssf.org/technical-initiatives/developer-best-practices/). It’s not the most glamorous part of Open Source, but it’s absolutely vital now.

Ultimately, my experiences – from the Docker mishap to managing dd-trace-go – have reinforced how interconnected the Open Source ecosystem is. We’re all links in a chain. By strengthening our own projects, we help secure and stabilize the broader ecosystem.

## Closing thoughts

Looking back at my journey, I feel incredibly grateful for the Open Source community. Open Source transformed my career and even my outlook on life. It taught me that sharing knowledge openly can create enormous value – often in ways we can’t predict. As I once phrased it, **releasing code into the wild is an act of kindness**, a way to help others scratch the same itch you had. You may never know how or by whom your work will be used, but that’s the beauty of it. Your small project might become a building block in someone else’s dream.

Open Source is a two-way street: you give something, and you almost always get something unexpected in return, be it new knowledge, friendship, or the satisfaction of solving a tough problem. In my journey from hacking on side projects to maintaining major libraries, that lesson has been constant. **Contributing and sharing in public is worth it** – for you, for others, and for the sheer progress of technology.

\newpage
