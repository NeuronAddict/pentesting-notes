# postgresql

## quick launch a machine for tests

docker run --name some-postgres -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

And psql with : 

```
psql -h 127.0.0.1 -U postgres
```

or pgadmin4


## doc

* https://www.postgresql.org/docs/
* fr : https://docs.postgresql.fr/11/
* https://docs.postgresql.fr/11/xfunc-c.html
* https://docs.postgresql.fr/11/sql-createfunction.html

