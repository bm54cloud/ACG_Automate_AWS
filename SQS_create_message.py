import boto3

sqs = boto3.client('sqs', region_name = 'us-east-2')

response = sqs.send_message(
    QueueUrl = 'https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS_2',
    MessageBody = 'This is a test to trigger Lambda SQS_trig_to_SNS')

print('Message Sent to Lambda SQS_trig_to_SNS')