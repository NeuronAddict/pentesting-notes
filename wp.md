# wordpress

## enum plugins / themes

Use fuzzdb for plugins / themes enum (fuzzdb/discovery/predictable-filepaths/cms).

# gobuster for fine search 

Use something like this for search inside folder :

```
gobuster dir --url http://<IP>/wp-content/plugins/wp-file-manager/ -w /usr/share/seclists/Discovery/Web-Content/big.txt -x txt,php
```


