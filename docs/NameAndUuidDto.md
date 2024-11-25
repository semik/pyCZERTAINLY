# NameAndUuidDto

Groups of the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 

## Example

```python
from openapi_client.models.name_and_uuid_dto import NameAndUuidDto

# TODO update the JSON string below
json = "{}"
# create an instance of NameAndUuidDto from a JSON string
name_and_uuid_dto_instance = NameAndUuidDto.from_json(json)
# print the JSON string representation of the object
print(NameAndUuidDto.to_json())

# convert the object into a dict
name_and_uuid_dto_dict = name_and_uuid_dto_instance.to_dict()
# create an instance of NameAndUuidDto from a dict
name_and_uuid_dto_from_dict = NameAndUuidDto.from_dict(name_and_uuid_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


