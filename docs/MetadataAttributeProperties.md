# MetadataAttributeProperties

Properties of the Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 
**var_global** | **bool** | Boolean determining if the Metadata is a global metadata. | [optional] [default to False]
**overwrite** | **bool** | Boolean determining if the new metadata content should overwrite (replace) existing content instead of appending. | [optional] [default to False]

## Example

```python
from openapi_client.models.metadata_attribute_properties import MetadataAttributeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataAttributeProperties from a JSON string
metadata_attribute_properties_instance = MetadataAttributeProperties.from_json(json)
# print the JSON string representation of the object
print(MetadataAttributeProperties.to_json())

# convert the object into a dict
metadata_attribute_properties_dict = metadata_attribute_properties_instance.to_dict()
# create an instance of MetadataAttributeProperties from a dict
metadata_attribute_properties_from_dict = MetadataAttributeProperties.from_dict(metadata_attribute_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


