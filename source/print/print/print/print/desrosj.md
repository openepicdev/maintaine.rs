# @desrosj -- Jonathan Desrosiers

> ![](https://i0.wp.com/github.com/desrosj.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/desrosj](https://github.com/desrosj)  
> [maintaine.rs/desrosj](https://maintaine.rs/desrosj)

Hello, my name is Jonathan Desrosiers. I started using WordPress to make websites for myself and some freelance clients. This eventually led to a day job building WordPress sites, then attending and speaking at WordCamps. One day I found a bug that was affecting my work and instead of working around it, I submitted a patch. That sparked a broader interest in how the software was built and maintained. I’ve been contributing to Open Source ever since.

I’ve been a contributor to the WordPress project since 2012, a Core committer since 2018, and a maintainer of several components throughout that time. WordPress overlaps with many other Open Source projects, so discovering upstream bugs is quite common. I try to submit fixes for these bugs as much as possible.

This essay is based on a talk[^177] I gave at WordCamp Europe 2025\.

## **The Impact of Open Source**

Software can change lives. Often in unanticipated ways. This is especially true with Open Source software. Open Source can be a creative outlet. It can empower you to transform your career, access jobs you previously couldn’t, find mentorship, feel a sense of belonging, start a business, or help others do the same.

For me, Open Source is about coming together despite our differences to accomplish a shared goal while sharing it with the world. When we tackle problems together, the solutions we build are more resilient, more innovative, and more impactful than anything we could create in silos.

As of June 2025, WordPress powers 61% of all websites using a known CMS (1[^178]). Looking at the entire picture, WordPress powers 43.5% of _all_ websites. Businesses, doctors, banks, governments, individuals, and nonprofits are just some of the stakeholders that rely on the WordPress project to deliver stable, reliable, and effective software across countless use cases.

Maintaining that software and making decisions that affect every user in unique ways is both a burden and a privilege. Sometimes, committing code to WordPress Core is terrifying. But there are frameworks in place to ensure that the best decisions are made.

We should all strive to understand how the software we rely on is maintained and how changes are evaluated.

## **What Is a Core Committer?**

A Core Committer in the WordPress project is a trusted contributor with write access to the canonical WordPress codebase. They’re responsible for keeping the project on track, upholding project’s philosophies, mentoring contributors, and deeply considering the impact of even the smallest change.

In the 22-year history of the project:

- 110 people have committed at least once.
- 89 have committed in the last 10 years.
- 55 have committed in the last 2 years.
- 23 maintain a once per month commit average over that same two year period.

There are many unique ways that an idea can make its way into the WordPress software that’s shipped to the world. This essay focuses only on committing to the Subversion (SVN) repository where the WordPress software lives. However, the principles I detail should be considered by all maintainers even those not operating within the WordPress project.

It’s also important to note: **committers are not always the same as component maintainers**. As of June 2025, the code base is divided up into 43 components and 20 subcomponents. There are 65 unique community members who actively maintain them. Of those contributors, 37 (\~57%) have been given commit access.

## **How Changes Are Made**

There are three main types of changes:

1. **Bug fixes**
2. **Enhancements or feature requests**
3. **Tasks**

Most changes start as a ticket in our bug tracker, Trac. Tickets begin by outlining a specific problem, not necessarily suggesting a solution. Discussion happens in comments, Slack, or elsewhere. Solutions are proposed through patches or linked GitHub pull requests.

Once a consensus is reached and testing is completed, a core committer reviews and, if appropriate, commits the change.

## **Other Change Pathways**

Not all changes begin with Trac. Some start with blog posts or community initiatives. For example:

- The **Performance Team** maintains canonical plugins to address performance issues or add new features.
- The addition of **WebP support** and the **Speculation Rules API** are examples of enhancements that started outside the core release process and later merged in.

The **block editor** (Gutenberg) uses a unique workflow. It acts as a long-running feature plugin, releasing updates every two weeks. These updates are integrated into core by updating the dependency manifest in the canonical codebase.

There’s no one-size-fits-all process. Good ideas can come from anywhere—first-time contributors or long-time veterans alike.

## **Evaluating Ideas**

Ideas should always be judged on their merits—not who proposed them. Only committers can merge code, but they are often the final eyes in a longer process.

Community feedback loops with users, developers, plugin and theme authors are essential. Consensus building, testing, documentation, and iteration drive the majority of change.

Showing up matters. But with presence comes responsibility: be prepared, listen actively, and be thoughtful in your proposals.

Presence grants a voice, not a vote. Commit access is merit-based and earned through long-term trust, consistent high-quality contributions, and respect from peers.

Still, we must remember: **not everyone can show up equally**. Time zones, language barriers, responsibilities, and financial realities vary widely. We must create multiple avenues for participation.

## **The Role of Consensus**

Building consensus is a core part of a committer’s job. Perfect consensus is rare—and when it does occur, it may even be suspicious. For complex changes, consensus must be explicit. For simple ones, it may be implicit.

For example, a committer might fix a two-character bug on their own. By doing so, they are assuming consensus—unless someone later raises concerns.

Disagreement is healthy and shows engagement. You can object to a change but still support the consensus and move forward. Rehashing endlessly causes burnout. Disagree and commit.

## **What Makes a Good Change?**

Creating a patch is easy. Understanding the root problem and articulating strong rationale is the hard part.

Good changes are:

- Well-scoped and practical
- Based on real user needs
- Maintainable and testable
- In line with project philosophy
- Justified with clear rationale and evidence
- Backward compatible (adhering to the 80/20 rule)

Avoid novelty for novelty’s sake. Ask _why_, not _why not_.

## **A Real Example: XML Sitemaps in WordPress 5.5**

- Consistent de facto standard supported by major search engines
- High demand: 4 of the top 15 plugins already provided this
- Simple default implementation with opt-out capability
- No new UI; integrates with existing search visibility settings
- Customizable via plugins and hooks

The feature exemplified:

- Democratizing publishing
- Shipping defaults that “just work”
- Avoiding feature overload for users

## **Sometimes the Best Decision Is to Say No**

Not every proposal fits the long-term goals of the project. Reasons might include:

- Poor rationale
- Lack of clarity
- Stability concerns
- High opportunity cost

A “no” today doesn't mean “no forever.” We should communicate clearly _why_ something is rejected and what would need to change to revisit it.

Sometimes a proposal is better off as a **feature plugin**, allowing faster iteration and more flexibility.

## **The Cost of Inaction**

We can’t respond to everything. But silence can lead to confusion, lost momentum, or missed opportunities—like readiness for a new PHP version.

Disciplined timelines and regular release cycles help reduce pressure and improve quality. They make it easier to say “not yet” instead of “never.”

When people pour time into a proposal, they deserve transparency—even if the answer is no. Good maintainers explain what’s weak and what’s promising. And they remain open to changing their minds when the rationale improves.

## **Evaluating Cost and Risk**

Cost isn’t just monetary. It includes:

- Maintenance burde
- User experience complexity
- Risk of regressions
- Long-term sustainability
- Opportunity cost (what are we _not_ doing instead?)

Even tiny code changes carry non-zero risk. WordPress’ strict commitment to **backward compatibility** is a pact with its users—and a powerful tool for risk mitigation.

## **Testing and Early Feedback**

Testing early helps avoid last-minute surprises. WordPress.org runs trunk; you can too. Test your plugins and themes with nightly builds. Catch issues before release day.

There’s also an unofficial game: “Will it break Matt’s site?” Discovering obscure edge cases is part of the fun—and vital to ensuring wide compatibility.

## **Stewardship and Trust**

When you commit code, you take on responsibility for it. You should be able to stand behind your changes and accept accountability.

Delegating work, even if you could do it faster, builds trust and encourages growth. Recognize others’ capabilities and empower them.

We are all stewards of this community. These philosophies helped WordPress grow to power 43% of the web.

None of us are perfect. But if we stay focused on users’ needs, follow clear decision-making frameworks, and uphold the core freedoms of the GPL, we can continue to democratize publishing—together.

## **Final Advices**

Consistency and approachability go a long way. I try to make space for new contributors by reviewing patches, answering questions, and encouraging contributions of all sizes. The key is to recognize that people contribute at different levels and with different motivations. But every shape and size of contribution is important. You can never know how much impact a code review or comment can have, so always give the best of what you have to offer.

Finally, don't bite off more than you can chew and start slowly. It's easy to take on too much, get burnt out, or make mistakes. At the same time, don't be afraid to ship something early and often. Shipping early can help to show progress and gather feedback more. But try not to sacrifice consistency, clarity, quality, and reliability.

## **Contact Information**

- [https://jonathandesrosiers.com/](https://jonathandesrosiers.com/)
- [https://profiles.wordpress.org/desrosj/](https://profiles.wordpress.org/desrosj/)

\newpage


[^177]: https://jonathandesrosiers.com/2025/06/how-a-core-committer-thinks-making-decisions-for-millions/
[^178]: https://w3techs.com/technologies/overview/content_management
