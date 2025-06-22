# @samdark -- Alexander Makarov

> ![](https://github.com/samdark.png){ width=64px height=64px }  
> [github.com/samdark](https://github.com/samdark)  
> [maintaine.rs/samdark](https://maintaine.rs/samdark)

I'm Alexander Makarov[^319] maintainer of the Yii framework[^318], and today I'm writing about my way in Open Source.

I graduated in 2007 from the Computer Science faculty and at that time I wasn't paying any attention to Open Source. I knew there were free software you're not paying for that some people did for whatever reason and there are paid software companies that did it for profit. I made some free software myself such as a cyber-club management system written in Delphi. I've posted it to some forums as a zip archive containing exe files but never thought that someone would ever want to look at the source code.

Around 2007 I was J2EE developer and I was searching for a cheap hosting to create my own blog. Java hosting was not cheap so I did a blog in PHP. First, without any framework. Then I've tried CodeIgniter and I liked it. It was simple and docs were awesome. I've co-created a community website about it, participated in docs translation, fixed some minor bugs. Then I've started wondering how does it work and found that I do not like many parts of the framework. I've tried to communicate with the framework team but then EllisLab, the organization behind it, was focused on other products so I was pretty much ignored. Disappointed, I've started looking elsewhere: Zend Framework, CakePHP... these were not as good as I wanted these to be... and then I've stumbled upon Yii. The website was full of low quality JPEG-s. It looked like something from 2001 but I've read the docs, tried it and it made perfect sense to me. In 2008 I've created another community, did translation and started to bring good things to Yii that I've seen in Java Struts, Spring, and, of course, CodeIgniter. By 2010 I was sending too many patch files (yeah, SVN and Google Code were still there) to review by core team so, instead, I was invited to join. Core team was awesome! After a year I've changed my opinion on Open Source overall and started to become a maintainer.

Nowadays Open Source to me is one of the ways I contribute to the world. I'm not really good at tolerating imperfection so sometimes I polish something or add a feature I need to products I use daily. And, of course, I'm maintaining the Yii framework. Doing that since 2010 and love it. I use it myself, I speak about it, I was invited to many places in the world to talk about it, knew great people because of it and love interacting with our team and community overall.

The community is driven by example. We are very different in the team but we keep doing high quality stuff, are communicating well and overall creating a very healthy place to be in. The most active community members are becoming maintainers eventually.

There are, of course, difficulties:

1. Lack of time. We're involved in commercial projects so the time we can allocate to Open Source is quite limited.
2. Lack of funding. We'd like to buy yourself time to work on Open Source full time but that is only partially possible thanks to the foundation we've created. It's quite small so personally, I'm not using any of the funds. Team members do and I am glad that they've got more time this way.
3. Can't really plan. Because it's hard to predict what time is available for each team member and even for myself, any deadlines start to make almost no sense.
4. Sometimes critics are hard on maintainers[^317].

To support your favorite product or maintainer you can:

1. Say "thanks!". That matters cause we're not getting it too often.
2. Provide constructive feedback.
3. Create issues.
4. Contribute with code.
5. Ask if another maintainer is needed.
6. Post about the product in question.
7. Contribute to a fund if there's any.

As the project grows, it becomes used by thousands of projects. Security becomes very important. At Yii we can't afford a bounty program but we've defined ways to communicate with security researchers. We use GitHub's advisories feature flow to report and fix issues discovered. Also, we deep-dived into security ourselves to make less mistakes. A good place to start learning is OWASP.

Recently AI/LLM started to be on hype. We're checking current trends and I'm really glad that we've decided to pursue 100% code coverage, 100% mutation score and near 100% type coverage. That allows us to leverage coding agents to improve our code. For example, we did some experiments about enhancing performance of core libraries and accepted half of the changes. All that thanks to tests. Coding agent worked a few days without stopping trying things, hallucinating, breaking code, fixing code, starting from scratch and repeating again and again.

As for projects without tests, I'm in the skeptics camp. At least for now. LLMs are being improved constantly and coding agents are as well. MCP gives more and more context. So in a year or two we might see a breakthrough in quality: less hallucinations, more quality, more "understanding". That would still require at least a single visionary engineer to lead the project.

If you're a maintainer, don't hesitate to ask for help, communicate with people and enjoy the process. People in Open Source are amazing.

\newpage


[^317]: https://github.com/samdark/opensource-hate
[^318]: https://www.yiiframework.com/
[^319]: https://github.com/samdark
