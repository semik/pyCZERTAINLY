# UserDto

List of Users with the role

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

## Example

```python
from pyCZERTAINLY.models.user_dto import UserDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserDto from a JSON string
user_dto_instance = UserDto.from_json(json)
# print the JSON string representation of the object
print(UserDto.to_json())

# convert the object into a dict
user_dto_dict = user_dto_instance.to_dict()
# create an instance of UserDto from a dict
user_dto_from_dict = UserDto.from_dict(user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


