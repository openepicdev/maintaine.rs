# @desrosj -- Jonathan Desrosiers

> ![](https://github.com/desrosj.png){ width=64px height=64px }  
> [github.com/desrosj](https://github.com/desrosj)  
> [maintaine.rs/desrosj](https://maintaine.rs/desrosj)

Hello, my name is Jonathan Desrosiers. I’ve been a credited contributor to the WordPress project since 2013, a Core Committer since 2018, and a maintainer of several components throughout that time.

I first encountered Open Source in college, using WordPress to build some websites for myself, school projects, and some freelance clients. That experience eventually led to a day job building WordPress sites, and soon after, I began attending and speaking at WordCamps.

One day, I found a bug that was affecting my work. Instead of working around it, I submitted a patch. That sparked a deeper interest in how the software was built and maintained. I’ve been contributing to Open Source ever since.

Because WordPress overlaps with many other Open Source projects, it’s common to discover upstream problems. This frequently leads to submitting bug reports or patches to other code bases. Even though each project has its own goals, there's a shared sense of collaboration and stewardship across the ecosystem that’s both gratifying and contagious.

This essay is based on a talk I gave at WordCamp Europe 2025[^178] titled _“How a Core Committer Thinks: Making Decisions for Millions,”_ which was heavily influenced by the works of Havoc Pennington[^179] and Karl Fogel[^180]. It also includes some thoughts from a blog post I published[^181] reflecting on the keynote session at the same event.

---

Software changes lives. Often in unanticipated ways.

This is especially true with Open Source software. Open Source can be a creative outlet. It can empower you to transform your career, access jobs you previously couldn’t, find mentorship, feel a sense of belonging, start a business, or help others do the same.

Open Source is about coming together despite our differences to accomplish a shared goal and publishing it for the benefit of the world. When we tackle problems together, the solutions we build are more resilient, more innovative, and more impactful than anything we could create in silos.

Maintaining Open Source software and making decisions that affect every user in unique ways is both a burden and a privilege. Just the thought of this scale can sometimes make committing code terrifying, even to seasoned maintainers. But having decision-making frameworks and foundational philosophies in place help ensure that we make the best choices we can for our users.

We should all strive to understand how the software we rely on in our personal and professional lives approach change and manage risk while making decisions. Here's how the WordPress core philosophies[^182] are used to guide maintainers when making decisions.

## Maintainers in the WordPress Project

As of June 2025, WordPress powers 43.5% of _all_ websites and 61% of websites using a known CMS.<sup>[1[^183]]</sup> Businesses, doctors, banks, governments, individuals, and nonprofits are just a few of the many stakeholders that rely on the project’s maintainers to deliver stable, reliable, and effective software across countless use cases.

In the WordPress project, a Core Committer is a trusted contributor that has been granted write access to the canonical WordPress code base. In addition to reviewing and authoring changes to the code base, they are also responsible for upholding the project’s philosophies, mentoring contributors, keeping the project on track, and deeply considering the impact of even the smallest change.

In the 22-year history of the project:

- 110 people have committed at least once
- 89 have committed in the last 10 years
- 55 have committed in the last 2 years
- 23 have maintained a once per month commit average over that same two-year period

There is also a second type of maintainer called a component maintainer. Component maintainers do not always have write access, but good ones exhibit many of the same qualities as committers while focusing on their small chunk of the software. Because of the overlapping responsibilities, it’s common for committers to also serve as component maintainers, and for component maintainers to eventually be granted committer status.

The code base is currently divided into 43 components and 20 sub-components with 65 unique contributors actively maintaining them. Of those contributors, 37 (approximately 57%) have been granted commit access. Every Open Source community should strive to achieve a healthy balance of new, intermediate, expert, and even emeritus contributors to ensure long-term stability. But that’s a topic to dive into another time!

## The Pathways of Change

There are many unique ways a change can find its way into the WordPress code that is shipped to the world. Like most software, change usually takes the form of a bug report, feature request, enhancement, or task. But while a ticket is the most common starting point, not all ideas originate there. Some begin with a “what if” on a personal blog, an issue in the user support forums, or even a working group at a Contributor Day[^184] event. Let’s explore three common pathways a change can move through the project before diving into the principles maintainers use to make decisions.

### Tickets in Trac

Most ideas start as a ticket in the project’s bug tracking software, Trac[^185]. Though antiquated in some ways, I’m fond of Trac because you must first outline and describe a specific problem in order to create a ticket. This step is sometimes skipped when solving problems in software (both intentionally and not), and can result in bad decisions or unforeseen consequences.

After the ticket is created, discussion happens in the comments or on the WordPress Slack instance[^186]. Once contributors feel that they have enough information, patches are created and attached to the ticket or submitted as pull requests to the wordpress-develop repository on GitHub[^187]. After a consensus is reached on a solution and adequate testing has been performed, a Core Committer gives a final review before committing (or rejecting) the proposed change.

### Canonical Feature Plugins

While tickets on Trac are the most prevalent path, some are built out by the community in the form of a plugin before a proposal to merge the functionality into the code base is published.

A great example of this practice today can be found with the Performance Team. They maintain several feature plugins that implement new and emerging ways of improving the performance of WordPress websites. While the desired end goal is to one day include these features in the software, they can also easily continue as canonical plugins should they not be a good fit at any given time.

In the most recent major release (6.8 “Cecil”[^188]), one such feature plugin was included after over 7 months of iterating, testing, and feedback: support for the new Speculation Rules API[^189]. Once the contributors focusing on this feature plugin were happy with the implementation, a Trac ticket[^190] was opened to further discuss the problem being addressed and review the code before a committer finally authored the changeset[^191].

### The Block Editor

The block editor (also known as the Gutenberg project[^192]) uses yet another unique workflow. It is maintained as a long-running feature plugin[^193] where new functionality is added and refined. Because the block editor is primarily built with JavaScript (with some TypeScript sprinkled in), the related code is published to over 100 different npm packages. This happens every two weeks when a new version of the plugin is released to the 300,000+ sites that currently have it activated. Before each major release[^194] of WordPress, changes are merged into the canonical code base by updating the dependency manifest.

## Evaluating Ideas

Having predictable workflows and expectations can be very helpful, but there is never a one-size-fits-all process. Good ideas can originate from anywhere at any time with no minimum level of experience required. As maintainers, we must always keep a sharp eye out. Even if our communities are discoverable, transparent, and approachable, ideas do not always land on our doorstep. Be willing to meet them where they are.

While process requirements can be a bit fluid, the decision-making frameworks should be more rigid. These frameworks should always focus on judging ideas based on their merit, never the identities of those who propose them. We must seek as many viewpoints as possible before making decisions.

## Change is Community Driven

While only committers can merge code, they are oftentimes just a final set of eyes in a longer process. Feedback loops with users, developers, and plugin and theme authors are essential. These feedback loops when combined with direction from leadership, additional testing, documentation, iteration, and some external influence (new industry standards, versions of PHP, MySQL, etc.) drive the majority of changes in the WordPress software.

### The Value of Presence

There’s a premise in Open Source that underscores the value and importance of active engagement. Decisions are made by those who show up.

By participating in discussions, contributing code, submitting bug reports or feature requests, or testing proposed changes, any individual can influence the direction of an Open Source project. By showing up, you ensure that your voice will be heard. But be aware, with presence comes responsibility. Showing up means being prepared, doing research, actively listening, and being thoughtful in your communication.

In my experience, this premise largely holds true, but there are some practical limits to this. For example, your presence grants you a voice, not necessarily a vote. As opposed to decisions being strictly made by those who show up (a do-ocracy), commit access in WordPress is meritocratic, and granted only after demonstrating a consistent track record of valuable and high-quality contributions, building long-term trust through engagement, and earning the respect of your peers.

### Equal Participation

The health of a project improves when decisions are inclusive and transparent. The quality of the outcome is higher when more unique voices are heard. But we must always remember that not everyone can “show up” equally (if at all). When it comes to participating, time zones, language and cultural barriers, personal and family responsibilities, disabilities, and financial circumstances can all affect a person’s ability to share their perspective. There should always be multiple ways to “show up” with reasonable time frames.

No one should be marginalized by a lack of opportunity.

### The Role of Consensus

One of the most important duties of a Core committer is collecting feedback to determine the best solution for the largest number of people. No matter how good someone is at consensus building, it will almost never be perfect. Perfect is so rare that you should be suspicious when it occurs. Consider whether certain perspectives are missing or if the right questions have been asked.

> “Consensus merely means an agreement that everyone is willing to live with” <sup>[2[^195]]</sup>.

In his writings, Karl Fogel explains that consensus can be either explicit or implicit. When seeking explicit consensus, always be clear what is being proposed. When someone objects, continue the discussion until the time is right to propose a new consensus. An example of implicit consensus is when a committer finds and fixes a small bug on their own. The act of committing is assuming consensus. If anyone objects, then a discussion can be had to reach a new consensus. If one can’t be reached, version control is a wonderful tool that allows for easily reverting a change.

### Disagree and Commit

When discussing changes in Open Source, disagreement is healthy and expected. It shows that contributors are engaged and care about the software. But endlessly rehashing the same discussions is tiresome and frustrating, and often leads to burnout.

One of the most important qualities in Open Source maintainers is the ability to disagree and commit. Even when someone disagrees with a decision, they should be able to clearly state their reasoning before publicly supporting the consensus to move the project forward over their own personal preferences.

Once a decision is made, moving forward together is essential.

## Quality Logic

Hopefully, anyone can show up and create a patch for your Open Source project. If they can't, there's work to be done to improve the contributor experience. That aside, creating patches is the easy part, even when it changes thousands of lines of code.

Producing strong rationale for a change is much harder. It requires a complete understanding of what the root problem actually is, an exploration of alternative solutions in depth, and recognition of motivations. If you propose a solution before the problem is fully understood, you're doing everyone a disservice.

The best ideas are rooted in real user problems, well-scoped and practical, maintainable and testable, and compatible with the project’s philosophies. It’s backed with evidence, context, and potential impact while avoiding speculation. Rationale should always go beyond personal desire and novelty, and demonstrate how the change will benefit the majority of your users.

> The guiding principle is simple: ask "why," rather than "why not" <sup>[3[^196]]</sup>.

## A Case Study: XML Sitemaps

In WordPress 5.5 “Eckstine,”[^197] a new API was added for generating an XML sitemap for every site. Let’s go through the process of evaluating the rationale presented when a proposal was made to include the feature.

- Sitemaps use a consistent, de facto standard supported by all major search engines. This speaks to the maintainability and predictability of the feature. There is a widely adapted standard shaping the expectations and requirements while limiting the scope.
- 4 out of the top 15 plugins on the WordPress.org plugin repository[^198] at the time shipped their own implementation of an XML sitemap. This demonstrated a widespread demand for the feature.
- Every site should have equal opportunity to be crawled by search engines and discovered by users. This strongly aligns with the project’s mission to democratize publishing[^199].

In addition to evaluating the idea, the implementation details should also be scrutinized.

- The implementation used sane yet comprehensive defaults. All publicly visible registered post types (e.g. posts, pages) and taxonomies (e.g. categories, tags), the site’s home page, etc.
- A reference to the sitemap file is automatically included in the `robots.txt` file.
- No new user facing interfaces were introduced.
- Site owners can customize their sitemap to their liking through the use of plugins or custom code.
- Sitemaps are enabled by default for all sites.

Let’s evaluate this feature by applying the project’s foundational philosophies[^200].

### Out of the box

“Great software should work with little configuration and setup. WordPress is designed to get you up and running and fully functional in no longer than five minutes.” In this case, the feature will “just work” without any action required by the user.

### Design for the majority

“Many end users of WordPress are non-technically minded.” The majority of people using the software don’t know or care what the XML schema for the Sitemap protocol is. These are the users we design the software for. They are the ones spending the most time using it. Applied here, all technical aspects of the feature are just handled on behalf of the user.

### Decisions, not options

“Every time you give a user an option, you are asking them to make a decision. When a user doesn’t care or understand the option this ultimately leads to frustration…Ultimately these choices end up being technical ones, choices that the average end user has no interest in. It’s our duty as developers to make smart design decisions and avoid putting the weight of technical choices on our end users.”

The Sitemap feature introduced no new options or user controls. The only way to alter the behavior of the feature is to change a pre-existing setting in the dashboard. This setting presents the site owner with one decision: should this site be visible to search engines? The code will take appropriate action to enable or disable Sitemaps behind the scenes based on this decision.

### Clean, lean, and mean/Striving for simplicity

“The core of WordPress will always provide a solid array of basic features. It’s designed to be lean and fast and will always stay that way…If the next version of WordPress comes with a feature that the majority of users immediately want to turn off, or think they’ll never use, then we’ve blown it.” In the project, this is also referred to as the 80% principle.

The implementation included a lean yet extensible foundation allowing plugins to easily adjust what the Sitemap includes. Despite this, “we’re never done with simplicity.”

### The vocal minority

“The number of people who create content on the internet represents approximately 1% (or less) of the people actually viewing that content.” In internet culture, this is known as the 1% rule. While it’s “really important to listen and respond to those who post feedback and voice their opinions on forums, they only represent a tiny fraction of our end users.”

We always need to consider and respect the massive and mostly silent user base. The fact that 4 of the top 15 plugins were shipping a Sitemap implementation demonstrated the vote of the silent majority while also clearly confirming that the feature met the 80% principle.

As a community, we should contemplate how to better engage with all users who are not yet vocal. After all, “each interaction with a user is an opportunity to get a new participant” <sup>[4[^201]]</sup>.

### Democratize Publishing

Supporting democratic publishing for all means not limiting the reach of someone’s voice because they:

- Don’t understand what a Sitemap is.
- What to include in one.
- How to best accomplish this technically.
- Don’t have the means to hire someone who does.

Enabling the feature by default for all WordPress sites strongly aligns with the mission to democratize publishing.

## Additional Considerations

The case study above shows how the feature strongly aligned with 6 of the 8 project philosophies. But what about the other 2? And what else should be considered when making decisions about changes to software?

### “No” doesn't mean Never

Oftentimes, doing nothing is the right thing. Not all proposals deserve implementation. Perhaps there’s poor rationale, a lack of clarity, or no compelling use case. Even when changes seem good, not everything will fit into the current long-term goals of the project. In software, stability is also a feature. And backwards compatibility is sacred.

> “In open source no is temporary, and yes is forever” <sup>[5[^202]]</sup>.

There can also be benefits to _not_ being merged into Core. If a feature is built out using the plugin model, it can simply live on as a community maintained canonical plugin. A plugin will not be restricted by the WordPress release cycle (usually 3 times per year). This extends feedback loops and can prevent faster iteration in the early days of a feature. And while backwards compatibility is still important, it’s not applied as a steadfast policy like when code ships in WordPress itself.

But beware of the costs associated with inaction. While inaction does not necessarily equate to inattention, it can contribute to a lack of clarity or risk losing momentum. Time-sensitive windows of opportunity can also be missed, such as supporting an upcoming version of PHP on release day. And postponing necessary fixes frequently makes problems more difficult to resolve in the future.

### Deadlines are not arbitrary

“Deadlines are not arbitrary, they’re a promise we make to ourselves and our users that helps us rein in the endless possibilities of things that could be a part of every release.“

Unless a project is retired, abandoned, or archived, the need to continuously make decisions will always be present. But the reality is that we have to draw a line somewhere at some point. In software, drawing the line usually comes in the form of a planned release cycle and code freezes. “Deadlines are not arbitrary” is another philosophy of the WordPress project that helps contributors to remain practical and focused.

One advantage of being disciplined with schedules and timelines is that it can help reduce the impact of saying “no.” Saying no is easier when timelines are clearly communicated and strictly enforced. When cycles are regular and predictable, the pressure to merge something just because is reduced. There will be another opportunity soon. “Never” becomes “not yet.”

Good communication skills are essential for Open Source maintainers. When contributors pour time and effort into a proposal or patch, they deserve transparency. This is especially important when the answer is “no.” What aspects of the change look reasonable and acceptable? Where is the rationale unclear or weak? When should they expect a window for reconsideration?

### Changing Our Minds

> “In the presence of good rationale, maintainers should be willing to change their mind often” <sup>[3[^203]]</sup>.

The best signal that an idea is ready to be reconsidered is the presence of new, clarified, or strengthened rationale. Maintainers should always be willing to change their minds as often as necessary. But they should be confident enough in their conclusions and how they were reached to stand by them under scrutiny. This concept is also referred to as “strong opinions loosely held.”

### Evaluating Cost and Risk

The most important part of any decision-making framework is evaluating cost and risk. Cost is not just monetary. What is the cost to maintain a given change? What complexities and friction does a change introduce to users? What are the risks for regressions? What are the impacts on extenders? Cost and risk can also be unknown or realized only in the future.

> “All code is presumed harmful, because it will have bugs and maintenance costs, and introduce behaviors that will interact with other features” <sup>[3[^204]]</sup>.

Even when one character or line is changed, there is still a non-zero amount of risk. Remember, stability is also a feature, and backwards compatibility is a sacred pact with users that has helped WordPress grow significantly over the last 22 years.

### Some Benefits of Backwards Compatibility

In many cases, the project’s commitment to backwards compatibility is a sharp tool in the toolbox for limiting the risk of breaking sites.

- There’s a safe baseline to evaluate against. “Will this break something that worked before?”
- It discourages reckless refactoring.
- Small, incremental changes are safer, encouraged, and usually preferred
- When plugins and themes depend on past behavior, regressions can be easier to catch early due to a wide range of real-world usage.

Backwards compatibility can also help limit downstream costs such as fewer support tickets, less documentation churn, and a lower level of developer frustration.

### Opportunity Cost

Time and resources are finite. Especially in Open Source projects.

Every feature merged or bug fixed is a vote against another that could have taken its place. The time to review, test, document, and support one change subracts time and resources from another somewhere else.

In some situations, a “no” can be given due to an unreasonably high opportunity cost. An example of this can be seen in the WordPress project leading up to the initial release of the new block editor in version 5.0 “Bebo.”[^205] It was important that as many contributors as possible were focused on the objective at hand. Many changes received a “no” answer in large part because of the amount of resources it drew away from the Gutenberg project.

### Maintainers Are the Code They Commit

> “It's easy to write a patch. It's hard to maintain a software project over the long term” <sup>[3[^206]]</sup>.

When a change is made to a code base, the committer making that change is taking on a lot of extra responsibility. In some ways, they now own that change and any resulting test failures, bugs, features built on top of the change, or even security issues that may follow. They must be willing to stand behind the changes they make until new rationale is presented.

The code you commit is an extension of you.

## Growing Your Community

Growing an Open Source project is not the focus of this essay, but expanding the pool of available contributors should be in the back of your mind with every action we take. Though unique challenges come with growth, a growing project means more resources available to squash bugs and build out features. After all, “given enough eyeballs, all bugs are shallow” <sup>[6[^207]]</sup>.

Maintainers play a critical role in community growth by conducting themselves in ways that embrace other contributors. Lead by example in everything you do. Be consistent and approachable. Make space for new contributors by reviewing their patches, answering questions, and encouraging contributions of all sizes. Recognize that everyone participates at different levels and with different motivations. It may not be immediately apparent how, but every size and shape of contribution is important in some way.

Consider a simple bug ticket with a clear solution. As a maintainer with deep knowledge, you could likely solve this better and faster than a new contributor. But delegating the task to someone else would be more constructive long-term in most cases. The act signals trust, helps build confidence, and strengthens the community dynamics. Other contributors will notice this and be more likely to volunteer or share their experience with colleagues. <sup>[7[^208]]</sup>

A simple code review or “great job” can be the difference between a one-time contributor and a future maintainer. You never know what someone needs to hear, so be generous with feedback.

## The Meaning in Our Work

If you’ve made it this far, you likely care deeply about Open Source software (and if not, you should). Few ideas have reshaped the modern world as profoundly as Open Source. You may not know it, but Open Source is everywhere you look. Routers, refrigerators, trains, cars, rockets<sup>[8[^209]]</sup>, stock exchanges<sup>[9[^210]]</sup>, and even nuclear research<sup>[10[^211]]</sup>.

When you’ve been trying to reproduce a bug with specific and obscure criteria for over an hour, it’s easy to lose sight of the meaning in our work as maintainers. But don’t ever forget that your work is important and matters. The “why” will not always be obvious.

The incredible stories of how Open Source is changing the world often go untold. The people writing those stories are busy doing the work, fundraising, caring for others, or simply trying to get by. If you are one of those stories,take the time to share it! Tell a maintainer how their work has impacted and empowered you. If you cross paths with a maintainer of software you rely on and they’re looking for sponsorship, support them if you have the means. I promise, they will appreciate it.

## Reflecting on Our Principles

We are all stewards of the projects we maintain, championing the guiding principles used to make decisions. No one project, maintainer, or contributor is perfect. Philosophies will be interpreted in different ways at different times, even by the same person. As maintainers, we should reflect on the decision-making frameworks we use.

Are they clearly defined and transparent? Are we following them to the best of our ability? How can our time and effort have a greater impact? Are we upholding the four core freedoms of the GPL[^212]? Are we focused on the needs of our long term goals, and the needs of our users?

The ideals I’ve described above helped WordPress grow to power over 43% of the web. For more than two decades, thousands of contributors have used the project’s philosophies to rally behind one shared mission: to democratize publishing.

These principles may not map perfectly to your project or community, and that’s okay. Every open source project has its own context, its own challenges, and its own mission. But one truth holds across all of them: every line matters, because software changes lives.

## **Contact Information**

- [https://jonathandesrosiers.com/](https://jonathandesrosiers.com/)
- [https://profiles.wordpress.org/desrosj/](https://profiles.wordpress.org/desrosj/)

## Citations

<sup>1</sup> "Usage Statistics and Market Share of Content Management Systems," _W3Techs – Web Technology Surveys_, accessed June 15, 2025, [https://w3techs.com/technologies/overview/content_management](https://w3techs.com/technologies/overview/content_management).

<sup>2</sup> Karl Fogel. _Producing Open Source Software_, Chapter 4. [https://producingoss.com/en/](https://producingoss.com/en/)

<sup>3</sup> Havoc Pennington. “Free Software UI.” [https://ometer.com/features.html](https://ometer.com/features.html)

<sup>4</sup> Karl Fogel. _Producing Open Source Software_, Chapter 8: Treat Every User as a Potential Participant. [https://producingoss.com/en/](https://producingoss.com/en/)

<sup>5</sup> Aaron Jorbin. _Five lessons from Eight Years as a WordPress Core Committer_ [https://aaron.jorb.in/five-lessons-from-eight-years-as-a-wordpress-core-committer/](https://aaron.jorb.in/five-lessons-from-eight-years-as-a-wordpress-core-committer/)

<sup>6</sup> Eric S. Raymond. “The Cathedral and the Bazaar,” Section 4: Release Early, Release Often. [http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html)

<sup>7</sup> Karl Fogel. _Producing Open Source Software_. Chapter 8: Delegation. [https://producingoss.com/en/delegation.html](https://producingoss.com/en/delegation.html)

<sup>8</sup> Vaughan-Nichols, Steven J. _From Earth to Orbit with Linux and SpaceX._ ZDNet, June 2, 2020. [https://www.zdnet.com/article/from-earth-to-orbit-with-linux-and-spacex/](https://www.zdnet.com/article/from-earth-to-orbit-with-linux-and-spacex/)

<sup>9</sup> _Red Hat to Ring the NYSE Opening Bell in Celebration of 20 Years of Open Source Leadership._ Red Hat, June 26, 2013. [https://www.redhat.com/en/about/press-releases/nyse-0](https://www.redhat.com/en/about/press-releases/nyse-0)

<sup>10</sup> Bahyl, Vladimir, Benjamin Chardi, Jan van Eldik, Ulrich Fuchs, Thorsten Kleinwort, Martin Murth, and Tim Smith. _Installing, Running and Maintaining Large Linux Clusters at CERN._ arXiv preprint cs/0306058, June 2003. [https://arxiv.org/abs/cs/0306058](https://arxiv.org/abs/cs/0306058)

## Further Reading

WordPress Project. “Philosophy.” _wordpress.org_. Accessed June 15, 2025. [https://wordpress.org/about/philosophy/](https://wordpress.org/about/philosophy/)

WordPress Project. _WordPress Core Handbook – Version Numbering._ WordPress.org. Accessed June 15, 2025. [https://make.wordpress.org/core/handbook/about/release-cycle/version-numbering/](https://make.wordpress.org/core/handbook/about/release-cycle/version-numbering/)

Jonathan Desrosiers. “How a Core Committer Thinks: Making Decisions for Millions.” _[jonathandesrosiers.com](http://jonathandesrosiers.com)_, June 2025 [https://jonathandesrosiers.com/2025/06/how-a-core-committer-thinks-making-decisions-for-millions/](https://jonathandesrosiers.com/2025/06/how-a-core-committer-thinks-making-decisions-for-millions/?utm_source=maintaine.rs&utm_medium=essay)

Jonathan Desrosiers. “The Impact of Open Source Work.” _[jonathandesrosiers.com](http://jonathandesrosiers.com)_, June 2025 [https://jonathandesrosiers.com/2025/06/the-impact-of-open-source-work/](https://jonathandesrosiers.com/2025/06/the-impact-of-open-source-work/?utm_source=maintaine.rs&utm_medium=essay)

\newpage


[^178]: https://jonathandesrosiers.com/2025/06/how-a-core-committer-thinks-making-decisions-for-millions/?utm_source=maintaine.rs&utm_medium=essay
[^179]: https://ometer.com/
[^180]: https://www.red-bean.com/kfogel/
[^181]: https://jonathandesrosiers.com/2025/06/the-impact-of-open-source-work/?utm_source=maintaine.rs&utm_medium=essay
[^182]: https://wordpress.org/about/philosophy/
[^183]: https://w3techs.com/technologies/overview/content_management
[^184]: https://make.wordpress.org/community/handbook/contributor-day/contributor-days/
[^185]: https://core.trac.wordpress.org/
[^186]: https://make.wordpress.org/chat/
[^187]: https://github.com/wordpress/wordpress-develop
[^188]: https://wordpress.org/news/2025/04/cecil/
[^189]: https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API
[^190]: https://core.trac.wordpress.org/ticket/62503
[^191]: https://core.trac.wordpress.org/changeset/59837
[^192]: https://ma.tt/2017/08/we-called-it-gutenberg-for-a-reason/
[^193]: https://wordpress.org/plugins/gutenberg/
[^194]: https://make.wordpress.org/core/handbook/about/release-cycle/version-numbering/
[^195]: https://producingoss.com/
[^196]: https://ometer.com/features.html
[^197]: https://wordpress.org/news/2020/08/eckstine/
[^198]: https://wordpress.org/plugins/
[^199]: https://wordpress.org/about/
[^200]: https://wordpress.org/about/philosophy/
[^201]: https://producingoss.com/
[^202]: https://aaron.jorb.in/five-lessons-from-eight-years-as-a-wordpress-core-committer/
[^203]: https://ometer.com/features.html
[^204]: https://ometer.com/features.html
[^205]: https://wordpress.org/news/2018/12/bebo/
[^206]: https://ometer.com/features.html
[^207]: http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html
[^208]: https://producingoss.com/en/producingoss.html#delegation
[^209]: https://www.zdnet.com/article/from-earth-to-orbit-with-linux-and-spacex/
[^210]: https://www.redhat.com/en/about/press-releases/nyse-0
[^211]: https://arxiv.org/abs/cs/0306058
[^212]: https://www.gnu.org/licenses/quick-guide-gplv3.html#the-foundations-of-the-gpl
