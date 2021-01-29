from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
import create_machine_image


from google.oauth2 import service_account
import googleapiclient.discovery


# Authenticate from local machine
# flow = InstalledAppFlow.from_client_secrets_file(
#     'security/client_secret_960394617171.json',
#     scopes=['https://www.googleapis.com/auth/cloud-platform'])

# credentials = flow.run_local_server()
# credentials = flow.run_console()
# ===================================================================

#  Authenticate using Service Account
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'security/uri-test-38aacab75c2a.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# ===================================================================


gce_service = build('compute', 'v1', credentials=credentials)

project_name = 'uri-test'
zone = 'us-east1-b'


def list_instances(project_name, zone):
    instances = gce_service.instances().list(
        project=project_name, zone=zone).execute()
    for instance in instances['items']:
        name = instance['name']
        name = (name[:40]) if len(name) > 40 else name
        selfLink = instance['selfLink']
    
    create_machine_image.Insert_Machine_Image(project_name,instances)
        

        
    return instances


list_instances(project_name, zone)
