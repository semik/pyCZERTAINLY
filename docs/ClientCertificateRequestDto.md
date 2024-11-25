# ClientCertificateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra_profile_uuid** | **str** | RA Profile UUID. Required if CSR is not uploaded | 
**source_certificate_uuid** | **str** | Source certificate UUID to specify in case of renew/rekey operation | [optional] 
**csr_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of attributes to create CSR. Required if CSR is not provided | [optional] 
**signature_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of attributes to sign the CSR | [optional] 
**request** | **str** | Certificate signing request encoded as Base64 string | [optional] 
**format** | [**CertificateRequestFormat**](CertificateRequestFormat.md) |  | [optional] [default to CertificateRequestFormat.PKCS10]
**token_profile_uuid** | **str** | Token Profile UUID. Required if CSR is not uploaded | [optional] 
**key_uuid** | **str** | Key UUID. Required if CSR is not uploaded | [optional] 
**issue_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of RA Profile related Attributes to issue Certificate | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.client_certificate_request_dto import ClientCertificateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateRequestDto from a JSON string
client_certificate_request_dto_instance = ClientCertificateRequestDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateRequestDto.to_json())

# convert the object into a dict
client_certificate_request_dto_dict = client_certificate_request_dto_instance.to_dict()
# create an instance of ClientCertificateRequestDto from a dict
client_certificate_request_dto_from_dict = ClientCertificateRequestDto.from_dict(client_certificate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


