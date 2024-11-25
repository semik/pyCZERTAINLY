# GroupRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Group | 
**description** | **str** | Description of the Group | [optional] 
**email** | **str** | Group contact email | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.group_request_dto import GroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRequestDto from a JSON string
group_request_dto_instance = GroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(GroupRequestDto.to_json())

# convert the object into a dict
group_request_dto_dict = group_request_dto_instance.to_dict()
# create an instance of GroupRequestDto from a dict
group_request_dto_from_dict = GroupRequestDto.from_dict(group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


