# HealthDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HealthStatus**](HealthStatus.md) |  | 
**description** | **str** | Detailed status description | [optional] 
**parts** | [**Dict[str, HealthDto]**](HealthDto.md) | Nested status of services | [optional] 

## Example

```python
from openapi_client.models.health_dto import HealthDto

# TODO update the JSON string below
json = "{}"
# create an instance of HealthDto from a JSON string
health_dto_instance = HealthDto.from_json(json)
# print the JSON string representation of the object
print(HealthDto.to_json())

# convert the object into a dict
health_dto_dict = health_dto_instance.to_dict()
# create an instance of HealthDto from a dict
health_dto_from_dict = HealthDto.from_dict(health_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


