# ObjectAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **object** | Object attribute content data | 

## Example

```python
from openapi_client.models.object_attribute_content import ObjectAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectAttributeContent from a JSON string
object_attribute_content_instance = ObjectAttributeContent.from_json(json)
# print the JSON string representation of the object
print(ObjectAttributeContent.to_json())

# convert the object into a dict
object_attribute_content_dict = object_attribute_content_instance.to_dict()
# create an instance of ObjectAttributeContent from a dict
object_attribute_content_from_dict = ObjectAttributeContent.from_dict(object_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


