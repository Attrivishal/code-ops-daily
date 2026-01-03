# List ALL S3 Buckets in Your AWS Account
# This shows buckets from ANY file/script that created them

import boto3

print("=== Listing ALL Your S3 Buckets ===")

# Connect to S3 (region doesn't matter for listing)
s3 = boto3.client('s3')

# get all buckets
buckets = s3.list_buckets()['Buckets']

print(f"Total buckets: {len(buckets)}")
print("~" * 30)
for bucket in buckets:
    print(f" - {bucket['Name']}")