# UpdateConditionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the condition | [optional] 
**items** | [**List[ConditionItemRequestDto]**](ConditionItemRequestDto.md) | List of the condition items to add to condition | 

## Example

```python
from openapi_client.models.update_condition_request_dto import UpdateConditionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConditionRequestDto from a JSON string
update_condition_request_dto_instance = UpdateConditionRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateConditionRequestDto.to_json())

# convert the object into a dict
update_condition_request_dto_dict = update_condition_request_dto_instance.to_dict()
# create an instance of UpdateConditionRequestDto from a dict
update_condition_request_dto_from_dict = UpdateConditionRequestDto.from_dict(update_condition_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


