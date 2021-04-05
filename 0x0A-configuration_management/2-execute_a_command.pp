# Resource EXEC for execute a command
exec { 'pkill':
path    => '/usr/bin:/usr/sbin:/bin',
command => 'pkill -KILL killmenow',
cwd     => '/home/luna/holberton-system_engineering-devops/0x0A-configuration_management',
creates => '/home/luna/holberton-system_engineering-devops/0x0A-configuration_management/killmenow',


}