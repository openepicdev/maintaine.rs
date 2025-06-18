# @jcubic -- Jakub T. Jankiewicz

> ![](https://github.com/jcubic.png){ width=64px height=64px }  
> [github.com/jcubic](https://github.com/jcubic)  
> [maintaine.rs/jcubic](https://maintaine.rs/jcubic)

My story with Open Source started when I finished high school in 2000. I started using GNU/Linux
around that time. At first, I used a dual boot with Windows, but soon ditched Windows and started
using Linux exclusively.

When I started college in 2002, I read two books:
_Hackers_[^357] by Steven Levy
and _Free as in Freedom_[^358] about Richard Stallman
and the GNU project. Those books had a huge influence on me. So, my introduction to Open Source came
from Free Software and Software Freedom. Note that the term hacker means clever programmer, and not
a cybercriminal.

My first contact with Open content was in 2006 when I joined OpenClipart[^359].
It's a site with Public Domain vector graphics in SVG format. SVG is the standard vector format for the web.

In 2007, during my last year of college, I had severe mental health issues, and the medication I was
taking made me unable to work. I also broke my laptop. I was not able to get my degree because I was
too sick to write my final thesis, which was the only thing left to do. Around 2010, I more or less
recovered (I still needed to take my meds), and around that time, I got myself a new laptop. You can say that this was the time when my digital life on the Internet began.

My first contribution to Open Source was reporting issues on GitHub to a project called BiwaScheme,
around 2010. I also contributed by updating documentation. It first started as a blog post and later
ended up as part of the Wiki.

At that time, I also created my first bigger OSS project called jQuery
Terminal[^360], which I'm still maintaining. Back then, jQuery was the most
popular front-end library. Because I was inspired by RMS, I picked the GNU GPL license for the
project. Soon, I was asked to make the license more permissive, so I switched to GNU LGPL. I got a
few contributors, and then I was asked again to change the license to MIT or to dual-license, like
jQuery did back then. This is what I did. After a while, I was approached by a company that wanted
to use my project but asked if all contributors had given permission to change the license. So, I
needed to contact individual contributors and ask for permission. From that time, I started using
the MIT license for JavaScript projects that run in the browser.

The same year, I also joined as a developer of OpenClipart and AikiFramework that OCAL used.
Aiki was an Open Source project led by Bassel Kartabil[^361]
that was later killed by the Syrian Regime during the civil war[^362].

During all those years, I created a few Open Source projects that were somewhat successful, like
Wayne[^363], Sysend[^364],
Tagger[^365], LIPS Scheme[^366],
Gaiman[^367], and
chat-gpt Bookmarklet[^368].

But my biggest project that I'm a maintainer of is
isomorphic-git[^369]. It's a pure JavaScript implementation of a git
version control client. Isomorphic
means that the project works in both the browser and Node.js. The aim of the project is to be as close to "canonical" git as possible.

The story of joining isomorphic-git started when I created a small application called Git Web
Terminal[^370], where I used both isomorphic-git and jQuery Terminal. When
working on Git Web Terminal, I started getting involved with isomorphic-git on its GitHub issues,
asking questions, providing answers, and writing some code. Soon, the author of the project asked if
I wanted to join the isomorphic-git organization. After a while, the original author left the
project, so I felt obligated to maintain it. I didn't want the project to die, like many others out
there. My code contribution was minimal, but I did review and merge Pull Requests and kept the
project alive. I still maintain it to this day.

While I was asked to write my Open Source story, I was also asked a few questions that I will answer below:

## **What’s Open Source to you?**

For me, FOSS is mostly about helping other people. You create something that you want to share with
the world. It's the same kind of volunteer work as contributing to Wikipedia, which also has an
impact on a lot of people.

## **How do you grow your community?**

A community of contributors starts from normal users that you need to get first. So, I would start
with investing in marketing. There are a lot of things you can do to promote your project, but in the
long term, I think that the most important is SEO. I've even written a blog post about this:

- How to Promote Your Open Source Project with SEO[^371]

## **What are the main challenges you face as a maintainer?**

I think the biggest challenge is getting people to contribute meaningful changes to my projects. And
getting bug reports when something is not working. From my experience, the majority of users don't report
bugs. If something is not working, they just deal with it or use something else.

But I've noticed that users report bugs if they are asked to. Isomorphic-git, which I'm a maintainer
of, has an internal error that asks users to report a bug. Because of this, we had a flood of bug
reports related to Salesforce CLI. It was their fault, and they quickly fixed the issue, but it
took a while before new bug reports stopped being created.

## **What advice would you give to current and new maintainers?**

Invest in automation, and always reply to users' feature requests and bug reports, even if it's
just:

Thank you for your report.

## **What do you think are the biggest security challenges facing Open Source today?**

I think the biggest challenge may be trusting tools like AI too much. AI was trained on code found
on the internet, like StackOverflow. And StackOverflow is known for having code snippets that are
vulnerable. If you trust AI-generated code, you may accidentally introduce vulnerabilities in your
code. The most problematic is so-called vibe coding, when you don't even check what the AI has
produced.

If you're interested in what I do, you can find me on Twitter/X at \@jcubic[^372].

\newpage


[^357]: https://en.wikipedia.org/wiki/Hackers:_Heroes_of_the_Computer_Revolution
[^358]: https://en.wikipedia.org/wiki/Free_as_in_Freedom
[^359]: https://openclipart.org/
[^360]: https://terminal.jcubic.pl/
[^361]: https://en.wikipedia.org/wiki/Bassel_Khartabil
[^362]: https://en.wikipedia.org/wiki/Syrian_civil_war
[^363]: https://github.com/jcubic/wayne
[^364]: https://github.com/jcubic/sysend
[^365]: https://github.com/jcubic/tagger
[^366]: https://lips.js.org/
[^367]: https://github.com/jcubic/gaiman
[^368]: https://github.com/jcubic/chat-gpt
[^369]: https://isomorphic-git.org/
[^370]: https://git-terminal.js.org/
[^371]: https://itnext.io/seo-for-open-source-projects-1a6b17ffeb8b
[^372]: https://x.com/jcubic
