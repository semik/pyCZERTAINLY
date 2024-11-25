# ResourcePermissionsRequestDto

Resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Resource | 
**allow_all_actions** | **bool** | Allow all actions. True &#x3D; Yes, False &#x3D; No | 
**actions** | **List[str]** | List of actions permitted | [optional] 
**objects** | [**List[ObjectPermissionsRequestDto]**](ObjectPermissionsRequestDto.md) | Object permissions | [optional] 

## Example

```python
from openapi_client.models.resource_permissions_request_dto import ResourcePermissionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePermissionsRequestDto from a JSON string
resource_permissions_request_dto_instance = ResourcePermissionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ResourcePermissionsRequestDto.to_json())

# convert the object into a dict
resource_permissions_request_dto_dict = resource_permissions_request_dto_instance.to_dict()
# create an instance of ResourcePermissionsRequestDto from a dict
resource_permissions_request_dto_from_dict = ResourcePermissionsRequestDto.from_dict(resource_permissions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


