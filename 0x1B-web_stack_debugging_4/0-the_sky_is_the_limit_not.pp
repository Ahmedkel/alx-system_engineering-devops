# Fixing high amount of requests problem

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  before   => Exec['restart-nginx'],
}

exec {'restart-nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
