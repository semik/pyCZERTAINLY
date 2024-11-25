# FileAttributeContentData

File attribute content data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | File content | 
**file_name** | **str** | Name of the file | 
**mime_type** | **str** | Type of the file uploaded | 

## Example

```python
from pyCZERTAINLY.models.file_attribute_content_data import FileAttributeContentData

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttributeContentData from a JSON string
file_attribute_content_data_instance = FileAttributeContentData.from_json(json)
# print the JSON string representation of the object
print(FileAttributeContentData.to_json())

# convert the object into a dict
file_attribute_content_data_dict = file_attribute_content_data_instance.to_dict()
# create an instance of FileAttributeContentData from a dict
file_attribute_content_data_from_dict = FileAttributeContentData.from_dict(file_attribute_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


