# here we see just a simple example of listing EC2 instances using boto3

import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.describe_instances()

print("\n=== Listing EC2 Instances ===")
print("Region: ap-south-1 (Mumbai)")
print("_" *40)

for res in response['Reservations']:
  for inst in res['Instances']:
    name = "N/A"
  if 'Tags' in inst:
      for tag in inst['Tags']:
        if tag['Key'] == 'Name':
          name = tag['Value']

        print(f"{name}: {inst['InstanceId']} - {inst['State']['Name']}")
