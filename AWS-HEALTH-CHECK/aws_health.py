"""
Quick AWS Health Check - One file, easy to use
"""
import boto3

def quick_aws_check():
    """Quick check of AWS services"""
    print("🚀 Quick AWS Health Check")
    print("=" * 40)
    
    try:
        # Check EC2
        ec2 = boto3.client('ec2')
        instances = ec2.describe_instances()
        running_instances = sum(1 for r in instances['Reservations'] for i in r['Instances'] if i['State']['Name'] == 'running')
        print(f"🖥️  EC2: {running_instances} running instances")
        
        # Check S3
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()
        print(f"📦 S3: {len(buckets['Buckets'])} buckets")
        
        # Check IAM Users
        iam = boto3.client('iam')
        users = iam.list_users()
        print(f"👤 IAM: {len(users['Users'])} users")

        # check Lambda
        try:
            lambda_client = boto3.client('lambda')
            functions = lambda_client.list_functions()
            print(f"⚙️  Lambda: {len(functions['Functions'])} functions")
        except:
            print("⚙️  Lambda: Could not check (may not have permissions)")
        
        # check VPCs
        try:
            vpc = boto3.client('ec2')
            vpcs = vpc.describe_vpcs()
            print(f"🌐 VPC: {len(vpcs['Vpcs'])} VPCs")
        except:
            print("🌐 VPC: Could not check (may not have permissions)")
        
        # check EKS
        try:
            eks = boto3.client('eks')
            clusters = eks.list_clusters()
            print(f"📊 EKS: {len(clusters['clusters'])} clusters")
        except:
            print("📊 EKS: Could not check (may not have permissions)")
        
        # Check ECR
        try:
            ecr = boto3.client('ecr')
            repositories = ecr.describe_repositories()
            print(f"🛢️  ECR: {len(repositories['repositories'])} repositories")
        except:
            print("🛢️  ECR: Could not check (may not have permissions)")
        
        # Check CloudWatch Alarms
        try:
            cloudwatch = boto3.client('cloudwatch')
            alarms = cloudwatch.describe_alarms()
            print(f"⏰ CloudWatch: {len(alarms['MetricAlarms'])} alarms")
        except:
            print("⏰ CloudWatch: Could not check (may not have permissions)")
        
        # Check Route53
        try:
            route53 = boto3.client('route53')
            zones = route53.list_hosted_zones()
            print(f"🌍 Route53: {len(zones['HostedZones'])} hosted zones")
        except:
            print("🌍 Route53: Could not check (may not have permissions)")
        
        # check elb
        try:
            elb = boto3.client('elbv2')
            load_balancers = elb.describe_load_balancers()
            print(f"🔀 ELB: {len(load_balancers['LoadBalancers'])} load balancers")
        except:
            print("🔀 ELB: Could not check (may not have permissions)")
        
        # check cloudfront
        try:
            cloudfront = boto3.client('cloudfront')
            distributions = cloudfront.list_distributions()
            dist_count = len(distributions['DistributionList']['Items']) if 'Items' in distributions['DistributionList'] else 0
            print(f"🌐 CloudFront: {dist_count} distributions")
        except:
            print("🌐 CloudFront: Could not check (may not have permissions)")
        
        # check sns
        try:
            sns = boto3.client('sns')
            topics = sns.list_topics()
            print(f"🔔 SNS: {len(topics['Topics'])} topics")
        except:
            print("🔔 SNS: Could not check (may not have permissions)")
        # check secrets manager
        try:
            secretsmanager = boto3.client('secretsmanager')
            secrets = secretsmanager.list_secrets()
            print(f"🔐 Secrets Manager: {len(secrets['SecretList'])} secrets")
        except:
            print("🔐 Secrets Manager: Could not check (may not have permissions)")
        
        # check backup
        try:
            backup = boto3.client('backup')
            vaults = backup.list_backup_vaults()
            print(f"🗄️  Backup: {len(vaults['BackupVaultList'])} backup vaults")
        except:
            print("🗄️  Backup: Could not check (may not have permissions)")
        
        # Check RDS
        try:
            rds = boto3.client('rds')
            databases = rds.describe_db_instances()
            print(f"🗄️  RDS: {len(databases['DBInstances'])} databases")
        except:
            print("🗄️  RDS: Could not check (may not have permissions)")
        
        print("\n✅ All checks completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Check your AWS credentials and permissions")

#This is for running the program
if __name__ == "__main__":

    quick_aws_check()
