>>> res = s.get("https://api.github.com/repos/python/cpython/pulls")
>>> commits_url = res.json()[0]['commits_url']
>>> commits = s.get(commits_url).json()
>>> print(commits[0]['commit']['message'])