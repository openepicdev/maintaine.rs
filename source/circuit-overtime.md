# @Circuit-Overtime -- Ayushman Bhattacharya

> ![](https://github.com/Circuit-Overtime.png){ width=64px height=64px }  
> [github.com/Circuit-Overtime](https://github.com/Circuit-Overtime)  
> [maintaine.rs/circuit-overtime](https://maintaine.rs/circuit-overtime)

I'm Ayushman Bhattacharya, a maintainer at [pollinations.ai](https://pollinations.ai), a Google Developer Groups on Campus organizer at JIS University, and a mentor for the GirlScript Summer of Code 2025 Open Source Internship and Open Source Connect 2025. I also ship a steady trickle of small projects under the [Elixpo](https://elixpo.com) umbrella, mostly around AI tooling and developer utilities.

I'm 20 and still in college, which probably matters, because most of what I know about Open Source I learned by lurking in repos that were way over my head and slowly working up the courage to open a PR.

## "What does this `git push` button even do?"

I made my GitHub account in 2020. For most of that first year, I didn't really contribute to anything; I pushed my own school projects, broke my own builds, and treated GitHub as a slightly more public Google Drive. The platform was a tool. The community didn't exist for me yet.

That changed during the 2021 lockdown. With nowhere to go and nothing to do, I started actually _reading_ other people's repositories. Not for a class, not for an assignment, just because I was curious. I'd hail from the era of Stack Overflow and Math Exchange, so reading documentation never felt like a chore. Now, instead of just reading docs, I was reading source code, and that turned out to be even more interesting. I'd open a library I depended on, click into a function, and follow the rabbit hole until I either understood what was happening or fell asleep.

Somewhere in that lockdown stretch, I started watching old talks. Linus Torvalds on Git. Talks from Linux Foundation events, PyCon, conference videos with three-digit view counts. The thing that stuck with me wasn't the technical material; it was the casualness with which these people talked about a project that millions of strangers depended on. It seemed both impossibly large and oddly approachable. They were, in the end, just people writing code in public.

I didn't know I'd quietly decided to become one of them until much later.

## "I have no business opening this PR"

The first contributions I made outside my own repos were the kind of contributions everyone makes: a typo in a README, a clarification in a doc, a missing edge case in an example. Tiny things. The kind of PR you'd be embarrassed to mention if you didn't remember how big a deal each one felt at the time.

What surprised me was how much you can learn just by submitting a small change. You read the CONTRIBUTING file. You figure out the project's branching style. You see how the maintainer phrases their review comments. You watch what gets merged and what gets quietly closed. By the time I'd done that across a handful of projects, I had a much better mental model of how Open Source actually works than any tutorial had given me.

I still wasn't a maintainer of anything in 2022 or 2023. I was contributing where I could, mostly for the practice and the puzzle of it. I was also still in high school for part of that, which is a strange backdrop for any of this.

## "Maybe I should just stay here"

In 2024, I started contributing to [pollinations.ai](https://pollinations.ai), an Open Source generative media platform led by Thomas Haferlach and Elliot Fouchy. I'd used the project as a user first, run into the kind of small papercut that any active user runs into, and opened a PR to fix it. Then another. Then a few more. There wasn't a moment where I decided to "join" pollinations; I just kept showing up.

What I appreciated, and what I think a lot of healthy Open Source projects share, is that nobody made a fuss about me being new, or being a student, or not having a Big Tech badge attached to my name. The PRs got reviewed. The feedback was direct. When I shipped something useful, it landed. When I overreached, someone said so plainly. That kind of low-ceremony trust is rare, and I think it's underrated as a community-building tool.

Over the next year I worked on parts of the image and text generation pipeline, integrations, and the unglamorous middle layer of any AI project: making the API surface usable, fixing the rough edges, fielding the issues that real users actually run into. At some point during 2025 I was invited into the organization as a maintainer. There wasn't a ceremony. Someone added me to a team in GitHub. I think that's how it usually goes.

I'd still call this the most important thing that happened to me in Open Source, not because the title changed anything mechanical, but because the responsibility did. The day before, a broken build was someone else's problem. The day after, it was mine.

## "Wait, who's reviewing all of these?"

Maintaining is mostly the unglamorous middle of things. It's a 2 AM hotfix because a deployment fell over. It's debugging a contributor's PR before you can fairly review it. It's rereading the same issue thread three times because the actual bug is buried under six paragraphs of context. It's saying "no" to a thoughtful feature request because it doesn't fit the project's scope, and trying to do it without making the contributor feel dismissed.

The hardest part, for me, has been volume. Issue notifications, review queues, the steady drip of "hey, quick question" pings; it stacks up faster than you'd think, especially when you're a student and also showing up to communities in person. The thing that's helped most is automation. Linters, formatters, CI checks, issue and PR templates; anything a bot can do is something I don't have to remember to do at 2 AM. The other thing that's helped is being honest, with myself and with contributors, about what I can pick up this week and what has to wait. Pretending you'll get to everything is how maintainers burn out.

## "Wait, _I_ run this meetup?"

The shift from "writing code" to "running a community" happened almost by accident. I was nominated as a mentor for Open Source Connect 2025 and the GirlScript Summer of Code 2025 Open Source Internship, which put me on the other side of the contributor experience for the first time. Around the same time, Ankita Chakraborty nominated me as the campus organizer for GDG on Campus at JIS University. Our first session, on October 13th, drew 250+ registrations.

For Hacktoberfest 2025, I co-hosted Kolkata's Hacktoberfest Meetup at JIS University with Abhishek Kushwaha and Hrittik Roy, with 290+ participants. I also ran Hacktoberfest events for pollinations.ai and Elixpo, and helped onboard 50+ new contributors across those efforts. Special thanks to Abiroy Karmakar, Deep Saha, and Abhranil Singha Roy, who showed up the way you hope contributors do. I ended October with a Hacktoberfest Super Contributor badge, but honestly the badge mattered less than watching first-time contributors land a merged PR and come back the next week with another one.

I think this is the part of being a maintainer that surprises people. The code is maybe half the job. The other half is making it possible for someone who has never opened a PR before to feel like they can.

## Maintainer Month topics

This year, Maintainer Month is highlighting project security and the implications of AI on Open Source, so a couple of thoughts:

- **On AI in Open Source**: I work on AI infrastructure, so I'm not going to pretend AI hasn't changed Open Source. It has. I ship faster, new contributors ramp up faster, boilerplate is cheaper. The real concern for maintainers is the asymmetry: AI lowers the cost of _producing_ a PR much faster than it lowers the cost of _reviewing_ one. We're already seeing PRs that look polished on the surface but quietly break invariants the AI didn't know about. The maintainer skill that's going to matter most over the next few years is reading code critically, not generating it. I try to apply that to my own AI-assisted work, too: if I can't explain why a change is correct, the change isn't ready.

- **On security as a contributor habit**: Most of what I've learned about Open Source security has been about making the safe path the easy path. A `SECURITY.md` so people know how to report things privately. Tokens with the least privilege they need. Dependabot and image scanning wired into CI so vulnerable dependencies get caught before a human has to remember to look. None of it is glamorous, and most of it doesn't feel necessary until the day it suddenly does.

---

If anything here resonated, or if you just want to talk Open Source, AI tooling, or community building, I'd love to hear from you.

- Personal Website: [https://elixpo.com](https://elixpo.com)
- LinkedIn: [https://www.linkedin.com/in/elixpo/](https://www.linkedin.com/in/elixpo/)
- GitHub: [https://github.com/Circuit-Overtime](https://github.com/Circuit-Overtime)
- Email: [ayushman@myceli.ai](mailto:ayushman@myceli.ai)

\newpage
