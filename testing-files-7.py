def test_javascript_to_python_simple():
    with get_temp_dir() as temp_dir:
        touch(os.path.join(temp_dir, 'foo.js'))
        touch(os.path.join(temp_dir, 'bar.py'))
        touch(os.path.join(temp_dir, 'baz.txt'))
        javascript_to_python(temp_dir)
        assert_that(set(os.listdir(temp_dir)),
                    is_({'foo.py', 'bar.py', 'baz.txt'}))