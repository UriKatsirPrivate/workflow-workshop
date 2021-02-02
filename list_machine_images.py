from googleapiclient.discovery import build
import json
import sys
import datetime

from google.oauth2 import service_account
import googleapiclient.discovery

gce_service = build('compute', 'beta')

def List_Machine_Images(request):
    request_json = request.get_json()
    project = request_json['project']
    
    Machine_Images = gce_service.machineImages().list(project=project).execute()

    return Machine_Images
