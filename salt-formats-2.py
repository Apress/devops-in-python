#!py
def run():
    if __grains__['os'] == 'CentOS':
        package_name = 'python-devel'
    elif __grains__['os'] == 'Debian':
        package_name = 'python-dev'
    else:
        raise ValueError("Unrecognized operating system",
                         __grains__['os'])
return { package_name: dict(pkg='installed') }