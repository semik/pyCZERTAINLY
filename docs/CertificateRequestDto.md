# CertificateRequestDto

Certificate request data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_type** | [**CertificateType**](CertificateType.md) |  | [optional] 
**certificate_request_format** | [**CertificateRequestFormat**](CertificateRequestFormat.md) |  | [optional] [default to CertificateRequestFormat.PKCS10]
**public_key_algorithm** | **str** | Public key algorithm | 
**signature_algorithm** | **str** | Certificate signature algorithm | 
**content** | **str** | Certificate request content | 
**common_name** | **str** | Certificate common name | 
**subject_dn** | **str** | Subject DN of the Certificate | 
**subject_alternative_names** | **Dict[str, object]** | Subject alternative names | [optional] 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | CSR Attributes | [optional] 
**signature_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Signature Attributes | [optional] 

## Example

```python
from openapi_client.models.certificate_request_dto import CertificateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateRequestDto from a JSON string
certificate_request_dto_instance = CertificateRequestDto.from_json(json)
# print the JSON string representation of the object
print(CertificateRequestDto.to_json())

# convert the object into a dict
certificate_request_dto_dict = certificate_request_dto_instance.to_dict()
# create an instance of CertificateRequestDto from a dict
certificate_request_dto_from_dict = CertificateRequestDto.from_dict(certificate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


