# ScepProfileEditRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the SCEP Profile | [optional] 
**ra_profile_uuid** | **str** | RA Profile UUID | [optional] 
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate | 
**ca_certificate_uuid** | **str** | UUID of the Certificate to be used as CA Certificate for SCEP Requests | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**renewal_threshold** | **int** | Minimum expiry days to allow renewal of certificate. Empty or the value &#39;0&#39; will be considered as null and half life of the certificate validity will be considered for the protocol | [optional] 
**include_ca_certificate** | **bool** | Include CA Certificate in the SCEP Message response | [optional] [default to False]
**include_ca_certificate_chain** | **bool** | Include CA Certificate Chain in the SCEP Message response | [optional] [default to False]
**challenge_password** | **str** | Challenge Password for the SCEP Request | [optional] 
**enable_intune** | **bool** | Status of Intune | [optional] 
**intune_tenant** | **str** | Intune Tenant | [optional] 
**intune_application_id** | **str** | Intune Application ID | [optional] 
**intune_application_key** | **str** | Intune Application Key | [optional] 

## Example

```python
from pyCZERTAINLY.models.scep_profile_edit_request_dto import ScepProfileEditRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfileEditRequestDto from a JSON string
scep_profile_edit_request_dto_instance = ScepProfileEditRequestDto.from_json(json)
# print the JSON string representation of the object
print(ScepProfileEditRequestDto.to_json())

# convert the object into a dict
scep_profile_edit_request_dto_dict = scep_profile_edit_request_dto_instance.to_dict()
# create an instance of ScepProfileEditRequestDto from a dict
scep_profile_edit_request_dto_from_dict = ScepProfileEditRequestDto.from_dict(scep_profile_edit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


