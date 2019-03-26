def test_error_lines():
    container_name = 'foo'

    def runner(args):
        if args[0] != 'docker':
            raise ValueError("Can only run docker", args)
        if args[1] != 'logs':
            raise ValueError("Can only run docker logs", args)
        if args[2] != container_name:
            raise ValueError("No such container", args[2])
        return iter(["hello\n", "error: 5 is not 6\n", "goodbye\n"])
    ret = error_lines(container_name, runner=runner)
    assert_that(list(ret), is_(["error: 5 is not 6"))