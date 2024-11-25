# ScheduledJobDetailDto


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
**user_uuid** | **str** |  | [optional] 
**object_data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.scheduled_job_detail_dto import ScheduledJobDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJobDetailDto from a JSON string
scheduled_job_detail_dto_instance = ScheduledJobDetailDto.from_json(json)
# print the JSON string representation of the object
print(ScheduledJobDetailDto.to_json())

# convert the object into a dict
scheduled_job_detail_dto_dict = scheduled_job_detail_dto_instance.to_dict()
# create an instance of ScheduledJobDetailDto from a dict
scheduled_job_detail_dto_from_dict = ScheduledJobDetailDto.from_dict(scheduled_job_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


