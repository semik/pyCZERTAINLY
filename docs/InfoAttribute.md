# InfoAttribute

Info attribute contains content that is for information purpose or represents additional information for object (metadata). Its content can not be edited and is not send in requests to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute for unique identification | 
**name** | **str** | Name of the Attribute that is used for identification | 
**description** | **str** | Optional description of the Attribute, should contain helper text on what is expected | [optional] 
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Content of the Attribute | 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**properties** | [**InfoAttributeProperties**](InfoAttributeProperties.md) |  | 

## Example

```python
from pyCZERTAINLY.models.info_attribute import InfoAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of InfoAttribute from a JSON string
info_attribute_instance = InfoAttribute.from_json(json)
# print the JSON string representation of the object
print(InfoAttribute.to_json())

# convert the object into a dict
info_attribute_dict = info_attribute_instance.to_dict()
# create an instance of InfoAttribute from a dict
info_attribute_from_dict = InfoAttribute.from_dict(info_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


