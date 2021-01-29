# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
import datetime
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC



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

# def Insert_Machine_Image(request):
def Delete_Machine_Image():
    # request_json = request.get_json()
    # project = request_json['project']
    project = 'uri-test'
    days_to_go_back=5
    Machine_Images = gce_service.machineImages().list(project=project).execute()
    # instances = request_json['items']
    for instance in Machine_Images['items']:
        name = instance['name']
        CreationTimestamp = datetime.fromisoformat(instance['creationTimestamp'])
        DeletionDate = utc.localize(datetime.today() - timedelta(days=days_to_go_back))

        if CreationTimestamp<DeletionDate:
            gce_service.machineImages().delete(project=project,machineImage=name).execute()
    # ddd = ''

    

Delete_Machine_Image()
