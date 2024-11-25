# StringAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **str** | String attribute value | 

## Example

```python
from pyCZERTAINLY.models.string_attribute_content import StringAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of StringAttributeContent from a JSON string
string_attribute_content_instance = StringAttributeContent.from_json(json)
# print the JSON string representation of the object
print(StringAttributeContent.to_json())

# convert the object into a dict
string_attribute_content_dict = string_attribute_content_instance.to_dict()
# create an instance of StringAttributeContent from a dict
string_attribute_content_from_dict = StringAttributeContent.from_dict(string_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


