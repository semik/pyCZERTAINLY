# DiscoveryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Discovery name | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes for Discovery | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**connector_uuid** | **str** | Discovery Provider UUID | 
**kind** | **str** | Discovery Kind | 
**triggers** | **List[str]** | List of triggers to be triggered after the discovery is finished, triggers will be evaluated in given order | [optional] 

## Example

```python
from openapi_client.models.discovery_dto import DiscoveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryDto from a JSON string
discovery_dto_instance = DiscoveryDto.from_json(json)
# print the JSON string representation of the object
print(DiscoveryDto.to_json())

# convert the object into a dict
discovery_dto_dict = discovery_dto_instance.to_dict()
# create an instance of DiscoveryDto from a dict
discovery_dto_from_dict = DiscoveryDto.from_dict(discovery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


