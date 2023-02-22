# Create SNS topic

# Import SDK
import boto3

# Call the SNS client
client = boto3.client('sns') 

# Use the create_topic action to create an SNS topic; Name is recquired
sns_topic = client.create_topic(Name='W15_SNS_topic') 
 