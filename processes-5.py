with tempfile.TemporaryFile() as fp:
    fp.write(contents)
    fp.write(of)
    fp.write(email)
    fp.flush()
    fp.seek(0)
    proc = Popen(["sendmail"], stdin=fp)
    result = proc.poll()