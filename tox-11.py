commands =
    {py36,py27,pypy}-unit: python -Wall \
                                  -Wignore::DeprecationWarning \
                                  -m coverage \
                                  run -m twisted.trial \
                                  --temp-directory build/_trial_temp \
                                  {posargs:ncolony}
    {py36,py27,pypy}-unit: coverage report --include ncolony* \
                           --omit */tests/*,*/interfaces*,*/_version* \                                    --show-missing --fail-under=100
    py27-lint: pylint --rcfile admin/pylintrc ncolony
    py27-lint: python -m ncolony tests.nitpicker
    py27-lint: flake8 ncolony
    {py36,py27,pypy}-func: python -Werror -W ignore::DeprecationWarning \
                                  -W ignore::ImportWarning \
                                  -m ncolony tests.functional_test