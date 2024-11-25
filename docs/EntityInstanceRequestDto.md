# EntityInstanceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entity instance name | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Entity instance Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**connector_uuid** | **str** | UUID of Entity Provider | 
**kind** | **str** | Entity instance Kind | 

## Example

```python
from openapi_client.models.entity_instance_request_dto import EntityInstanceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityInstanceRequestDto from a JSON string
entity_instance_request_dto_instance = EntityInstanceRequestDto.from_json(json)
# print the JSON string representation of the object
print(EntityInstanceRequestDto.to_json())

# convert the object into a dict
entity_instance_request_dto_dict = entity_instance_request_dto_instance.to_dict()
# create an instance of EntityInstanceRequestDto from a dict
entity_instance_request_dto_from_dict = EntityInstanceRequestDto.from_dict(entity_instance_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


