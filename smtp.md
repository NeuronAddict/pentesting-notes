root@kali:~/pentesting-notes/checklists# nc -nv 127.0.0.1 2525
(UNKNOWN) [127.0.0.1] 2525 (?) open
220 myserver ESMTP Exim 4.84_2 Fri, 01 Mar 2019 18:59:34 -0500
EHLO myserver.byme
250-myserver Hello myserver.byme [127.0.0.1]
250-SIZE 52428800
250-8BITMIME
250-PIPELINING
250 HELP
MAIL FROM: <root@myserver.byme>
250 OK
RCPT TO: <root@myserver.byme>
250 Accepted
DATA
354 Enter message, ending with "." on a line by itself
From: "John Smith" <jsmith@port25.com>
To: "Jane Doe" <jdoe@port25.com>
Subject: test message sent from manual telnet session
Date: Wed, 11 May 2011 16:19:57 -0400
Hello World,
This is a test message sent from a manual telnet session.
.
250 OK id=1gzs6r-0000kr-EM
QUIT
221 myserver closing connection

