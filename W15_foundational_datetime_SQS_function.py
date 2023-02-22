# Import SDK and libraries
import boto3
import datetime 
import time
import json

# Lambda function
def lambda_handler(event, context):
    # Get current date/time in UTC format (string)
    utc_ts = datetime.datetime.now().timestamp() 
    # Convert UTC format string to human readable format
    utc_hr = time.ctime(utc_ts) 
    # Get the service client
    sqs = boto3.client('sqs', region_name = 'us-east-2') 
    # Action to send message to SQS
    sqs.send_message( 
        # URL of the SQS queue you want to send a message to
        QueueUrl = "https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS", 
        # Contents of the message you want to send
        MessageBody = utc_hr) 
    return {
        'statusCode': 200,
        'body': json.dumps(utc_hr)
    }