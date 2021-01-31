# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
import datetime


from google.oauth2 import service_account
import googleapiclient.discovery

#  Authenticate using Service Account
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'security/uri-test-38aacab75c2a.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# ===================================================================

# Local testing
gce_service = build('compute', 'beta', credentials=credentials)
# -------------------------------------------------------------

# Run on GCP
# gce_service = build('compute', 'beta')
# -------------------------------------------------------------

# config = {
#     "name": datetime.datetime.now().strftime(("%Y-%m-%d-%H-%M-%S")),
#     "sourceInstance": "https://www.googleapis.com/compute/v1/projects/uri-test/zones/us-east1-b/instances/vpn-from-aws-1"
# }


def Insert_Machine_Image(request):
    request_json = request.get_json()

    if 'items' in request_json:
        project = request_json['project']
        instances = request_json['items']

        for instance in instances:
            name = instance['name']
            name = (name[:40]) if len(name) > 40 else name
            selfLink = instance['selfLink']
            config = {
                "name": name + '-' + datetime.datetime.now().strftime(("%d-%m-%Y-%H-%M-%S")),
                "sourceInstance": selfLink
            }
            gce_service.machineImages().insert(project=project, body=config).execute()


input1 = ''
Insert_Machine_Image(input1)
