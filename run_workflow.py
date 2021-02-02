# https://cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/create
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
    # parent = request_json['parent']
    parent = "projects/uri-test/locations/us-central1/workflows/CreateMachineImage"
    # body = request_json['body']
    body = {"argument": '{"project": "uri-test","zone": "us-east1-b"}'}
    workflow = workflow_service.projects().locations().workflows().executions().create(
      parent= parent, body= body).execute()

    # The code below will cause the workflow to fail because no body is provided
    # workflow = workflow_service.projects().locations().workflows().executions().create(
    #   parent= parent).execute()  

    return workflow

run_workflow('')
