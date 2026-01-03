import boto3 
# here we are going to delete a bucket
s3 = boto3.client('s3')
print("=== Deleting an S3 Bucket ===")

# listing all buckets to choose from

try:
    buckets =s3.list_buckets()['Buckets']
    print(f"Your Buckets Are:{len(buckets)} ")
    print("~" *30)
    for bucket in buckets:
      print (f" - {bucket['Name']}")

    # ask for bucket name to delete
    bucket_name = input("Enter the bucket name you want to delete: ").strip().lower()

    # delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f" Bucket -> {bucket_name} deleted successfully!")

except Exception as e:
    print(f" Error: {e}")
    print("\n Common fixes:")
    print("1. Make sure the bucket is empty")
    print("2. Check if bucket name is correct")
    print("3. Verify AWS credentials are set")