>>> thing = [{"hello": 1, "world": 2}, None, True]
>>> json.dumps(thing)
'[{"hello": 1, "world": 2}, null, true]'
>>> json.loads(_)
[{'hello': 1, 'world': 2}, None, True]