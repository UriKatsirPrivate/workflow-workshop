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


# def Insert_Machine_Image(request):
def List_Machine_Images():
    # request_json = request.get_json()
    # project = request_json['project']
    project = 'uri-test'
    # instances = request_json['items']
    Machine_Images = gce_service.machineImages().list(project=project).execute()

    return Machine_Images


List_Machine_Images()
