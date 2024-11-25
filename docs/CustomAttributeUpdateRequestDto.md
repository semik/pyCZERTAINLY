# CustomAttributeUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Attribute description | [optional] 
**label** | **str** | Friendly name of the the Attribute | 
**visible** | **bool** | Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user. | [optional] [default to True]
**group** | **str** | Group of the Attribute, used for the logical grouping of the Attribute | [optional] 
**required** | **bool** | Boolean determining if the Attribute is required. If true, the Attribute must be provided. | [optional] [default to False]
**read_only** | **bool** | Boolean determining if the Attribute is read only. If true, the Attribute content cannot be changed. | [optional] [default to False]
**list** | **bool** | Boolean determining if the Attribute contains list of values in the content | [optional] [default to False]
**multi_select** | **bool** | Boolean determining if the Attribute can have multiple values | [optional] [default to False]
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Predefined content for the attribute if needed. The content of the Attribute must satisfy the type | [optional] 
**resources** | [**List[Resource]**](Resource.md) | List of resource to be associated with the custom attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.custom_attribute_update_request_dto import CustomAttributeUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeUpdateRequestDto from a JSON string
custom_attribute_update_request_dto_instance = CustomAttributeUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeUpdateRequestDto.to_json())

# convert the object into a dict
custom_attribute_update_request_dto_dict = custom_attribute_update_request_dto_instance.to_dict()
# create an instance of CustomAttributeUpdateRequestDto from a dict
custom_attribute_update_request_dto_from_dict = CustomAttributeUpdateRequestDto.from_dict(custom_attribute_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


