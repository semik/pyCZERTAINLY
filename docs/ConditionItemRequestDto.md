# ConditionItemRequestDto

List of the condition items to add to condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_source** | [**FilterFieldSource**](FilterFieldSource.md) |  | 
**field_identifier** | **str** | Field identifier of the condition item | 
**operator** | [**FilterConditionOperator**](FilterConditionOperator.md) |  | 
**value** | **object** | Value of the condition item | [optional] 

## Example

```python
from pyCZERTAINLY.models.condition_item_request_dto import ConditionItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionItemRequestDto from a JSON string
condition_item_request_dto_instance = ConditionItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConditionItemRequestDto.to_json())

# convert the object into a dict
condition_item_request_dto_dict = condition_item_request_dto_instance.to_dict()
# create an instance of ConditionItemRequestDto from a dict
condition_item_request_dto_from_dict = ConditionItemRequestDto.from_dict(condition_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


