import boto3


ec2_client = boto3.client('ec2')         # resource service client


AMI_id = 'ami-04b4f1a9cf54c11d0'  
instance_type = input("Input the instance type\n\t>> ") #'t2.micro'  
key_name = input("Input the ssh key name\n\t>> ")    # vockey

# function to list available VPCs and subnets
def list_vpcs_and_subnets():
    response = ec2_client.describe_vpcs()
    vpcs = response['Vpcs']
    print("Available VPCs:")
    for vpc in vpcs:
        print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}")
    
    vpc_id = input("Enter the VPC ID you want to use:\t")

    # Describe subnets in the selected VPC
    response = ec2_client.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    subnets = response['Subnets']
    print(f"Available subnets in VPC {vpc_id}:")
    for subnet in subnets:
        # Print Subnet details and Availability Zone
        subnet_id = subnet['SubnetId']
        cidr_block = subnet['CidrBlock']
        availability_zone = subnet['AvailabilityZone']
        print(f"Subnet ID: {subnet_id}, CIDR Block: {cidr_block}, Availability Zone: {availability_zone}")

    subnet_id = input("Enter the Subnet ID you want to use:\t")
    return vpc_id, subnet_id
    
# get VPC and Subnet details
vpc_id, subnet_id = list_vpcs_and_subnets()

# launch a new instance
while True:
    user_has_AMI = input('Do you have your own AMI image id? and your instance type?\n\t1 - Yes\n\t2 - No\n\t>> ')  # ask if the user has any instance image id

    if user_has_AMI == '1':
        AMI_id = input('Insert the AMI image id:\t')  # ask user for the id of the instance
        instance_type = input('Insert the instance type:\t')  # ask user for the id of the instance
        break

    elif user_has_AMI == '2':

        print(f'The default AMI image id is:\t{AMI_id}')

        print(f'The default instance type is:\t{instance_type}')
        break
    else:
        print('Select a valid option')
    
instance_name = input('Enter a name for the instance:\t')

# create instance
try:
    response = ec2_client.run_instances(
        ImageId=AMI_id,
        InstanceType=instance_type,
        MinCount=1,  
        MaxCount=1,  
        KeyName=key_name,
        SubnetId=subnet_id,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': instance_name}
                ]
            }
        ]
    )
    
    instance = response['Instances'][0]
    instance_id = instance['InstanceId'] 
    instance_name = instance['Tags'][0]['Value'] 
    print(f"Instancia creada: {instance_name}, ID {instance_id}")

except Exception as e:
    print(f"Error al crear la instancia: {str(e)}")


# add to a group
ec2_client = boto3.client('ec2')

# get security groups
response = ec2_client.describe_security_groups()

print("Available Security Groups:")
for sg in response['SecurityGroups']:
    print(f"ID: {sg['GroupId']}, Name: {sg['GroupName']}")


security_group_id = input('Enter the ID of the security group:\t')
print('Only for studying porpouse its going to give permissions to everyone using the ip range 0.0.0.0')

ec2_client.modify_instance_attribute(
    InstanceId=instance_id,
    Groups=[security_group_id]
)

print(f'Security group with ID: {security_group_id} linked with {instance_id}')

# get the ip
ec2_resource = boto3.resource('ec2')

instances = ec2_resource.instances.filter(
    Filters=[ {'Name': 'tag:Name', 'Values': [instance_name]}])
for instance in instances:
    if instance.public_ip_address is not None:
        print(f'Instance details\n\tName: {instance_name} \n\tID: {instance.id} \n\tIP: {instance.public_ip_address}')