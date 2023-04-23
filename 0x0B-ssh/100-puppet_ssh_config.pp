# using Puppet to make changes to our configuration file

include stdlib

File_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  content   => "PasswordAuthentication no\n"
}

File_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  content   => "IdentityFile ~/.ssh/school\n"
}
