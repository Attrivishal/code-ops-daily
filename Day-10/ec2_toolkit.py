"""
Simple EC2 Manager
Manage your AWS servers
"""

import boto3

def main():
    while True:
        print("\n--- EC2 Manager ---")
        print("1. List servers")
        print("2. Create server")
        print("3. Stop server")
        print("4. Start server")
        print("5. Delete server")
        print("6. Exit")
        
        choice = input("\nChoose 1-6: ")
        
        # Connect to AWS
        ec2 = boto3.client('ec2', region_name='ap-south-1')
        
        # 1. List servers
        if choice == '1':
            print("\nYour servers:")
            response = ec2.describe_instances()
            
            for res in response['Reservations']:
                for server in res['Instances']:
                    # Get server name
                    name = 'no-name'
                    if 'Tags' in server:
                        for tag in server['Tags']:
                            if tag['Key'] == 'Name':
                                name = tag['Value']
                    
                    print(f"{name} - {server['InstanceId']} - {server['State']['Name']}")
        
        # 2. Create server
        elif choice == '2':
            name = input("Server name: ")
            
            try:
                response = ec2.run_instances(
                    ImageId='ami-0f5ee92e2d63afc18',
                    InstanceType='t2.micro',
                    MinCount=1,
                    MaxCount=1,
                    KeyName='boto3-key',  # Change to your key
                    TagSpecifications=[{
                        'ResourceType': 'instance',
                        'Tags': [{'Key': 'Name', 'Value': name}]
                    }]
                )
                
                server_id = response['Instances'][0]['InstanceId']
                print(f"Created: {name} ({server_id})")
                print("Wait 2 minutes")
                
            except Exception as e:
                print(f"Error: {e}")
        
        # 3. Stop server
        elif choice == '3':
            server_id = input("Server ID to stop: ")
            
            try:
                ec2.stop_instances(InstanceIds=[server_id])
                print(f"Stopping {server_id}")
            except Exception as e:
                print(f"Error: {e}")
        
        # 4. Start server
        elif choice == '4':
            server_id = input("Server ID to start: ")
            
            try:
                ec2.start_instances(InstanceIds=[server_id])
                print(f"Starting {server_id}")
            except Exception as e:
                print(f"Error: {e}")
        
        # 5. Delete server
        elif choice == '5':
            server_id = input("Server ID to delete: ")
            
            confirm = input(f"Type 'delete' to delete {server_id}: ")
            
            if confirm == 'delete':
                try:
                    ec2.terminate_instances(InstanceIds=[server_id])
                    print(f"Deleting {server_id}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Cancelled")
        
        # 6. Exit
        elif choice == '6':
            print("Thank you for using EC2 Toolkit! Have a great day!")
            break
        
        # Wrong choice
        else:
            print("Choose 1-6 only")

# Run the program
if __name__ == "__main__":
    main()