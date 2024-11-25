# GlobalMetadataDefinitionDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | 
**name** | **str** | Name of the Attribute | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**description** | **str** | Attribute description | 
**enabled** | **bool** | Boolean determining if the Attribute is enabled. Required only for Custom Attribute | [optional] 
**type** | [**AttributeType**](AttributeType.md) |  | 
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [optional] [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalMetadataDefinitionDetailDto from a JSON string
global_metadata_definition_detail_dto_instance = GlobalMetadataDefinitionDetailDto.from_json(json)
# print the JSON string representation of the object
print(GlobalMetadataDefinitionDetailDto.to_json())

# convert the object into a dict
global_metadata_definition_detail_dto_dict = global_metadata_definition_detail_dto_instance.to_dict()
# create an instance of GlobalMetadataDefinitionDetailDto from a dict
global_metadata_definition_detail_dto_from_dict = GlobalMetadataDefinitionDetailDto.from_dict(global_metadata_definition_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


