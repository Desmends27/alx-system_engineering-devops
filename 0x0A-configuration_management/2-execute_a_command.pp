# puppet to kill a process

exec {'kill':
  command =>'pkill -f killmenow',
  path    => 'usr/bin'
}
