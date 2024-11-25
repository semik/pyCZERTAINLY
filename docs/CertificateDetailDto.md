# CertificateDetailDto


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
**extended_key_usage** | **List[str]** | Extended key usages | [optional] 
**key_usage** | **List[str]** | Key usages | 
**subject_type** | [**CertificateSubjectType**](CertificateSubjectType.md) |  | 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Certificate metadata | [optional] 
**certificate_content** | **str** | Base64 encoded Certificate content | 
**subject_alternative_names** | **Dict[str, object]** | Subject alternative names | [optional] 
**locations** | [**List[LocationDto]**](LocationDto.md) | Locations associated to the Certificate | [optional] 
**non_compliant_rules** | [**List[CertificateComplianceResultDto]**](CertificateComplianceResultDto.md) | Certificate compliance check result | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**key** | [**KeyDto**](KeyDto.md) |  | [optional] 
**certificate_request** | [**CertificateRequestDto**](CertificateRequestDto.md) |  | [optional] 
**source_certificate_uuid** | **str** | Source certificate UUID | [optional] 
**issue_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of issue attributes | [optional] 
**revoke_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of revoke attributes | [optional] 
**related_certificates** | [**List[CertificateDto]**](CertificateDto.md) | List of related certificates | [optional] 
**protocol_info** | [**CertificateProtocolDto**](CertificateProtocolDto.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.certificate_detail_dto import CertificateDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateDetailDto from a JSON string
certificate_detail_dto_instance = CertificateDetailDto.from_json(json)
# print the JSON string representation of the object
print(CertificateDetailDto.to_json())

# convert the object into a dict
certificate_detail_dto_dict = certificate_detail_dto_instance.to_dict()
# create an instance of CertificateDetailDto from a dict
certificate_detail_dto_from_dict = CertificateDetailDto.from_dict(certificate_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


