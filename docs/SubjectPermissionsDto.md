# SubjectPermissionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_all_resources** | **bool** | Allow all resources, True &#x3D; Yes, False &#x3D; No | 
**resources** | [**List[ResourcePermissionsDto]**](ResourcePermissionsDto.md) | Resources | 

## Example

```python
from openapi_client.models.subject_permissions_dto import SubjectPermissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectPermissionsDto from a JSON string
subject_permissions_dto_instance = SubjectPermissionsDto.from_json(json)
# print the JSON string representation of the object
print(SubjectPermissionsDto.to_json())

# convert the object into a dict
subject_permissions_dto_dict = subject_permissions_dto_instance.to_dict()
# create an instance of SubjectPermissionsDto from a dict
subject_permissions_dto_from_dict = SubjectPermissionsDto.from_dict(subject_permissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


