with NamedTemporaryFile() as fp:
    fp.write("line 1\n")
    fp.write("line 2\n")
    fp.flush()
    function_taking_file_name(fp.name)