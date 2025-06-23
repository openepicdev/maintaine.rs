# @bxcodec -- Iman Tumorang

> ![](https://github.com/bxcodec.png){ width=64px height=64px }  
> [github.com/bxcodec](https://github.com/bxcodec)  
> [maintaine.rs/bxcodec](https://maintaine.rs/bxcodec)

I’m Iman Tumorang[^356], currently working as a full-time engineer at Veriff[^355], one of the biggest ID verification solution startups in Estonia. Prior to this, I also worked in a couple of industries, such as payment, media, and CRM. Throughout my professional journey, I’ve been following the open-source community. Even though I haven’t made considerable contributions to any popular projects, I can proudly say I’ve been maintaining a couple of my Golang libraries, which a few people fortunately use.

I noticed a correlation between my professional career and open-source contributions. All my Golang libraries are inspired by the problems I encounter in my work. Sometimes, I need to create a small library to speed up development time. If I see that it can be helpful in the public, I will make it open-source; if not, it will remain an internal source within the company.

In this story, I will share how I delved into the world of Open Source, including the learnings, the challenges, and, of course, the fun of it.

## **...How did it start?**

Back in 2016, my first job, I was lucky enough to land a position at a small startup in Jakarta, Indonesia. It was a company that offered CRM solutions. However, perhaps because the market was a bit unstable at that time, the company shut down its business six months after I joined. One month before the company publicly announced its shutdown, the CTO had already advised us to look for new jobs. As a junior engineer, it was challenging. What would I say to a new interviewer if they saw my resume showing only six months of experience?

So, what did I do? In one month, I learned what the new industry trend is. I saw a couple of big companies (startups) moving to Golang. I knew this because I have a couple of friends working at some of those big companies. So, I learned Golang, even though my stack initially included only NodeJS and Ruby on Rails. I dedicated my time to learning Golang while looking for new opportunities.

I made my first Golang library, [https://github.com/bxcodec/saint.](https://github.com/bxcodec/saint) Back then, I didn’t clearly know anything about Open Source; I realized that later. I built that simple library just for the sake of my portfolio and also as proof to recruiters: “Look, my resume shows I worked with NodeJs and Ruby on Rails, but I can learn Golang in 1 month, including building a new open-source library that people can use.”

Luckily enough, with some friends' connections, I landed a new company that will become my starting point for creating more libraries and getting noticed by many companies that actually affect my career.

## **Proudest Moment\!**

So, in my second company, I learned a lot, especially about engineering practice and Open Source. Thanks to my former Engineering Manager—shout out to: [https://github.com/uudashr](https://github.com/uudashr). I still remember when I was working with Go, using VSCode. I saw my manager’s library being used as one of the official libraries for the Golang plugin in VSCode. Wow\! How amazing was that? Almost all Go engineers who use VSCode rely on his library. When I saw that, I was so amazed by him.

Learning from him, I started to make some blog posts too. I became a “Curious Engineer” who is always learning new things and creating new things. One of my posts became popular overnight, suddenly, out of nowhere, including my GitHub repository, gaining popularity: [https://github.com/bxcodec/go-clean-arch](https://github.com/bxcodec/go-clean-arch). That’s when I felt I had achieved something I never expected. I feel so proud that everyone is looking at my code and even using it as a reference. In real life, when I attend Golang community meetups, people talk about the code I made; they praise it and even tell me that they use it as a standard in their company. This is what it feels like to make an impact, even without really working in their companies.

Not stopping there, I made another blog post and a new library in Golang, [https://github.com/bxcodec/faker.](https://github.com/bxcodec/faker) It is also popular; I can see some people are using it. The statistics (download/clone count) show that they’re using it in their projects. When it always gets downloaded/cloned, it’s probably because of the CI/CD. Once again, I feel it really makes me happy that I can be impactful on the community.

And because of these two projects on GitHub, I became one of the top Go GitHub developers in Indonesia, LOL. It is based on GitHub stars gained.

With these stats, I can easily apply to any company in Indonesia back then. At least I will get noticed first. Even though I know it’s just a kind of fun thing to do, I think it helps motivate me to work more on my open-source libraries. I address the new issues that people raise in the library, or maybe think of creating a new library that might be useful for others.

## **Challenges as Maintainers\!**

Since then, I’ve created a couple of libraries, but I think because I was not that active anymore (fewer blog posts), my newer libraries are not gaining any traction like my faker library. In the meantime, I was also getting busier at my job, solving business problems, dealing with life, COVID depressions, etc. It was challenging to stay optimistic. This also affected my libraries; I somehow wasn’t able to keep them maintained anymore. I will only take a look when it’s a critical issue (e.g., security, breaking changes, etc.). For small issues, usually there are always good people who make contributions and fix them for me. So I just need to review and approve them.

One of the biggest challenges is prioritizing. For example, I have a full-time job, which involves dealing with business issues and sometimes tight deadlines. It can be stressful and frustrating. These conditions only lead me to deprioritize the libraries that I maintain. I felt guilty because I sometimes see people raising issues, yet I never reply until five months later. This has become a problem. For some important libraries used by many people, such as [https://github.com/bxcodec/faker](https://github.com/bxcodec/faker), I moved them to a new GitHub organization, where I can invite other contributors to help me maintain them. However, for libraries that are not widely used, I maintain them myself.

I remembered that GitHub released a new feature about donations, but still, my projects are not significant enough to make people willing to donate. It’s just a small library that can be easily replaced by others. So donations are really not helping me to stay motivated; I can’t switch careers to be a full-time open-source maintainer. Maintaining Open Source is a noble responsibility; you must not expect anything in return. When people donate, don’t take it for granted; instead, be more serious about maintaining the project.

To address this motivation or prioritization issue, I actually made my library used by the company I worked for. For example, this library [https://github.com/bxcodec/dbresolver](https://github.com/bxcodec/dbresolver) is about managing DB connections for both RW and RO connections with load balancer functionality. I created this while working at Xendit, the biggest payment gateway in Southeast Asia. This library is used in one of the core projects at Xendit, which gives me some responsibility to maintain the open-source version since I have a real user utilizing it. Additionally, I can leverage it for marketing by saying, 'Hey, this company is using this' – even though I was the one who developed it, LOL.

## **Final Thoughts**

I’ll be real, I’m not a noble person. I worked for money to support my family and my lifestyle. Working for free is not my style. Working on Open Source definitely does not give me any monetary value directly. Instead, what I gain is a better portfolio and a new network through collaborations that can later help me land new jobs through referrals, etc. For most of the biggest players, yes, they can get donations, but for small fry like myself, I don’t dare to dream that much. I believe that helping people with a spirit of community will benefit me later in different forms. It doesn’t have to involve money every time.

For the community itself, Open Source helps us advance technology. With many people collaborating on one project, it helps us shape a better approach to building systems. People can easily look at the source code and make improvements if they think they can make it better. I’ve experienced this many times; thanks to all my contributors, it helps me think and shape my knowledge about building an extensible, reusable, and scalable library.

Even though I was really busy with other stuff in my job, I always tried to spare a couple of hours each month to take a look at my Open Source projects. Sometimes, if someone raised a PR, I still tried to prioritize it during the weekend. However, it is only possible when there are no urgent matters like family, job, etc.

Lastly, you're doing well for all the maintainers who read this\! When you feel down, it’s okay to take a break, as there are many important things in real life for you. Take a short break and return with recharged energy. There’s always the option to extend responsibilities to new contributors; inviting new people to become main contributors could be a possibility. Unless you receive regular donations that cover your monthly expenses, it can become your full-time job.

And for the contributors, everyone, as one of the maintainers of small libraries, I truly appreciate your time spent writing PRs, making improvements, and even doing something as small as raising GitHub issues; it really means a lot to the maintainers.

And last but not least, people are using Open Source. I appreciate your trust in the Open Source project and your willingness to try and implement it in production. This gives the maintainers a sense of fulfillment. Let’s celebrate this Open Source month with more contributions and the use of Open Source projects.

\newpage


[^355]: https://veriff.com
[^356]: https://imantumorang.com/
