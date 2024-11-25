# CertificateComplianceCheckDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_uuids** | **List[str]** | List of UUIDs of the Certificates | [optional] 

## Example

```python
from pyCZERTAINLY.models.certificate_compliance_check_dto import CertificateComplianceCheckDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateComplianceCheckDto from a JSON string
certificate_compliance_check_dto_instance = CertificateComplianceCheckDto.from_json(json)
# print the JSON string representation of the object
print(CertificateComplianceCheckDto.to_json())

# convert the object into a dict
certificate_compliance_check_dto_dict = certificate_compliance_check_dto_instance.to_dict()
# create an instance of CertificateComplianceCheckDto from a dict
certificate_compliance_check_dto_from_dict = CertificateComplianceCheckDto.from_dict(certificate_compliance_check_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


