# Resource EXEC for execute a command
exec { 'pkill':
path    => '/usr/bin',
command => 'pkill -KILL killmenow',

}