# here we are seeing a simple example of stopping EC2 instances using boto3

import boto3 

ec2 = boto3.client('ec2', region_name= 'ap-south-1')

# # Get your instance ID from list_ec2.py
instance_id = input("Instance ID to stop: ")

ec2.stop_instances(InstanceIds=[instance_id])
print(f"🛑 Stopping {instance_id}...")
print("Takes 1 minute. Check with: python3 list_ec2.py")