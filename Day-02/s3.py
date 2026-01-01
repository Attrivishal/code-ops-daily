# aws_final.py - Works after boto3 installed
import boto3 # type: ignore

def create_s3():
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(
            Bucket='my-bucket-12345',  # Change to unique name
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            }
        )
        print("✅ S3 bucket created!")
    except Exception as e:
        print(f"Error: {e}")

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("Your buckets:")
    for bucket in response['Buckets']:
        print(f"  - {bucket['Name']}")

# Test it
list_buckets()
# create_s3()  # Uncomment to createclear
