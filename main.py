from pprint import pprint
import os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def start_stop_server(req):
    command = req.args.get("command")
    command = command.lower()
    dbinstance = req.args.get("instance")
    projectId = os.environ.get("GCP_PROJECT")
    if(projectId is None):
        projectId = os.environ.get("GCLOUD_PROJECT")

    if(projectId is None):
        projectId = "telkomsel-retail-intelligence"
    
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)

    policy = "NEVER"
    if(command == "start"):
        policy = "ALWAYS"
    
    data = {
        "settings": {
            "activationPolicy": policy
        }
    }

    request = service.instances().patch(project=projectId, instance=dbinstance, body=data)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)
    return "Ok"