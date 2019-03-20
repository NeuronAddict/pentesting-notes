# ldap

## get nse :

```
nmap -p 389 -sV --script ldap-rootdse <ip>
```

## search for entries :

```
ldapsearch -x -H ldap://<ip> -b dc=lightweight,dc=htb -D "uid=ldapuser,ou=People,dc=lightweight,dc=htb"  -w "<password>"
```

## with nmap

Get root : 

```
nmap -p 389 -sV --script ldap-search --script-args 'ldap.username="uid=ldapuser1,ou=People,dc=lightweight,dc=htb",ldap.password=<password>' <ip>
```

## links

* https://mparienti.developpez.com/cours/openldap/
* https://www.digitalreplica.org/2015/10/openldap-for-ldap-plain-text-password-capture/
* 
