def javascript_to_python_1(dirname):
    for fname in os.listdir(dirname):
        if fname.endswith('.js'):
            os.rename(fname, fname[:3] + '.py')