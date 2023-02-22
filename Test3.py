import boto3

sqs = boto3.client('sqs', region_name = 'us-east-2')

response = sqs.receive_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS'
)

messages = response['Messages']

for message in messages:
    data = message['Body']
    print(data)