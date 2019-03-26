def test_get_get():
    result = dict(url='http://httpbin.org/get')
    headers = 'HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n'
    output = headers + json.dumps(result)
    fake_sock = FakeSimpleSocket(to_send=output, chunk_size=1)
    value = get_get(fake_sock)
    assert_that(value, is_(result))