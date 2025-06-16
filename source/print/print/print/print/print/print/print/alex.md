# @alex -- Alex Gaynor

> ![](https://i0.wp.com/github.com/alex.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/alex](https://github.com/alex)  
> [maintaine.rs/alex](https://maintaine.rs/alex)

My name is Alex, and I’ve been involved in Open Source software for more than 15 years. My first contribution was to Django, the Python web framework. Every day, I’d go back to Trac to see if there were any new replies to my issue and patch, and over time I started to see other issues that I could help out on (even if it was just to point out that one issue was a duplicate of another). My contributions snowballed from there. These days, while I work on many projects, the ones that get most of my time and attention are the Python Cryptographic Authority family of libraries, which are the most popular cryptography libraries for Python.

## The impact of AI on Open Source

The easiest prediction is that the impact on Open Source will be similar to the impact on software engineering in general. While this is surely true, it's not terribly interesting. Instead, I want to share two experiences I’ve had, and one I’m hoping to have.

The first experience I’ve had is users submitting low quality pull requests that strongly appear to be the output of a not-particularly-good LLM. These are frustrating and a waste of time. I don’t care if a PR was developed with an LLM or not, I care whether it’s low quality. And one thing you can certainly do with an LLM is produce large amounts of low quality code and accompanying prose, forcing maintainers to wade through plausible sounding nonsense before rejecting a PR.

A more positive experience I’ve had is using an LLM to write a PR. Our project gets a fair number of feature requests which would be entirely reasonable for us to add, but for which I have absolutely no motivation to work on. I’d be happy to review a PR, but not enthused to do the work myself. By using an LLM, I can square this circle: the LLM can generate a patch (including docs and tests) and then I can review it. This is not a solution to a technical problem – these feature requests are rarely especially complex, and indeed this workflow only works _because_ I’m entirely capable of writing the code myself. Instead, it solves a motivation problem: some feature requests I never find myself enthusiastic about, but I’m always in the mood to review code.

A final experience, which I have not had yet, but which I’m hoping LLMs can assist with is issue triage. A substantial portion of the issues filed against us are installation issues, almost all of which involve a misconfigured Python environment. While I have a lot of sympathy for users who are confused and frustrated by Python’s packaging tools, these issues are also exhausting for maintainers. I’m daring to dream of a world where maintainers can mark issues as appearing to fit a particular archetype, and allow an LLM to provide guidance to a user to resolve their issues, or alternatively to gather enough information to identify that something might really be a bug. All without requiring a maintainer to exhibit superhuman patience.

\newpage
