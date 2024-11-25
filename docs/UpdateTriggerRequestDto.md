# UpdateTriggerRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the trigger | [optional] 
**type** | [**TriggerType**](TriggerType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**ignore_trigger** | **bool** | Flag if to ignore object when trigger rules are matched and do not perform any actions and stop evaluating other triggers. Based on context could have other implications to object processing. If ignore is set, trigger does not have any actions. | 
**event** | **str** | Event of the trigger | [optional] 
**event_resource** | [**Resource**](Resource.md) |  | [optional] 
**rules_uuids** | **List[str]** | List of UUIDs of existing rules to add to the trigger | [optional] 
**actions_uuids** | **List[str]** | List of UUIDs of existing actions to add to the trigger | [optional] 

## Example

```python
from openapi_client.models.update_trigger_request_dto import UpdateTriggerRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTriggerRequestDto from a JSON string
update_trigger_request_dto_instance = UpdateTriggerRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTriggerRequestDto.to_json())

# convert the object into a dict
update_trigger_request_dto_dict = update_trigger_request_dto_instance.to_dict()
# create an instance of UpdateTriggerRequestDto from a dict
update_trigger_request_dto_from_dict = UpdateTriggerRequestDto.from_dict(update_trigger_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


