#Install a package with Puppet
package { 'puppet-lint':
ensure => '2.1.1',
name   => 'puppet-lint'

}