# pip install boto3 -- to install boto3 first
import boto3
# AWS credentials and region configuration
region = #your-aws-region
access_key = #your-access-key
secret_key = #your-secret-key

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Define parameters for the instance
instance_params = {
    'ImageId': # The ID of the AMI you want to use
    'InstanceType': 't2.micro',  # Instance type (e.g., t2.micro)
    'KeyName': 'N-Virginia',  # Key pair name to access the instance
    'MinCount': 1,
    'MaxCount': 1,
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Test1'  # Name tag for the instance
                }
            ]
        }
    ]
}
# Create the instance
response = ec2.run_instances(**instance_params)

# Get instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance {instance_id} is being created.")