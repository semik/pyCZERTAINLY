# TriggerDetailDto


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
**rules** | [**List[RuleDetailDto]**](RuleDetailDto.md) | List of Rules in the Rule Trigger | 
**actions** | [**List[ActionDetailDto]**](ActionDetailDto.md) | List of Action Groups in the Rule Trigger | 

## Example

```python
from openapi_client.models.trigger_detail_dto import TriggerDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDetailDto from a JSON string
trigger_detail_dto_instance = TriggerDetailDto.from_json(json)
# print the JSON string representation of the object
print(TriggerDetailDto.to_json())

# convert the object into a dict
trigger_detail_dto_dict = trigger_detail_dto_instance.to_dict()
# create an instance of TriggerDetailDto from a dict
trigger_detail_dto_from_dict = TriggerDetailDto.from_dict(trigger_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


