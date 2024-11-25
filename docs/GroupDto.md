# GroupDto

Groups associated to the key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Group | [optional] 
**email** | **str** | Group contact email | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.group_dto import GroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDto from a JSON string
group_dto_instance = GroupDto.from_json(json)
# print the JSON string representation of the object
print(GroupDto.to_json())

# convert the object into a dict
group_dto_dict = group_dto_instance.to_dict()
# create an instance of GroupDto from a dict
group_dto_from_dict = GroupDto.from_dict(group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


