import osimport boto3
from botocore.exceptions import ClientError

ROLE_ARN = os.environ['ROLE_ARN']

ec2 = boto3.client('ec2')
logs = boto3.cleint('logs')

def lambda_handler(event, context):
    try:
        # Extract the VPC ID from the event
        vpc_id = event['detail']['responseElements']['vpc']['vpcId']
        
        flow_logs_group = 'VPCFlowLogs-' + vpc_id
        
        print('VPC: ' + vpc_id) # This will print to CloudWatch logs
        
        try:
            response = logs.create_log_group(
                logGroupName = flow_logs_group)
        except ClientError:
            print(f"Log group '{flow_logs_group}' already exists.")
        
        # Determine if VPC flow logs are already enabled on VPC you created
        response = ec2.describe_flow_logs(
            Filter=[
                {
                    'Name': 'resource-id',
                    'Values': [
                        vpc_id,
                        ]
                    },
                ],
            )
        
        if len(response['FlowLogs']) > 0:
            print('VPC Flow Logs are ENABLED') # This will print to CloudWatch logs
        else:
            print('VPC FLow Logs are DISABLED. Enabling ... ')
            
            response = ec2.create_flow_logs(
                ResourceIds = [vpc_id],
                ResourceType = 'VPC',
                TrafficType = 'ALL',
                LogGroupName = flow_logs_group,
                DeliverLogsPermissionArn = ROLE_ARN,
            )
            
            print('Created Flow Logs: ' + response['FlowLogsIds'][0])
    
    except Exception as e:
        print('Error - reason "%s"' % str(e))
        