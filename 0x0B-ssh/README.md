<p align="center">
    <img alt="oxoB - SSH" src="https://www.hostinger.es/tutoriales/wp-content/uploads/sites/7/2017/09/encriptacion-simetrica-tutorial-ssh.jpg" />
</p>
<h1 align="center">
    SECURE SHELL
</h1>

## 🧐 Learning Objects

- **What is a server**
- **Where servers usually live**
- **What is SSH**
- **How to create an SSH RSA key pair**
- **How to connect to a remote host using an SSH RSA key pair**
- **The advantage of using #!/usr/bin/env bash instead of /bin/bash**

## 🛠 TOOLS

- Any text editor, VI, VIM , EMACS
- Your servers with Facts

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
  <td> 0-use_a_private_key</td>
  <td>Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

    Requirements:

- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase

   </td>
</tr>
<tr>
  <td>1</td>
  <td>1-create_ssh_key_pair</td>
  <td>Write a Bash script that creates an RSA key pair.

Requirements:

    Name of the created private key must be holberton
    Number of bits in the created key to be created 4096
    The created key must be protected by the passphrase betty

</td>
</tr>
<tr>
  <td>2</td>
  <td>2-ssh_config</td>
  <td>Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
    Your SSH client configuration must be configured to refuse to authenticate using a password

</td>
</tr>
<tr>
  <td>3</td>
  <td></td>
  <td>Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

</td>
</tr>
<tr>
  <td>4</td>
  <td>4-puppet_ssh_config.pps</td>
  <td>Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
    Your SSH client configuration must be configured to refuse to authenticate using a password

</td>
</tr>
</td>
</tr>
</tbody>
</table>

## _BY_ @Giraluna1
