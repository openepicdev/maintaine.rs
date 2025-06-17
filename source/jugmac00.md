# @jugmac00 -- Jürgen Gmach

> ![](https://github.com/jugmac00.png){ width=64px height=64px }  
> [github.com/jugmac00](https://github.com/jugmac00)  
> [maintaine.rs/jugmac00](https://maintaine.rs/jugmac00)

Hi, my name is [Jürgen Gmach](https://github.com/jugmac00), and I am an open-source advocate by heart.

Although I started writing code already at the age of 13 (generation C64), and
I have been a professional software engineer since 2007, I only started
contributing to open-source software a couple of years ago.

While I had been using many open-source applications and tools like Drupal,
WordPress, Roundcube, Dovecot, Postfix, Apache, Nginx, PHP, Python, and a few
Linux distributions for several years, I never felt the need or the urge to
contribute to them - they just worked.

## Turning point

Things changed when I became the maintainer of a 14-year-old custom intranet
application built on the Zope / Python 2 stack. Python 2 support ended in
2020, which meant I needed to migrate the application to Python 3. The problem
was that there was no Python 3 version available for Zope.

As a team of one, migrating both the application and the Zope framework was a
mission impossible.

## ... But Zope is open-source software

Luckily, Zope is both open-source software and was still used by a couple of
companies, which funded a series of sprints, where dozens of developers from
diverse companies and organizations came together and with combined efforts
over several years, successfully ported Zope to Python 3. An open-source
success story!

## This was only the beginning

During the migration, we needed to make sure that Zope is both working on
Python 2 and 3 at the same time. As we had to migrate around 300 libraries, it
was a real pain to create and update separate environments for Python 2 and 3
for each of them.

During the sprint, I learned about a tool that automatically creates different
environments for your libraries and runs the test suite for each configuration.
The tool is called [tox](https://tox.wiki/en/latest/), and I immediately fell
in love with it.

tox (always lowercase, even at the beginning of a sentence) had a few issues
and rough edges, so at first I created several issues on its bug tracker, but
after a while, I felt this relentless urge to give something back. At first I
started looking through all the reported issues of the project, to get an
overview of what needed to be done, closed a couple of already fixed issues,
and then I just started working on tickets - one after another. The code base
used bleeding-edge tools and Python versions, and I got invaluable feedback on
my pull requests from a very experienced engineer. I just could not stop
anymore.

## Congratulations

After a while, the maintainer of tox announced me as a maintainer myself!

I could not believe it, becoming the maintainer of a tool, which offers so
much value, which gets downloaded more than 20 million times a month, and which
is used both across other high-profile open-source projects and multi-billion
dollar companies alike.

Being the maintainer of such a high-profile tool might have also had a big
impact when I successfully applied at Canonical. Meanwhile, I work full time on
Open Source helping to maintain Ubuntu, one of the most popular Linux
distributions of our time. I also contributed to several hundreds of open
source projects to a varying degree, and I am a frequent speaker at
conferences, where I share my experience and try to remove the barriers for
others to become part of the Open Source success story.

## Maintainer woes

Being a maintainer of a high-profile open-source application such as tox is not
always shiny. You need to manage your time and the expectations of your users.

There is always the decision of whether I should fix the latest reported bug,
or spend time with my family.

Users of your open-source applications are humans, too, and as such there are
also not so friendly ones. Several times I faced angry users who complained
about a bug, or who insisted heavily on new features or requested help to
debug their 500 lines configuration file for their multi-billion dollar
company.

At this time, I read the blog post
[I am not your supplier](https://www.softwaremaxims.com/blog/not-a-supplier),
which resonated with me and helped me prioritize the important things in life.

## Free lunch is over

While you can handle overambitious requests more easily, it is another thing to
receive a security issue - especially when you are busy in life with other
things.

Then you need to have the ability to defer work to other maintainers and ask
for help in the community.

## Security

When it comes to security, we both apply the best practices like two-factor
authentication, using security linters, and so on, at some point you need to
rely on others.

For tox we make heavy use of the security features offered by GitHub, that is
e.g. [Dependabot](https://github.com/dependabot) which helps with keeping the
dependencies secure, which is one of the greatest challenges in today's
security landscape. Supply-chain attacks are a real threat.

## What you can do

I love being an open-source maintainer, getting in touch with users across the
world, and knowing my contribution helps tens of thousands of users.

As an open-source user, you can do a couple of things. The most obvious one
is certainly helping to fund the project, either directly or via your employer
which relies on the project. Even the smallest contribution counts.

But there are many other ways. Take great care when creating issues, e.g.
making it as easy as possible for the maintainers to reproduce a bug.

Even if you are a happy user, and you do not need a bug fix or a new feature,
reach out to the maintainer of your favorite project and say "Thank you!". This
will conjure a smile on the maintainer's face - I know firsthand.

Please never forget, that even with all the anonymity the web offers, at the
very end, a maintainer is still a human. Be kind. Be friendly. Be part of the
open-source movement.

_This text is licensed via Creative Commons BY-SA 4.0_

\newpage
