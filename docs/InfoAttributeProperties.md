# InfoAttributeProperties

Properties of the Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.info_attribute_properties import InfoAttributeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InfoAttributeProperties from a JSON string
info_attribute_properties_instance = InfoAttributeProperties.from_json(json)
# print the JSON string representation of the object
print(InfoAttributeProperties.to_json())

# convert the object into a dict
info_attribute_properties_dict = info_attribute_properties_instance.to_dict()
# create an instance of InfoAttributeProperties from a dict
info_attribute_properties_from_dict = InfoAttributeProperties.from_dict(info_attribute_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


