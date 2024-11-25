# CredentialAttributeContentData

Credential attribute content data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**kind** | **str** | Credential Kind | 
**attributes** | [**List[DataAttribute]**](DataAttribute.md) | List of Credential Attributes | 

## Example

```python
from openapi_client.models.credential_attribute_content_data import CredentialAttributeContentData

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAttributeContentData from a JSON string
credential_attribute_content_data_instance = CredentialAttributeContentData.from_json(json)
# print the JSON string representation of the object
print(CredentialAttributeContentData.to_json())

# convert the object into a dict
credential_attribute_content_data_dict = credential_attribute_content_data_instance.to_dict()
# create an instance of CredentialAttributeContentData from a dict
credential_attribute_content_data_from_dict = CredentialAttributeContentData.from_dict(credential_attribute_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


