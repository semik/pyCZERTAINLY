# CmpProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the CMP Profile | [optional] 
**ra_profile_uuid** | **str** | RA Profile UUID that the CMP Profile is associated with | [optional] 
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate for the associated RA Profile. Required when raProfileUuid is provided | [optional] 
**revoke_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to revoke Certificate for the associated RA Profile. Required when raProfileUuid is provided | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes for CMP Profile | [optional] 
**request_protection_method** | [**ProtectionMethod**](ProtectionMethod.md) |  | 
**response_protection_method** | [**ProtectionMethod**](ProtectionMethod.md) |  | 
**shared_secret** | **str** | Shared secret for the CMP Request. Required when requestProtectionMethod is sharedSecret | [optional] 
**signing_certificate_uuid** | **str** | UUID of the Certificate to be used as signing certificate for CMP responses. Required when responseProtectionMethod is signature | [optional] 
**name** | **str** | Name of the CMP Profile | 
**variant** | **str** | Variant of the CMP Profile | 

## Example

```python
from openapi_client.models.cmp_profile_request_dto import CmpProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CmpProfileRequestDto from a JSON string
cmp_profile_request_dto_instance = CmpProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(CmpProfileRequestDto.to_json())

# convert the object into a dict
cmp_profile_request_dto_dict = cmp_profile_request_dto_instance.to_dict()
# create an instance of CmpProfileRequestDto from a dict
cmp_profile_request_dto_from_dict = CmpProfileRequestDto.from_dict(cmp_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


