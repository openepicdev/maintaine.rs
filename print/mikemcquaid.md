# @mikemcquaid -- Mike McQuaid

> ![](https://github.com/mikemcquaid.png){ width=64px height=64px }  
> [github.com/mikemcquaid](https://github.com/mikemcquaid)  
> [maintaine.rs/mikemcquaid](https://maintaine.rs/mikemcquaid)

Hi, I'm Mike McQuaid, the Project Leader for Homebrew and CTPO of Workbrew.

I've worked on Open Source software in some form for 20 years.
I got started in a fairly traditional way, using desktop Linux in university in the early 2000s.
Through this I ended up helping people out in IRC channels, submitting bugs and then patches on bug trackers and modifying existing software for my own use.

After a previous failed attempt, my big jump into Open Source came through my work on Google Summer of Code for KDE in 2007.
I stayed involved after this as a KDE contributor for a few years until I moved primarily to macOS.
Shortly after this in 2009, I started contributing to and then maintaining Homebrew, the macOS (and now Linux) Open Source package manager.
My proudest non-Homebrew work is a single, random commit to the Linux kernel under my old name ("Mike Arthur") in 2006.
Most of my Open Source work has been in the Homebrew ecosystem for the last 10 years but I've dabbled with various other projects.

## Homebrew

I was the third maintainer involved in Homebrew, after Max (the creator) and Adam (who I joined).
Since Max stepped down, I've been in an informal leadership role and as the elected "Project Leader" since 2019.

I've spent a lot of work on Homebrew not not just the engineering aspects but also trying to make the project more sustainable.
This has included:

- working on a "contributor funnel" from user to contributor to maintainer
- figuring out how best to ask people for money to support the project
- fundraising for our initial CI hardware and building partners with companies like MacStadium so we can afford a better CI system
- general fundraising and finding a fiscal host for the project (Open Source Collective, previous Open Collective Foundation and Software Freedom Conservancy)
- creating, encouraging and improving automation to scale ~30 maintainers to millions of users
- building a community of maintainers, many of whom meet up in person once a year at Homebrew's AGM
- encouraging a culture of maintainer support, boundaries and intolerance to bad community behaviour
- defining and reducing the support footprint so we're able to handle millions of users

## Challenges

The hardest part of all this has been (and likely will continue to be) helping maintainers (including myself) to not burn out while keeping users happy.
Too many Open Source users are overly entitled and think a bad bug is an excuse to be rude or demand a quick fix.
Sometimes, things can get darker still with things bleeding into personal abuse and harassment.
I once had someone say they were going to turn up and harass me at a conference talk I was giving.
I'm lucky enough to not be threatened by stuff like this but: it's completely unacceptable behaviour in our community and we should be more aggressive in shutting it down.

## Contributors

Contributors have been a huge part of Homebrew's success.
Our contributor to maintainer ratio is >100:1.
We've achieved some of this with automation and some of it just trying to make it as easy as possible to contribute and get feedback without needing a human to help.
Most of our contributors are great.
If you want to be a great contributor, please:

- don't argue with maintainers, assume they know better about the software they are maintaining (until you're also a maintainer)
- try to address your code review comments in a timely manner
- don't open PRs you aren't willing to finish
- don't expect people to tell you exactly how to implement something; there's a point at which it'll just be quicker for the maintainer to do it
- feel free to use AI tools but ensure you're very carefully reviewing the output yourself and not deferring that to maintainers

## Security

As a package manager used by millions, Homebrew is very conscious of our security profile.
We continue to try and improve it over time but some of the best practises we've introduced have been:

- being a maintainer is a responsibility, not a privilege, and if you're no longer doing maintainer work: you will lose your access
- we avoid giving everyone access to everything but instead give people as little access as they can to do their work
- we lean heavily on automation but ensure we always have a human verifying/confirming/approving results before it is shipped to users
- we use GitHub functionality for many things and try to integrate as many of their security features as possible
- we try to design each component of Homebrew to not fully trust any other component or piece of infrastructure
- we encourage users to adopt secure configurations (e.g. macOS versions that receive security updates)
- we have had several third-party penetration tests

The biggest challenge facing Open Source security today is filtering out the signal from the noise.
We get large amounts of "drive-by security spam" where people have claimed to find some vulnerability with our website that's e.g. statically generated.
Similarly, we end up with a lot of reports from novices with a passion for security who can be overly fixated on threat models that professional security researchers consider insignificant.
All of this takes a lot of time and energy away from legitimate security problems and means security disclosures are, sadly but correctly, assumed to be non-applicable more often than not.

## AI

LLM AI tooling is becoming increasingly widely used in our industry.
I use it fairly heavily myself; mostly as a good autocomplete (even when writing this article) rather than generating entire files/posts/PRs.\

I think LLM AI tooling has the potential to be positive for Open Source but the jury is still out for now.
To be really effective: you need to ensure you do extensive review of any AI generated output.
Who are some of the best people in the world at extensive code review?
Open Source maintainers.
This is why I think it could be useful for those folks.

Sadly, some contributors have used it to generate entire PRs they don't understand and expect the maintainer to review their AI slop for them.
This slows everyone down and, much like the security spam above, poisons the well for everyone.

## Advice

I've worked on Homebrew for 16 years this year and never taken more than a couple of weeks "off" in that time.
I enjoy it and seem to be resistant to the burnout that's affected other maintainers.

The main reason I think I've been able to do this is in my mantra (and blog post):
"Open Source Maintainers Owe You Nothing"[^75].

I encourage every maintainer to read and internalise this.
Unless it's your full-time job to work on your open-source project: you can walk away at any time, guilt-free.
Additionally, no-one can make you do anything you don't want to do.

When I was employed at GitHub I (pretty much single handedly) built the "archive a repository" feature exactly for this reason.
I wanted to allow people to walk away and not get notifications any more while allowing others to view and fork their work.

Once you start to dread getting issues or contributions on your Open Source project: it's probably time to leave.

If it's not time to leave: think about the parts of it that fill you with dread and consider how you can adjust your documentation, policies, templates, code or even just personal boundaries to not have to do these any more.

Most of all though: good luck.
It's not always easy.
If it was: everyone would be doing it.
You're contributing to the biggest collaborative effort humankind has ever tried.
You are a hero for even trying.
Keep up the good work!

\newpage


[^75]: https://mikemcquaid.com/open-source-maintainers-owe-you-nothing/
