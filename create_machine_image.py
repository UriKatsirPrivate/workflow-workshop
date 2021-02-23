# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import sys
import datetime


# from google.oauth2 import service_account
import googleapiclient.discovery

# Run on GCP
gce_service = build('compute', 'beta')
# -------------------------------------------------------------


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
