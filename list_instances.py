# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
# import create_machine_image


from google.oauth2 import service_account
import googleapiclient.discovery

#  Authenticate using Service Account
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'security/uri-test-38aacab75c2a.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# ===================================================================

# Local testing
gce_service = build('compute', 'v1', credentials=credentials)
# -------------------------------------------------------------

# Run on GCP
# gce_service = build('compute', 'v1')
# -------------------------------------------------------------

def list_instances(request):
    request_json = request.get_json()
    project = request_json['project']
    zone = request_json['zone']
    instances = gce_service.instances().list(
        project=project, zone=zone).execute()
    # for instance in instances['items']:
    #     name = instance['name']
    #     name = (name[:40]) if len(name) > 40 else name
    #     selfLink = instance['selfLink']
    
    # create_machine_image.Insert_Machine_Image(project_name,instances)
        
    return instances

input1 = {"project": 5, "zone": "us-east1-b"}
list_instances(input1)
