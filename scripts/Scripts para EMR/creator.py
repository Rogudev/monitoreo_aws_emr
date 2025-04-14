import boto3


# EMR client
emr_client = boto3.client('emr')

# cluster name
cluster_name = input('Input the name for the cluster: \n\t>> ')                       

release_label = input("Input the EMR version (example: 'emr-6.5.0') \n\t>> ")       # EMR version

# define applications for the cluster
applications = []
apps = input("Input the apps to use, separate them with ','\n\t>> ").split(',')
for app in apps:
    applications.append(
        {'Name': app.capitalize()}
    )


# define the master and slave instances
master_instance_count = 1
slave_instance_count = int(input("Input the number of slave instances (e.g., 2, 3): \n\t>> "))

# total instance count (1 master + number of slaves)
total_instance_count = master_instance_count + slave_instance_count


# define master and slave instances types
master_instance_type = 'm4.large'  
slave_instance_type = 'm4.large'   


instances = {
    'MasterInstanceType': master_instance_type,         # master instances
    'SlaveInstanceType': slave_instance_type,           # slave instances

    'InstanceCount': total_instance_count,              # total number of instances (1 master + 2 slaves)

    'KeepJobFlowAliveWhenNoSteps': True,                # Keep it active

    'Ec2KeyName': 'vockey',                             # Key Pair name
}


# Create cluster
try:
    response = emr_client.run_job_flow(
        Name=cluster_name,
        ReleaseLabel=release_label,
        Instances=instances,
        Applications=applications,
        VisibleToAllUsers=True,
        JobFlowRole='EMR_EC2_DefaultRole',  
        ServiceRole='EMR_DefaultRole',     
        Tags=[
            {'Key': 'Name', 'Value': cluster_name},
            {'Key': 'Environment', 'Value': 'Dev'},
        ]
    )

    # Show cluster ID
    cluster_id = response['JobFlowId']
    print(f"EMR cLuster created with ID: \t{cluster_id}")
    
except Exception as e:
    print(f"Error acreating EMR cluster: {str(e)}")