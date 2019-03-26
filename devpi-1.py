(playground)$ pip install \
              -i http://localhost:3141/root/pypi/+simple/ \
              httpie glom
(playground)$ http --body https://httpbin.org/get | glom '{"url":"url"}'
{
  "url": "https://httpbin.org/get"
}