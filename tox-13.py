[testenv:docs]
changedir = docs
deps =
    sphinx
    Twisted
commands =
    sphinx-build -W -b html -d {envtmpdir}/doctrees . {envtmpdir}/html
basepython = python2.7