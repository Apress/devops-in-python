>>> import code
>>> code.interact(banner="Welcome to the special interpreter",
...               local=dict(special=[1, 2, 3]))
Welcome to the special interpreter
>>> special
[1, 2, 3]
>>> ^D
now exiting InteractiveConsole...
>>> special
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'special' is not defined