# GlobalMetadataCreateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Attribute | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**description** | **str** | Attribute description | [optional] 
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [optional] [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.global_metadata_create_request_dto import GlobalMetadataCreateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalMetadataCreateRequestDto from a JSON string
global_metadata_create_request_dto_instance = GlobalMetadataCreateRequestDto.from_json(json)
# print the JSON string representation of the object
print(GlobalMetadataCreateRequestDto.to_json())

# convert the object into a dict
global_metadata_create_request_dto_dict = global_metadata_create_request_dto_instance.to_dict()
# create an instance of GlobalMetadataCreateRequestDto from a dict
global_metadata_create_request_dto_from_dict = GlobalMetadataCreateRequestDto.from_dict(global_metadata_create_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


