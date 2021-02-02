from googleapiclient.discovery import build
import json
import sys


from google.oauth2 import service_account
import googleapiclient.discovery

# Run on GCP
gce_service = build('compute', 'v1')
# -------------------------------------------------------------

def list_instances(request):
    request_json = request.get_json()
    project = request_json['project']
    zone = request_json['zone']
    instances = gce_service.instances().list(
        project=project, zone=zone).execute()
            
    return instances

