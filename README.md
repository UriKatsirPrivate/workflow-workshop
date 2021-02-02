# Workflows workshop
 GCP workflows workshop for Machine Images

## Deliverables
By the end of this workshop, you will have a working solution for:
1. Creating machine images (across all zones).
2. Deleting machine images older than configured number of days.
3. Run the Create and Delete workflows on a pre-defined schedule using Cloud Scheduler.

## Prerequisites
1. GCP project
2. Service account with Cloud Functions Invoker, Compute Admin and Workflows Admin permissions.
3. Clone the [workflow-workshop](https://github.com/UriKatsirPrivate/workflow-workshop) repository from Github.
4. Create all five functions in your project using Python 3.7. Use the service account created above.
5. Execute 'list_zones' function using {"project":"ENTER YOUR PROJECT NAME"} as input. The function should return all zones.
6. Execute 'list_instances' function using {"project":"ENTER YOUR PROJECT NAME","zone":"ENTER ONE ZONE WITH INSTANCES"} as input. The function should all instances in the specified zone.

## To-Do
1. Create MachineImage based on labels

### Supporting References
1. [Machine Images REST API](https://cloud.google.com/compute/docs/reference/rest/beta/machineImages)
2. [Cron expressions generator](https://www.freeformatter.com/cron-expression-generator-quartz.html) and [Here](https://crontab.cronhub.io/) and [Here](http://www.cronmaker.com/;jsessionid=node01jr1tu19xhphf1oxtzv8emirge173782.node0?0)
3. [Scheduling a workflow using Cloud Scheduler](https://cloud.google.com/workflows/docs/schedule-workflow)


