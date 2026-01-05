"""
AWS VPC Cleanup Script
Finds and deletes unused VPCs to save costs
"""
import boto3
import sys
from datetime import datetime, timedelta

class VPCCleaner:
    def __init__(self, region='ap-south-1', dry_run=True):
        self.region = region
        self.dry_run = dry_run
        self.ec2 = boto3.client('ec2', region_name=region)
        self.elbv2 = boto3.client('elbv2', region_name=region)
        self.rds = boto3.client('rds', region_name=region)
        self.ecs = boto3.client('ecs', region_name=region)
        
        self.unused_vpcs = []
        self.deleted_vpcs = []
        
    def find_unused_vpcs(self):
        """Find VPCs that have no active resources"""
        print("🔍 Scanning for unused VPCs...")
        print("=" * 60)
        
        # Get all VPCs
        response = self.ec2.describe_vpcs()
        all_vpcs = response['Vpcs']
        
        for vpc in all_vpcs:
            vpc_id = vpc['VpcId']
            vpc_name = self._get_vpc_name(vpc)
            is_default = vpc.get('IsDefault', False)
            
            print(f"\n📋 Checking VPC: {vpc_name} ({vpc_id})")
            
            # Skip default VPC
            if is_default:
                print(f"   ⏭️  Skipping: Default VPC (cannot delete)")
                continue
            
            # Check if VPC has resources
            has_resources = self._check_vpc_resources(vpc_id)
            
            if not has_resources:
                print(f"   ✅ UNUSED: No resources found")
                self.unused_vpcs.append({
                    'vpc_id': vpc_id,
                    'name': vpc_name,
                    'cidr': vpc.get('CidrBlock', 'N/A'),
                    'created_time': self._get_vpc_creation_time(vpc_id)
                })
            else:
                print(f"   🔄 IN USE: Has active resources")
        
        print(f"\n📊 Found {len(self.unused_vpcs)} unused VPCs")
        return self.unused_vpcs
    
    def _get_vpc_name(self, vpc):
        """Get VPC name from tags"""
        name = "Unnamed"
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
        return name
    
    def _check_vpc_resources(self, vpc_id):
        """Check if VPC has any resources"""
        checks = [
            self._check_ec2_instances,
            self._check_eni,
            self._check_load_balancers,
            self._check_nat_gateways,
            self._check_vpc_endpoints,
            self._check_rds_instances,
            self._check_ecs_clusters,
            self._check_subnets,
            self._check_peering_connections,
            self._check_vpn_connections
        ]
        
        for check_func in checks:
            if check_func(vpc_id):
                return True
        
        return False
    
    def _check_ec2_instances(self, vpc_id):
        """Check for EC2 instances in VPC"""
        try:
            response = self.ec2.describe_instances(
                Filters=[
                    {'Name': 'vpc-id', 'Values': [vpc_id]},
                    {'Name': 'instance-state-name', 'Values': ['pending', 'running', 'stopped']}
                ]
            )
            
            instances = []
            for reservation in response['Reservations']:
                instances.extend(reservation['Instances'])
            
            if instances:
                print(f"   🖥️  EC2 Instances: {len(instances)}")
                return True
        except Exception as e:
            print(f"   ⚠️  EC2 check error: {e}")
        
        return False
    
    def _check_eni(self, vpc_id):
        """Check for Elastic Network Interfaces"""
        try:
            response = self.ec2.describe_network_interfaces(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            if response['NetworkInterfaces']:
                print(f"   🔌 ENIs: {len(response['NetworkInterfaces'])}")
                return True
        except:
            pass
        
        return False
    
    def _check_load_balancers(self, vpc_id):
        """Check for ALB/NLB"""
        try:
            response = self.elbv2.describe_load_balancers()
            
            for lb in response['LoadBalancers']:
                if lb.get('VpcId') == vpc_id:
                    print(f"   ⚖️  Load Balancer: {lb['LoadBalancerName']}")
                    return True
        except:
            pass
        
        return False
    
    def _check_nat_gateways(self, vpc_id):
        """Check for NAT Gateways"""
        try:
            response = self.ec2.describe_nat_gateways(
                Filter=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            if response['NatGateways']:
                print(f"   🌐 NAT Gateways: {len(response['NatGateways'])}")
                return True
        except:
            pass
        
        return False
    
    def _check_rds_instances(self, vpc_id):
        """Check for RDS instances"""
        try:
            response = self.rds.describe_db_instances()
            
            for db in response['DBInstances']:
                if db.get('DBSubnetGroup', {}).get('VpcId') == vpc_id:
                    print(f"   🗄️  RDS Instance: {db['DBInstanceIdentifier']}")
                    return True
        except:
            pass
        
        return False
    
    def _check_subnets(self, vpc_id):
        """Check for subnets with resources"""
        try:
            # Get all subnets in VPC
            subnets = self.ec2.describe_subnets(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for subnet in subnets['Subnets']:
                subnet_id = subnet['SubnetId']
                
                # Check if subnet has any network interfaces
                enis = self.ec2.describe_network_interfaces(
                    Filters=[{'Name': 'subnet-id', 'Values': [subnet_id]}]
                )
                
                if enis['NetworkInterfaces']:
                    print(f"   📍 Subnet {subnet_id} has ENIs")
                    return True
        except:
            pass
        
        return False
    
    def _check_vpc_endpoints(self, vpc_id):
        """Check for VPC endpoints"""
        try:
            response = self.ec2.describe_vpc_endpoints(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            if response['VpcEndpoints']:
                print(f"   🔗 VPC Endpoints: {len(response['VpcEndpoints'])}")
                return True
        except:
            pass
        
        return False
    
    def _check_ecs_clusters(self, vpc_id):
        """Check for ECS clusters"""
        try:
            response = self.ecs.list_clusters()
            
            for cluster_arn in response['clusterArns']:
                cluster_name = cluster_arn.split('/')[-1]
                
                # Get cluster details
                cluster_details = self.ecs.describe_clusters(clusters=[cluster_arn])
                
                # Check if cluster uses this VPC (simplified check)
                print(f"   🐳 ECS Cluster: {cluster_name}")
                return True
        except:
            pass
        
        return False
    
    def _check_peering_connections(self, vpc_id):
        """Check for VPC peering connections"""
        try:
            response = self.ec2.describe_vpc_peering_connections(
                Filters=[
                    {'Name': 'requester-vpc-info.vpc-id', 'Values': [vpc_id]},
                    {'Name': 'status-code', 'Values': ['active']}
                ]
            )
            
            if response['VpcPeeringConnections']:
                print(f"   🤝 VPC Peering: {len(response['VpcPeeringConnections'])}")
                return True
        except:
            pass
        
        return False
    
    def _check_vpn_connections(self, vpc_id):
        """Check for VPN connections"""
        try:
            response = self.ec2.describe_vpn_connections(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            if response['VpnConnections']:
                print(f"   🔐 VPN Connections: {len(response['VpnConnections'])}")
                return True
        except:
            pass
        
        return False
    
    def _get_vpc_creation_time(self, vpc_id):
        """Get VPC creation time from tags or estimate"""
        try:
            response = self.ec2.describe_vpcs(VpcIds=[vpc_id])
            vpc = response['Vpcs'][0]
            
            # Check for creation time tag
            if 'Tags' in vpc:
                for tag in vpc['Tags']:
                    if tag['Key'] == 'CreationTime':
                        return tag['Value']
        except:
            pass
        
        return "Unknown"
    
    def delete_unused_vpcs(self):
        """Delete unused VPCs"""
        if not self.unused_vpcs:
            print("❌ No unused VPCs found to delete")
            return []
        
        print(f"\n🗑️  Ready to delete {len(self.unused_vpcs)} VPCs")
        print("=" * 60)
        
        for vpc_info in self.unused_vpcs:
            vpc_id = vpc_info['vpc_id']
            vpc_name = vpc_info['name']
            
            print(f"\n📦 VPC: {vpc_name} ({vpc_id})")
            print(f"   CIDR: {vpc_info['cidr']}")
            print(f"   Created: {vpc_info['created_time']}")
            
            if self.dry_run:
                print(f"   🧪 DRY RUN: Would delete VPC")
                self.deleted_vpcs.append(vpc_info)
            else:
                print(f"   🗑️  DELETING VPC...")
                
                try:
                    # Delete VPC and all its components
                    success = self._delete_vpc_components(vpc_id)
                    
                    if success:
                        print(f"   ✅ Successfully deleted VPC")
                        self.deleted_vpcs.append(vpc_info)
                    else:
                        print(f"   ❌ Failed to delete VPC")
                except Exception as e:
                    print(f"   ❌ Error deleting VPC: {e}")
        
        return self.deleted_vpcs
    
    def _delete_vpc_components(self, vpc_id):
        """Delete all components of a VPC before deleting VPC"""
        try:
            # 1. Delete NAT Gateways
            self._delete_nat_gateways(vpc_id)
            
            # 2. Delete VPC Endpoints
            self._delete_vpc_endpoints(vpc_id)
            
            # 3. Delete Internet Gateway
            self._delete_internet_gateway(vpc_id)
            
            # 4. Delete Subnets
            self._delete_subnets(vpc_id)
            
            # 5. Delete Route Tables (except main)
            self._delete_route_tables(vpc_id)
            
            # 6. Delete Network ACLs (except default)
            self._delete_network_acls(vpc_id)
            
            # 7. Delete Security Groups (except default)
            self._delete_security_groups(vpc_id)
            
            # 8. Finally, delete VPC
            self.ec2.delete_vpc(VpcId=vpc_id)
            
            return True
            
        except Exception as e:
            print(f"   ⚠️  Error in cleanup: {e}")
            return False
    
    def _delete_nat_gateways(self, vpc_id):
        """Delete NAT Gateways"""
        try:
            nat_gateways = self.ec2.describe_nat_gateways(
                Filter=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for nat in nat_gateways.get('NatGateways', []):
                nat_id = nat['NatGatewayId']
                state = nat['State']
                
                if state != 'deleted':
                    print(f"      Deleting NAT Gateway: {nat_id}")
                    self.ec2.delete_nat_gateway(NatGatewayId=nat_id)
                    
                    # Wait for deletion
                    waiter = self.ec2.get_waiter('nat_gateway_deleted')
                    waiter.wait(NatGatewayIds=[nat_id])
        except:
            pass
    
    def _delete_vpc_endpoints(self, vpc_id):
        """Delete VPC Endpoints"""
        try:
            endpoints = self.ec2.describe_vpc_endpoints(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for endpoint in endpoints.get('VpcEndpoints', []):
                endpoint_id = endpoint['VpcEndpointId']
                print(f"      Deleting VPC Endpoint: {endpoint_id}")
                self.ec2.delete_vpc_endpoints(VpcEndpointIds=[endpoint_id])
        except:
            pass
    
    def _delete_internet_gateway(self, vpc_id):
        """Detach and delete Internet Gateway"""
        try:
            # Get Internet Gateway for VPC
            igws = self.ec2.describe_internet_gateways(
                Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}]
            )
            
            for igw in igws.get('InternetGateways', []):
                igw_id = igw['InternetGatewayId']
                
                # Detach from VPC
                print(f"      Detaching Internet Gateway: {igw_id}")
                self.ec2.detach_internet_gateway(
                    InternetGatewayId=igw_id,
                    VpcId=vpc_id
                )
                
                # Delete Internet Gateway
                print(f"      Deleting Internet Gateway: {igw_id}")
                self.ec2.delete_internet_gateway(InternetGatewayId=igw_id)
        except:
            pass
    
    def _delete_subnets(self, vpc_id):
        """Delete all subnets in VPC"""
        try:
            subnets = self.ec2.describe_subnets(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for subnet in subnets.get('Subnets', []):
                subnet_id = subnet['SubnetId']
                print(f"      Deleting Subnet: {subnet_id}")
                self.ec2.delete_subnet(SubnetId=subnet_id)
        except:
            pass
    
    def _delete_route_tables(self, vpc_id):
        """Delete non-main route tables"""
        try:
            route_tables = self.ec2.describe_route_tables(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for rt in route_tables.get('RouteTables', []):
                rt_id = rt['RouteTableId']
                
                # Skip main route table
                if not any(assoc.get('Main', False) for assoc in rt.get('Associations', [])):
                    print(f"      Deleting Route Table: {rt_id}")
                    self.ec2.delete_route_table(RouteTableId=rt_id)
        except:
            pass
    
    def _delete_network_acls(self, vpc_id):
        """Delete non-default Network ACLs"""
        try:
            acls = self.ec2.describe_network_acls(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for acl in acls.get('NetworkAcls', []):
                acl_id = acl['NetworkAclId']
                
                # Skip default ACL
                if not acl.get('IsDefault', False):
                    print(f"      Deleting Network ACL: {acl_id}")
                    self.ec2.delete_network_acl(NetworkAclId=acl_id)
        except:
            pass
    
    def _delete_security_groups(self, vpc_id):
        """Delete non-default Security Groups"""
        try:
            sgs = self.ec2.describe_security_groups(
                Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
            )
            
            for sg in sgs.get('SecurityGroups', []):
                sg_id = sg['GroupId']
                sg_name = sg['GroupName']
                
                # Skip default security group
                if sg_name != 'default':
                    print(f"      Deleting Security Group: {sg_name} ({sg_id})")
                    self.ec2.delete_security_group(GroupId=sg_id)
        except:
            pass
    
    def generate_report(self):
        """Generate cleanup report"""
        if not self.deleted_vpcs and not self.unused_vpcs:
            print("📊 No VPCs analyzed")
            return
        
        print("\n" + "=" * 60)
        print("📊 VPC CLEANUP REPORT")
        print("=" * 60)
        
        if self.unused_vpcs:
            print(f"\n🔍 Unused VPCs Found: {len(self.unused_vpcs)}")
            for vpc in self.unused_vpcs:
                status = "✅ DELETED" if vpc in self.deleted_vpcs else "⏳ Pending"
                print(f"   • {vpc['name']} ({vpc['vpc_id']}) - {status}")
        
        if self.deleted_vpcs:
            print(f"\n🗑️  VPCs Deleted: {len(self.deleted_vpcs)}")
            for vpc in self.deleted_vpcs:
                print(f"   • {vpc['name']} ({vpc['vpc_id']})")
        
        # Cost savings estimate
        # Each VPC costs ~$0.10 per hour for NAT Gateway + other resources
        estimated_savings = len(self.deleted_vpcs) * 0.10 * 24 * 30  # Monthly savings
        print(f"\n💰 Estimated Monthly Savings: ${estimated_savings:.2f}")
        print(f"💰 Estimated Yearly Savings: ${estimated_savings * 12:.2f}")
        
        print(f"\nMode: {'DRY RUN' if self.dry_run else 'LIVE DELETION'}")
        print("=" * 60)

def main():
    """Main function with command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='AWS VPC Cleanup Tool')
    parser.add_argument('--region', default='ap-south-1', help='AWS region')
    parser.add_argument('--dry-run', action='store_true', default=True, 
                       help='Dry run mode (default: True)')
    parser.add_argument('--live', action='store_true', 
                       help='Live mode (actually delete VPCs)')
    parser.add_argument('--vpc-id', help='Specific VPC ID to check')
    
    args = parser.parse_args()
    
    # If --live is specified, disable dry run
    if args.live:
        args.dry_run = False
    
    print("🚀 AWS VPC Cleanup Tool")
    print(f"📍 Region: {args.region}")
    print(f"🔧 Mode: {'DRY RUN' if args.dry_run else 'LIVE DELETION'}")
    print("=" * 60)
    
    # Ask for confirmation in live mode
    if not args.dry_run:
        response = input("\n⚠️  WARNING: This will DELETE VPCs permanently!\nType 'DELETE' to continue: ")
        if response != 'DELETE':
            print("❌ Operation cancelled")
            sys.exit(1)
    
    # Create cleaner instance
    cleaner = VPCCleaner(region=args.region, dry_run=args.dry_run)
    
    # Find unused VPCs
    unused_vpcs = cleaner.find_unused_vpcs()
    
    if unused_vpcs:
        # Ask for confirmation before deletion
        if not args.dry_run:
            print(f"\n⚠️  About to delete {len(unused_vpcs)} VPCs")
            response = input("Proceed? (yes/no): ")
            if response.lower() != 'yes':
                print("❌ Deletion cancelled")
                sys.exit(0)
        
        # Delete VPCs
        deleted = cleaner.delete_unused_vpcs()
        
        # Generate report
        cleaner.generate_report()
    else:
        print("\n✅ No unused VPCs found. All VPCs have active resources.")

if __name__ == "__main__":
    main()