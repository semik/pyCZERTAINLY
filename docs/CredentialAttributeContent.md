# CredentialAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | [**CredentialAttributeContentData**](CredentialAttributeContentData.md) |  | 

## Example

```python
from openapi_client.models.credential_attribute_content import CredentialAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialAttributeContent from a JSON string
credential_attribute_content_instance = CredentialAttributeContent.from_json(json)
# print the JSON string representation of the object
print(CredentialAttributeContent.to_json())

# convert the object into a dict
credential_attribute_content_dict = credential_attribute_content_instance.to_dict()
# create an instance of CredentialAttributeContent from a dict
credential_attribute_content_from_dict = CredentialAttributeContent.from_dict(credential_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


