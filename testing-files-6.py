def touch(fname, content=''):
    with open(fname, 'a') as fpin:
        fpin.write(content)