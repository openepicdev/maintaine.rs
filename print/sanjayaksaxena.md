# @sanjayaksaxena -- Sanjaya Kumar Saxena

> ![](https://github.com/sanjayaksaxena.png){ width=64px height=64px }  
> [github.com/sanjayaksaxena](https://github.com/sanjayaksaxena)  
> [maintaine.rs/sanjayaksaxena](https://maintaine.rs/sanjayaksaxena)

Open Source is not just about code availability—it is a powerful philosophy of collaborative innovation. To me, as a builder, tinkerer, and maintainer of the winkJS[^163] project in Javascript and its flagship library winkNLP[^162], Open Source represents freedom with responsibility. My builder instinct thrives in the freedom to create transparent solutions, my tinkerer spirit relishes the ability to continuously improve what others have started, and my maintainer mindset embraces the responsibility to ensure security, performance, and reliability for all users.

Beyond popularity[^161], industry recognition[^160] or compliance achievements[^159], what drives me is the opportunity to advance collective knowledge rather than serve corporate interests alone—creating tools that honor diverse skills and contributions equally in the process.

## Proprietary Roots to Open Source

My engagement with Open Source began when I was in my 50s, and it contrasts with my early years in software development. Starting my career in the early 1980s in India, I found myself in a setting that was dominated by closed-source, proprietary systems.

The turning point arrived in the 2010s during my involvement in analytics and NLP projects, notably one designed to assist Indian farmers[^158]. Presenting our analytics-driven NLP research at international conferences made me question why we were limiting these innovations to academic circles instead of Open Sourcing them—a realization that fundamentally transformed my approach to technology development.

Inspired by this shift in perspective, the core team members at the organisation I co-founded—Prateek[^157], Rachna[^156] and I—began to wonder, “Why not Open Source?” This simple yet powerful question sparked a journey toward creating the Open Source project winkJS.

## License, Philosophy, and the True Meaning of “Open”

Initially, we Open Sourced smaller NLP and machine learning utilities under the AGPLv3 license, before ambitiously moving forward to develop an integrated NLP tool—winkNLP. Soon, however, we were confronted with a philosophical dilemma: the somewhat restrictive copyleft nature of AGPLv3 inadvertently limited the freedom of developers, contradicting our initial purpose.

An intense internal debate about what "open" genuinely means led us to a critical realization: genuine contribution to Open Source has to originate from within—it can't be mandated through restrictive licensing. In a pivotal moment of clarity, winkJS transitioned to the MIT license[^155], embracing a philosophy that genuinely aligned with our vision.

This wasn’t merely a licensing change—it was a commitment to trusting the community, honoring collaboration, and embodying the true spirit of Open Source.

## Code with Conscience

Our MIT license adoption coincided with an unwavering commitment to development practices prioritizing reliability and security. From day one, we established non-negotiable standards: 100% test coverage, comprehensive static analysis, and thorough documentation.

This rigor proved invaluable when the tests caught a critical security issue known as Regular Expression Denial of Service (ReDoS)—a vulnerability where malicious inputs can drastically slow down or halt software—in one of the regular expressions used by winkNLP’s tokenization engine, a core component responsible for breaking text into meaningful units.

Our coding guidelines[^154] addressed everything from basic security practices—prohibiting eval() and mandating Object.create()—to sophisticated protections against ReDoS attacks. Perhaps our most consequential decision was eliminating external dependencies entirely from winkNLP, dramatically enhancing security while enabling precise performance optimization.

Contributors embraced these standards with impressive dedication. One even went so far as to refactor their implementation multiple times and add thorough tests—demonstrating a level of care and commitment that reflects the values we strive to uphold.

After releasing winkNLP, discovering the OpenSSF Best Practices Guidelines was a key moment. They helped us refine our processes, and their principles now guide all our Open Source work.

## And the Journey Continues

The work continues today with winkComposer[^153]—a real-time streaming-analytics framework. Just as our earlier work in NLP aimed to democratize language processing, winkComposer seeks to transform how developers work with continuous streams of data. The philosophy remains consistent: create tools that are open, reliable, and useful.

Processing millions of tokens per second without dependencies taught me lean design; that experience now shapes my streaming engine. This evolution reflects my own growth as a developer. The lessons learned from building secure, dependency-free libraries guide how I approach streaming analytics—creating lightweight, modular components—robust enough for finance yet lean enough for IoT gateways.

What excites me most is how winkComposer combines statistical methods, narrow AI with knowledge graphs and Open Source LLM powered reasoning system, bringing the analytical power once reserved for batch processing into the streaming world using Node.js. We're building it with a focus on high-performance and reliability while embracing Responsible AI principles and OpenSSF security standards—another step in our mission to make technology accessible through Open Source.

## Final Thoughts

Embracing Open Source has instilled in me an appreciation for what it means to have freedom with responsibility, and it has been inspirational to witness how community engagement amplifies innovation. My advice to maintainers, both experienced and new, is straightforward: embrace openness, rigorously uphold your project’s standards, and trust the community. High standards are never barriers; rather, they inspire trust and collective excellence.

Ultimately, Open Source isn't just about writing code—it's about shaping an equitable technological future, collaboratively and transparently. I warmly invite anyone who shares this vision to join, contribute, and build alongside us—join winkComposer’s discussions[^152] or [write to me](mailto:sanjaya@graype.in) directly. Together, our collective efforts can create solutions that transcend individual capabilities and genuinely serve the community.

**Contact information**

- [https://github.com/sanjayaksaxena](https://github.com/sanjayaksaxena)
- [http://winkjs.org/](http://winkjs.org/)

\newpage


[^152]: https://github.com/winkjs/wink-composer/discussions
[^153]: https://github.com/winkjs/wink-composer
[^154]: https://github.com/winkjs/wink-nlp/blob/master/CONTRIBUTING.md
[^155]: https://winkjs.org/blog/a-more-permissive-license.html
[^156]: https://github.com/rachnachakraborty
[^157]: https://github.com/prtksxna
[^158]: https://winkjs.org/blog/nlp-in-agriculture.html
[^159]: https://www.bestpractices.dev/en/projects/6035
[^160]: https://www.linkedin.com/posts/nasscom-ai_enterprise-nasscomaigc2023-nasscomai-activity-7227576407755735040-QcpL
[^161]: https://www.star-history.com/#winkjs/wink-nlp&Date
[^162]: https://github.com/winkjs/wink-nlp
[^163]: https://github.com/winkjs
