requests_session = requests.Session()
requests_session.auth = functools.partial(sign,
    aws_session=boto3.Session(),
    region='us-east-1',
    service='es',
)