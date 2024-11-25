# RaProfileScepDetailResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**scep_available** | **bool** | SCEP availability flag - true &#x3D; yes; false &#x3D; no | 
**url** | **str** | SCEP URL | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue Certificate | [optional] 

## Example

```python
from openapi_client.models.ra_profile_scep_detail_response_dto import RaProfileScepDetailResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RaProfileScepDetailResponseDto from a JSON string
ra_profile_scep_detail_response_dto_instance = RaProfileScepDetailResponseDto.from_json(json)
# print the JSON string representation of the object
print(RaProfileScepDetailResponseDto.to_json())

# convert the object into a dict
ra_profile_scep_detail_response_dto_dict = ra_profile_scep_detail_response_dto_instance.to_dict()
# create an instance of RaProfileScepDetailResponseDto from a dict
ra_profile_scep_detail_response_dto_from_dict = RaProfileScepDetailResponseDto.from_dict(ra_profile_scep_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


