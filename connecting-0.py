with contextlib.context(SSHClient()) as client:
    client.connect(some_host)
    ## Do things with client