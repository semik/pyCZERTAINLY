# TriggerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the trigger | [optional] 
**type** | [**TriggerType**](TriggerType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**ignore_trigger** | **bool** | Flag if to ignore object when trigger rules are matched and do not perform any actions and stop evaluating other triggers. Based on context could have other implications to object processing. If ignore is set, trigger does not have any actions. | 
**event** | **str** | Event that should fire trigger | [optional] 
**event_resource** | [**Resource**](Resource.md) |  | [optional] 

## Example

```python
from openapi_client.models.trigger_dto import TriggerDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDto from a JSON string
trigger_dto_instance = TriggerDto.from_json(json)
# print the JSON string representation of the object
print(TriggerDto.to_json())

# convert the object into a dict
trigger_dto_dict = trigger_dto_instance.to_dict()
# create an instance of TriggerDto from a dict
trigger_dto_from_dict = TriggerDto.from_dict(trigger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


