# Privilege escalation checklist

Inspired from g0tmi1k priv esc checklist (https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/). 
The order is adapted to match the more probables things that I discover.

## LINUX

### Distribution / kernel
```
uname -a
cat /etc/*-release
cat /etc/issue
TODO : see proc entries
```

### get users list
cat /etc/passwd
cat /etc/group
cat /etc/shadow

### Current user
id

### Clear text passwords

Always try to get password if web is compromised.
```
grep -i user [filename]
grep -i pass [filename]
grep -C 5 "password" [filename]
find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"   # Joomla
```

### What can we do with sudo ?

Efficient if password are discovered
* sudo -l
* doas # see /etc/login.conf, /etc/doas.conf

And search for command that ca execute arbitrary code (ie nmap can launch a shell, vi too, more with short...).
see inside_exec.md

### other home folders

If other users are here, look at home folder for interesting files (ie .bash_history, .ssh, .cache, ...).
For all users, try su with discoreved password (ie, sql config in web files)

### privesc check script

unix-privesc-check or other

### local exploits

Any local exploit out of the box? for this kernel and system?

### Are sensitive files writables or readables:
```
ls -al /etc/passwd /etc/shadow # maybe incorrect

find / -writable 2>/dev/null # writable files (search for files that root can execute, ie cron)
find /etc -writable 2>/dev/null # sometimes sensitives files like passwd or shadow are modifiables
find . -writable -user root # owned by root but user writable
find /etc/ -readable -type f 2>/dev/null               # readables files on etc
```

#### without -writable or -readable
```
find / -perm /200 -user www-data -o -perm /020 -group www-data -o -perm /002 # writable files by www-data:www-data TODO : test
next, you can search writables by all current groups

find / -user root -perm -2005 # owned by root and word readable executable
```

### any SUID ?
```
find / -perm /u=s -type f -exec ls -al {} \; 2>/dev/null # find suid executables
find / -perm -4000 -exec ls -al '{}' \; 2> /dev/null

find / -perm /g=s -type f -exec ls -al {} \; 2>/dev/null # find suid executables
find / -perm -2000 -exec ls -al '{}' \; 2> /dev/null
```
* suid files https://unix.stackexchange.com/questions/180867/how-to-search-for-all-suid-sgid-files#180868
```
find "$DIRECTORY" -perm /4000' # find suid
find "$DIRECTORY" -perm /2000 # find guid
find "$DIRECTORY" -perm /6000 # both
```
Trick : https://www.gnu.org/software/coreutils/manual/html_node/Directory-Setuid-and-Setgid.html. Suid folders can be interestings.


useful suid programs :
* sudo
* su
* doas
* pkexec <-- can work if sudo don't
* all custom programs, especially on home folders ;)

### any cron ?

cron task are often executeds by root.
Custom cron (cron.d, crontab) are more often vulnerables ;)
```
/var/spool/cron/crontabs
/etc/crontab
/etc/cron.d can have files executed frequently
/etc/cron.*
```
ex : checkrootkit 0.49 is vulnerable.

pspy is useful to track processes : https://github.com/DominicBreuker/pspy.

### Listening services
netstat -taupen

### Running processes
Are sensivites services running as root (ie mysql)
ps aux
ps aux | grep root
ps -ef | grep root

### What packages / versions are installed ? 

Useful for exploit

Start by the ps aux, 
dpkg -l
yum list installed

### local exploit from root launched servicesls

### What in the logs?
ls -al /var/log
...

### Write and execute folders

To move sensitives files used by other users.

```
find / -writable -type d 2>/dev/null      # world-writeable folders
find / -perm -222 -type d 2>/dev/null     # world-writeable folders
find / -perm -o w -type d 2>/dev/null     # world-writeable folders
find / -perm -o x -type d 2>/dev/null     # world-executable folders
find / \( -perm -o w -perm -o x \) -type d 2>/dev/null   # world-writeable & executable folders
```

### Automate 
http://pentestmonkey.net/tools/audit/unix-privesc-check
https://github.com/mzet-/linux-exploit-suggester


### Search for exploits

- search local exploits from the system (work great with old systems)
DON'T SEARCH SOFTWARE EXPLOIT BEFORE SEARCH SYSTEM LOCAL EXPLOIT
- list interesting softwares -> search exploit

Sometime, older exploit works. ex : edb-40847 work on ubuntu 14.04.5LTS/4.4.0-31-generic

## LINKS

* https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
* https://pentestlab.blog/category/privilege-escalation/
* http://www.fuzzysecurity.com/tutorials/16.html
* https://www.thegeekstuff.com/2011/08/linux-var-log-files/
* http://www.0daysecurity.com/penetration-testing/enumeration.html
* http://hackingandsecurity.blogspot.com/2016/05/local-linux-enumeration-privilege.html
* http://hackingandsecurity.blogspot.com/2017/09/oscp-linux-priviledge-escalation.html
* 


