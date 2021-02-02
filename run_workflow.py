from googleapiclient.discovery import build
import json
import sys

from google.oauth2 import service_account
import googleapiclient.discovery

#  Authenticate using Service Account
SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
SERVICE_ACCOUNT_FILE = 'security/uri-test-38aacab75c2a.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# ===================================================================

# Local testing
workflow_service = build('workflowexecutions', 'v1', credentials=credentials)
# -------------------------------------------------------------

# Run on GCP
# workflow_service = build('workflowexecutions', 'v1')
# -------------------------------------------------------------


def run_workflow(request):
    # request_json = request.get_json()
    # project = request_json['project']
    workflow = workflow_service.projects().locations().workflows().executions().create(
      parent="projects/uri-test/locations/us-central1/workflows/CreateMachineImage", body= {
        "argument": "{\"project\":\"uri-test\",\"zone\":\"us-east1-b\"}"
      }).execute()

    return workflow

run_workflow('')
