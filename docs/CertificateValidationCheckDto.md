# CertificateValidationCheckDto

Certificate validation check results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_check** | [**CertificateValidationCheck**](CertificateValidationCheck.md) |  | 
**status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | 
**message** | **str** | Certificate validation check result message | [optional] 

## Example

```python
from openapi_client.models.certificate_validation_check_dto import CertificateValidationCheckDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateValidationCheckDto from a JSON string
certificate_validation_check_dto_instance = CertificateValidationCheckDto.from_json(json)
# print the JSON string representation of the object
print(CertificateValidationCheckDto.to_json())

# convert the object into a dict
certificate_validation_check_dto_dict = certificate_validation_check_dto_instance.to_dict()
# create an instance of CertificateValidationCheckDto from a dict
certificate_validation_check_dto_from_dict = CertificateValidationCheckDto.from_dict(certificate_validation_check_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


