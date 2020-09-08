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
    route_id = event['pathParameters']['route_id']
    obj = s3.Object('avengers.digicam.intek.edu.vn', route_id)
    body = obj.get()['Body'].read()
    message = {
        'route_data' : body.decode('utf-8'),
        'hello_message' : 'Hi, I wish you a great day.',
    }
    return {
        'statusCode': 200,
        'body': json.dumps(message),
    }
