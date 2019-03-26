from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

def sign(request, *, aws_session, region, service):
    aws_request = AWSRequest(
        method=request.method.upper(),
        url=to_canonical_url(request.url),
        data=request.body,
    )
    credentials = aws_session.get_credentials()
    SigV4Auth(credentials, service, region).add_auth(request)
    request.headers.update(**aws_request.headers.items())