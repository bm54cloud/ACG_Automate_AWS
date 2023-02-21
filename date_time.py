import boto3
import datetime 
import time
import pytz
import json

def lambda_handler(event, context):
    utc_ts = datetime.datetime.now(pytz.utc)
    mst_ts = utc_ts.astimezone(pytz.timezone('US/Mountain'))
    sqs = boto3.client('sqs', region_name = 'us-east-2')
    sqs.send_message(
        QueueUrl = "https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS",
        MessageBody = mst_ts)
    return {
        'statusCode': 200,
        'body': json.dumps(mst_ts)
    }