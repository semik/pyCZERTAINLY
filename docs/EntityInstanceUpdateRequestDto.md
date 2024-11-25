# EntityInstanceUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Entity instance Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.entity_instance_update_request_dto import EntityInstanceUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityInstanceUpdateRequestDto from a JSON string
entity_instance_update_request_dto_instance = EntityInstanceUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(EntityInstanceUpdateRequestDto.to_json())

# convert the object into a dict
entity_instance_update_request_dto_dict = entity_instance_update_request_dto_instance.to_dict()
# create an instance of EntityInstanceUpdateRequestDto from a dict
entity_instance_update_request_dto_from_dict = EntityInstanceUpdateRequestDto.from_dict(entity_instance_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


