# ResourcePermissionsDto

Resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Resource | 
**allow_all_actions** | **bool** | Allow all actions. True &#x3D; Yes, False &#x3D; No | 
**actions** | **List[str]** | List of actions permitted | 
**objects** | [**List[ObjectPermissionsDto]**](ObjectPermissionsDto.md) | Object permissions | 

## Example

```python
from openapi_client.models.resource_permissions_dto import ResourcePermissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePermissionsDto from a JSON string
resource_permissions_dto_instance = ResourcePermissionsDto.from_json(json)
# print the JSON string representation of the object
print(ResourcePermissionsDto.to_json())

# convert the object into a dict
resource_permissions_dto_dict = resource_permissions_dto_instance.to_dict()
# create an instance of ResourcePermissionsDto from a dict
resource_permissions_dto_from_dict = ResourcePermissionsDto.from_dict(resource_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


