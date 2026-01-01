# Dictionary 

student_prop ={
  "name" : "Vishal",
  "Age" : "21",
  "Course" : "BCA"
}
print("Age is:",student_prop["Age"])

s3_bucket =[
  {
    "Key": "photos/profile.jpg",
        "Size": 204822,  
        "LastModified": "2024-01-15T10:30:00",
        "StorageClass": "LOCAL"
  },
  {
    "Key": "photos/profile.jpg",
        "Size": 204800,  
        "LastModified": "2024-01-15T10:30:00",
        "StorageClass": "LOCAL" 
  },
  {
    "Key": "photos/profile.jpg",
        "Size": 203800, 
        "LastModified": "2024-01-15T10:30:00",
        "StorageClass": "STANDARD"
  }
]
print("S3 bucket containers are shown below: ")
for bucket in s3_bucket:
    print("s3-bucket size is:",bucket["StorageClass"])



# Real time task is get PULL request information on a repo using python
# using Kubernetes 



