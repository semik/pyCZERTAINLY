# CredentialRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Credential name | 
**kind** | **str** | Credential Kind | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Credential Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**connector_uuid** | **str** | UUID of Credential provider Connector | 

## Example

```python
from pyCZERTAINLY.models.credential_request_dto import CredentialRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialRequestDto from a JSON string
credential_request_dto_instance = CredentialRequestDto.from_json(json)
# print the JSON string representation of the object
print(CredentialRequestDto.to_json())

# convert the object into a dict
credential_request_dto_dict = credential_request_dto_instance.to_dict()
# create an instance of CredentialRequestDto from a dict
credential_request_dto_from_dict = CredentialRequestDto.from_dict(credential_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


