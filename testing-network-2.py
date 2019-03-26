@attr.s(frozen=True)
class Gist:

    files = attr.ib()

@attr.s(frozen=True):
class Response:

    content = attr.ib()

    def json(self):
        return json.loads(content)

@attr.s(frozen=True)
class FakeSession:

    _gists = attr.ib()

    def get(self, url):
        parsed = hyperlink.URL.from_text(url)
        if parsed.host == 'api.github.com':
            tail = path.rsplit('/', 1)[-1]
            gist = self._gists[tail]
            res = dict(files={name: f'http://example.com/{tail}/{name}'
                              for name in gist.files})
            return Repsonse(json.dumps(res))
        if parsed.host == 'example.com':
            _ignored, gist, name = path.split('/')
            return Response(self.gists[gist][name])