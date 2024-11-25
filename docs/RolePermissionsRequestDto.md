# RolePermissionsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_all_resources** | **bool** | Allow all resources, True &#x3D; Yes, False &#x3D; No | 
**resources** | [**List[ResourcePermissionsRequestDto]**](ResourcePermissionsRequestDto.md) | Resources | [optional] 

## Example

```python
from pyCZERTAINLY.models.role_permissions_request_dto import RolePermissionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissionsRequestDto from a JSON string
role_permissions_request_dto_instance = RolePermissionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(RolePermissionsRequestDto.to_json())

# convert the object into a dict
role_permissions_request_dto_dict = role_permissions_request_dto_instance.to_dict()
# create an instance of RolePermissionsRequestDto from a dict
role_permissions_request_dto_from_dict = RolePermissionsRequestDto.from_dict(role_permissions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


