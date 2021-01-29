import json


def hello_world(request):
    # {"project": 5, "zone": "us-east1-b"}
    request_json = request.get_json()
    project = request_json['project']
    zone = request_json['zone']
    # return json.dumps(project)
    return "Project is: " + project + " and zone is: " + zone
