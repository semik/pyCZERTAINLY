# CertificateDto

CA Certificate for the SCEP Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Certificate | 
**common_name** | **str** | Certificate common name | 
**serial_number** | **str** | Certificate serial number | [optional] 
**issuer_common_name** | **str** | Certificate issuer common name | [optional] 
**issuer_dn** | **str** | Issuer DN of the Certificate | [optional] 
**subject_dn** | **str** | Subject DN of the Certificate | 
**not_before** | **datetime** | Certificate validity start date | [optional] 
**not_after** | **datetime** | Certificate expiration date | [optional] 
**public_key_algorithm** | **str** | Public key algorithm | 
**signature_algorithm** | **str** | Certificate signature algorithm | 
**key_size** | **int** | Certificate key size | 
**state** | [**CertificateState**](CertificateState.md) |  | 
**validation_status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**fingerprint** | **str** | SHA256 fingerprint of the Certificate | [optional] 
**groups** | [**List[GroupDto]**](GroupDto.md) | Groups associated to the Certificate | [optional] 
**owner** | **str** | Certificate Owner | [optional] 
**owner_uuid** | **str** | Certificate Owner UUID | [optional] 
**certificate_type** | [**CertificateType**](CertificateType.md) |  | [optional] 
**issuer_serial_number** | **str** | Serial number of the issuer | [optional] 
**compliance_status** | [**ComplianceStatus**](ComplianceStatus.md) |  | [optional] 
**issuer_certificate_uuid** | **str** | UUID of the issuer certificate | [optional] 
**private_key_availability** | **bool** | Private Key Availability | 
**trusted_ca** | **bool** | Indicator whether CA is marked as trusted, set to null if certificate is not CA | 

## Example

```python
from pyCZERTAINLY.models.certificate_dto import CertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateDto from a JSON string
certificate_dto_instance = CertificateDto.from_json(json)
# print the JSON string representation of the object
print(CertificateDto.to_json())

# convert the object into a dict
certificate_dto_dict = certificate_dto_instance.to_dict()
# create an instance of CertificateDto from a dict
certificate_dto_from_dict = CertificateDto.from_dict(certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


