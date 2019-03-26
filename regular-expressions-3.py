>>> reobj = re.compile(r"""
... (?P<prefix>a) # The beginning -- always an a
... (?P<body>b+)  # The middle -- any numbers of b, for emphasis
... (?P<suffix>a) # An a at the end to properly anchor
... """, re.VERBOSE)
>>> m = reobj.search("hello abba world")
>>> m.groups()
('a', 'bb', 'a')
>>> m.group('prefix'), m.group('body'), m.group('suffix')
('a', 'bb', 'a')