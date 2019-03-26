def get_get(sock):
    sock.connect(('httpbin.org', 80))
    sock.send(b'GET /get HTTP/1.0\r\nHost: httpbin.org\r\n\r\n')
    res = sock.recv(1024)
    return json.loads(res.decode('ascii').split('\r\n\r\n', 1)[1]))