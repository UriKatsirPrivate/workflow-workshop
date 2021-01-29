from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
import datetime


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


gce_service = build('compute', 'beta', credentials=credentials)

project_name = 'uri-test'
# zone = 'us-east1-b'

# config = {
#     "name": datetime.datetime.now().strftime(("%Y-%m-%d-%H-%M-%S")),
#     "sourceInstance": "https://www.googleapis.com/compute/v1/projects/uri-test/zones/us-east1-b/instances/vpn-from-aws-1"
# }


def Insert_Machine_Image(project_name, instances):
    for instance in instances['items']:
        name = instance['name']
        name = (name[:40]) if len(name) > 40 else name
        selfLink = instance['selfLink']
        config = {
            "name": name + '-' + datetime.datetime.now().strftime(("%d-%m-%Y-%H-%M-%S")),
            "sourceInstance": selfLink
        }
        Machine_Image = gce_service.machineImages().insert(
            project=project_name, body=config).execute()

# Insert_Machine_Image(project_name)
