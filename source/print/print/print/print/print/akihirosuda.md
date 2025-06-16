# @akihirosuda -- Akihiro Suda

> ![](https://i0.wp.com/github.com/akihirosuda.png?resize=200%2C200&ssl=1){ width=64px height=64px }  
> [github.com/akihirosuda](https://github.com/akihirosuda)  
> [maintaine.rs/akihirosuda](https://maintaine.rs/akihirosuda)

I'm Akihiro Suda[^179], a software engineer at NTT[^180] in Japan.

I've been a contributor and a maintainer of several projects related to container virtualization on Linux for almost a decade.

## Container Ecosystem I've been involved with

### Docker/Moby

My container journey began a decade ago with Docker[^181], the most popular containerization platform.
While the Docker Desktop products are proprietary, most of their underlying non-GUI components have been Open Sourced (Apache License 2.0) and openly developed in the community.
The Open Source parts are also known as Moby[^182] since 2017.

I began my contributions to Docker (later Moby) circa 2016 when I encountered several issues[^183], especially those related to the filesystem.
My regular commitment was well recognized, and it fortunately resulted in my appointment[^184] as a maintainer, although I had never been affiliated with Docker, Inc.
I appreciate the company for making the maintainership open to the community.

In 2018, I implemented the Rootless mode[^185] as a major functional contribution, which strengthens security by running the Docker daemon without root privileges, leveraging technologies incubated in LXC and runc, and my new user-mode networking stack (slirp4netns[^186] and RootlessKit[^187]).
Rootless mode was upstreamed into Docker in 2019.
Ahead of Docker, some portions of my work were also incorporated into Podman, an alternative implementation of Docker by Red Hat, which had been also pursuing Rootless containers at the same time.
I was pleased to influence both projects.

### BuildKit

BuildKit[^188] is the framework used by the modern implementation of the `docker build` command for building container images efficiently.

I was appointed one of the initial maintainers of the project in 2017, as I was already proposing a similar (but much poorer) mechanism[^189] on my own.
My own work was just untidily grafted into the legacy implementation of `docker build` and quite inferior in extensibility and maintainability.

BuildKit was established to rethink the whole design of `docker build` from scratch.
Through the collaboration in the community, the project successfully enabled innovations such as concurrent task scheduling, efficient caching, and an extensible Dockerfile format.

### containerd & runc

containerd[^190] and runc[^191] are the common runtimes used by both Docker and Kubernetes.

containerd provides high-level gRPC services for managing the lifecycle of containers and container images.
runc provides low-level wrappers for Linux kernel's facilities such as `namespaces(7)`[^192] and `cgroups(7)`[^193], following the Open Container Initiative[^194] (OCI - not to be confused with "Oracle Cloud Infrastructure") Runtime Specification[^195].

I've also been a maintainer of containerd (2017-), runc (2020-), and OCI Runtime Spec (2022-).
It may sound like I'm maintaining so many projects, but it's just a small world: all these projects are tightly interwoven in one ecosystem, and a change in one project often incurs changes in other ones.
So, it is crucial to coordinate these projects closely.

Coordination is tough, though; it is quite common to take multiple months, or even years, to implement a single feature.
A feature proposal is sometimes stalled due to fierce objections - but this case is rare.
The actual reason is often due to bikeshedding, or simply due to forgetting.
It still remains an open question how to advance a proposal that did not get much attention despite its usefulness.

### nerdctl & Lima

In 2020, I launched nerdctl[^196] (contaiNERD CTL), a Docker-compatible CLI for containerd, so as to facilitate experimenting with the cutting-edge features of containerd that were not present, and could not be easily implemented, in Docker at that time[^197].

In the following year I also launched Lima[^198] (LInux MAchines), a tool to create a virtual machine optimized for running containerd and nerdctl.
I originally designed Lima as "containerd Machine" to bring the concept of the former Docker Machine[^199] into the containerd ecosystem, but I changed my mind after all and released Lima with the leeway to allow non-containerd workloads too.

Both projects were well received in the community, and adopted by several third-party projects such as Rancher Desktop[^200] (SUSE), Finch[^201] (AWS), and Colima[^202].

Through launching the two successful projects, I realized again the importance of the people.
The key to success is how to attract contributors, and how to keep them motivated.
This includes showing appreciation, sorting out "low-hanging fruit" tasks, accommodating release schedules, and maintaining clear governance.

## My Journey Onward

I'll still continue to work with containers; however, I envision that containers in the next decade may not look like that of today.

### Stronger Isolation Technology

With the rise of LLMs, people now have a growing tendency to execute arbitrary code without reviewing them at all.
Contemporary containers are still effective in alleviating the security risk in executing malicious code; however, sophisticated malware may break out of the container by exploiting vulnerabilities of the container runtime or the Linux kernel.
The next decade may see the drastic revival of virtual machines (e.g., Kata[^203], notably with PVM[^204]) to strengthen the isolation, at the cost of performance, increased memory footprint, and reduced flexibility.
However, this does not mean that the current container ecosystem, and the community, have to be scrapped.
Even when a technological trend shifts, the community still remains there to help maintain interoperability across the old and the new stacks.

### WebAssembly

WebAssembly (WASM) is also emerging as a secure alternative to containers. It is also promising for offloading server-side logic to web browsers.

However, migrating a container image to WASM is not always easy due to the difference in the toolchains.

My teammate Masashi Yoshimura[^205] is now working on elfconv[^206] project that directly converts ELF binaries in a container image to WASM.
This is quite a challenging project, as an enormous number of CPU instructions and Linux syscalls have to be reimplemented for WASM.
Our success will depend on whether we can build the community for collaboration on reimplementing them.

### Library Sandboxing

When writing software, it is practically inevitable to depend on third-party libraries.
This supply chain is now under attack.
Notably, the liblzma incident[^207] in 2024 demonstrated that even well-known libraries could be compromised by a malicious contributor.
Also, there has been an ongoing incident[^208] of fake Go modules published with very plausible content and a high number of GitHub stars.

To mitigate such attacks, I'm now working on a new project "gomodjail"[^209], the "jail" for Go modules.
gomodjail is similar to containers in the sense of syscall restrictions, but it works in much finer granularity.
My current focus is on the Go language, but I hope that I will be able to apply the same sandboxing technique to other languages too, as similar incidents have occurred[^210] in other language communities.

\newpage


[^179]: https://github.com/AkihiroSuda
[^180]: https://www.rd.ntt/e/
[^181]: https://www.docker.com
[^182]: https://github.com/moby
[^183]: https://github.com/AkihiroSuda/issues-docker
[^184]: https://github.com/moby/moby/pull/27931
[^185]: https://rootlesscontaine.rs
[^186]: https://github.com/rootless-containers/slirp4netns
[^187]: https://github.com/rootless-containers/rootlesskit
[^188]: https://github.com/moby/buildkit
[^189]: https://github.com/moby/moby/issues/32550
[^190]: https://containerd.io
[^191]: https://runc.io
[^192]: https://man7.org/linux/man-pages/man7/namespaces.7.html
[^193]: https://man7.org/linux/man-pages/man7/cgroups.7.html
[^194]: https://opencontainers.org
[^195]: https://github.com/opencontainers/runtime-spec
[^196]: https://github.com/containerd/nerdctl
[^197]: https://medium.com/nttlabs/nerdctl-359311b32d0e
[^198]: https://lima-vm.io
[^199]: https://github.com/docker/machine
[^200]: https://rancherdesktop.io/
[^201]: https://runfinch.com/
[^202]: https://github.com/abiosoft/colima
[^203]: https://katacontainers.io
[^204]: https://github.com/virt-pvm/misc/blob/main/pvm-get-started-with-kata.md
[^205]: https://github.com/yomaytk
[^206]: https://github.com/yomaytk/elfconv
[^207]: https://tukaani.org/xz-backdoor/
[^208]: https://mhouge.dk/blog/rogue-one-a-malware-story
[^209]: https://github.com/AkihiroSuda/gomodjail
[^210]: https://thehackernews.com/2025/05/malicious-npm-packages-infect-3200.html
