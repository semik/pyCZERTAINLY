# ResourceEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Resource event code | 
**produced_resource** | [**Resource**](Resource.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_event_dto import ResourceEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceEventDto from a JSON string
resource_event_dto_instance = ResourceEventDto.from_json(json)
# print the JSON string representation of the object
print(ResourceEventDto.to_json())

# convert the object into a dict
resource_event_dto_dict = resource_event_dto_instance.to_dict()
# create an instance of ResourceEventDto from a dict
resource_event_dto_from_dict = ResourceEventDto.from_dict(resource_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


