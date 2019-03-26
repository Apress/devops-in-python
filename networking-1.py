>>> import socket, json, pprint
>>> s = socket.socket()
>>> s.connect(('httpbin.org', 80))
>>> s.sendall(b'GET /get HTTP/1.0\r\nHost: httpbin.org\r\n\r\n')
>>> resp = b''
>>> while True:
...     more = s.recv(1024)
...     if more == b'':
...             break
...     resp += more
...
>>> pprint.pprint(json.loads(resp.decode('ascii').split('\r\n\r\n')[1]))
{'args': {},
 'headers': {'Connection': 'close', 'Host': 'httpbin.org'},
 'origin': '73.162.254.113',
 'url': 'http://httpbin.org/get'}