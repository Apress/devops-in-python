>>> fp = open("things.txt", "w")
>>> fp.write("""\
... one line
... two lines
... red line
... blue line
... """)
39
>>> fp.close()
>>> fpin = open("things.txt")
>>> next(fpin)
'one line\n'
>>> next(fpin)
'two lines\n'
>>> next(fpin)
'red line\n'
>>> next(fpin)
'blue line\n'
>>> next(fpin)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration