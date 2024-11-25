# ScheduledJobHistoryDto

Scheduled job history

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_uuid** | **str** | Scheduled job UUID | [optional] 
**start_time** | **datetime** | Start time of triggered task | 
**end_time** | **datetime** | End time of triggered task | [optional] 
**status** | [**SchedulerJobExecutionStatus**](SchedulerJobExecutionStatus.md) |  | 
**result_message** | **str** | Message explaining result status | [optional] 
**result_object_type** | [**Resource**](Resource.md) |  | [optional] 
**result_object_identification** | **List[str]** | Result object identification (UUID) | [optional] 

## Example

```python
from openapi_client.models.scheduled_job_history_dto import ScheduledJobHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJobHistoryDto from a JSON string
scheduled_job_history_dto_instance = ScheduledJobHistoryDto.from_json(json)
# print the JSON string representation of the object
print(ScheduledJobHistoryDto.to_json())

# convert the object into a dict
scheduled_job_history_dto_dict = scheduled_job_history_dto_instance.to_dict()
# create an instance of ScheduledJobHistoryDto from a dict
scheduled_job_history_dto_from_dict = ScheduledJobHistoryDto.from_dict(scheduled_job_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


