# Workflows workshop
 GCP workflows workshop for Machine Images

## Deliverables
By the end of this workshop, you will have a working solution for:
1. Creating machine images (across all zones).
2. Deleting machine images older than configured number of days.
3. Run the Create and Delete workflows on a pre-defined schedule using Cloud Scheduler.

## Prerequisites
1. GCP project.
2. Service account with Cloud Functions Invoker, Compute Admin, Pub/Sub Admin, and Workflows Admin permissions.
3. Clone the [workflow-workshop](https://github.com/UriKatsirPrivate/workflow-workshop) repository from Github.

## Execution
1. Create all five cloud functions in your project using Python 3.7. Use the service account created in the Prerequisites section above.
2. Execute 'list_zones' function using {"project":"ENTER YOUR PROJECT NAME"} as input. The function should return all zones.
3. Execute 'list_instances' function using {"project":"ENTER YOUR PROJECT NAME","zone":"ENTER ONE ZONE WITH INSTANCES"} as input. The function should all instances in the specified zone.
4. Modify "CreateMachineImagesInAllZones.yaml" and "DeleteMachineImage.workflow.yaml" workflow definitions by modifying the url args to point to your deployed functions.
5. Create two workflows: "CreateMachineImagesInAllZones" and "DeleteMachineImage" using the modified .yaml definitions from the previous step. Use the service account created in the Prerequisites section above.
6. Execute the workflows using the sample input provided in the workflow definition files.
7. [Schedule the workflows to run on a predefined schedule](https://cloud.google.com/workflows/docs/schedule-workflow). See cron expression generators from the "Supporting References" section below.
8. If you want to debug locally, Install the [Python Client for Cloud Workflows](https://github.com/googleapis/python-workflows).

## To-Do
1. Create MachineImage based on labels.

### Supporting References
1. [Machine Images REST API](https://cloud.google.com/compute/docs/reference/rest/beta/machineImages).
2. [Workflows REST API](https://cloud.google.com/workflows/docs/reference/executions/rest).
3. [Cron expressions generator](https://www.freeformatter.com/cron-expression-generator-quartz.html) and [Here](https://crontab.cronhub.io/) and [Here](http://www.cronmaker.com/;jsessionid=node01jr1tu19xhphf1oxtzv8emirge173782.node0?0).
4. [Scheduling a workflow using Cloud Scheduler](https://cloud.google.com/workflows/docs/schedule-workflow).