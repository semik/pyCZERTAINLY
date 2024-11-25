# CredentialDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**kind** | **str** | Credential Kind | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Credential Attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**connector_uuid** | **str** | UUID of Credential provider Connector | 
**connector_name** | **str** | Name of Credential provider Connector | 

## Example

```python
from pyCZERTAINLY.models.credential_dto import CredentialDto

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialDto from a JSON string
credential_dto_instance = CredentialDto.from_json(json)
# print the JSON string representation of the object
print(CredentialDto.to_json())

# convert the object into a dict
credential_dto_dict = credential_dto_instance.to_dict()
# create an instance of CredentialDto from a dict
credential_dto_from_dict = CredentialDto.from_dict(credential_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


