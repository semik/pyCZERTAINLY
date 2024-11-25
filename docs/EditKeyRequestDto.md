# EditKeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_profile_uuid** | **str** | UUID of the token profile | 
**name** | **str** | Name of the Cryptographic Key | 
**description** | **str** | Description of the Cryptographic Key | 
**owner_uuid** | **str** | Key Owner UUID | [optional] 
**group_uuids** | **List[str]** | UUIDs of the groups to associate with key | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.edit_key_request_dto import EditKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditKeyRequestDto from a JSON string
edit_key_request_dto_instance = EditKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(EditKeyRequestDto.to_json())

# convert the object into a dict
edit_key_request_dto_dict = edit_key_request_dto_instance.to_dict()
# create an instance of EditKeyRequestDto from a dict
edit_key_request_dto_from_dict = EditKeyRequestDto.from_dict(edit_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


