def get_files(gist_id, session=None):
    if session is None:
        session = requests.Session()
    gist = session.get(f"https://api.github.com/gists/{gist_id}").json()
    result = {}
    for name, details in gist["files"].items():
        result[name] = session.get(details["raw_url"]).content
    return result