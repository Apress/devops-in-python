(devpi)$ pip install devpi-client twine
(devpi)$ devpi use http://localhost:3141
(devpi)$ devpi user -c testuser password=123
(devpi)$ devpi login testuser --password=123
(devpi)$ devpi index -c dev bases=root/pypi
(devpi)$ devpi use testuser/dev
(devpi)$ twine upload --repository http://localhost:3141/testuser/dev \
               -u testuser -p 123 my-package-18.6.0.tar.gz
(devpi)$ pip install -i http://localhost:3141/testuser/dev my-package