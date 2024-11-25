# UserDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the User | 
**username** | **str** | Username of the user | 
**first_name** | **str** | First name of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the user | [optional] 
**description** | **str** | Description of the user | [optional] 
**groups** | [**List[NameAndUuidDto]**](NameAndUuidDto.md) | Groups of the user | 
**enabled** | **bool** | Status of the user. True &#x3D; Enabled, False &#x3D; Disabled | 
**system_user** | **bool** | Is System user. True &#x3D; Yes, False &#x3D; No | 
**certificate** | [**UserCertificateDto**](UserCertificateDto.md) |  | [optional] 
**roles** | [**List[RoleDto]**](RoleDto.md) | Roles for the user | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.user_detail_dto import UserDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailDto from a JSON string
user_detail_dto_instance = UserDetailDto.from_json(json)
# print the JSON string representation of the object
print(UserDetailDto.to_json())

# convert the object into a dict
user_detail_dto_dict = user_detail_dto_instance.to_dict()
# create an instance of UserDetailDto from a dict
user_detail_dto_from_dict = UserDetailDto.from_dict(user_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


