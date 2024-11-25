# FileAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | [**FileAttributeContentData**](FileAttributeContentData.md) |  | 

## Example

```python
from pyCZERTAINLY.models.file_attribute_content import FileAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttributeContent from a JSON string
file_attribute_content_instance = FileAttributeContent.from_json(json)
# print the JSON string representation of the object
print(FileAttributeContent.to_json())

# convert the object into a dict
file_attribute_content_dict = file_attribute_content_instance.to_dict()
# create an instance of FileAttributeContent from a dict
file_attribute_content_from_dict = FileAttributeContent.from_dict(file_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


