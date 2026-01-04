"""
Simple S3 Toolkit
Create, list, delete S3 buckets and upload files
"""

import boto3
import os

def s3_toolkit():
    print("\n=== S3 Toolkit ===")
    print("1. Create bucket")
    print("2. List buckets")  
    print("3. Delete bucket")
    print("4. Upload file")
    print("5. List files in bucket")
    print("6. Exit")
    
    # Get user choice
    try:
        choice = int(input("Choose option (1-6): "))  # Changed to 1-6
    except:
        print("Please enter a number 1-6")  # Changed to 1-6
        return False
    
    # Connect to S3
    s3 = boto3.client('s3', region_name='ap-south-1')
    
    # Option 1: Create bucket
    if choice == 1:
        name = input("Bucket name: ").strip().lower()
        
        # Basic name check
        if len(name) < 3 or len(name) > 63:
            print("Name must be 3-63 characters")
            return False
        
        try:
            s3.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
            )
            print(f"Created: {name}")
        except Exception as e:
            print(f"Error: {e}")
    
    # Option 2: List buckets
    elif choice == 2:
        try:
            buckets = s3.list_buckets()['Buckets']
            if buckets:
                print(f"You have {len(buckets)} bucket(s):")
                for bucket in buckets:
                    print(f"  • {bucket['Name']}")
            else:
                print("No buckets found")
        except Exception as e:
            print(f"Error: {e}")
    
    # Option 3: Delete bucket  
    elif choice == 3:
        name = input("Bucket to delete: ").strip()
        
        try:
            # Check if bucket has files
            files = s3.list_objects_v2(Bucket=name)
            if 'Contents' in files:
                print(f"Bucket has {len(files['Contents'])} files")
                confirm = input("Delete anyway? (yes/no): ")
                if confirm != 'yes':
                    print("Cancelled")
                    return False
                
                # Delete files first
                for file in files['Contents']:
                    s3.delete_object(Bucket=name, Key=file['Key'])
            
            # Delete bucket
            s3.delete_bucket(Bucket=name)
            print(f"Deleted: {name}")
        except Exception as e:
            print(f"Error: {e}")
    
    # Option 4: Upload file
    elif choice == 4:
        bucket = input("Bucket name: ").strip()
        filename = input("File to upload: ").strip()
        
        # Check if file exists
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            return False
        
        try:
            s3.upload_file(filename, bucket, filename)
            print(f"Uploaded {filename} to {bucket}")
        except Exception as e:
            print(f"Error: {e}")

    # Option 5: List files in bucket
    elif choice == 5:  # ✅ FIXED: Proper indentation
        bucket = input("Bucket name: ").strip()
        
        try:
            # List all files in the bucket
            files = s3.list_objects_v2(Bucket=bucket)
            
            if 'Contents' in files:
                print(f"\nFiles in '{bucket}':")
                for item in files['Contents']:
                    size_kb = item['Size'] / 1024
                    modified = item['LastModified'].strftime("%Y-%m-%d %H:%M")
                    print(f"  • {item['Key']}")
                    print(f"    Size: {size_kb:.1f} KB, Modified: {modified}")
            else:
                print(f"No files found in '{bucket}'")
                
        except Exception as e:
            print(f"Error: {e}")

    # Option 6: Exit
    elif choice == 6:  # ✅ FIXED: Proper indentation
        print("Thank you for using AWS S3 Toolkit. Goodbye!")
        return True  # Stop the loop
    
    # Invalid choice
    else:
        print("Please choose 1-6")  # Changed to 1-6
    
    return False  # Continue running

# Main program
print("AWS S3 Toolkit")
print("Region: ap-south-1 (Mumbai)")
print("-" * 30)

# Run until user exits
while True:
    if s3_toolkit():
        break
    print() 