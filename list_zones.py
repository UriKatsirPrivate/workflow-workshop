from googleapiclient.discovery import build
import json
import sys

from google.oauth2 import service_account
import googleapiclient.discovery

gce_service = build('compute', 'v1')

def list_zones(request):
  request_json = request.get_json()
  project = request_json['project']
  zones = gce_service.zones().list(project=project).execute()

  return zones