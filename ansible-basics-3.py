import sys

if '--host' in sys.argv[1:]:
    print(json.dumps({}))

print(json.dumps(dict(all='localhost')))