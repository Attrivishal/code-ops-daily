# here we see how to start an EC2 instance using boto3
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

instance_id=(input("Write Your instance ID to start: "))

ec2.start_instances(InstanceIds=[instance_id])
print(f"🚀 Starting {instance_id}...")
print("Takes 1-2 minute to be ready.")