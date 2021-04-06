# Client configuration file (w/puppet)
# Use Identity file and not authentication

file_line { 'Declare identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn off passwd auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
