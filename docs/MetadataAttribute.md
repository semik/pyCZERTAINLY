# MetadataAttribute

Info attribute contains content that is for metadata. Its content can not be edited and is not send in requests to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute for unique identification | 
**name** | **str** | Name of the Attribute that is used for identification | 
**description** | **str** | Optional description of the Attribute, should contain helper text on what is expected | [optional] 
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Content of the Attribute | 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**properties** | [**MetadataAttributeProperties**](MetadataAttributeProperties.md) |  | 

## Example

```python
from openapi_client.models.metadata_attribute import MetadataAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataAttribute from a JSON string
metadata_attribute_instance = MetadataAttribute.from_json(json)
# print the JSON string representation of the object
print(MetadataAttribute.to_json())

# convert the object into a dict
metadata_attribute_dict = metadata_attribute_instance.to_dict()
# create an instance of MetadataAttribute from a dict
metadata_attribute_from_dict = MetadataAttribute.from_dict(metadata_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


