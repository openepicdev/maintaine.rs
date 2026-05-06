# @Circuit-Overtime -- Ayushman Bhattacharya

> ![](https://github.com/Circuit-Overtime.png){ width=64px height=64px }  
> [github.com/Circuit-Overtime](https://github.com/Circuit-Overtime)  
> [maintaine.rs/circuit-overtime](https://maintaine.rs/circuit-overtime)

I'm Ayushman Bhattacharya, a maintainer at [pollinations.ai](https://pollinations.ai), a Google Developer Groups on Campus organizer at JIS University, and a mentor for the GirlScript Summer of Code 2025 and Open Source Connect 2025. I also ship a steady trickle of small projects under the [Elixpo](https://github.com/elixpo) umbrella, mostly around AI tooling and developer utilities.

I'm 20 and still in college, which probably matters, because most of what I know about Open Source I learned by lurking in repos that were way over my head and slowly working up the courage to open a PR.

## "What does this `git push` button even do?"

I made my GitHub account in 2020. For most of that first year, I didn't really contribute to anything; I pushed my own school projects, broke my own builds, and treated GitHub as a slightly more public Google Drive. The platform was a tool. The community didn't exist for me yet.

That changed during the 2021 lockdown. With nowhere to go and nothing to do, I started actually _reading_ other people's repositories. Not for a class, not for an assignment, just because I was curious. I'd hail from the era of Stack Overflow and Math Exchange, so reading documentation never felt like a chore. Now, instead of just reading docs, I was reading source code, and that turned out to be even more interesting. I'd open a library I depended on, click into a function, and follow the rabbit hole until I either understood what was happening or fell asleep.

Somewhere in that lockdown stretch, I started watching old talks. Linus Torvalds on Git. Talks from Linux Foundation events, PyCon, conference videos with three-digit view counts. The thing that stuck with me wasn't the technical material; it was the casualness with which these people talked about a project that millions of strangers depended on. It seemed both impossibly large and oddly approachable. They were, in the end, just people writing code in public.

I didn't know I'd quietly decided to become one of them until much later.

## "I have no business opening this PR"

The first contributions I made outside my own repos were the kind of contributions everyone makes: a typo in a README, a clarification in a doc, a missing edge case in an example. Tiny things. The kind of PR you'd be embarrassed to mention if you didn't remember how big a deal each one felt at the time.

What surprised me was how much you can learn just by submitting a small change. You read the CONTRIBUTING file. You figure out the project's branching style. You see how the maintainer phrases their review comments. You watch what gets merged and what gets quietly closed. By the time I'd done that across a handful of projects, I had a much better mental model of how Open Source actually works than any tutorial had given me.

I still wasn't a maintainer of anything in 2022 or 2023. I was contributing where I could, mostly for the practice and the puzzle of it. I was also still in high school nearly a fresher for part of that, which is a strange backdrop for any of this.

## "Maybe I should just stay here"

In 2024, I started contributing to [pollinations.ai](https://pollinations.ai), an Open Source generative media platform led by [Thomas Haferlach](https://github.com/voodoohop) and [Elliot Fouchy](https://github.com/ElliotEtag). I'd used the project as a user first, and my very first contribution wasn't a code fix; it was a PR to enlist a project of my own that I'd built on top of pollinations into their ecosystem. That alone felt like a milestone.

The bigger turning point came soon after, when I built a Discord bot powered by the pollinations API. The team invited it into their official community Discord, and it caught on faster than I expected. People were using it daily generating synthetic media. For someone who'd spent the last few years lurking in other people's repos, having strangers on the internet actually use something I'd built, and care enough to file bugs against it, was a different kind of feeling entirely.

That's also when GitHub started to look different to me. I went from "I should send a PR for the thing that bugs me" to actually picking up issues from the tracker, debugging things I hadn't broken, and trying to fix problems for users I'd never meet. That shift, from scratching your own itch to scratching someone else's, is the part that I think makes you a contributor for real. Up until that point I was just a user with commit access; afterwards, I was someone who felt some responsibility for the project itself.

I still remember the feeling of the first PR titled `Merged to main #xxx`. I don't think it ever fully wore off. I get a smaller version of the same feeling every time it happens.

Somewhere along the way I built [search.elixpo](https://github.com/pollinations/search.elixpo), a research-based project on crawlers and rankers paired with an LLM-supported native search engine, now part of the organization. It uses a three-tier caching architecture under the hood, and building it taught me more about systems design, eviction policies, and the cost of getting cache invalidation wrong than any course or tutorial I've taken.

What I appreciated about pollinations, and what I think a lot of healthy Open Source projects share, is that nobody made a fuss about me being new, or being a student, or not having a Big Tech badge attached to my name. The PRs got reviewed. The feedback was direct. When I shipped something useful, it landed. When I overreached, someone said so plainly. That kind of low-ceremony trust is rare, and I think it's underrated as a community-building tool.

Over the next year I worked on parts of the image and text generation pipeline, integrations, and the unglamorous middle layer of any AI project: making the API surface usable, fixing the rough edges, fielding the issues that real users actually run into. At some point during 2025 I was invited into the organization as a maintainer during hacktoberfest 25' and it has been a part of my life ever since.

I'd still call this the most important thing that happened to me in Open Source, not because the title changed anything mechanical, but because the responsibility did. The day before, a broken build was someone else's problem. The day after, it was mine.

## "Wait, who's reviewing all of these?"

Maintaining is mostly the unglamorous middle of things. It's a 2 AM hotfix because a deployment fell over. It's debugging a contributor's PR before you can fairly review it. It's rereading the same issue thread three times because the actual bug is buried under six paragraphs of context. It's saying "no" to a thoughtful feature request because it doesn't fit the project's scope, and trying to do it without making the contributor feel dismissed.

The hardest part, for me, has been volume. Issue notifications, review queues, the steady drip of "hey, quick question" pings; it stacks up faster than you'd think, especially when you're a student and also showing up to communities in person. The thing that's helped most is automation. Linters, formatters, CI checks, issue and PR templates; anything a bot can do is something I don't have to remember to do at 2 AM. The other thing that's helped is being honest, with myself and with contributors, about what I can pick up this week and what has to wait. Pretending you'll get to everything is how maintainers burn out.

## "Wait, _I_ run this meetup?"

The shift from "writing code" to "running a community" happened almost by accident. I was nominated as a mentor for Open Source Connect 2025 and the GirlScript Summer of Code 2025 Open Source Internship, which put me on the other side of the contributor experience for the first time. Around the same time, Ankita Chakraborty nominated me as the campus organizer for GDG on Campus at JIS University. Our first session, on October 13th, drew 250+ registrations.

For Hacktoberfest 2025, I co-hosted Kolkata's Hacktoberfest Meetup at JIS University with 290+ participants. I also ran Hacktoberfest events for pollinations.ai and Elixpo, and helped onboard 100+ new contributors across those efforts. I ended October with a Hacktoberfest Super Contributor badge, but honestly the badge mattered less than watching first-time contributors land a merged PR and come back the next week with another one.

I think this is the part of being a maintainer that surprises people. The code is maybe half the job. The other half is making it possible for someone who has never opened a PR before to feel like they can.

## Proudest moment

There isn't one single moment, more a stack of small ones from the last year that, taken together, feel like something I'd never have predicted at 18.

The first is realizing that strangers on the internet were quietly depending on things I'd built. My Discord bot was running daily for users I'd never spoken to. [search.elixpo](https://github.com/pollinations/search.elixpo), a research-style project on crawlers, rankers, and an LLM-supported native search engine, had been adopted into the pollinations organization and was being used by people I'd only ever seen as GitHub avatars. I closed October 2025-26 ranked the #1 contributor at pollinations, with a Hacktoberfest Super Contributor badge to go with it. None of those numbers felt like the proud part. The proud part was that the projects mattered to people who weren't me.

The second is maintaining my own organization, [Elixpo](https://github.com/elixpo). It started as a place to put my side projects and quietly turned into a small ecosystem of tools other people actually use. It's a reminder that you don't need permission to be a maintainer; you can just decide to be one and start showing up for the work.

The third is becoming the campus organizer for [GDG on Campus, JIS University](https://www.linkedin.com/posts/elixpo_had-a-fabulous-february-with-my-gdg-jis-university-ugcPost-7432876888978771968-67ra). Going from someone who lurked on conference talks during the 2021 lockdown to someone running events at his own university for 250+ registrants is a kind of full-circle that doesn't fully land until you're standing in the room.

And finally, the maintainer invitation at pollinations and the work that came with it during Hacktoberfest. Co-hosting [Kolkata's Hacktoberfest Meetup at JIS University](https://www.linkedin.com/posts/elixpo_hacktoberfest-hacktoberfet-gdg-ugcPost-7388671602709864448-bdwT) with 290+ participants, and running events for pollinations and Elixpo that helped onboard 100+ new contributors, was the part that made me understand the maintainer job isn't really about the code. It's about the room. The proudest version of that month isn't the contributor badge; it's the mental list of first-time contributors who came back the next week and contributed again.

## What working with agentic systems taught me

I work on AI infrastructure, so I'm not going to pretend AI hasn't changed Open Source. It has. I ship faster, new contributors ramp up faster, boilerplate is cheaper. The real concern for maintainers is the asymmetry: AI lowers the cost of _producing_ a PR much faster than it lowers the cost of _reviewing_ one. We're already seeing PRs that look polished on the surface but quietly break invariants the AI didn't know about. The maintainer skill that's going to matter most over the next few years is reading code critically, not generating it. I try to apply that to my own AI-assisted work, too: if I can't explain why a change is correct, the change isn't ready.

We've also been experimenting with using AI to help us close that review-side gap. At pollinations, a co-maintainer and I built a PR review framework that runs CCR against our own custom pollinations model, wired up as a GitHub Action so it kicks in automatically on every pull request. It catches the obvious stuff fast, flags risky changes for human eyes, and has noticeably cut down our review turnaround. The implementation lives under [`.github/workflows`](https://github.com/pollinations/pollinations/tree/main/.github/workflows) in the pollinations repo if you're curious how it's wired up.

The bigger thing I've taken away from a year of working with agentic systems is that they don't replace judgment, they amplify whatever judgment you already had. A maintainer with good taste gets more leverage out of an agent. A maintainer without it ships more bad code, faster. The skill ceiling didn't get lower; the floor got more crowded.

## Final thoughts

I'm still pretty new to all of this. I've been a maintainer for less than a year. I'm 20. There are people in this book who've been doing Open Source longer than I've been alive, and every time I read one of their stories I feel like I've sat in on a quiet apprenticeship I didn't pay tuition for.

If there's anything I've learned that feels worth passing on, it's that nothing about Open Source is as gatekept as it looks from the outside. The people who maintain the projects you depend on are mostly just people with day jobs, families, classes, and a stubborn willingness to keep showing up. You can become one of them by doing exactly that. Find a project you actually use. Open small PRs. Read the codebase like it's worth reading. Be patient with the maintainers, because they're patient with you. Eventually somebody adds you to a team in GitHub and the responsibility shifts and you keep going.

To the maintainers reading this: thank you for the projects, the reviews, the late-night replies on issues, the documentation you wrote at no one's request. To the contributors: thank you for the typo fixes, the bug reports with reproductions, the PRs that turned out to be more work than you expected. And to anyone reading this who hasn't sent their first PR yet, I promise the imposter syndrome doesn't fully go away, but it does get quieter. Send the PR.

---

If anything here resonated, or if you just want to talk Open Source, AI tooling, or community building, I'd love to hear from you.

- Personal Website: [https://elixpo.com](https://elixpo.com)
- LinkedIn: [https://www.linkedin.com/in/elixpo/](https://www.linkedin.com/in/elixpo/)
- GitHub: [https://github.com/Circuit-Overtime](https://github.com/Circuit-Overtime)
- Email: [ayushman@myceli.ai](mailto:ayushman@myceli.ai)

\newpage
