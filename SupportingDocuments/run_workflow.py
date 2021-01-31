import requests


def run_workflow(request):

    url = "https://workflowexecutions.googleapis.com/v1/projects/uri-test/locations/us-central1/workflows/CreateMachineImage/executions"

    payload = "{\n  \"argument\": \"{\\\"project\\\":\\\"uri-test\\\",\\\"zone\\\":\\\"us-east1-b\\\"}\"\n}"
    headers = {
        'Authorization': 'Bearer ya29.A0AfH6SMDp_qONSWf7GCYwcSycrxeHr30Xgbx7JmvrttYF1QiVKfchK2ya3u2xdGmtiB-2ErVaExxy4aqw5wjMk00mxqjqrnGkseumZK_zSXfutR2W1gpZUNA6Ssl-FUJVXCsk_d1Y9Nc28JKkbc1p2Y5sSPIjtw',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

run_workflow("")