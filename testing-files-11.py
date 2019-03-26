def test_analyze_debian_paths():
    with get_temp_dir() as root:
        touch(os.path.join(root, 'foo.list'),
              content='deb http://foo.example.com\n')
        ret = list(analyze_debian_paths(relative_to=root))
        assert(ret, equals_to(['foo.example.com']))