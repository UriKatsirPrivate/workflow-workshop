import googleapiclient.discovery
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import sys
import datetime
from datetime import datetime, timedelta
import pytz

utc = pytz.UTC


gce_service = build('compute', 'beta')


def Delete_Machine_Image(request):
    request_json = request.get_json()
    project = request_json['project']
    days_to_keep_images = int(request_json['days_to_keep_images'])
    Machine_Images = request_json['items']
    for Machine_Image in Machine_Images:
        name = Machine_Image['name']
        CreationTimestamp = datetime.fromisoformat(
            Machine_Image['creationTimestamp'])
        DeletionDate = utc.localize(
            datetime.today() - timedelta(days=days_to_keep_images))

        if CreationTimestamp < DeletionDate:
            gce_service.machineImages().delete(project=project, machineImage=name).execute()
