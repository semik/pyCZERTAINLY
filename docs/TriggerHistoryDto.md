# TriggerHistoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**trigger_uuid** | **str** | UUID of the trigger. | 
**object_uuid** | **str** | UUID of the object that the trigger has been evaluated on. | [optional] 
**reference_object_uuid** | **str** | Reference UUID of the object that the trigger has been evaluated on. | [optional] 
**conditions_matched** | **bool** | All conditions in the trigger have been matched. | 
**actions_performed** | **bool** | All actions in the trigger have been performed. | 
**triggered_at** | **datetime** | Time at which has the trigger been triggered | 
**message** | **str** | Additional message.  | [optional] 
**records** | [**List[TriggerHistoryRecordDto]**](TriggerHistoryRecordDto.md) | List of records for each action that has not been performed and each condition that has not been evaluated. | 

## Example

```python
from openapi_client.models.trigger_history_dto import TriggerHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryDto from a JSON string
trigger_history_dto_instance = TriggerHistoryDto.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryDto.to_json())

# convert the object into a dict
trigger_history_dto_dict = trigger_history_dto_instance.to_dict()
# create an instance of TriggerHistoryDto from a dict
trigger_history_dto_from_dict = TriggerHistoryDto.from_dict(trigger_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


