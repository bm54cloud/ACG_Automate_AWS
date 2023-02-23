# Import SDK and libraries
import boto3
import json

# Lambda function
#def lambda_handler(event, context):

#THIS WORKS
# Create SQS client and adjust region as needed
# for loop and interate through, call publish on each interation
sqs = boto3.client('sqs', region_name = 'us-east-2') 
# Receive message from SQS using URL of the queue
response = sqs.receive_message(QueueUrl = 'https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS_2')

message = response['Messages'][0]['Body']
print(message) # This will print to CloudWatch

# make this into a function that takes string value and call publish 
# Send message to SNS topic
sns = boto3.client('sns', region_name = 'us-east-2')
    
pub_mess = sns.publish(
    TopicArn = 'arn:aws:sns:us-east-2:925367513330:W15_SNS_topic', 
    Message = message)
print(pub_mess)