# CertificateComplianceResultDto

Certificate compliance check result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | 
**rule_name** | **str** | Name of the rule | 
**rule_description** | **str** | Description of the rule | 
**status** | [**ComplianceRuleStatus**](ComplianceRuleStatus.md) |  | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Attributes of the rule | [optional] 

## Example

```python
from openapi_client.models.certificate_compliance_result_dto import CertificateComplianceResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateComplianceResultDto from a JSON string
certificate_compliance_result_dto_instance = CertificateComplianceResultDto.from_json(json)
# print the JSON string representation of the object
print(CertificateComplianceResultDto.to_json())

# convert the object into a dict
certificate_compliance_result_dto_dict = certificate_compliance_result_dto_instance.to_dict()
# create an instance of CertificateComplianceResultDto from a dict
certificate_compliance_result_dto_from_dict = CertificateComplianceResultDto.from_dict(certificate_compliance_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


