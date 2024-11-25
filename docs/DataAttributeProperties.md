# DataAttributeProperties

Properties of the Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 
**required** | **bool** | Boolean determining if the Attribute is required. If true, the Attribute must be provided. | [default to False]
**read_only** | **bool** | Boolean determining if the Attribute is read only. If true, the Attribute content cannot be changed. | [default to False]
**list** | **bool** | Boolean determining if the Attribute contains list of values in the content | [default to False]
**multi_select** | **bool** | Boolean determining if the Attribute can have multiple values | [default to False]

## Example

```python
from pyCZERTAINLY.models.data_attribute_properties import DataAttributeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DataAttributeProperties from a JSON string
data_attribute_properties_instance = DataAttributeProperties.from_json(json)
# print the JSON string representation of the object
print(DataAttributeProperties.to_json())

# convert the object into a dict
data_attribute_properties_dict = data_attribute_properties_instance.to_dict()
# create an instance of DataAttributeProperties from a dict
data_attribute_properties_from_dict = DataAttributeProperties.from_dict(data_attribute_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


