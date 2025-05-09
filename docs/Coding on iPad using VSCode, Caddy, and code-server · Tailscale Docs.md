# Coding on iPad using VSCode, Caddy, and code-server · Tailscale Docs
[Coding on iPad using VSCode, Caddy, and code-server · Tailscale Docs](https://tailscale.com/kb/1166/vscode-ipad#step-4-install-tailscale-on-your-ipad) 

 [Visual Studio Code](https://code.visualstudio.com/) has quickly become the text editor many people use for their day-to-day work. Its cross-platform compatibility, speed, and plethora of extensions make it an easy choice.

Coder.com's [code-server](https://github.com/cdr/code-server) lets you run VSCode on a server and access it on any device, including an iPad. This is a natural pairing for Tailscale, which lets you secure a server, and easily access it from anywhere.

However, [code-server isn't safe to expose over the public internet](https://github.com/coder/code-server/blob/main/docs/guide.md#expose-code-server), which usually leads to installing a public-facing ssh proxy or an http reverse proxy like nginx in front of it. Tailscale eliminates all that, giving you a fast, private connection no matter where you are.

[Prerequisites](#prerequisites)
-------------------------------

Before you begin this guide, you'll need a few things:

*   An iPad or similar tablet, or a laptop to access your VSCode server remotely. An external keyboard and mouse input will make writing code easier.
    
*   A server to host code-server. This guide assumes you're using an Ubuntu 20.04 server, but the steps should be similar for most hosting providers and Ubuntu versions. You can also install code-server on a desktop computer or server at home.
    
*   Lastly, you'll need a Tailscale account. You can [create a free solo account in a few seconds](https://login.tailscale.com/start).
    

### [Step 1: Install Tailscale on an Ubuntu server](#step-1-install-tailscale-on-an-ubuntu-server)

After spinning up a new server, ssh into it with your account details.

Then, install Tailscale with a single command:

Alternatively, we provide [manual installation instructions](https://tailscale.com/download).

Once it is installed, and you've run `tailscale up` on your Raspberry Pi, continue to the next step.

Now, let's confirm everything is working by ssh-ing into the server over Tailscale. We'll exit the machine and re-ssh with our Tailscale IP.

First, find and copy [your machine's Tailscale IP](https://tailscale.com/kb/1033/ip-and-dns-addresses). The easiest way to do this is to run

And copy the 100.x.y.z address. Once you've found it, `exit` your ssh session, and start a new one with your newly copied Tailscale IP.

If you've enabled [MagicDNS](https://tailscale.com/kb/1081/magicdns) on your network, you can use your server's MagicDNS hostname instead of the IP address.

### [Step 2: Install code-server](#step-2-install-code-server)

On your server, run the following one-line command to install code-server.

You can also download pre-built binaries from their [GitHub releases page](https://github.com/cdr/code-server/releases).

Once the installation is complete, configure code-server to start on boot by running the following command:

code-server is now running on your local machine, on port 8080. Now, we'll expose this server over Tailscale.

### [Step 3: Make code-server available on the Tailscale interface](#step-3-make-code-server-available-on-the-tailscale-interface)

By default, code-server only allows access from the local device (127.0.0.1), and restricts access with a password.

Since we'll only be accessing code-server over Tailscale, and Tailscale already uses your existing Single Sign-On (SSO) identity provider, there's no need for password-based auth — we can already trust that you're authorized if you can even access the server!

To do this, we'll update code-server's configuration. First, we'll open up the config file at `~/.config/code-server/config.yaml`

The default config file looks something like this:

We'll update the `auth` field to `none` and remove the `password` field, and make the service available only on your Tailscale IP address.

After these changes, your config file should look like this (don't forget to replace `<copied 100.x.y.z address>` with your Tailscale IP address!):

Apply these changes by restarting code server:

### [Step 4: Install Tailscale on your iPad](#step-4-install-tailscale-on-your-ipad)

The last step is to install and sign in to Tailscale on your iPad. You can find Tailscale in the App Store. Make sure you log in with the same account as on your server, so the two devices can see each other.

[Download Tailscale](https://tailscale.com/download)

Once you're authenticated, you should be able to access your server from the iPad by visiting `http://100.x.y.z:8080/`. (Make sure to fill in the right IP address or MagicDNS hostname!)

### [Step 5: Write code!](#step-5-write-code)

You're done! Access your VSCode instance from anywhere. You can code from a café near your home or from the other side of the world. It's all the same. And it's only accessible over Tailscale.

There are a few caveats to coding on an iPad.

For more configuration options, explore the [code-server repository's FAQ documentation](https://github.com/cdr/code-server/blob/main/docs/FAQ.md).

### [Bonus: use https with Let's Encrypt](#bonus-use-https-with-lets-encrypt)

code-server works fine over plain http (over an encrypted+authenticated Tailscale link) but some features will be unavailable. To make it fully functional, you'll need to set up https.

1.  First, [get an automated Tailscale LetsEncrypt certificate](https://tailscale.com/kb/1153/enabling-https).
    
2.  Then, use that cert by setting up a [Caddy- or nginx-based web proxy](https://coder.com/docs/code-server/latest/guide#using-lets-encrypt-with-nginx).
    

### [Bonus: additional firewall settings](#bonus-additional-firewall-settings)

Since we'll be developing on this device, chances are it'll have access to sensitive information such as private code or private data. To keep things safe, you may want to restrict all access to the server to only be over Tailscale.

For more details on how to further lock down a server, [read our guide on Ubuntu and ufw](https://tailscale.com/kb/1077/secure-server-ubuntu).