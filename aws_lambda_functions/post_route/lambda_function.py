import json
import boto3
import uuid
import os

s3 = boto3.resource('s3',
                    aws_access_key_id=os.environ['aws_access_key_id'],
                    aws_secret_access_key=os.environ['aws_secret_access_key'],
                    aws_session_token=os.environ['aws_session_token'],
                    )

def lambda_handler(event, context):
    # TODO implement
    request_body = json.loads(event['body'])
    try:
        route_data = request_body['route_data']
        uuid_key = str(uuid.uuid1()).split('-')[0]

        bucket = s3.Bucket('avengers.digicam.intek.edu.vn')
        bucket.put_object(Key=uuid_key, Body=route_data)

        message = {
            "route_id" : uuid_key,
        }

        return {
            'statusCode': 200,
            'body': json.dumps(message),
        }

    except Exception as e:
        message_error = {
            "error" : "Your request is invalid, try again with new data",
        }
        return {
            'statusCode': 400,
            'body': json.dumps(message_error),
        }
