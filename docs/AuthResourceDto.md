# AuthResourceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | [**Resource**](Resource.md) |  | 
**display_name** | **str** | Resource label | 
**list_objects_endpoint** | **str** | Listing Endpoint | [optional] 
**object_access** | **bool** | If resource has Object access permissions. True &#x3D; Yes, False &#x3D; No | 
**actions** | [**List[ActionDto]**](ActionDto.md) | List of Actions for the Resource | 

## Example

```python
from pyCZERTAINLY.models.auth_resource_dto import AuthResourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResourceDto from a JSON string
auth_resource_dto_instance = AuthResourceDto.from_json(json)
# print the JSON string representation of the object
print(AuthResourceDto.to_json())

# convert the object into a dict
auth_resource_dto_dict = auth_resource_dto_instance.to_dict()
# create an instance of AuthResourceDto from a dict
auth_resource_dto_from_dict = AuthResourceDto.from_dict(auth_resource_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


