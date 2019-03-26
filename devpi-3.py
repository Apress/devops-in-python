$ mkdir -p ~/.pip && cat > ~/.pip/pip.conf << EOF
[global]
index-url = http://localhost:3141/root/pypi/+simple/

[search]
index = http://localhost:3141/root/pypi/