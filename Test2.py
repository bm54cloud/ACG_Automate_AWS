import boto3
import datetime 
from datetime import timedelta
import json


#utc_ts = datetime.datetime.now().timestamp()
#print(utc_ts)
#utc_hr = time.ctime(utc_ts)
#print(utc_hr)
mst = datetime.datetime.today() - timedelta(hours=7)
print()

def lambda_handler(event, context):
    mst = datetime.datetime.today() - timedelta(hours=7)
    sqs = boto3.client('sqs', region_name = 'us-east-2')
    sqs.send_message(
        QueueUrl = "https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS",
        MessageBody = mst)
    return {
        'statusCode': 200,
        'body': json.dumps(mst)
        }
        