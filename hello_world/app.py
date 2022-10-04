import json

import boto3

# import requests


def lambda_handler(event, context):
    region = "ap-south-1"
    secret_name = "my-secrets-manager-08"

    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager", 
        region_name=region
    )
    
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secrets_response = get_secret_value_response["SecretString"]
    string = json.loads(secrets_response)["key1"]
    return string
