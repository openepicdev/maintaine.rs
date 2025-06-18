# @akihirosuda -- Akihiro Suda

> ![](https://github.com/akihirosuda.png){ width=64px height=64px }  
> [github.com/akihirosuda](https://github.com/akihirosuda)  
> [maintaine.rs/akihirosuda](https://maintaine.rs/akihirosuda)

I'm Akihiro Suda[^213], a software engineer at NTT[^214] in Japan.

I've been a contributor and a maintainer of several projects related to container virtualization on Linux for almost a decade.

## Container Ecosystem I've been involved with

### Docker/Moby

My container journey began a decade ago with Docker[^215], the most popular containerization platform.
While the Docker Desktop products are proprietary, most of their underlying non-GUI components have been Open Sourced (Apache License 2.0) and openly developed in the community.
The Open Source parts are also known as Moby[^216] since 2017.

I began my contributions to Docker (later Moby) circa 2016 when I encountered several issues[^217], especially those related to the filesystem.
My regular commitment was well recognized, and it fortunately resulted in my appointment[^218] as a maintainer, although I had never been affiliated with Docker, Inc.
I appreciate the company for making the maintainership open to the community.

In 2018, I implemented the Rootless mode[^219] as a major functional contribution, which strengthens security by running the Docker daemon without root privileges, leveraging technologies incubated in LXC and runc, and my new user-mode networking stack (slirp4netns[^220] and RootlessKit[^221]).
Rootless mode was upstreamed into Docker in 2019.
Ahead of Docker, some portions of my work were also incorporated into Podman, an alternative implementation of Docker by Red Hat, which had been also pursuing Rootless containers at the same time.
I was pleased to influence both projects.

### BuildKit

BuildKit[^222] is the framework used by the modern implementation of the `docker build` command for building container images efficiently.

I was appointed one of the initial maintainers of the project in 2017, as I was already proposing a similar (but much poorer) mechanism[^223] on my own.
My own work was just untidily grafted into the legacy implementation of `docker build` and quite inferior in extensibility and maintainability.

BuildKit was established to rethink the whole design of `docker build` from scratch.
Through the collaboration in the community, the project successfully enabled innovations such as concurrent task scheduling, efficient caching, and an extensible Dockerfile format.

### containerd & runc

containerd[^224] and runc[^225] are the common runtimes used by both Docker and Kubernetes.

containerd provides high-level gRPC services for managing the lifecycle of containers and container images.
runc provides low-level wrappers for Linux kernel's facilities such as `namespaces(7)`[^226] and `cgroups(7)`[^227], following the Open Container Initiative[^228] (OCI - not to be confused with "Oracle Cloud Infrastructure") Runtime Specification[^229].

I've also been a maintainer of containerd (2017-), runc (2020-), and OCI Runtime Spec (2022-).
It may sound like I'm maintaining so many projects, but it's just a small world: all these projects are tightly interwoven in one ecosystem, and a change in one project often incurs changes in other ones.
So, it is crucial to coordinate these projects closely.

Coordination is tough, though; it is quite common to take multiple months, or even years, to implement a single feature.
A feature proposal is sometimes stalled due to fierce objections - but this case is rare.
The actual reason is often due to bikeshedding, or simply due to forgetting.
It still remains an open question how to advance a proposal that did not get much attention despite its usefulness.

### nerdctl & Lima

In 2020, I launched nerdctl[^230] (contaiNERD CTL), a Docker-compatible CLI for containerd, so as to facilitate experimenting with the cutting-edge features of containerd that were not present, and could not be easily implemented, in Docker at that time[^231].

In the following year I also launched Lima[^232] (LInux MAchines), a tool to create a virtual machine optimized for running containerd and nerdctl.
I originally designed Lima as "containerd Machine" to bring the concept of the former Docker Machine[^233] into the containerd ecosystem, but I changed my mind after all and released Lima with the leeway to allow non-containerd workloads too.

Both projects were well received in the community, and adopted by several third-party projects such as Rancher Desktop[^234] (SUSE), Finch[^235] (AWS), and Colima[^236].

Through launching the two successful projects, I realized again the importance of the people.
The key to success is how to attract contributors, and how to keep them motivated.
This includes showing appreciation, sorting out "low-hanging fruit" tasks, accommodating release schedules, and maintaining clear governance.

## My Journey Onward

I'll still continue to work with containers; however, I envision that containers in the next decade may not look like that of today.

### Stronger Isolation Technology

With the rise of LLMs, people now have a growing tendency to execute arbitrary code without reviewing them at all.
Contemporary containers are still effective in alleviating the security risk in executing malicious code; however, sophisticated malware may break out of the container by exploiting vulnerabilities of the container runtime or the Linux kernel.
The next decade may see the drastic revival of virtual machines (e.g., Kata[^237], notably with PVM[^238]) to strengthen the isolation, at the cost of performance, increased memory footprint, and reduced flexibility.
However, this does not mean that the current container ecosystem, and the community, have to be scrapped.
Even when a technological trend shifts, the community still remains there to help maintain interoperability across the old and the new stacks.

### WebAssembly

WebAssembly (WASM) is also emerging as a secure alternative to containers. It is also promising for offloading server-side logic to web browsers.

However, migrating a container image to WASM is not always easy due to the difference in the toolchains.

My teammate Masashi Yoshimura[^239] is now working on elfconv[^240] project that directly converts ELF binaries in a container image to WASM.
This is quite a challenging project, as an enormous number of CPU instructions and Linux syscalls have to be reimplemented for WASM.
Our success will depend on whether we can build the community for collaboration on reimplementing them.

### Library Sandboxing

When writing software, it is practically inevitable to depend on third-party libraries.
This supply chain is now under attack.
Notably, the liblzma incident[^241] in 2024 demonstrated that even well-known libraries could be compromised by a malicious contributor.
Also, there has been an ongoing incident[^242] of fake Go modules published with very plausible content and a high number of GitHub stars.

To mitigate such attacks, I'm now working on a new project "gomodjail"[^243], the "jail" for Go modules.
gomodjail is similar to containers in the sense of syscall restrictions, but it works in much finer granularity.
My current focus is on the Go language, but I hope that I will be able to apply the same sandboxing technique to other languages too, as similar incidents have occurred[^244] in other language communities.

\newpage


[^213]: https://github.com/AkihiroSuda
[^214]: https://www.rd.ntt/e/
[^215]: https://www.docker.com
[^216]: https://github.com/moby
[^217]: https://github.com/AkihiroSuda/issues-docker
[^218]: https://github.com/moby/moby/pull/27931
[^219]: https://rootlesscontaine.rs
[^220]: https://github.com/rootless-containers/slirp4netns
[^221]: https://github.com/rootless-containers/rootlesskit
[^222]: https://github.com/moby/buildkit
[^223]: https://github.com/moby/moby/issues/32550
[^224]: https://containerd.io
[^225]: https://runc.io
[^226]: https://man7.org/linux/man-pages/man7/namespaces.7.html
[^227]: https://man7.org/linux/man-pages/man7/cgroups.7.html
[^228]: https://opencontainers.org
[^229]: https://github.com/opencontainers/runtime-spec
[^230]: https://github.com/containerd/nerdctl
[^231]: https://medium.com/nttlabs/nerdctl-359311b32d0e
[^232]: https://lima-vm.io
[^233]: https://github.com/docker/machine
[^234]: https://rancherdesktop.io/
[^235]: https://runfinch.com/
[^236]: https://github.com/abiosoft/colima
[^237]: https://katacontainers.io
[^238]: https://github.com/virt-pvm/misc/blob/main/pvm-get-started-with-kata.md
[^239]: https://github.com/yomaytk
[^240]: https://github.com/yomaytk/elfconv
[^241]: https://tukaani.org/xz-backdoor/
[^242]: https://mhouge.dk/blog/rogue-one-a-malware-story
[^243]: https://github.com/AkihiroSuda/gomodjail
[^244]: https://thehackernews.com/2025/05/malicious-npm-packages-infect-3200.html
