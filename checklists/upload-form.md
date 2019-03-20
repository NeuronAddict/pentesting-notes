# upload form


- Content-Type —>Change the parameter in the request header using Burp, ZAP etc.
- Put server executable extensions like file.php5, file.shtml, file.asa, file.cert
- Changing letters to capital form file.aSp or file.PHp3
- Using trailing spaces and/or dots at the end of the filename like file.asp… … . . .. .. , file.asp , file.asp.
- Use of semicolon after the forbidden extension and before the permitted extension example: file.asp;.jpg (Only in IIS 6 or prior)
- Upload a file with 2 extensions—> file.php.jpg
- Use of null character—> file.asp%00.jpg (and try whit directly remplace null char via zap/burp)
- Create a file with a forbidden extension —> file.asp:.jpg or file.asp::$data
- Combination of the above

## PHP formats

The following extensions can be executed : 

* php
* phtml
* php5
* phar

## Links

https://pentestlab.blog/2012/11/29/bypassing-file-upload-restrictions/
