# ObjectPermissionsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Object | 
**name** | **str** | Name of the Object | 
**allow** | **List[str]** | Allowed Action list | [optional] 
**deny** | **List[str]** | Denied Action list | [optional] 

## Example

```python
from openapi_client.models.object_permissions_request_dto import ObjectPermissionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectPermissionsRequestDto from a JSON string
object_permissions_request_dto_instance = ObjectPermissionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ObjectPermissionsRequestDto.to_json())

# convert the object into a dict
object_permissions_request_dto_dict = object_permissions_request_dto_instance.to_dict()
# create an instance of ObjectPermissionsRequestDto from a dict
object_permissions_request_dto_from_dict = ObjectPermissionsRequestDto.from_dict(object_permissions_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


