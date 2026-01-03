# Creation of Bucket with real life AWS credentials

# first we have to import boto3 library
import boto3

print("=== Creating My First bucket  ===")

# We have to connect first to S3 service WITH REGION
s3 = boto3.client('s3', region_name='ap-south-1')

# ask for bucket name
bucket_name = input("Enter your bucket name: (must be unique all times): ").strip().lower()

# create the bucket WITH LocationConstraint
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'  

    }
)

print(f" Bucket -> {bucket_name} created successfully in ap-south-1!")

#  this is how we upoload a file to the bucket
file_name = "my_test_file.txt"
with open(file_name, 'w') as f:
    f.write(f"This file was uploaded to bucket: {bucket_name}\n")
    f.write("Created using Boto3 Python script.\n")

print(f"\n Created test file: {file_name}")

# Upload the file
s3.upload_file(file_name, bucket_name, file_name)
print(f" Uploaded {file_name} to bucket {bucket_name}")
print(f"\n Access your file at:")
