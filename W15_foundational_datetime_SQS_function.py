# Import libraries
import boto3
import datetime 
import time
import json

# Lambda function
def lambda_handler(event, context):
    utc_ts = datetime.datetime.now().timestamp() # Gets current date/time in UTC format (string)
    utc_hr = time.ctime(utc_ts) # Converts UTC format string to human readable format
    sqs = boto3.client('sqs', region_name = 'us-east-2') # Get the service client
    sqs.send_message( # Action to send message to SQS
        QueueUrl = "https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS", # URL of the SQS queue you want to send a message to
        MessageBody = utc_hr) # Contents of the message you want to send
    return {
        'statusCode': 200,
        'body': json.dumps(utc_hr)
    }