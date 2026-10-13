---
title: "RDP"
tags:
  - cs/hacking
  - cs/hacking/htb
created: 2022-07-11
type: note
---
Stands for Remote Desktop Protocol.

## Mounting using rdesktop
```bash
rdesktop 10.10.10.132 -d HTB -u administrator -p 'Password' -r disk:linux='home/user/rdesktop/files'
```

```bash
xfreerdp /v:10.10.10.132 /d:HTB /u:administrator /p:'Password' /drive:linux,home/plaintext/htb/academy/filetransfer'
```

We can then go to `\\tsclient\` directory to transfer files to and from the RDP session.


> [!nav]
> [[hacking-hub|Hacking]]
