import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name = 'us-east-2')

# Create the queue with name and attributes
queue = sqs.create_queue(
  QueueName='W15_SQS', 
  Attributes={'DelaySeconds': '5', 'VisibilityTimeout': '60'})

# Print queue url that is created
print(queue.url)
