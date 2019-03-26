>>> import socket, json, pprint
>>> s = socket.socket()
>>> s.connect(('httpbin.org', 80))
>>> s.send(b'GET /get HTTP/1.0\r\nHost: httpbin.org\r\n\r\n')
40
>>> res = s.recv(1024)
>>> pprint.pprint(json.loads(
...               res.decode('ascii').split('\r\n\r\n', 1)[1]))
{'args': {},
 'headers': {'Connection': 'close', 'Host': 'httpbin.org'},
 'origin': '73.162.254.113',
 'url': 'http://httpbin.org/get'}