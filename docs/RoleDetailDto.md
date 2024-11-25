# RoleDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the user | [optional] 
**email** | **str** | Role contact email | [optional] 
**system_role** | **bool** | Is system role. True &#x3D; Yes, False &#x3D; No | 
**users** | [**List[UserDto]**](UserDto.md) | List of Users with the role | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.role_detail_dto import RoleDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoleDetailDto from a JSON string
role_detail_dto_instance = RoleDetailDto.from_json(json)
# print the JSON string representation of the object
print(RoleDetailDto.to_json())

# convert the object into a dict
role_detail_dto_dict = role_detail_dto_instance.to_dict()
# create an instance of RoleDetailDto from a dict
role_detail_dto_from_dict = RoleDetailDto.from_dict(role_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


