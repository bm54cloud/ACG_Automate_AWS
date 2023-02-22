# Build a simple contact form using API gateway, SES, and Lambda
# Build form that client can fill out and submit
# Form will be sent to endpoint in API gateway, which will proxy the request to a Lambda function
# Lambda function will parse out the content of that request, saving the info to an Amazon DynamoDB table
# Lambda function will also reflect the data back to the user in an email using SES
# Contact form built using Bootstrap toolkit
# Use code with LinuxAcademy HTML file at https://github.com/linuxacademy/content-lambda-boto3/blob/master/WebApps/Contact-Form/webapp/index.html
# Use code with form.js at https://github.com/linuxacademy/content-lambda-boto3/blob/master/WebApps/Contact-Form/webapp/js/form.js
# Specify cross domain = True

# Go to DynamboDB console and create table
# Create new IAM role/policy using AWS service: Lambda, create policy with standard cloudwatch log statements, allow ses:SendEmail, allow ses:SendRawEmail, 
# allow dynamodb:PutItem to table ARN
# Go back and attach policy to new role

import json
import os
import uuid
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

CHARSET = 'UTF-8'
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
SENDER_EMAIL = os.environ['SENDER_EMAIL']  # Must be configured in SES
SES_REGION = 'us-east-1'


dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name=SES_REGION) #SES does not run in OHIO


def lambda_handler(event, context):
    print(event)
    data = json.loads(event['body'])
    print(json.dumps(data))

    try:

        content = 'Message from ' + \
            data['first_name'] + ' ' + data['last_name'] + '\n' + \
            data['company'] + '\n' + \
            data['address1'] + '\n' + \
            data['address2'] + '\n' + \
            data['city'] + '\n' + \
            data['state'] + '\n' + \
            data['zip'] + '\n' + \
            data['email'] + '\n' + \
            data['phone'] + '\n' + \
            data['budget'] + '\n' + \
            data['message']
        save_to_dynamodb(data)
        response = send_mail_to_user(data, content)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message Id:", response['MessageId'])

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": ""
    }

def save_to_dynamodb(data):
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
    table = dynamodb.Table(DYNAMODB_TABLE)
    item = {
        'id': str(uuid.uuid1()),
        'first_name': data['first_name'],  # required
        'last_name': data['last_name'],  # required
        'company': data['company'] if data['company'] else None,
        'address1': data['address1'] if data['address1'] else None,
        'address2': data['address2'] if data['address2'] else None,
        'city': data['city'] if data['city'] else None,
        'state': data['state'] if data['state'] else None,
        'zip': data['zip'] if data['zip'] else None,
        'email': data['email'],  # required
        'phone': data['phone'],  # required
        'budget': data['budget'],  # required
        'message': data['message'],  # required
        'createdAt': timestamp,
        'updatedAt': timestamp
    }
    table.put_item(Item=item)
    return


def send_mail_to_user(data, content):
    return ses.send_email(
        Source=SENDER_EMAIL,
        Destination={
            'ToAddresses': [
                data['email'],
            ],
        },
        Message={
            'Subject': {
                'Charset': CHARSET,
                'Data': 'Thank you for contacting us!'
            },
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': content
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': content
                }
            }
        }
    )

# Set API Gateway
# Create new rest API, give it a name and regional endpoint, then create API
# Actions, create method, select psot, click checkmark, integrate with Lambda function, then Lambda proxy integration
# Select Lambda Region that is in same region as API gateway, Save
# Enable CORS -> POST, Actions, Enable CORS, leave defaults, click Enable CORS and replace existing CORS header
# Actions, Deploy API (have to select this if you make any changes to your API)
# New stage, name Prod, deploy
# Make note of API endpoint URL; use this in index.html file