<p align="center">
    <img alt="0x0C. Web server" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" />
</p>
<h1 align="center">
    WEB SERVER
</h1>

## 🛠 TOOLS

# Links for you read:

- [Adding and removing nginx response header](https://blog.confirm.ch/adding-and-removing-nginx-response-headers/)
- [HAproxy and Load Balancing](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts#load-balancing-algorithms)

# Install Docker

For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

- [Mac OS](https://docs.docker.com/docker-for-mac/install/)
- [Windows](https://docs.docker.com/docker-for-windows/install/)
- [ubuntu 14.04](https://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/)
- [ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)
- [Ubuntu 18-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

## 🧐 Background Context

In this project, some of the tasks will be graded on 2 aspects:

    Is your web-01 server configured according to requirements
    Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer.

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

    start an ubuntu:16.04 Docker container
    run your script on it
    see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.

## 📝 FILES

<table>
<thead>
<tr>
  <th>TASK</th>
  <th>Directory</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td></td>
  <td> README.md</td>
  <td>...<td>
</tr>
<tr>
  <td>0</td>
  <td>0-transfer_file</td>
  <td>Write a Bash script that transfers a file from our client to a server:

Requirements:

- Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username scp connects with
  4. The path to the SSH private key that scp uses
- Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
- scp must transfer the file to the user home directory ~/
- Strict host key checking must be disabled when using scp

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-install_nginx_web_server</td>
  <td>Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

- Install nginx on your web-01 server
- Nginx should be listening on port 80
- When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Holberton School
- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
- You can’t use systemctl for restarting nginx

</td>
</tr>
<tr>
    <td>2</td>
    <td>2-setup_a_domain_name</td>
    <td>.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your tools space. Feel free to drop a thank you tweet for .TECH Domains.

Provide the domain name in your answer file.

Requirement:

- provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
- configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
- go to your profile and enter your domain in the Project website url field

</td>
</tr>
<tr>
    <td>3</td>
    <td>3-redirection</td>
    <td>Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

- The redirection must be a “301 Moved Permanently”
- You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
- Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

</td>
</tr>
<tr>
    <td>4</td>
    <td>4-not_found_page_404</td>
    <td>Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

- The page must return an HTTP 404 error code
- The page must contain the string Ceci n'est pas une page
- Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

</td>
</tr>
</td>
</tr>
</tbody>
</table>

By @Giraluna1
