import boto3 

client = boto3.client('s3', region_name='us-east-1')  

response = client.create_bucket(
    Bucket='vishal-demo-123', 
)

print("Bucket created successfully!")
print("Bucket owner: ")
print(f" ID: {response['Owner']['ID'
]}")
print(f"  Display Name: {response['Owner'].get('DisplayName', 'N/A')}")
