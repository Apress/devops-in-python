[testenv:py27-wheel]
skip_install = True
deps =
      coverage
      Twisted
      wheel
      gather
commands =
      mkdir -p {envtmpdir}/dist
      pip wheel . --no-deps --wheel-dir {envtmpdir}/dist
      sh -c "pip install --no-index {envtmpdir}/dist/*.whl"
      coverage run {envbindir}/trial \
               --temp-directory build/_trial_temp {posargs:ncolony}
      coverage report --include */site-packages/ncolony* \
                      --omit */tests/*,*/interfaces*,*/_version* \
                      --show-missing --fail-under=100