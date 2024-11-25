# RaProfileCmpDetailResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**cmp_available** | **bool** | CMP availability flag - true &#x3D; yes; false &#x3D; no | 
**cmp_url** | **str** | CMP URL | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue Certificate | [optional] 
**revoke_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to revoke Certificate | [optional] 

## Example

```python
from openapi_client.models.ra_profile_cmp_detail_response_dto import RaProfileCmpDetailResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RaProfileCmpDetailResponseDto from a JSON string
ra_profile_cmp_detail_response_dto_instance = RaProfileCmpDetailResponseDto.from_json(json)
# print the JSON string representation of the object
print(RaProfileCmpDetailResponseDto.to_json())

# convert the object into a dict
ra_profile_cmp_detail_response_dto_dict = ra_profile_cmp_detail_response_dto_instance.to_dict()
# create an instance of RaProfileCmpDetailResponseDto from a dict
ra_profile_cmp_detail_response_dto_from_dict = RaProfileCmpDetailResponseDto.from_dict(ra_profile_cmp_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


