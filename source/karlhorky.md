# @karlhorky -- Karl Horky

> ![](https://i0.wp.com/github.com/karlhorky.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/karlhorky](https://github.com/karlhorky)  
> [maintaine.rs/karlhorky](https://maintaine.rs/karlhorky)

Hi, I'm Karl Horky ([GitHub](https://github.com/karlhorky),
[LinkedIn](https://www.linkedin.com/in/karlhorky/)), Technical
Founder at [UpLeveled](https://upleveled.io) - tech education
programs for all skill levels.

In an educational landscape of AI-generated solutions,
disconnected islands of knowledge and barriers to entry, I focus
on helping students level up by designing accessible curricula
and contributing to Open Source.

## Then and Now

I've been in Open Source for over 13 years, and in tech for more
than 20, through which I have used a range of languages and
technologies, from QBasic and C to Perl, PHP, Python, Ruby on
Rails and then finally on to JavaScript / TypeScript.

Now I mostly work with TypeScript, React, Next.js, Node.js, SQL
and Bash.

Through my work in education, I've become interested in:

- new approaches in web frameworks like React Server Components /
  Server Actions and the Islands Architecture
- SQL-in-JS tooling like [SafeQL](https://safeql.dev/),
  [`prettier-plugin-embed`](https://github.com/Sec-ant/prettier-plugin-embed/blob/main/ConfigExamples.md),
  [Postgres.js](https://github.com/porsager/postgres)
- secure-by-default and pit-of-success approaches to building
  safe and correct software, eg. enforcement and guidance through
  linting rules and expressive, strict API design
- patterns to reduce abstraction and indirection in code

## UpLeveled and Open Source

My work at UpLeveled has focused on designing, developing and
delivering accessible curricula for students ranging from
beginners to more experienced engineers.

As part of this work, we maintain some of our own Open Source
projects:

- [Preflight](https://github.com/upleveled/preflight): command
  line interface for students to check their code quality
- [`eslint-config-upleveled`](https://github.com/upleveled/eslint-config-upleveled)
  and
  [`eslint-plugin-upleveled`](https://github.com/upleveled/eslint-plugin-upleveled):
  ESLint config and plugin with custom rules
- [System Setup](https://github.com/upleveled/system-setup):
  Windows, macOS and Linux setup guides
- numerous example repositories like [Examples of Broken Security
  with Next.js +
  Postgres.js](https://github.com/upleveled/security-vulnerability-examples-next-js-postgres)
  and [UpLeveled Next.js example - Winter
  2025](https://github.com/upleveled/next-js-example-winter-2025-eu)

## Papercuts

In addition to our own projects, UpLeveled also lives what we
teach and aims to be good Open Source citizens by contributing to
other projects when we encounter problems.

One common type of problem we encounter is the "papercut":

1. bugs or inconsistencies which appear to be minor
2. to more experienced developers, mildly annoying and not worth
   fixing
3. to students, potentially a blocker to their learning

These papercuts can include errors during setup steps,
documentation issues, small bugs and even security issues.

By fixing these papercuts, we can help students focus on learning
and building projects, and raise all boats by contributing the
fix to everyone else.

## Upgrading

Another area of focus for UpLeveled is keeping up to date:

- we produce new versions of our curricula multiple times per
  year
- we upgrade to new versions of OSes, browsers, runtimes,
  frameworks and libraries
- we report and fix any issues we encounter during the upgrades
- we adopt new patterns and consider new tools

Some examples of issues and pull requests related to these
upgrades:

In January 2023, while adopting the Next.js App Router and
switching our material to React Server Components, we found that
Route Handlers did not have the same capabilities to check return
types using TypeScript, and contributed this feature to Next.js:

- [Add optional generic parameter to
  `NextResponse`](https://github.com/vercel/next.js/pull/47526)
  in `vercel/next.js`

During a June 2024 iteration on our Expo / React Native lecture,
we switched the scaffolder and template we used and dropped the
obsolete config in `.npmrc`:

- [Switch to `create-expo-app` + `blank-typescript`, remove
  `.npmrc`
  cmds](https://github.com/upleveled/system-setup/pull/79) in
  `upleveled/system-setup`

More recently, a March 2025 upgrade to
`eslint-import-resolver-typescript@4.2.0` caused resolution
errors for Bun modules like `bun:test` while using
`eslint-plugin-import-x`, which we fixed with a documentation
update:

- [Document eslint-import-resolver-typescript `bun` option, fix
  ESM
  import](https://github.com/un-ts/eslint-plugin-import-x/pull/262)
  in `un-ts/eslint-plugin-import-x`

## Supporting Ecosystem Evolution

Over the long term, another goal of UpLeveled is to help evolve
the ecosystem by extending compatibility, encouraging adoption of
new technologies and discussing new standards proposals.

Extending compatibility has included issues and pull requests
such as:

- [Node.js Type Stripping in
  `node_modules/*/*.ts`](https://github.com/nodejs/typescript/issues/14)
  in `nodejs/typescript`
- [Add nested
  transforms](https://github.com/porsager/postgres/pull/460) in
  `porsager/postgres`
- [Support for SafeQL on
  Windows](https://github.com/ts-safeql/safeql/issues/80#issuecomment-1882913207)
  in `ts-safeql/safeql`
- [Recognize referential actions as keywords in ON
  UPDATE/DELETE](https://github.com/sql-formatter-org/sql-formatter/pull/849)
  in `sql-formatter-org/sql-formatter`

Encouraging adoption of new technologies has also ranged across
multiple topics, but an area which has often required additional
attention has been ESM, including TypeScript module resolution:

- ["module": "node16" error: `This expression is not
callable`](https://github.com/postcss/postcss/issues/1814) in
  `postcss/postcss`
- [disposable-email-domains: Use CommonJS export for "module":
  "node16"](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/64137)
  in `DefinitelyTyped/DefinitelyTyped`
- [Module not found: Fully Specified ESM Imports (with `.js`
  extension) in
  TypeScript](https://github.com/vercel/next.js/issues/41961) in
  `vercel/next.js`

While we have not yet invested the time to become deeply involved
in shaping standards by activities like writing spec docs or
becoming a TC39 champion, we have at times added feedback in
existing discussions or contributed short proposal notes:

- [Skip parameters in function parameter
  lists](https://bsky.app/profile/karlhorky.com/post/3lomlbj5gts2m)
  on Bluesky
- [`await fetch.json(url)`
  proposal](https://x.com/karlhorky/status/1758072415114957091)
  on Twitter
- [Standard wire data format + form field error message UI for
  showing server validation errors without
  JS](https://x.com/karlhorky/status/1689254427159375873) on
  Twitter
- [Add style ordinal/cardinal to NumberFormat
  (RBNF)](https://github.com/tc39/ecma402/issues/494#issuecomment-2249792266)
  in `tc39/ecma402`

## Tips for Contributors

I can highly recommend getting involved in Open Source - benefits
include the ability to:

- learn about new technologies
- learn how to communicate and work with others
- network with developers in the community
- become familiar with interesting projects

There are plenty of resources on how to get started with open
source, so I won't write another guide on that. If you're looking
for a good place to start, try [How to Contribute to Open Source
by Open Source
Guides](https://opensource.guide/how-to-contribute/).

Here are my more personal field notes for contributors:

1. Superpower: match the style and philosophy of the project
   - read the code of the project and try to match the style
   - also match the philosophy or goal of the project, if there
     is one
   - avoids wasting time on back and forth
2. Superpower: review your own contributions
   - read your own code as if you're the reviewer
   - try to find issues and fix them before submitting
   - comment on surprising or unusual parts of your contribution
3. Start small, but contribute widely
   - to ease into Open Source, make small contributions - small
     contributions are also helpful for others
   - if you resolve or work around an issue others have reported,
     add your approach if it's not already there
   - if you find a small issue, report or fix it
   - get into the habit of looking through the issues and pull
     requests of projects you use - soon you'll be contributing
     to a wide range of projects
4. Don't fall in love with your solution
   - be open to feedback and changes
   - acknowledge that your solution might not be the best one, or
     may not be accepted at all
5. Use AI carefully in your contributions
   - AI can help you understand the codebase and suggest changes
     that match the style
   - review AI-generated code carefully - it can produce
     low-quality output aka "AI slop"
   - using AI tools can make the difference between contributing
     and not contributing
6. Use the [Refined
   GitHub](https://github.com/refined-github/refined-github)
   browser extension to simplify the GitHub interface and add
   helpful features
7. Report issues with enough information to make them actionable
   - explain what you were trying to do
   - describe what you observed
   - describe what you expected
   - include a minimal reproduction repo or code block
   - include the steps to reproduce the issue
   - include relevant version numbers
   - prefer code blocks over screenshots
   - think through the problem and provide a guess of what the
     problem might be near the end of the issue

## Suggestions for Maintainers

During my time contributing to Open Source, I have also developed
opinions on how projects can optimize their CX (Contributor
Experience) for new contributors:

1. Optimize for contributions from web clients such as the GitHub
   web interface
   - avoid requiring a full local dev environment or terminal
     execution, also for contributions changing tests
2. Optimize for AI-assisted contributions
   - describe the project's style and provide instructions for
     LLMs in standard locations like
     `.github/instructions/*.instructions.md` or `.cursor/rules/*.mdc`
3. Simplify documentation and make it easier to understand for a
   wide audience
   - avoid jargon
   - prioritize clarity over purity / brevity - short
     explanations are often not enough for a wide audience
   - don't avoid repetition - it can help with navigation and
     comprehension
   - embed runnable examples and playgrounds in the docs
4. Provide a bug reproduction template
   - example: [Next.js repro
     template](https://codesandbox.io/p/devbox/github/vercel/next.js/tree/canary/examples/reproduction-template)
   - example: [Reproduction Template of ESLint
     Stylistic](https://github.com/eslint-community/eslint-stylistic-repro-template)
   - example: [GitHub template for creating a Rspack minimal
     reproducible
     example](https://github.com/web-infra-dev/rspack-repro)
   - more examples: [Awesome Open Source
     Automation](https://github.com/karlhorky/awesome-open-source-automation)

\newpage
