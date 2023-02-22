# Import SDK and libraries
import boto3
import json

# Lambda function
#def lambda_handler(event, context):

    # Create SQS client and adjust region as needed
sqs = boto3.client('sqs', region_name = 'us-east-2') 
    # Receive message from SQS
response = sqs.receive_message(
    QueueUrl = 'https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS')
print(response)
#message = response['Messages']
#print(message)

    
   
    
# Send message to SNS topic
#sns = boto3.client('sns', region_name = 'us-east-2')
    
#pub_mess = sns.publish(TopicArn = 'arn:aws:sns:us-east-2:925367513330:W15_SNS_topic'
    ##Message = )