
# THIS README SHOULD BE FIXED SINCE SOME OF THE INFO IS NOT CORRECT

### SSH Connections manager

---
Stores SSH information so that you can easily connect to remote servers without remembering username, ports etc.  

The tool has the options to remove/add SSH info and connect.



---
#### Important notes: 
>The script was forked from my [friend](https://github.com/kostadin-tonchekliev). 
The idea was all his, I just stole it to improve it a bit and practice. 

>It is completely re-written, and I don't think that both scripts have much in common in terms of syntax. 

>The original script can be found [HERE](https://github.com/kostadin-tonchekliev/python-scripts/tree/main/SSH-connection-manager).

---
#### Usage:

- Just execute it and you'll see :D
```
❯ ./main.py
SSH Connection Manager ver 4.0

Please select an action:
> Amazon (SSH)
  GCP (SSH)
  Remove Connections
  Add New
  Exit
```

- Removing server:
```SSH Connection Manager ver 4.0
Remove:
> [ ] test (SSH)
  [ ] Exit
Press <space>, <tab> for multi-selection and <enter> to select and accept
```

- Adding a server: 
```
❯ ./main.py
Give a label: Amazon
Give a username: some_username_here
Give a server: aws.amazon.com
Port number: 22
Custom key (leave empty if "detects_default_key"): amazon.priv
[+] Successfully added - "Amazon (SSH)"!
```

---
#### Some Additional info:

- The data is being recorded in a `ssh_data.ini` file. Example:
```buildoutcfg
[test (SSH)]
command = ssh -p 22 test@asd -i /Users/some_user/.ssh/

[Amazon (SSH)]
command = ssh -p 22 some_username_here@aws.amazon.com -i /Users/some_user/.ssh/amazon.priv
```