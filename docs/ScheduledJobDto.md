# ScheduledJobDto

Scheduled jobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the scheduled job | 
**job_name** | **str** | Name of the scheduled job | 
**job_type** | **str** | Type of scheduled job (job processor name) | 
**cron_expression** | **str** | CRON expression representing configuration of pattern how to run scheduled job | 
**enabled** | **bool** | Status of the scheduled job. True &#x3D; Enabled, False &#x3D; Disabled | 
**one_time** | **bool** | Is scheduled job triggered only once | 
**system** | **bool** | Is system scheduled job | 
**last_execution_status** | [**SchedulerJobExecutionStatus**](SchedulerJobExecutionStatus.md) |  | 

## Example

```python
from pyCZERTAINLY.models.scheduled_job_dto import ScheduledJobDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJobDto from a JSON string
scheduled_job_dto_instance = ScheduledJobDto.from_json(json)
# print the JSON string representation of the object
print(ScheduledJobDto.to_json())

# convert the object into a dict
scheduled_job_dto_dict = scheduled_job_dto_instance.to_dict()
# create an instance of ScheduledJobDto from a dict
scheduled_job_dto_from_dict = ScheduledJobDto.from_dict(scheduled_job_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


