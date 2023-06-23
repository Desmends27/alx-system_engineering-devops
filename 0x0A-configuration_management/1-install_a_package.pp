#install flask from pip3n

package{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
