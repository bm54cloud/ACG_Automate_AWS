import json
import boto3


# Get SNS client and adjust region as needed
sns = boto3.client('sns', region_name = 'us-east-2')

def lambda_handler(event, context):
    for record in event['Records']:
        print(record)
        response = record['body']
        print(response)
        
        pub_mess = sns.publish(
            TopicArn = 'arn:aws:sns:us-east-2:925367513330:W15_SNS_topic', 
            Message = response)
        print(pub_mess)  # This will print to CloudWatch
    
    else:
        print('No messages in the queue')
    return {
        'statusCode': 200,
        'body': json.dumps('')
    }
