# @blyxyas -- Alejandra Gonzalez

> ![](https://github.com/blyxyas.png){ width=64px height=64px }  
> [github.com/blyxyas](https://github.com/blyxyas)  
> [maintaine.rs/blyxyas](https://maintaine.rs/blyxyas)

I'm Alejandra, one of the people that maintains Clippy[^336], Rust's[^337] official linter. And for this Maintainer Month of May I've come to [opensource.org](https://opensource.org) about some often-overlook aspects of maintaining a FOSS project, some of my personal story with FOSS, some tips about software security, and how to better help maintainers as a contributor. Strap in because this will be a wild ride!

## Who are you again?

As I said, I'm one of the people that maintains Rust's official linter, Clippy. You can execute Rust's linter any time[^1] if you have [Cargo] installed via `cargo clippy`. I've been working on Clippy full time as a maintainer for about 2 years. In that time I've implemented several lints, fixed a lot of bugs, reviewed hundreds of pull requests, implemented benchmarking tools into Clippy and integrated Clippy into other benchmarking tools. Even proposed a Rust Project Goal that got accepted!

While I'm not the oldest maintainer, (not even close) I have some things to say, and I think that my advice could be valuable to whoever is happy to hear it.

## The hard aspects of being a maintainer

While being a maintainer is wonderful (that's why I do it), it takes a special kind of person to revisit the same software every day for years without a monetary driving force behind it.

For me, some hard aspects include:

- Having a Life/Work/Open-Source balance
- Maintaining even when you have outside conflicts.
- Taking part and giving feedback on the schedule that the contributors deserve.
- Making hard decisions, taking everything always into account because ultimately you're the final say into a lot of things
- Avoiding burnout (this is a really important point and should be talked about more)

I've struggled with all these aspects in different stages of my life, reaching some kind of stability is always hard because the environment is always changing (both in and out of FOSS).

At the end of the day we're humans managing human work. With people that deserve their reviews, reviews that deserve their quality assurance (in a timely manner) and users that deserve that their issues be resolved. Everything takes a little bit of time, and we only have limited time in our day.

You will eventually learn to balance everything out (not that I've completely reached out that priced phase yet). I promise ;)

## What about security?

Security was this Maintainer Month's topic, so I'll also give out some pieces of advice from the bottom of my heart. I'm trying to avoid those blanked, safe statements like "make sure you have good tests" because they don't really help anyone. I'll give more concrete tips at the risk of sounding too specialized.

1. Always keep in mind where your code will be run!
   It's easy to forget that your code will run on all kinds of architectures, on all kinds of operative systems, sometimes in a server, sometimes with arbitrary user-controlled inputs. This includes but is not limited to:

   - Arbitrary Unicode inputs.
   - Strings Arbitrarily-length
   - Maybe URLs or paths to files
   - File system access.

   If there's **any** probability that an end-user might exploit your FOSS project to get access into someone's server, you should disclose it!

2. Keep your CI pipelines safe
   - You probably use CI (and if you don't, absolutely do!) as a way to test your project before launching it to the greater product, make sure that your workflow files are safe! Don't use unknown dependencies (in fact, use as little dependencies as possible), with as little external applications as possible.
   - Each dependency on your CI pipeline (this includes applications / bots in your repo) is a possible vector of attack, [each `run` field is a weak point.](runweakpoint)
3. Better and smaller pull requests produce better code

   - Avoid big pull requests. Making pull requests smaller is the best strategy to improve review times, code quality and overall team mentality.
   - Pull requests under 150 lines are reviewed the fastest and thus, can fix issues the fastest.
   - As a general guideline, always think about all the boundaries that the pull request code might handle, and how to break in the worst way possible that poor contributor's code.
   - Get in the mud, explore the deep end of your contributor's code[^2]. Break your tests, read documentation for every single one of the added functions, see if functions could be removed, check if loops could be early-returned.
   - Don't forget to talk to your contributors about documentation!

4. Use automated tooling

   - This is a very simple step, don't guess about memory leaks, use a heap memory profiler (like [heaptrack]). Don't guess about memory safety, use a static
     code analyzer or a language that has memory safety built-in (like Rust). Don't guess about the origin of something, bisect it in your program (like with `git bisect`[^338]).
   - Know your system, the better you know the tools you're using the better code you'll produce and the faster you'll be able to iterate on a design. With this I don't mean learning a fancy-schmancy IDE or keyboard layout, but learning to make `perf` valuable, learning to read stack traces, learning to efficiently search throughout your documentation to find that edge case that has been bugging you out all week.

5. Keep learning
   - Even if your brain is huge, with the best-quality gray matter in this sector of the galaxy, there have been people before you. The big advantage we have over humans before our time is the collective knowledge that aids us to achieve excellence. Do not let your ego and pride get in the way of making great software, because precisely the way to make great software is knowing who to ask the right question to get the desired results.

## What can I do as a contributor?

First, thanks a lot for wanting to help your fellow developers! The biggest help that you can provide (for me) is not really in the code itself, but in what surrounds that code.

- Improve your pull request descriptions, have detailed commit messages (with descriptions directly on the commits!), split your pull requests into several commits and for features, don't try to cram too much into a single pull request. Review you yourself your pull requests (in the Pull Request interface itself) before publishing it, you'll find a lot of slip-ups this way.

- Help with long-standing issues, if you're a trusted contributor, help to give labels (if you have that authority). Give your opinion, get minimal reproducible examples of buggy behaviors!

- Help with documentation! Not everything has to be about code, adding and updating documentation is probably one of the most valuable things that you can do in a codebase.

## Conclusion

And that's everything I'll talk about today! I hope that you have learned something new and used your critical thinking skills to decide if these thoughts fit your mental model. Thanks for listening to my ramblings and have a great week. Peace!

[^1]: (unless you have a `minimal` profile set in your configuration).
[^2]: You can actually fetch a remote pull request with `git fetch origin pull/$pr_num/head:$branch_name`!


\newpage

[^336]: https://github.com/rust-lang/rust-clippy
[^337]: https://rust-lang.org
[^338]: https://git-scm.com/docs/git-bisect
