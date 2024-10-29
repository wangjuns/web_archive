# Docker vs. Containerd: A Quick Comparison (2023)
[Docker vs. Containerd: A Quick Comparison (2023)](https://kodekloud.com/blog/docker-vs-containerd/) 

 A while back, Kubernetes announced that it would be replacing Docker with another container runtime, Containerd, after v1.20. This announcement caused a lot of panic and confusion among Kubernetes users.

In this blog, we’ll expound on the impact of this change by providing a comparison between Docker and its replacement, Containerd. Additionally, we’ll cover how Kubernetes uses Docker and what you can expect after Kubernetes starts using Containerd.

What Is Docker?
---------------

**Docker is a tool that provides a standardized format for packaging applications and their dependencies into containers.** It also provides a way to manage and orchestrate containerized applications, allowing users to easily deploy and manage their applications using Docker tools such as Docker Swarm.

Containers existed way before Docker. But Docker made everything easier with a rather simple approach. This is not to say that it was simple for the developers to write this utility. But it was simple for users to manage containers with it.

Docker gives us a way to do everything we want with containers, with a single tool, without needing to download additional programs. It simplifies our user experience.

To understand what Containerd is and how it works, we must first understand how Docker works.

_Try the Docker Run Lab for free:_

[![](https://kodekloud.com/blog/content/images/2024/02/2-Try-The-Docker-Labs-For-Free-1.png)
](https://kode.wiki/48sEkCI?ref=kodekloud.com)

__Docker Run Lab__

### Old Monolithic Docker

Docker was a pretty complex program that went through many, many changes during its lifetime. In the beginning, this was what is called a "monolithic" utility. Monolithic, in this case, means "one inseparable thing."

In other words, it was a big program that could do a lot of stuff. Some part of its code was responsible for pulling in container images. Another part was responsible for starting up containers and so on.

### How Docker Works

Once everybody started to use containers, Docker became more and more complex. When you have a complex system, breaking it up into smaller pieces can simplify things. For example, let's think about a command like this:

```
docker run --name webserver -p 80:80 -d nginx
```

This pulls in the "nginx" image and immediately starts a container that runs this Nginx application. This, in turn, gives us access to a web server. People can now connect to it on port 80 and see whatever web page we have there. Now, let's think about what Docker, as a program, has to do here. First of all, it needs to have some part in its code that can understand our command:

```
docker run --name webserver -p 80:80 -d nginx
```

It must somehow "translate" this internally and know what the human wants to achieve here. That's the job of the Docker CLI, "Command Line Interface." After it understands what we want, some other part of its code needs to pull in the "nginx" container image. Next, another part of the code has to start that container and make it accessible on port 80. And this is where we get to the interesting bit and, finally, where **Containerd** comes in.

To learn more about how Docker works internally, check out this blog: [How Docker works](https://kodekloud.com/blog/docker-for-beginners/#how-does-docker-work).

What Is Containerd?
-------------------

**Containerd is a container runtime that provides a lightweight and streamlined way to run containers.** It puts a lot of emphasis on the robustness, simplicity, and portability of containers.

When Docker was monolithic, a single application translated our command, then pulled in the container image, started it, and made it accessible on port 80. Nowadays, that's not true anymore. In a very simplified form, this is what currently happens:

The **Docker CLI** utility accepts the command. Then it figures out what we want to do. After it understands our intention, it passes this intention to the **Docker Daemon**. This daemon is a separate program (from Docker CLI) that always runs in the background and waits for instructions. After the Docker Daemon receives our desired action, it tells another app, called a **container runtime**, to pull in the container image. This container runtime is called **Containerd**.

Learn more about [container runtime](https://kodekloud.com/blog/container-runtime-interfaces-in-k8s/#what-is-container-runtimes-interface-cri)!

So we can now finally understand what Containerd is. In tech terms, it is a container runtime. This is a sort of Container manager. It takes care of things such as:

*   Downloading container images.
*   Uploading container images.
*   Setting up networking between these containers so that they can communicate with each other or the outside world.
*   Managing data and files stored inside these containers.
*   Starting, stopping, and restarting containers.

Containerd is called a high-level container runtime. For some actions, it makes use of yet another runtime, called a low-level container runtime. This low-level runtime is called **runc**. For example, when Containerd needs to start a container, it tells runc to do that.

All of these, Docker CLI, Docker Daemon, containerd, runc, are entirely separate programs. Pretty impressive how so many programs pass jobs along to each other just to start a container. And we even skipped some small steps it goes through to keep things simpler. But how did we end up from monolithic Docker to this collection of entirely separate applications talking to each other?

Well, after years and years of work, Docker developers started to split up different sections of Docker's code. So one part of the code became **containerd**. Some other parts became **runc**. But why? First of all, this makes things simpler for developers. Now, instead of digging through various files and trying to find the part of the code responsible for starting containers, developers can just go directly to **runc**, which has a separate [GitHub page](https://github.com/opencontainers/runc?ref=kodekloud.com).

> In the past, **runc** was just some section of Docker's code responsible for starting containers. But developers slowly extracted that code and made it into an entirely separate utility to make development easier.

Docker and Containerd in Kubernetes
-----------------------------------

Think of the Docker as a big car with all of its parts: the engine, the steering wheel, the pedals, and so on. And if we need the engine, we can easily extract it and move it into another system.

This is exactly what happened when Kubernetes needed such an engine. They basically said, "Hey, we don't need the entire car that is Docker; let's just pull out its container runtime/engine, Containerd, and install that into Kubernetes."

Read more about why Kubernetes did this in this blog post: [Kubernetes Removed Docker. What Happens Now](https://kodekloud.com/blog/kubernetes-removed-docker-what-happens-now/)"

**The reason why Docker was split into many smaller components is so that they can be freely moved around and plugged into other systems.** It gives server administrators a lot of flexibility to build their Kubernetes infrastructure however they want, with pieces that work best for them.

This is not limited to Kubernetes. Pieces like Containerd can be inserted into whatever system we want. In fact, Containerd can even be used directly on our computer. However, 99% of users won't want to use Containerd directly without first going through Docker. Let's see why.

Docker vs. Containerd: What Is The Difference?
----------------------------------------------

Docker was written with human beings in mind. We can imagine it as a sort of translator that tells an entire factory, filled with robots, about what the human wants to build or do. Docker CLI is the actual translator, some of the other pieces in Docker are like robots in a factory.

On the left side, we have the human needing to do something with containers. In the middle, we have Docker CLI + all of its other components. And, at the right, we have some actions performed by Docker, such as building a container, pulling an image, or starting a container. So Docker is a middleman, accepting commands from humans and then producing a result.

![](https://kodekloud.com/blog/content/images/2022/07/docker_containerd_diagram-1.png)

For example, for a command like

```
docker run --name webserver -p 80:80 -d nginx
```

this is how actions flow from one Docker component to the other, until, finally, the container starts:

![](https://kodekloud.com/blog/content/images/2022/07/docker_flow_diagram-1.png)

Again, for simplicity, we left some parts out, like the Docker Daemon. But in a nutshell, this is what happens after someone enters that command:

1.  Docker CLI understands what we want to do and then sends instructions to containerd.
2.  containerd does its magic and downloads the Nginx image if it's not available.
3.  Next, containerd tells runc to start this container
4.  And we finally get our result: nginx running in a little isolated container box.

It's easy to see that the Docker CLI is not necessarily required for this action. This means we don't really need Docker with all of its parts, such as the Docker CLI, Docker Daemon, and some of its other bits and pieces. However, we still need containerd and runc to start a container.

So why not tell Containerd directly about our intention? If we skip running Docker CLI and the Docker Daemon, we will at least use less memory on our system, right? It would be more efficient, that is true. It's one of the reasons why Kubernetes removed Docker and opted to use C**ontainerd** directly. But that's a tradeoff that is only useful on servers running hundreds of containers.

For our personal computer, where we just run a few containers and test things out, this wouldn't make a noticeable difference. But if Kubernetes can skip the middleman that is Docker and tell containerd directly about what it wants to do, containers can start up a bit faster. And half a second here, half a second there, with hundreds of containers, can add up and show noticeable improvements.

But keep in mind Kubernetes is a program, and Containerd is also a program. And programs can quickly talk to each other, even if the language they speak is complex. containerd is developed from the ground up **to let other programs give it instructions**. It receives instructions in a specialized language named **API calls**.

The messages sent in API calls need to follow a certain format so that the receiving program can understand them.

![](https://kodekloud.com/blog/content/images/2022/07/api_call_diagram-1.png)

It would be tedious for humans to send API calls every time they want to tell Containerd to do something. But when developers write programs that should interact with Containerd, they implement ways to send the correct API calls. So apps can efficiently communicate with each other through these APIs.

Here is an example of a small program connecting to Containerd and instructing it to download a container image:

```
package main

import (
        "context"
        "log"

        "github.com/containerd/containerd"
        "github.com/containerd/containerd/namespaces"
)

func main() {
        if err := redisExample(); err != nil {
                log.Fatal(err)
        }
}

func redisExample() error {
        client, err := containerd.New("/run/containerd/containerd.sock")
        if err != nil {
                return err
        }
        defer client.Close()

        ctx := namespaces.WithNamespace(context.Background(), "example")
        image, err := client.Pull(ctx, "docker.io/library/redis:alpine", containerd.WithPullUnpack)
        if err != nil {
                return err
        }
        log.Printf("Successfully pulled %s image\n", image.Name())

        return nil
}
```

Source code extracted from this page: [https://github.com/containerd/containerd/blob/main/docs/getting-started.md](https://github.com/containerd/containerd/blob/main/docs/getting-started.md?ref=kodekloud.com)

Do we want to write such stuff just to pull in a container image? Of course not. So Docker, on the other hand, with its Docker CLI, is built to receive **instructions from human beings**. It's more "human-friendly", letting us do many things, with rather short commands that are easy to write and easy to remember.

![](https://media.tenor.com/jWqkTaE-TAUAAAAC/late-night-seth-seth-meyers.gif)

Experimenting with Containerd
-----------------------------

But if we want to experiment with Containerd, we can do that without making complex API calls. If we do have Docker installed on our system, Containerd is already installed, too, since Docker needs it. And there are a few utilities we can use to speak to containerd directly. One method is through the **ctr** utility. For example, to tell Containerd to download the nginx image, we would enter a command like this:

```
sudo ctr images pull docker.io/library/nginx:latest
```

To see what commands ctr supports, we enter this:

```
ctr
```

![](https://lh3.googleusercontent.com/glhUsaZoKCVUn6u-V1l_3n4-im8LlOrQDDVjpIzI2DRTJ4fkwQjQYdOnuufvHnT6zS5_w5RWOsKICAaeEOk35j5_jnxBldbPeREUmP7oCqmFgEKJiYwRWw3Yo3Q6bD0DCRwP-pBXFaZ4eWgJC58)

To get help about a certain subcommand, we just write "ctr subcommand\_name" with no further parameters/instructions. For example, if we want to see how we can use the "images" subcommand, we can write:

```
ctr images
```

![](https://lh4.googleusercontent.com/3EMRk4ZB7M47kMxIGAQu71TuqhFUENrxl4WZiRqWvDHmeLKteQ8sibBh-e69Bq5Hfa4D-esNWp0rkGFfbgzaJPKGFd1jftJqnbDuYvq1L6Vtw0qM-4QlBAtSBN5SoJcQL0-hu_6BFr3Noy7eYKo)

But this **ctr** command is more of a "shortcut" meant for simple interactions with Containerd, in case someone needs to debug things or test some stuff. Imagine we are developers and just implemented some cool new stuff into Containerd. Now we want to test if the container image is downloaded faster with some optimizations we made.

Sending an API call to Containerd would be tedious. But with ctr, we can bypass writing and sending an API call. We write less, in the form of short commands, and test faster. ctr then does the heavy lifting and sends the correct API calls. So **ctr** is not really meant to be used as we use the Docker CLI. It may seem similar, but that is not its purpose. Plus, it doesn't support everything we can do with Docker.

There is also a tool called [nerdctl](https://github.com/containerd/nerdctl?ref=kodekloud.com). This has to be downloaded and installed separately. nerdctl tries to mimic Docker CLI's syntax. So it's a way to write Docker-like commands, but without actually talking to Docker. Instead, it tells Containerd directly about the actions we want to take.

Remember how we'd use this command to start an Nginx container?

```
docker run --name webserver -p 80:80 -d nginx
```

This, of course, goes through all of those steps, telling Docker CLI about what we want to do, which then goes to the Docker Daemon, and then finally reaches containerd at some point. With nerdctl, we can tell Containerd directly to start our container with a command like:

```
nerdctl run --name webserver -p 80:80 -d nginx
```

So, we skip going through the Docker CLI and the Docker Daemon.

nerdctl has the added benefit of giving us access to the newest features implemented into Containerd. For example, we can work with encrypted container images, a rather new feature in 2022 that will eventually be implemented into regular Docker commands, too.

However, these features are still experimental and unsafe for production workloads. So nerdctl isn't geared toward end-users. It's also a tool aimed at developers or system administrators who want an easy way to test or debug Containerd's features. That is, they can quickly test things with simple nerdctl commands rather than complex API instructions, as we mentioned earlier when discussing the **ctr** utility.

So there we have it! Hopefully, this clears up the mystery about what Docker is, how it's built, and what containerd is.

How Does Kubernetes Use Docker?
-------------------------------

Kubernetes uses Docker as its default container runtime. This means that Kubernetes can manage and orchestrate containers, allowing users to easily deploy and manage containerized applications using Kubernetes tools. By combining Kubernetes and Docker, users benefit from the scalability and flexibility of Kubernetes while also leveraging the benefits of containerization provided by Docker.

[Try our FREE Kubernetes Challenges](https://kodekloud.com/courses/kubernetes-challenges/?ref=kodekloud.com)

How will Kubernetes Use Containerd?
-----------------------------------

Docker was not designed to seamlessly embed inside Kubernetes. Docker has an abstraction layer containing UX enhancements that make it human-friendly. However, Kubernetes doesn’t need or use these enhancements.

Instead, Kubernetes uses another tool called Dockershim to get the Docker capabilities it needs, which is Containerd. But why does Kubernetes need to use Dockershim instead of going to Containerd directly? It is needed because Docker isn’t compliant with the Container Runtime Interface (CRI).

Once Docker is removed, Kubernetes will also stop using Dockershim. Instead, it’ll use Containerd directly, making the process of orchestrating containers much simpler and faster.

Polish your containerization skills with our hands-on [Docker Course](https://kodekloud.com/courses/docker-for-the-absolute-beginner/?ref=kodekloud.com):

[

Docker Training Course for the Absolute Beginner | KodeKloud

Learn Docker with simple and easy hands-on Labs

![](https://assets-global.website-files.com/62a8969da1ab561666c8c408/6319fe59c5677ae4cb8ae16f_favicon.png)

![](https://assets-global.website-files.com/62a8969da1ab56329dc8c41e/6412bd8d73926ccddfc202fb_Docker%20Training%20Course%20For%20Absolute%20Beginners.png)


](https://kodekloud.com/courses/docker-for-the-absolute-beginner/?ref=kodekloud.com)

* * *

You may also be interested in the following:

*   [How Dockerfile Works](https://kodekloud.com/blog/how-dockerfile-works/)
*   [How GitHub Works](https://kodekloud.com/blog/how-github-works/)
*   [A Complete Guide to Docker Networking](https://kodekloud.com/blog/networking-docker-containers/)
*   [CI/CD with Docker for Beginners](https://kodekloud.com/blog/ci-cd-with-docker/)
*   [What Is Kubernetes DaemonSet and How to Use It?](https://kodekloud.com/blog/kubernetes-daemonset/)
*   [What Are Objects Used for in Kubernetes? 11 Types of Objects Explained](https://kodekloud.com/blog/kubernetes-objects/)
*   [ClusterIP vs. NodePort vs. LoadBalancer: Key Differences and When to Use Them?](https://kodekloud.com/blog/clusterip-nodeport-loadbalancer/)

*    [![](https://kodekloud.com/blog/content/images/size/w100/2022/07/3-headshot-1.png)](https://kodekloud.com/blog/author/alexandru/)