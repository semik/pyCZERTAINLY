# LocationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Location | [optional] 
**entity_instance_uuid** | **str** | UUID of Entity instance | 
**entity_instance_name** | **str** | Name of Entity instance | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Location attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**support_multiple_entries** | **bool** | If the location supports multiple Certificates | [default to False]
**support_key_management** | **bool** | If the location supports key management operations | [default to False]
**certificates** | [**List[CertificateInLocationDto]**](CertificateInLocationDto.md) | List of Certificates in Location | 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Location metadata | [optional] 

## Example

```python
from openapi_client.models.location_dto import LocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDto from a JSON string
location_dto_instance = LocationDto.from_json(json)
# print the JSON string representation of the object
print(LocationDto.to_json())

# convert the object into a dict
location_dto_dict = location_dto_instance.to_dict()
# create an instance of LocationDto from a dict
location_dto_from_dict = LocationDto.from_dict(location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


