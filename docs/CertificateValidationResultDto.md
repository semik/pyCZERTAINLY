# CertificateValidationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | 
**validation_checks** | [**Dict[str, CertificateValidationCheckDto]**](CertificateValidationCheckDto.md) | Certificate validation check results | [optional] 

## Example

```python
from openapi_client.models.certificate_validation_result_dto import CertificateValidationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateValidationResultDto from a JSON string
certificate_validation_result_dto_instance = CertificateValidationResultDto.from_json(json)
# print the JSON string representation of the object
print(CertificateValidationResultDto.to_json())

# convert the object into a dict
certificate_validation_result_dto_dict = certificate_validation_result_dto_instance.to_dict()
# create an instance of CertificateValidationResultDto from a dict
certificate_validation_result_dto_from_dict = CertificateValidationResultDto.from_dict(certificate_validation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


