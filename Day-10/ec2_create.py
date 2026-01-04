"""
Step 1: Create Your First EC2 Instance
Simple script to launch an EC2 virtual server
"""

import boto3

print("\n=== Creating my First EC2 intance ===")
print("Region: ap-south-1 (Mumbai)")
print("Instance Type: t2.micro (Free Tier eligible)")
print("_" *40)

# Connect to EC2
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Ask for instance name 
instance_name = input("Enter a name for your instance: ").strip()

# Create EC2 instance
print(f"\n Launching EC2 instance '{instance_name}'...")
print("This may take a few minutes...")
try:
  # launch instance
  response = ec2.run_instances(
    ImageId='ami-0f5ee92e2d63afc18',  # Amazon Linux 2 AMI (HVM), SSD Volume Type
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='MyWebServer-Key',  # Change to your key pair name
    TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': instance_name},
                    {'Key': 'CreatedBy', 'Value': 'Boto3'},
                    {'Key': 'Purpose', 'Value': 'Learning'}
                ]
            }
        ]
  )
  # 4. Show results
  instance_id = response['Instances'][0]['InstanceId']
    
  print(f"\n✅ SUCCESS!")
  print(f"Instance ID: {instance_id}")
  print(f"Instance Name: {instance_name}")
  print(f"Type: t2.micro (Free Tier)")
  print(f"Region: ap-south-1 (Mumbai)")
    
  print("\n📋 Next Steps:")
  print("1. Wait 2 minutes for instance to start")
  print("2. Check AWS Console: https://ap-south-1.console.aws.amazon.com/ec2")
  print("3. Run: python list_ec2.py (we'll create this next)")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\n🔧 Common Fixes:")
    print("1. Check AWS credentials: aws configure")
    print("2. Create a Key Pair in AWS Console:")
    print("   - Go to EC2 → Key Pairs → Create")
    print("   - Name: 'boto3-key' (or update line 33)")
    print("3. Check IAM permissions")
