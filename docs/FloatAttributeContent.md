# FloatAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **float** | Float attribute value | 

## Example

```python
from openapi_client.models.float_attribute_content import FloatAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of FloatAttributeContent from a JSON string
float_attribute_content_instance = FloatAttributeContent.from_json(json)
# print the JSON string representation of the object
print(FloatAttributeContent.to_json())

# convert the object into a dict
float_attribute_content_dict = float_attribute_content_instance.to_dict()
# create an instance of FloatAttributeContent from a dict
float_attribute_content_from_dict = FloatAttributeContent.from_dict(float_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


