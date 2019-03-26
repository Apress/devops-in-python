>>> reader = csv.DictReader(fileobj)
>>> list(reader)
[OrderedDict([('Username', 'alice'),
              ('Timestamp', '1514793600.0'),
              ('Success', 'False')]),
 OrderedDict([('Username', 'bob'),
              ('Timestamp', '1539154800.0'),
              ('Success', 'True')])]