# EditTokenProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of Token Profile | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes for Token Profile | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] 
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | [optional] 

## Example

```python
from openapi_client.models.edit_token_profile_request_dto import EditTokenProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditTokenProfileRequestDto from a JSON string
edit_token_profile_request_dto_instance = EditTokenProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(EditTokenProfileRequestDto.to_json())

# convert the object into a dict
edit_token_profile_request_dto_dict = edit_token_profile_request_dto_instance.to_dict()
# create an instance of EditTokenProfileRequestDto from a dict
edit_token_profile_request_dto_from_dict = EditTokenProfileRequestDto.from_dict(edit_token_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


