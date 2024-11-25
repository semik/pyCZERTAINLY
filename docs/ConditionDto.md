# ConditionDto

List of conditions in the Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the condition | [optional] 
**type** | [**ConditionType**](ConditionType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**items** | [**List[ConditionItemDto]**](ConditionItemDto.md) | List of the condition items | 

## Example

```python
from pyCZERTAINLY.models.condition_dto import ConditionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionDto from a JSON string
condition_dto_instance = ConditionDto.from_json(json)
# print the JSON string representation of the object
print(ConditionDto.to_json())

# convert the object into a dict
condition_dto_dict = condition_dto_instance.to_dict()
# create an instance of ConditionDto from a dict
condition_dto_from_dict = ConditionDto.from_dict(condition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


