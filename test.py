#WORKS
import boto3
import datetime 
import time
import json

def lambda_handler(event, context):
    utc_ts = datetime.datetime.now().timestamp()
    utc_hr = time.ctime(utc_ts)
    sqs = boto3.client('sqs', region_name = 'us-east-2')
    sqs.send_message(
        QueueUrl = "https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS",
        MessageBody = utc_hr)
    return {
        'statusCode': 200,
        'body': json.dumps(utc_hr)
    }




