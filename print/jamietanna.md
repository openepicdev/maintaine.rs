# @jamietanna -- Jamie Tanna

> ![](https://github.com/jamietanna.png){ width=64px height=64px }  
> [github.com/jamietanna](https://github.com/jamietanna)  
> [maintaine.rs/jamietanna](https://maintaine.rs/jamietanna)

My name's Jamie Tanna[^255] and I've been contributing to Open Source for >11 years, which extends to before my professional career began.

As with many others, my first foray into Open Source was a few spelling and grammar fixes[^256], but I remember being part of a computer security forum several years prior, where we would share code.

Over the years, I've contributed in various ways to projects - helping answer others' issues on issue trackers, submitting suggestions for bug fixes, implementing features, writing/improving documentation and helping contribute to discussions about the way the project is shaped, but I've also been one of those annoying "any updates?" users, too.

As I started more regularly contributing to Open Source while I was working at a large financial institution, I was incentivised to contribute to projects out-of-hours, instead of going through our fairly gnarly Open Source policy.

This was a bit frustrating as it slowed down my ability to help fix issues that we were blocked by internally, but it still at least meant I was getting the work done. On the flip side, the company missed out on having their corporate email address associated with the changes.

In recent years, I've fortunately worked at companies with a better policy around contributing to projects, but I've also found that I'm a much stronger advocate for myself (and for the company) to allow me to do the Open Source work on my work time, rather than my personal time.

I've enjoyed being in the place in my career and at a company where - if there is a need to raise a bug upstream, or indeed finding the fix to a bug we're facing, or there's functionality we want to contribute, I can go ahead and do that without much pomp and ceremony.

At the end of the day, we all benefit from continuing to work on the commons, companies most of all[^257]!

## Collector of Open Source projects

I have quite a number of projects I've built (with differing levels of support) that I have a page on my website[^258] listing all the projects!

The main ones that folks may know are `oapi-codegen`[^259], the OpenAPI-to-Go code generator, and dependency-management-data[^260], a tool for better understanding your dependency tree.

I've also previously been the primary maintainer for the Jenkins job-dsl-plugin[^261], and on the maintainer team for Wiremock[^262], and I've had contributor access to several projects over the last decade, and I'm also a fairly regular contributor to a number of other projects like Renovate[^263].

Something that may be clear from the projects is that they're in a spread of different ecosystems - there's a lot in Jenkins, Java and Cucumber, or a number in Go, or around the OpenAPI ecosystem, or more recently, in the dependency management and insight space.

These all follow where my "focus" as an engineer has been at a given point in time, some of which I've been continuing to work on after I've stepped away from that ecosystem.

The Open Source project I've been most consistently contributing[^264] to is my personal website and blog[^265], which is also an Open Source project in of itself. It's shared freely to the world, with mostly `Apache-2.0` code snippets, and I truly do see this as another project I continue to invest in, whether writing blog posts as a form of blogumentation[^266], or sharing some lukewarm takes about Git commits[^267].

## Where does the time go?

As a maintainer, I'd say the biggest challenge I have right now as a maintainer is _time_.

As above, you've seen that I have a number of projects - all of which are in various states of maintenance needs - and my blog where I want to actively continue working on, as well as "life stuff".

Of my two "main" projects, `oapi-codegen` demands a fair bit of time, and dependency-management-data is something I'm continuing to build in functionality for.

At time of writing, `oapi-codegen` has 503 open issues, and 173 open Pull Requests. Earlier this year we were up at ~600 issues, and ~150 open PRs, as far as I can remember.

Although I describe myself as co-maintainer of `oapi-codegen`, my co-maintainer (and project creator) is currently super busy and unable to work on the project. This means I'm doing the majority of the work - there's a lot of work to triage, prioritise, debug, add test cases to reproduce and then fix issues, let alone taking on new functionality that could be seen as "it's _just_ a case of merging this PR".

As noted in a post from last May[^268], we indicated that we'd like to try and move to a more sustainable model, taking in sponsorship to try and make the work on the project more consistent.

I'm incredibly fortunate to say that I have several sponsors[^269] who are great, and each paying for 1hr/month for me to work on the project, and my employer, Elastic[^270] gives me 4hr/month to work on the project.

I understand that this _absolutely_ isn't the norm and is really quite privileged to be able to say I not only have some "free time" to work on the project, let alone that some of it is paid! With the appreciation I hold for their sponsorship to pay for a number of hours of work, there is still, unfortunately, not enough time.

If you rely on any of the projects I maintain, I'd love to talk with you about sponsoring me[^271]!

## The art of "doing it right"

The other, very intertwined, difficulty I face as a maintainer is complexity.

As `oapi-codegen` is built on top of OpenAPI[^272], there's a lot of functionality that a user _could_ use in their OpenAPI documentation, which we then need to support in `oapi-codegen` - it's a very powerful specification that allows elegant descriptions of metadata, but then requires tooling to respond to those complex use-cases.

To make matters a little harder, we often need to be led by users with examples of functionality they're using, before we can add support into the project for what they're doing.

When we end up trying to fix these sorts of issues, we also want to support this in a backwards-compatible way, making sure generated code only changes if necessary, otherwise making it an opt-in feature. This adds complexity with more internal feature flags, on top of complex specifications that may be in use.

As a project, we're trying hard to build sustainability in our documentation and our test suite - I recently spent a lot of time rebuilding our documentation, which now means that previously raised contributions (some as old as ~6 years) need to have this documentation retrofitted to them (usually by us, the maintainers) before they can be accepted.

As we're trying to make the project more sustainable - with better documentation and test suite - this does come at the cost of having to slightly slow down to make sure changes are done in the "right" way.

One option is I can already hear folks saying is that we could "use AI to triage those issues" or "use AI to suggest specifications that need to be implemented", but I worry about the accuracy and I'd prefer to have issues taking a bit longer to get to, rather than being solved incorrectly, especially as I'd prefer to personally introduce a bug rather than it being via i.e. an LLM.

## Advice to maintainers

If I had any advice for any new or current maintainers, it would be learn what your boundaries are, and enforce them.

This is a good life lesson, too, but especially with Open Source where we see a lot more entitlement, a lot of the time from large companies.

In Open Source, we're constantly doing free work which the industry benefits from[^273], and as Mike McQuaid puts it, Open Source Maintainers Owe You Nothing[^274].

Understand what this project is _to you_ the maintainer and what you do/do not want to take on as contributions, and then ideally make it clear by using something like a GitHub badge for [unmaintained.tech](https://unmaintained.tech/) or Joseph Hale's PSAs[^275] to indicate maintenance status, or adding information into `CONTRIBUTING.md` about what is/isn't in scope for the project.

Unless you're getting paid as your day job, it's taking up precious free time, and although we love you for doing it, you should only be doing it if you enjoy it. And even if you are getting paid for it, you can't magic up more hours in the day, or necessarily prioritise things differently based on the whims of _one_ of your users.

Secondly, I'd indicate that you should try to be transparent and intentional.

In a post to `oapi-codegen` last year[^276], we made it clear that we appreciate there's a gap in the maintenance we've been doing, and do want to improve it, but can't feasibly without more financial support.

Having this difficult conversation with your users can help set expectations, and I promise you it'll make you feel better.

## Call to action for users

I've got a couple of final things I'd like to leave you, dear reader, with.

The first one is to go forth with empathy, and to remember that your maintainers are _people_. We have lives behind the screen you may not be aware of, other commitments that may mean this project we work on _for free_ and for the good of others isn't the most important thing.

The second is to please go and say something nice to one of the maintainers in your life. I guarantee they may only get 1-2 positive messages all year, or it's usually "Hey, this project is great, thanks! BTW, there's a massive bug ..." and that it'll make their day.

And a final one is to talk to your company about sponsoring Open Source[^277], and see if you can start helping the people doing the very hard work you rely upon.

Let's try and make the human side of Open Source more sustainable.

\newpage


[^255]: https://www.jvt.me
[^256]: https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System/pull/18
[^257]: https://www.jvt.me/posts/2022/10/22/tech-industry-free-labour/
[^258]: https://www.jvt.me/open-source/
[^259]: https://github.com/oapi-codegen/oapi-codegen
[^260]: https://dmd.tanna.dev
[^261]: https://github.com/jenkinsci/job-dsl-plugin/
[^262]: https://github.com/wiremock/wiremock
[^263]: https://docs.renovatebot.com/
[^264]: https://www.jvt.me/archives/
[^265]: https://www.jvt.me
[^266]: https://www.jvt.me/posts/2017/06/25/blogumentation/
[^267]: https://www.jvt.me/posts/2024/07/12/things-know-commits/
[^268]: https://github.com/oapi-codegen/oapi-codegen/discussions/1606
[^269]: https://github.com/oapi-codegen/oapi-codegen#sponsors
[^270]: https://elastic.co
[^271]: https://www.jvt.me/support-me/
[^272]: https://www.openapis.org/
[^273]: https://www.jvt.me/posts/2022/10/22/tech-industry-free-labour/
[^274]: https://mikemcquaid.com/open-source-maintainers-owe-you-nothing/
[^275]: https://github.com/thehale/PSAs
[^276]: https://github.com/oapi-codegen/oapi-codegen/discussions/1606
[^277]: https://humanwhocodes.com/blog/2021/05/talk-to-your-company-sponsoring-open-source/
