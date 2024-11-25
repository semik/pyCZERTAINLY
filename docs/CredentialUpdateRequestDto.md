# CredentialUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Credential Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.credential_update_request_dto import CredentialUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialUpdateRequestDto from a JSON string
credential_update_request_dto_instance = CredentialUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(CredentialUpdateRequestDto.to_json())

# convert the object into a dict
credential_update_request_dto_dict = credential_update_request_dto_instance.to_dict()
# create an instance of CredentialUpdateRequestDto from a dict
credential_update_request_dto_from_dict = CredentialUpdateRequestDto.from_dict(credential_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


