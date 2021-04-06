# Client configuration file (w/puppet)
# Use Identity file and not authentication

file_line { 'Use the private key':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '   IdentityFile ~/.ssh/holberton',

}

file_line { 'authenticate without a pwd':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '     PasswordAuthentication no',

}