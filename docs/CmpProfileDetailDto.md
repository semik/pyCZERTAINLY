# CmpProfileDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**variant** | **str** | Variant of the CMP Profile | 
**description** | **str** | CMP Profile description | [optional] 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**cmp_url** | **str** | CMP URL | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue a Certificate for the associated RA Profile | [optional] 
**revoke_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to revoke a Certificate for the associated RA Profile | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes for CMP Profile | [optional] 
**request_protection_method** | [**ProtectionMethod**](ProtectionMethod.md) |  | 
**response_protection_method** | [**ProtectionMethod**](ProtectionMethod.md) |  | 
**signing_certificate** | [**CertificateDto**](CertificateDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.cmp_profile_detail_dto import CmpProfileDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of CmpProfileDetailDto from a JSON string
cmp_profile_detail_dto_instance = CmpProfileDetailDto.from_json(json)
# print the JSON string representation of the object
print(CmpProfileDetailDto.to_json())

# convert the object into a dict
cmp_profile_detail_dto_dict = cmp_profile_detail_dto_instance.to_dict()
# create an instance of CmpProfileDetailDto from a dict
cmp_profile_detail_dto_from_dict = CmpProfileDetailDto.from_dict(cmp_profile_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


