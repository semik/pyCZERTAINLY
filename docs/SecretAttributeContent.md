# SecretAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | [**SecretAttributeContentData**](SecretAttributeContentData.md) |  | 

## Example

```python
from openapi_client.models.secret_attribute_content import SecretAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of SecretAttributeContent from a JSON string
secret_attribute_content_instance = SecretAttributeContent.from_json(json)
# print the JSON string representation of the object
print(SecretAttributeContent.to_json())

# convert the object into a dict
secret_attribute_content_dict = secret_attribute_content_instance.to_dict()
# create an instance of SecretAttributeContent from a dict
secret_attribute_content_from_dict = SecretAttributeContent.from_dict(secret_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


