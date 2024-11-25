# RoleRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the role | [optional] 
**description** | **str** | Description for the role | [optional] 
**email** | **str** | Role contact email | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.role_request_dto import RoleRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleRequestDto from a JSON string
role_request_dto_instance = RoleRequestDto.from_json(json)
# print the JSON string representation of the object
print(RoleRequestDto.to_json())

# convert the object into a dict
role_request_dto_dict = role_request_dto_instance.to_dict()
# create an instance of RoleRequestDto from a dict
role_request_dto_from_dict = RoleRequestDto.from_dict(role_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


