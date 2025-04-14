import boto3

ec2 = boto3.resource('ec2') 

instance_name = input("What's the name of the instance?:\t")

instances = ec2.instances.filter(
    Filters=[ {'Name': 'tag:Name', 'Values': [instance_name]}])
for instance in instances:
    if instance.public_ip_address is not None:
        print(f'Instance ID: {instance.id}, Public IP: {instance.public_ip_address}')