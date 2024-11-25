# TextAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **str** | Text attribute value | 

## Example

```python
from openapi_client.models.text_attribute_content import TextAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of TextAttributeContent from a JSON string
text_attribute_content_instance = TextAttributeContent.from_json(json)
# print the JSON string representation of the object
print(TextAttributeContent.to_json())

# convert the object into a dict
text_attribute_content_dict = text_attribute_content_instance.to_dict()
# create an instance of TextAttributeContent from a dict
text_attribute_content_from_dict = TextAttributeContent.from_dict(text_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


