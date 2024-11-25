# ScepProfileDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**description** | **str** | SCEP Profile description | [optional] 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**include_ca_certificate** | **bool** | Include CA certificate in the SCEP response | 
**include_ca_certificate_chain** | **bool** | Include CA certificate chain in the SCEP response | 
**renew_threshold** | **int** | Renewal time threshold in days | [optional] 
**scep_url** | **str** | SCEP URL | [optional] 
**enable_intune** | **bool** | Status of Intune | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue a Certificate | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**ca_certificate** | [**CertificateDto**](CertificateDto.md) |  | [optional] 
**intune_tenant** | **str** | Intune tenant | [optional] 
**intune_application_id** | **str** | Intune application ID | [optional] 

## Example

```python
from pyCZERTAINLY.models.scep_profile_detail_dto import ScepProfileDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfileDetailDto from a JSON string
scep_profile_detail_dto_instance = ScepProfileDetailDto.from_json(json)
# print the JSON string representation of the object
print(ScepProfileDetailDto.to_json())

# convert the object into a dict
scep_profile_detail_dto_dict = scep_profile_detail_dto_instance.to_dict()
# create an instance of ScepProfileDetailDto from a dict
scep_profile_detail_dto_from_dict = ScepProfileDetailDto.from_dict(scep_profile_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


