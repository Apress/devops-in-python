def javascript_to_python_2(dirname):
    for fname in glob.glob(os.path.join(dirname, "*.js")):
        os.rename(fname, fname[:3] + '.py')