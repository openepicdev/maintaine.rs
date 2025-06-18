# @atodorov -- Alexander Todorov

> ![](https://github.com/atodorov.png){ width=64px height=64px }  
> [github.com/atodorov](https://github.com/atodorov)  
> [maintaine.rs/atodorov](https://maintaine.rs/atodorov)

My name is Alex, a software quality engineer and fellow Open Source contributor
from Bulgaria. At present I am a co-organizer of FOSDEM's Testing and Continuous Delivery
devroom and the project lead for Kiwi TCMS - a popular test management system.

You can follow what I do at
[https://github.com/atodorov/](https://github.com/atodorov/) and [https://kiwitcms.org](https://kiwitcms.org)

## How did you get involved with Open Source?

I have been involved with Open Source for a very long time, almost 30 years
at this point, however in the early days I was only a user. And not a very skilled
one at that. During my early teenage years I became interested in computers
and programming and somehow started experimenting with FreeBSD and early
versions of Red Hat Linux. It was probably more of a coincidence than
anything else.

Much later, early 2000s if I remember correctly, while working on some
small project I remember having issues with one particular Perl module
which would inspect image files and return their width and height. It didn't work
correctly for the latest version of the Flash file format. Everything being plain text
I was able to make some adjustments and make it work on my computer. At some point I
realized I could just email the author of this module and tell them how to improve the code.
Which is precisely what I did, very naively I should add, I didn't send a patch or anything
like that. I just described which lines in a function need changing and how. That was
my first contribution to Open Source.

## What’s Open Source to you?

Nothing less than everything, really. Open Source is heavily infused into my personal
and professional life for the past 20 years. As fate would have it I haven't really
worked much outside of the Open Source industry.

Shortly after that initial contribution I started my first paid job as a software developer
and it was only natural to be looking for job opportunities with Linux as it was
my primary operating system for home use.

I was lucky I guess. I was writing software in Pascal on Linux which was exactly what I wanted.
Meanwhile I started contributing
translations and small bits into various projects, not even sure why. I think
I was just experimenting at that point.

Shortly afterwards I got lucky again because my passion for Open Source was
recognized by Ben Levenson at Red Hat and I accidentally landed
my dream job. I took a leap of faith and relocated to another country
to become a software test engineer. All this just because I wanted to work with Linux.

This is where I noticed first hand how Open Source is actually put together and started contributing
more heavily with technical contributions. I recall one of my more meaningful contributions
was in virt-manager, GUI improvements, in 2007. Then it gradually escalated around the
software tools and components I was using at work.

## What projects are you involved in?

Currently I am working on and off on several Django packages which I use as
dependencies but primarily on Kiwi TCMS which is a popular test management system
and arguably one of the very few Open Source variants left standing. It is a web based
application used by QA engineers and their managers to track and organize testing related work.
Think of it as one of the many pieces which you have in your software development and delivery
infrastructure. Such systems are also part of what's called Application Lifecycle Management
and could be found in large organizations.

Kiwi TCMS itself has a classic Open Source history - it was created by Red Hat, then published on GitHub,
then discontinued and left to slowly die out. I forked over after most upstream activity had stopped.
In fact forked three different times until it became Kiwi TCMS as we know it today.

## How do you grow your community?

Hard question. In the early days I was more centered around finding volunteers, working with
students (for example with Major League Hacking) and doing coding sprints at
various conferences. These days my focus is more towards building a sustainable Open Source
business practice and being able to support a core team of maintainers than anything else.

## What are the main challenges you face as a maintainer?

As in countless other projects our core user base doesn't necessarily have the skills
to contribute technically and most of the lower hanging fruits have already been picked up.
The challenge of course is being able to respond to feature requests and free (as in beer)
support calls for users with less technical experience.

There is also the ongoing task of maintenance and just keeping up-to-date with new dependency versions
even without adding new features in the application itself. Lately it's also become apparent
that I need to become even more involved with some of our dependency stack and help out other fellow maintainers.

## What are some ways contributors can better support maintainers?

Here's a broader answer which also includes consumers of Open Source:

Think about you human fellows who spend their time and often sacrifice a lot
just to deliver the library that you need. This is especially true for small communities.

Don't demand anything from the maintainer, don't be rude, be patient
and try to help yourself before engaging with the rest of the community.

If you are using a project commercially, consider helping out. Other fellow developers
will value your technical contributions and your effort to learn more than anything else.
Ask for advice or pointers, hack up a proof of concept and be ready to iterate
as many times as requested on the schedule of the maintainer. Plan for this and be a good
Open Source citizen.

If you can only offer monetary support, ask your company to do so adequately
or better yet seek commercial support where possible.
$50 for this new feature or a bug fix that you depend on is probably not going to cut it.

## What are some of the key security practices you’ve implemented in your project?

I love this question because originally our code base did have lots of vulnerabilities.
The most critical one was remote code execution which was relatively easy to exploit.

Being a tester myself I view security as just another piece of the software development
puzzle that we need to integrate with our day-to-day workflow. What I like to do on most projects is:

- Enable all kinds of linters and static analysis tools that are relevant. This helps me clean-up
  code smells and security related issues which are due to common mistakes.
- Enable all tools and keep enabling new ones over time as I get to know about them. Disable the ones
  which don't appear to bring value. My current favorite is MegaLinter, although there may be more
  suitable tools depending on the programming language used.
- Scan all of your code base plus the entire dependency stack and take action as soon as you can.
  When I say "all" I really mean all of it - software, its test suite, infrastructure as code, CI scripts
  and YAML files, etc. It is astonishing what you would find and at the same time it is a mountain
  of work to sift through all the reports and patch out (or just silence) issues further down the stack.
  Most often than not that means asking other Open Source projects to adopt similar tools and
  practices as you do which opens more and more work for everyone involved
- Use tools to automatically upgrade your dependencies to their latest versions
- Establish a security policy and channels for researchers to disclose issues responsibly.
  Kiwi TCMS used to have
  several channels for doing this, currently it's only via GitHub
- Join security bounty programs if applicable - Kiwi TCMS has been part of one in the past which helped
  discover and fix vulnerabilities on our side
- If you are running a production instance, for example a demo installation, enable traceback reporting,
  e.g. Sentry, which helps you find out various kinds of failures you had never imagined.
  I tend to view these as critical and
  possibly security related until I get to know otherwise

One thing which I am interested in doing but not quite there yet is to engage with some sort of
penetration testing service / security audit service, preferably led by a team with a strong affinity
towards Open Source. However this is something which doesn't apply to all projects.

From the point of view of your own project all of the above means constant maintenance and very likely
refactoring and updating your implementation as you get to know things. Since Kiwi TCMS started as
a legacy code base I've worked on extensive refactoring in several key areas. Some areas have been refactored
two or three times until they got to a point which is elegant, easy to maintain and relatively secure.

## What do you think are the biggest security challenges facing Open Source today?

I'm not quite sure. It's probably a mix of lack of development time/resource;
lack of some technical knowledge about what may constitute a future problem;
lack of overall vision towards security and probably a healthy dose of "I don't care".

That's also a challenge on the side of the consumers of Open Source. They need
to be as equally aware as the developers they trust. Just because something is Open Source
doesn't mean it is secure.

I've seen plenty of blatant violations with some of Kiwi TCMS' own forks. For example people
publishing their SSH keys or account passwords on GitHub and not changing them even after
I send them an email to alert them about their mistake. In one particular example I've
seen this continue for years.

Mistakes do happen but let's learn and improve when we discover them.

## What’s the impact of AI on Open Source development?

I can't say. I haven't used many AI tools myself and I am a bit skeptical
that they provide good value. Maybe I'm just old school.

## What advice would you give to current and new maintainers?

Being a maintainer is oftentimes grunt work which takes its toll and one
should really love what they are doing to continue doing it. Oftentimes it looks
completely irrational "working" as a maintainer, especially on smaller projects.
Had I known how much work and challenges there would be being involved
as an Open Source maintainer and contributor I would have probably not done it!

To anyone new I would say: spend enough time to find out what you are getting yourself into
and make sure that this is what you really want (for whatever reasons you may have)!

\newpage
