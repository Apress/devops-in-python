deps =
    {py36,py27,pypy}-unit: coverage
    {py27,pypy}-lint: pylint==1.8.1
    {py27,pypy}-lint: flake8
    {py27,pypy}-lint: incremental
    {py36,py27,pypy}-{func,unit}: Twisted