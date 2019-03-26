>>> reobj = re.compile('(?P<prefix>a)(?P<body>b+)(?P<suffix>a)')
>>> m = reobj.search('hello abba world')
>>> m.group('prefix')
'a'
>>> m.group('body')
'bb'
>>> m.group('suffix')
'a'