#!/usr/local/bin/python3
banned = [
    'exec', 'eval', 'import', '__import__', 'open', 'breakpoint',
    '__class__', '__mro__', '__subclasses__', '__globals__',
    'system', 'os', 'cat', 'flag',
]

while True:
    code = input('> ')

    if len(code) > 99:
        print('noi')
        continue

    if any(b in code for b in banned):
        print('nahi')
        continue

    try:
        exec(code, {'__builtins__': {}})
    except Exception:
        pass
