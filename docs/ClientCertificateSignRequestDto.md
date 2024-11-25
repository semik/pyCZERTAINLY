# ClientCertificateSignRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of attributes to create CSR. Required if CSR is not provided | [optional] 
**signature_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of attributes to sign the CSR | [optional] 
**request** | **str** | Certificate signing request encoded as Base64 string | 
**format** | [**CertificateRequestFormat**](CertificateRequestFormat.md) |  | [optional] [default to CertificateRequestFormat.PKCS10]
**token_profile_uuid** | **str** | Token Profile UUID. Required if CSR is not uploaded | [optional] 
**key_uuid** | **str** | Key UUID. Required if CSR is not uploaded | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of RA Profile related Attributes to issue Certificate | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.client_certificate_sign_request_dto import ClientCertificateSignRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateSignRequestDto from a JSON string
client_certificate_sign_request_dto_instance = ClientCertificateSignRequestDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateSignRequestDto.to_json())

# convert the object into a dict
client_certificate_sign_request_dto_dict = client_certificate_sign_request_dto_instance.to_dict()
# create an instance of ClientCertificateSignRequestDto from a dict
client_certificate_sign_request_dto_from_dict = ClientCertificateSignRequestDto.from_dict(client_certificate_sign_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


