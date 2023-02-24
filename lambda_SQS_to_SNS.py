# Import SDK and librarires
import boto3
import json

# Create Lambda function
def lambda_handler(event, context):
    sns = boto3.client('sns', region_name = 'us-east-2') # Call the SNS client and assign the Region 
    for message in event['Records']: # Iterate through the event 'Records' (event is the SQS Trigger)
        print(message) # Print message to CloudWatch for tracking purposes (optional)
        body = message['body'] # Call the 'body' object from 'Records' as this contains your SQS message
        pub_mess = sns.publish( # Publish the 'body' message to the Topic via its specific ARN
            TopicArn = 'arn:aws:sns:us-east-2:925367513330:W15_SNS_topic', 
            Message = body)
        print(pub_mess) # Print pub_mess to CloudWatch for tracking purposes (optional)
        
    return { 
        'statusCode': 200
    }
    
  