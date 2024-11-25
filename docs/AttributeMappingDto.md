# AttributeMappingDto

List of attribute mappings between mapping attributes and (recipient) custom attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping_attribute_uuid** | **str** | Mapping Attribute UUID | 
**mapping_attribute_name** | **str** | Mapping Attribute Name | 
**custom_attribute_uuid** | **str** | Custom Attribute Uuid | 
**custom_attribute_label** | **str** | Custom Attribute Label | 

## Example

```python
from pyCZERTAINLY.models.attribute_mapping_dto import AttributeMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeMappingDto from a JSON string
attribute_mapping_dto_instance = AttributeMappingDto.from_json(json)
# print the JSON string representation of the object
print(AttributeMappingDto.to_json())

# convert the object into a dict
attribute_mapping_dto_dict = attribute_mapping_dto_instance.to_dict()
# create an instance of AttributeMappingDto from a dict
attribute_mapping_dto_from_dict = AttributeMappingDto.from_dict(attribute_mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


