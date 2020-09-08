import boto3
import botocore
import uuid

s3 = boto3.resource('s3',
                    aws_access_key_id='ASIAUCRC4HNLAJAPYTE6',
                    aws_secret_access_key='K3RpnDycgeTbLsC7Slfpn8iwgcQx2CrMgGslhN8w',
                    aws_session_token='FwoGZXIvYXdzEDIaDE7fUavF0EfK2fc4MCLHAcLHRsKjlImwZV2k8PbJFFNci3Hj4wMIdNQzCbtRPy9FWGpjYkSACDZzkZ+CFr1MrQODQ5/YZxyKI3ymZOVuDXMB4cwawGloKL57M+gdGdR9tNPL7bADrEdWJzwEJcjZtqA681H3QHD8oKiudvrvwPkIukvxT0T7YOb6LEIOBwnlB5PW/GASKT77fqkn1K3uvNLD/BEwbN+1GdvOesWNPZL2oa/JTC2wzsI3lGhE/yZUJ54wxJjV15gW181hzPPLowBNDiL4w4kog7eL+AUyLRkR7JQKy01UOvKGefHK/QnP1TKe+rjHxLZtzBv89F4bg4iIyz5E575+06gDHg=='
                    )

def store_route_aws_s3(route_data):
    bucket = s3.Bucket('avengers.digicam.intek.edu.vn')
    uuid_key = str(uuid.uuid1())
    bucket.put_object(Key=uuid_key, Body=route_data)
    return uuid_key


def get_route_aws_s3(route_uuid):
    obj = s3.Object('avengers.digicam.intek.edu.vn', route_uuid)
    body = obj.get()['Body'].read()
    return body.decode('utf-8')

{
  "route_id": "902b09ed",
  "event": {
    "resource": "/",
    "path": "/",
    "httpMethod": "POST",
    "headers": null,
    "multiValueHeaders": null,
    "queryStringParameters": null,
    "multiValueQueryStringParameters": null,
    "pathParameters": null,
    "stageVariables": null,
    "body": "{body:\"yo\"}",
    "isBase64Encoded": false
  }
}
