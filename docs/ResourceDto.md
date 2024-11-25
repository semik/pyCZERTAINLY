# ResourceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**Resource**](Resource.md) |  | 
**has_object_access** | **bool** | If resource has Object access permissions. True &#x3D; Yes, False &#x3D; No | 
**has_custom_attributes** | **bool** | Support assigning custom attributes to resource objects | 
**has_groups** | **bool** | Support assigning groups to resource objects | 
**has_owner** | **bool** | Support assigning owner to resource objects | 
**has_events** | **bool** | Has events that can be used in triggers | 
**has_rule_evaluator** | **bool** | Has rule evaluator that can evaluate conditions and actions | 

## Example

```python
from openapi_client.models.resource_dto import ResourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDto from a JSON string
resource_dto_instance = ResourceDto.from_json(json)
# print the JSON string representation of the object
print(ResourceDto.to_json())

# convert the object into a dict
resource_dto_dict = resource_dto_instance.to_dict()
# create an instance of ResourceDto from a dict
resource_dto_from_dict = ResourceDto.from_dict(resource_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


