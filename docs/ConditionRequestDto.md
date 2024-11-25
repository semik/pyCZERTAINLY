# ConditionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the condition | 
**description** | **str** | Description of the condition | [optional] 
**type** | [**ConditionType**](ConditionType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**items** | [**List[ConditionItemRequestDto]**](ConditionItemRequestDto.md) | List of the condition items to add to condition | 

## Example

```python
from openapi_client.models.condition_request_dto import ConditionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionRequestDto from a JSON string
condition_request_dto_instance = ConditionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConditionRequestDto.to_json())

# convert the object into a dict
condition_request_dto_dict = condition_request_dto_instance.to_dict()
# create an instance of ConditionRequestDto from a dict
condition_request_dto_from_dict = ConditionRequestDto.from_dict(condition_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


