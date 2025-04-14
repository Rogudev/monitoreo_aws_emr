import boto3
import time
import os
import pygame

# emr client
emr_client = boto3.client('emr')

# check status
def check_cluster_status(cluster_id):
    try:
        cluster_status = emr_client.describe_cluster(
            ClusterId=cluster_id
        )
        return cluster_status['Cluster']['Status']['State']
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# get the master's public DNS
def get_master_node_public_dns(cluster_id):
    try:
        # Get cluster details
        cluster_details = emr_client.describe_cluster(ClusterId=cluster_id)
        ec2_instance_id = cluster_details['Cluster']['MasterPublicDnsName']

        # Print the public DNS
        return ec2_instance_id
    except Exception as e:
        print(f"Error fetching master node public DNS: {str(e)}")
        return None

# get all clusters
def list_clusters():
    try:
        clusters = emr_client.list_clusters()
        return clusters['Clusters']  # Devuelve una lista de clústeres
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def playsound(filename):
    # start mixer
    pygame.mixer.init()
    
    # load file
    pygame.mixer.music.load(f'sounds/{filename}.mp3')
    
    # play
    pygame.mixer.music.play()
    
    # waiter
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":

    # get all clusters
    clusters = list_clusters()

    if clusters:
        print("Available clusters:")
        for cluster in clusters:
            # get the name and id
            cluster_name = cluster['Name']
            cluster_id = cluster['Id']
            print(f"Cluster name: {cluster_name}, ID: {cluster_id}")
        
        cluster_id = input("\nIntroduce el ID del clúster EMR que deseas verificar: ")

        # check the status
        if cluster_id:
            while True:
                estado = check_cluster_status(cluster_id)

                if estado:
                    print(f"Cluster status: {cluster_id}: {estado}")
                else:
                    print("Error checking the cluster's status.")
                
                if estado == 'STARTING':
                    print('\Checking again in 60s...')
                    time.sleep(60)  # 60s delay

                elif estado == 'WAITING':
                    print('\tThe cluster is ready')
                    
                    master_dns = get_master_node_public_dns(cluster_id)
                    if master_dns:
                        print(f"Master node public DNS: {master_dns}")

                    for i in range(0,3):
                        playsound(filename='cluster_ready')
                    
                    break

                elif estado == 'TERMINATED_WITH_ERRORS':
                    print('\tError while creating EMR')
                    break
        else:
            print("Insert a valid ID.")
    else:
        print("There are no available clusters.")
