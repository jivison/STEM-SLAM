# Using ssh_setup.sh
### This readme refers to the file ssh_setup.sh

### _Just a note that to paste into terminal, use &nbsp;```CTRL + SHIFT + V``` instead of &nbsp;```CTRL + V```_

Run the file using 
```bash
bash ssh_setup.sh
```
in its directory.

It should guide you through with prompts.

### __The first prompt is:__
```
Please enter the path where the rsa file should be generated (absolute):
```
For our sensors, enter 
```
/home/pi/.ssh/stem_server_rsa
```

### __The next prompt is:__
```
Please enter the path where the playbook is located:
```
The playbook being refered here to is from the github repository. It should be:
```
/home/pi/STEM-SLAM/server_files/controls/ansible/generateSSH.yaml
```

### __The next prompt is similar.__
```
Please enter the path where the yaml vars file is located:
```
Enter:
```
/home/pi/STEM-SLAM/server_files/controls/ansible/server_host.yaml
```

### __The next prompt is:__
```
Please enter the target ssh host:
```
This is asking for the IP address of the target computer. In our case, this is ```10.32.230.37```

### __The next prompt is similar:__
```
Please enter the target ssh user:
```
This is asking for the username of the target computer. In our case, this is ```stem-server```

### __Potential prompt:__
If the rsa_file you entered already exists, it'll give you this prompt asking you if you want to overwrite it or not. 
```
/home/mattecatte/.ssh/test_rsa already exists.
Overwrite (y/n)? 
```
It should be fine if you type in ```y```.

### __The next two prompts are:__
```
Enter passphrase (empty for no passphrase): 
```
and
```
Enter same passphrase again: 
```
Just leave these blank by hitting enter.

### __Next prompt:__

After spitting out a bunch of garbage, including a cool randomart image, it'll ask you to edit the yaml vars file. Instead, don't do that and ignore it and the proceding 
```
Are you sure?!
```

It'll then spit out more stuff. Here's where the errors could happen. If the files you entered in earlier weren't good, it'll produce a big wall of red text. Other wise, you should see some green and yellow text and then 
```bash
'SSH set up on this machine with the target host and user: $user@$host'
```





## Sample runthrough

### _This is me running this file on my computer. Just a note that I didn't have access to the server at the time of writing, so the last command (cp) isn't run._

```
[mattecatte@localhost STEM-SLAM]$ bash ssh_setup.sh 
Please enter the path where the rsa file should be generated (absolute): /home/mattecatte/.ssh/test_rsa
Please enter the path where the playbook is located: /home/mattecatte/STEM-SLAM/server_files/controls/ansible/generateSSH.yaml
Please enter the path where the yaml vars file is located: /home/mattecatte/STEM-SLAM/server_files/controls/ansible/hosts.yaml
Please enter the target ssh host: 10.32.230.37
Please enter the target ssh user: stem-server
Generating public/private rsa key pair.
/home/mattecatte/.ssh/test_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/mattecatte/.ssh/test_rsa.
Your public key has been saved in /home/mattecatte/.ssh/test_rsa.pub.
The key fingerprint is:
SHA256:s0OkYwtYmIk1H95UoWg+LUu9LVlksq/WfX/qcXXnYKg mattecatte@localhost.localdomain
The key's randomart image is:
+---[RSA 2048]----+
|  o . ..o.       |
| o B = .         |
|. + * + +        |
|   = o B     .   |
|  . * B S   . o +|
|   . * X o . . o+|
|    . =.=.E   . o|
|      .o... .  o.|
|     ..    . o+o |
+----[SHA256]-----+
Before preceding, edit the yaml vars file to ADD your information. I would reccomend copy pasting an earlier host and then editing the data.
Once you are done this, hit enter to continue.
Are you sure?!

PLAY [localhost] **************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [localhost]

TASK [Generating ssh config file (@ ~/.ssh/config)] ***************************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP ********************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0   
```


