# upload form

## search for vulnerable code

* list upload forms (images, logo, avatars, attachments, )
* list upload functions (move_uploaded_file for php, ...)
* zip extract (temp folder for extraction can be accessible)
  * try path traversal with zip extract
* files write into controlled path (ex : copy of a remote page on local area) << not really an upload, but interesting
* try files remplacements (ex : image)
* php inclusion can execute code into an image file

REMEMBER : an app can show an error but have upload the file on an accessible area.

## PHP formats

Based on this config of apache : 

```
<FilesMatch ".+\.ph(p[345]?|t|tml)$">
    SetHandler application/x-httpd-php
</FilesMatch>
<FilesMatch ".+\.phps$">
    SetHandler application/x-httpd-php-source
    # Deny access to raw php sources by default
    # To re-enable it's recommended to enable access to the files
    # only in specific virtual host or directory
    Require all denied
</FilesMatch>
# Deny access to files without filename (e.g. '.php')
<FilesMatch "^\.ph(p[345]?|t|tml|ps)$">
    Require all denied
</FilesMatch>
```

The following extensions can be executed : 

* php
* php3
* php4
* php5
* phtml
* pht << who denied this on his upload form?

Sometimes other can be executed : 

* phar

## test upload form

From https://pentestlab.blog/2012/11/29/bypassing-file-upload-restrictions/ :

- Content-Type —>Change the parameter in the request header using Burp, ZAP etc.
- Put server executable extensions like file.php5, file.shtml, file.asa, file.cert
- Changing letters to capital form file.aSp or file.PHp3
- Using trailing spaces and/or dots at the end of the filename like file.asp… … . . .. .. , file.asp , file.asp.
- Use of semicolon after the forbidden extension and before the permitted extension example: file.asp;.jpg (Only in IIS 6 or prior)
- Upload a file with 2 extensions—> file.php.jpg
- Use of null character—> file.asp%00.jpg (or try directly place null char via zap/burp)
- Create a file with a forbidden extension —> file.asp:.jpg or file.asp::$data
- Combination of the above

## Links
* https://pentestlab.blog/2012/11/29/bypassing-file-upload-restrictions/
* https://www.owasp.org/index.php/Unrestricted_File_Upload
* pht : https://www.file-extensions.org/pht-file-extension, https://stackoverflow.com/questions/32912839/what-are-pht-files
