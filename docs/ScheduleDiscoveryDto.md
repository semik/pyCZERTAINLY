# ScheduleDiscoveryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**one_time** | **bool** |  | [optional] 
**request** | [**DiscoveryDto**](DiscoveryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.schedule_discovery_dto import ScheduleDiscoveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDiscoveryDto from a JSON string
schedule_discovery_dto_instance = ScheduleDiscoveryDto.from_json(json)
# print the JSON string representation of the object
print(ScheduleDiscoveryDto.to_json())

# convert the object into a dict
schedule_discovery_dto_dict = schedule_discovery_dto_instance.to_dict()
# create an instance of ScheduleDiscoveryDto from a dict
schedule_discovery_dto_from_dict = ScheduleDiscoveryDto.from_dict(schedule_discovery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


