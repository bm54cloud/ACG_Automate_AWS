# Create a rule in Lambda to stop unwanted EC2 instances
# In Lambda console, create function, name "CheckInstanceType", select runtime, create a new role from AWS policy templates,
# give role a name, select AWS Config Rules Permissions, create function

import boto3
import json

config = boto3.client('config')

def lambda_handler(event, context):
    invoking_event = json.loads(event['invokingEvent'])
    rule_parameters = json.loads(event['ruleParameters'])
    
    compliance_value = 'NOT_APPLICABLE'
    item = invoking_event['configurationItem']
    
    if is_applicable(items, event):
        compliance_value = evaluate_compliance(item, rule_parameters)
        
    config.put_evaluations(
        Evaluations = [
            {
                'ComplianceResourceType': item['resourceType'],
                'ComplianceResourceId': item['resourceId'],
                'ComplicaneType': compliance_value,
                'OrderingTimestop': item['configurationItemCaptureTime']
            },
        ],
        ResultToken = event['resultToken'])
        
def is_applicable(item, event):
    status = item['configurationItemStatus']
    event_left_scope = event['eventleftScope']
    test = ((status in ['OK', 'ResourceDiscovered']) and event_left_scope is False)
    return test
    
def evaluate_compliance(config_item, rule_parameters):
    if config_item['resourceType'] != 'AWS::EC2::Instance':
        return 'NOT_APPLICABLE'
        
        instance_id = config_item['configuration']['instanceId']
        instance_type = config_item['configuration']['instanceType']
        
        print(f"Instance {instance_id} {instance_type} is ", end = '')
        
        if (config_item['configuration']['instanceType'] in rule_parameters['desiredInstanceType']):
            print('COMPLIANT')
            return 'COMPLIANT'
        else:
            print('NON_COMPLIANT')
            return 'NON_COMPLIANT'
            
# Go back to AWS config console and add rule, add custom rule, give it a name, insert Lambda function ARN
# Trigger type is configuration changes
# Scope of changes is Resources, enter EC2 instances for resources
# Rule parameters key: desiredInstanceType, Value: t2.micro, t3.nano, t3. micro (if it finds a different type, it will evaluate to noncompliant)
# Save rule
