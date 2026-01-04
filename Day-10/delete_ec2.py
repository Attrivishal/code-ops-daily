# here we see how to delete an EC2 instance using boto3

import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

instance_id = input("Instance ID to DELETE: ")
print("⚠️  WARNING: This PERMANENTLY deletes the instance!")
confirm = input(f"Type 'DELETE' to confirm: ")

if confirm == 'DELETE':
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"🗑️  Deleting {instance_id}...")
    print("Takes 2-3 minutes to completely remove.")
else:
    print("✅ Cancelled.")