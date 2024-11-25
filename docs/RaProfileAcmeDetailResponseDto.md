# RaProfileAcmeDetailResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**acme_available** | **bool** | ACME availability flag - true &#x3D; yes; false &#x3D; no | 
**directory_url** | **str** | ACME Directory URL | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue Certificate | [optional] 
**revoke_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to revoke Certificate | [optional] 

## Example

```python
from pyCZERTAINLY.models.ra_profile_acme_detail_response_dto import RaProfileAcmeDetailResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RaProfileAcmeDetailResponseDto from a JSON string
ra_profile_acme_detail_response_dto_instance = RaProfileAcmeDetailResponseDto.from_json(json)
# print the JSON string representation of the object
print(RaProfileAcmeDetailResponseDto.to_json())

# convert the object into a dict
ra_profile_acme_detail_response_dto_dict = ra_profile_acme_detail_response_dto_instance.to_dict()
# create an instance of RaProfileAcmeDetailResponseDto from a dict
ra_profile_acme_detail_response_dto_from_dict = RaProfileAcmeDetailResponseDto.from_dict(ra_profile_acme_detail_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


