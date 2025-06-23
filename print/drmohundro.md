# @drmohundro -- David Mohundro

> ![](https://github.com/drmohundro.png){ width=64px height=64px }  
> [github.com/drmohundro](https://github.com/drmohundro)  
> [maintaine.rs/drmohundro](https://maintaine.rs/drmohundro)

I'm David Mohundro and I'm a software architect living in the Memphis, TN area. During the day, I work at Clear Function[^254] and at night, I'm helping raise my four kids. I've been blogging at https://mohundro.com and my most well known Open Source project is SWXMLHash[^253].

My early interactions with Open Source were primarily just on the receiving end of Open Source projects - mostly as a user, but also as a learner. I was intimidated by the prospect of working on Open Source and didn't think I had much I could offer; however, the fact that I could look at the source and learn so much from it increased my desire to join in.

All the Open Source projects I've started really began either as learning projects or as tools to help me in my other projects. SWXMLHash started because I was working on an Objective-C project that worked with a SOAP API and I wanted to convert it to Swift as a learning exercise. I barely knew either language, but I knew that working with SOAP APIs by hard-coding XML in a string was less than ideal. By publishing what I had learned in the open, I was able to share with the community. The funny thing now is, I've never released any code that actually _uses_ SWXMLHash in it! But others have benefited from it and that is exciting to me.

One of my most exciting moments as an Open Source maintainer was when, out of the blue, a contributor I had never interacted with submitted a pull request to implement custom serialization, which is now the preferred way to work with the library. That's when I realized the library was bigger than me. And that's one of the things I love about Open Source - the projects can take on a life of their own!

Even with all of this, I still have plenty of struggles while working with Open Source - I still struggle with impostor syndrome. I also struggle with growing a regular set of maintainers. Most of my projects are small enough that they don't require more people, but it means the bus factor for my projects is still one.

I haven't had to deal with security concerns _too much_ with any projects thus far. That being said, it is still something I have to keep in mind, because the reality of Open Source is that impacts of security are felt far outside of just my code now. I'm not a fan of the term "software supply chain," but it does communicate that the impact of a breach is a lot larger now. Some of the things I try to do are to limit the number of upstream dependencies I pull in - the benefits are that my code is more self-contained and easier to reason about (and more secure!) as well as simpler to build and release. A harder thing to do for me is to say no to contributions. I haven't had any known attempts to sneak malicious code in a pull request, but I have had requests that didn't really align with what I had hoped to do - those conversations are hard for me to have because I want to be welcoming, but I also don't want to maintain something that doesn't make sense to me or the project.

Another thing that I haven't yet had experience with is a "drive by pull request" that was built entirely with AI tooling, though I suspect it is only a matter of time. I've used enough LLM tooling at this point to recognize the value, while also remaining skeptical, which feels like a healthy balance to me. I suspect we'll see more early Open Source projects that were kickstarted by coding assistants, because the barrier to entry from idea to initial spike is so much smaller... my concern is that as one of these projects sees more widespread usage, we'll see more security issues because the authors will be less familiar with the bulk of the code because it was written by an AI tool.

My advice for anyone interested in contributing to Open Source or starting a new Open Source project - just take that first step. If contributing is too intimidating, pull a project that you respect down and _read_ the source. You'll learn a lot from just seeing how others build software. Check out the issues and show some curiosity. If you've got an idea for a project, try building out a spike and see what you can do with it. Finally, if you use a project frequently, let the maintainers know that you appreciate it. Open Source is often a thankless task, so words of encouragement mean a lot!

\newpage


[^253]: https://github.com/drmohundro/SWXMLHash
[^254]: https://clearfunction
