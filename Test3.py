#lambda function

import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement
    now = datetime.now()
    date_time = now.strftime("%m-%d-%y %H:%M:%S")
    
    sqs = boto3.client('sqs')
    
    response = sqs.send_message(
        QueueUrl='https://sqs.us-west-2.amazonaws.com/542986597955/luitw15-queue',
        Messagebody=time_date)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    