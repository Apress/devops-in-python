@attr.s
class DummyShell:

    _container_name = attr.ib()

    def batch(self, *args, **kwargs):
        if (args == ['docker', 'logs', self._container_name] and
            kwargs == {}):
            return "hello\nerror: 5 is not 6\ngoodbye\n", ""
        raise ValueError("unknown command", self, args, kwargs)

def test_error_lines():
    container_name = 'foo'
    executor = seashore.Executor(DummyShell(container_name))
    ret = error_lines(container_name, executor)
    assert_that(list(ret), is_(["error: 5 is not 6"]))