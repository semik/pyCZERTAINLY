# EntityInstanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Entity instance Attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**status** | **str** | Status of Entity instance | 
**connector_uuid** | **str** | UUID of Entity Provider | 
**connector_name** | **str** | Name of Entity Provider | 
**kind** | **str** | Entity instance Kind | 

## Example

```python
from openapi_client.models.entity_instance_dto import EntityInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityInstanceDto from a JSON string
entity_instance_dto_instance = EntityInstanceDto.from_json(json)
# print the JSON string representation of the object
print(EntityInstanceDto.to_json())

# convert the object into a dict
entity_instance_dto_dict = entity_instance_dto_instance.to_dict()
# create an instance of EntityInstanceDto from a dict
entity_instance_dto_from_dict = EntityInstanceDto.from_dict(entity_instance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


