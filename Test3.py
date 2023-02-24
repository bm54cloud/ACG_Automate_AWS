# Import SDK and libraries
import boto3
import json

# Lambda function
def lambda_handler(event, context):
    # Get SQS client and adjust region as needed
    sqs = boto3.client('sqs', region_name = 'us-east-2') 
    
    # Receive message from SQS using URL of the queue
    response = sqs.receive_message(QueueUrl = 'https://sqs.us-east-2.amazonaws.com/925367513330/W15_SQS')
    has_messages = 'Messages' in response 
    if has_messages == True:
        # Get SNS client and adjust region as needed
        sns = boto3.client('sns', region_name = 'us-east-2')
        messages = response['Messages']
        for message in messages:
            body = message['Body']
          
            # Publish message to SNS topic
            pub_mess = sns.publish(
                TopicArn = 'arn:aws:sns:us-east-2:925367513330:W15_SNS_topic', 
                Message = body)
            print(pub_mess)  # This will print to CloudWatch
    
    else:
        print('No messages in the queue')
        
    return {
        'statusCode': 200,
        'body': json.dumps('')
    }

