# SecretAttributeContentData

Secret attribute content data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | Secret attribute data | [optional] 
**protection_level** | **str** | Level of protection of the data | [optional] 

## Example

```python
from pyCZERTAINLY.models.secret_attribute_content_data import SecretAttributeContentData

# TODO update the JSON string below
json = "{}"
# create an instance of SecretAttributeContentData from a JSON string
secret_attribute_content_data_instance = SecretAttributeContentData.from_json(json)
# print the JSON string representation of the object
print(SecretAttributeContentData.to_json())

# convert the object into a dict
secret_attribute_content_data_dict = secret_attribute_content_data_instance.to_dict()
# create an instance of SecretAttributeContentData from a dict
secret_attribute_content_data_from_dict = SecretAttributeContentData.from_dict(secret_attribute_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


