# ObjectPermissionsDto

Object permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Object | 
**name** | **str** | Name of the Object | 
**allow** | **List[str]** | Allowed Action list | 
**deny** | **List[str]** | Denied Action list | 

## Example

```python
from openapi_client.models.object_permissions_dto import ObjectPermissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectPermissionsDto from a JSON string
object_permissions_dto_instance = ObjectPermissionsDto.from_json(json)
# print the JSON string representation of the object
print(ObjectPermissionsDto.to_json())

# convert the object into a dict
object_permissions_dto_dict = object_permissions_dto_instance.to_dict()
# create an instance of ObjectPermissionsDto from a dict
object_permissions_dto_from_dict = ObjectPermissionsDto.from_dict(object_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


