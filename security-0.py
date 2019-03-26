from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

class MyAdapter(HTTPAdapter):
    pass


s = requests.Session()
s.mount('https://', MyAdapter())