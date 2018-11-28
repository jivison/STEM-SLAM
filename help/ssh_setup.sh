#!/bin/bash

echo "Please refer to the README at https://github.com/mattecatte/STEM-SLAM/blob/master/help/READMEs/ssh_setup.md if you are stuck or have no clue what you are doing"; echo; echo


read -p "Please enter the path where the rsa file should be generated (absolute): " rsa_path
read -p "Please enter the path where the playbook is located: " playbook_path
read -p "Please enter the path where the yaml vars file is located: " yaml_path
read -p "Please enter the target ssh host: " host
read -p "Please enter the target ssh user: " user 

ssh-keygen -t rsa -f $rsa_path

echo "Before preceding, edit the yaml vars file to ADD your information. I would reccoment copy pasting an earlier host and then editing the data."

read -p "Once you are done this, hit enter to continue."

read -p "Are you sure?!"

ansible-playbook "$playbook_path" -e "@/$yaml_path"

printf "Attempting to ssh into host: $host with user: $user\nIf this doesn't work try enabling the ssh interface."

cat "$rsa_path.pub" | ssh "$user"@"$host"  'cat >> ~/.ssh/authorized_keys'

echo "SSH set up on this machine with the target host and user: $user@$host"

