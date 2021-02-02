# from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import sys
import datetime
from datetime import datetime, timedelta
import pytz

utc = pytz.UTC

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
    # delete_images_older_than_days = 5
    project = 'uri-test'
    days_to_go_back = 3
    # days_to_go_back = int(request_json['days_to_go_back'])
    # Machine_Images = request_json['items']
    Machine_Images = gce_service.machineImages().list(project=project).execute()
    # Machine_Image = request_json['items']
    for Machine_Image in Machine_Images['items']:
        name = Machine_Image['name']
        CreationTimestamp = datetime.fromisoformat(Machine_Image['creationTimestamp'])
        DeletionDate = utc.localize(datetime.today() - timedelta(days=days_to_go_back))

        if CreationTimestamp < DeletionDate:
            gce_service.machineImages().delete(project=project, machineImage=name).execute()
    # ddd = ''


Delete_Machine_Image()
