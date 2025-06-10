# @hzoo -- Henry Zhu

> ![](https://i0.wp.com/github.com/hzoo.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/hzoo](https://github.com/hzoo)  
> [maintaine.rs/hzoo](https://maintaine.rs/hzoo)

**Interviewer:** Congratulations for being part of Maintainer Month\! I’m going to ask some questions that I shared with other maintainers. These are basic questions like how you got involved with Open Source, what Open Source means to you.

**Henry:** I would like to frame how I got involved in Open Source very specifically because I think it's a typical experience. People are very intimidated by Open Source, even though they use it a lot. Consuming Open Source is really easy \- you can import a package on NPM or whatever language. But to contribute, you have to make a GitHub account, and while it's easier than before, there are cultural barriers to get around.

Open Source is its own culture, and every project is almost like its own [city or country](https://increment.com/open-source/the-city-guide-to-open-source/). I think we all want to respect different cultures, and I feel like I would love that people do that for every project or language.

The way I got involved was realizing that somebody was working on the projects that I use. I like to make the analogy that it's similar to volunteering in a garden, or a library, or a church. It's like going to church where they give you breakfast or worship and small groups. These things are set up for you. You participate and then you go home. It's very consumerist.

It's the same with coding \- you use React, ESLint, uBlock Origin or whatever, and then one day you might finally realize, "Wait, who is working on this? Who is maintaining this? Are they getting paid?"

Someone told me that contributing is a thing anyone can do. It's very similar to Wikipedia \- anyone can contribute, but most people don't. I started by looking into projects I was using personally. You don't want to get involved in a random project \- you want something you actually use.

I tried working on a project and it was too complicated, so I ended up working on a linter, which eventually became [ESLint](https://eslint.org/). I was fixing spacing and formatting, which is now solved through [Prettier](https://prettier.io/). That helped me learn about Babel.

I think most people get involved in Open Source by accident. People are perfectly capable of contributing, but they don't know the non-technical aspects of Open Source.

**Interviewer:** How did you get involved with Babel?

**Henry:** I didn't create [Babel](https://babeljs.io/). Someone else made it. What happened was I just showed up. I answered some questions in the issues and did some basic docs. I didn't even know the project well. I was just interested, and everyone was using it. They put my name on a blog post saying "Thank you for contributing." I felt almost guilty because I barely did anything, but it actually made me want to do more.

**Interviewer:** That's how you get people involved \- you acknowledge them.

**Henry:** Exactly\! You acknowledge them in any way, because everyone's time is valuable. If they spent any amount of time trying to help, that's awesome. It definitely worked \- it got me to become the maintainer, which is crazy.

Basically, the person that made Babel left, and I became the accidental maintainer, which is crazy because I didn't even know how it worked. It wasn't my code, but they left.

**Interviewer:** Were you afraid that suddenly you were maintaining a very complex project? How did you feel about that?

**Henry:** It was a psychological thing. In my mind, I thought the person that made it would come back. So I considered myself the interim maintainer or interim person in charge. That actually helped me psychologically to not think it was all on me. I thought, "Oh, they're going to come back at any point," and I just kept doing my stuff.

But then a year later, I was like, "Wait, I don't think they're coming back." And that was really scary. But I had spent so much time thinking they were going to come back, and that helped me learn. By the time I realized they weren't coming back, I thought, "I think I can do this."

It's like joining a church, attending one service, and then the pastor leaves and you're the pastor. That's crazy\! But it ended up being six or seven years of my life. After a while, I was intentionally like, "Okay, I'm going to do this."

**Interviewer:** There was a point in your work at Babel that you decided to do less coding and focus more on community. Why did you feel that need? Was it an easy transition or was it by accident as well?

**Henry:** I wrote about this a little bit in a [blog](https://www.henryzoo.com/oss) about quitting. It relates to quitting my job too. I worked at Adobe, and I moved to New York City to work there because they found me through Open Source. The only reason I joined was I thought I would do Open Source at work. That didn't happen, but my bosses were amazing. Eventually, I asked them, "Can I do Babel half-time?" and I did that. After a year, I felt like I couldn't compromise myself doing half job, half Open Source. So I just quit, and they were very supportive.

In 2018, Babel was becoming more important in JavaScript, and I felt I could do more to sustain the project by leaving my job. Having been involved longer, I realized the most important things about the project were the non-technical side \- the community.

Yes, it's a compiler, so there are fewer people who can contribute code-wise. But I don't think of myself as that good of a programmer, so I thought, "I'm sure other people will show up to contribute code." And there have been. But not everyone's going to show up to do the other work.

I realized what I thought was important in the project, and no one else was going to do the other work, so I might as well do it because I cared about the project as a whole. It's not like I knew anything about the other things either \- I didn't know much about the project to begin with. I was just willing to do whatever was needed.

People showed up to do the code, so I was okay letting others do that while I worked on other things, which was essentially around how to get money, partnering with companies, stuff like that. That took a lot of time and was hard because I'm not a salesperson.

Sales in Open Source is very different because I'm not selling a SaaS product. I'm saying, "You already use Babel every day. Will you give back?" It's weird because everyone's already using it for free. It's more like, "Can you give money so that we can sustain this project?" We could do this for free, but we might burn out. People leave for health reasons, getting older, having kids, getting married, moving. There's no obligation to do any of this, which makes it special but also makes it hard.

**Interviewer:** This is related to the [tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons), right? You have 100 companies using the project, and maybe five of them support it. Why should a company sponsor if the other five are already doing that? If you don't have those skills around fundraising and trying to compel people to sponsor, it can be quite challenging.

**Henry:** Yeah, it's actually crazy that we raised so much. Looking back at our Open Collective, I think we've fundraised over a million dollars, which is actually kind of crazy.

**Interviewer:** You did a wonderful job. You learned your way.

**Interviewer:** I think you already touched on ways people can contribute and the main challenges. Would you like to talk about security practices?

**Henry:** When people come to a project, they feel like they need a very specific thing to do. That's a problem in any organization. People just show up and want to be told what to do. I wish people had more agency \- you might make a pull request that might get rejected, but you could communicate with the maintainer: "Is it worth working on?" I think about how we get people to be proactive and have ownership over a project.

Security is similar \- it's something that always needs to be thought about at the base level. Most security practices are practical \- you have 2FA, you don't add everybody to the org, you have read-only versus write access.

The supply chain stuff is more interesting. There were times where people shared their old password \- I think that happened in ESLint \- and then someone published it to npm. Now we have people who might join your project with the intention of doing something bad. I don't think you can solve that because what's the difference between a real contributor who does good work and a fake contributor who's intentionally trying to do something bad later? You can't know that a year later.

I think you have to learn to trust people. That's always going to be hard, especially in JavaScript. When I started, I literally didn't do anything to deserve getting added to the project, but they added me.

**Interviewer:** When you became a maintainer, there was a lot of trust. It was pretty risky \- it could go wrong in so many ways, even unintentionally. If you weren't able to continue the project and deal with the complexities, it could be a challenge. There's a lot of trust happening in Open Source.

**Henry:** There always has to be a level of trust with humans. I think that relates to AI too \- everyone says, "What if we have AI, then we don't need maintainers anymore." But AI can literally create bugs and security vulnerabilities. Someone could probably intentionally insert security issues through AI-generated PRs.

The tragedy of the commons in Open Source is around contribution, not distribution. The whole point of Open Source is that anyone can read and download for free. But the problem is there aren't enough people helping.

Nadia Eghbal, who I did a [podcast](https://hopeinsource.com/) with, wrote a book called "[Working in Public](https://press.stripe.com/working-in-public)." She has this two-by-two grid of different kinds of projects based on contributor growth and user growth. Babel was cited as an example of what's called "the stadium" \- low contributor growth, high user growth. So you have like two or three people and hundreds of thousands of users. That just [doesn't work](https://xkcd.com/2347/).

The problem with AI is that it could potentially make this problem worse. You might think, "We're going to have more contributors because it's easier to contribute." But I'm thinking, well, someone has to review it. Yes, you can use AI to review the code, but I don't think anyone would use a project where the reviews were AI-driven. The person still has to look line by line, just in case of a supply chain attack.

I also had a thought that AI might change what things would be Open Source. I feel like it will lead to fewer small projects being Open Source because AI could just copy them. I could give the AI this project, and it would just inline it in your project. Why even import it from a package manager when AI could just implement the code? It's basically like forking, but you don't need a repo \- it's just inline in your project.

So I feel like it would lead to bigger Open Source projects because AI will use them as dependencies, but it won't literally rewrite them. But for all these small things, AI will just rewrite them automatically, so there's almost no need to have small projects.

**Interviewer:** Is there something else you'd like to share?

**Henry:** I would love to share why I do Open Source and why I quit my job. The podcast that I do, it's called [Hope In Source](https://hopeinsource.com/). That has been really fun for me.

I would like to offer to people in Open Source to think about it in a spiritual sense. There is something that people could be missing out on by not thinking from that lens. When I think about Open Source, I think about volunteer work, helping people, and that's very similar to serving in a church.

For me, that's always been the motivating factor. People ask, "Why did you quit your job? Why do you do this?" I think it's a great way for me to live out what I believe \- values around ownership, community, stuff like that. It's different from the default way of thinking about it in Silicon Valley.

I want to not just say I love community all the time, but live that out in my life. That was one of the reasons why I quit \- how do I best live out these values? I also felt that if I stayed at a company in that culture, it would change who I am. I want to discover new values or retain the old values that I've had.

**Interviewer:** Thank you so much for sharing your thoughts, Henry. I really appreciate your time to share your experience with the community.

**Henry:** Thank you! A shout out to the current maintainers: Nicolò Ribaudo, Huáng Jùnliàng, liuxingbaoyu.

\newpage
