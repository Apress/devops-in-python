setenv =
    TMPDIR = {envtmpdir}
commands =
    python -m 'import os;os.makedirs(sys.argv[1])' {envtmpdir}
    # rest of test commands