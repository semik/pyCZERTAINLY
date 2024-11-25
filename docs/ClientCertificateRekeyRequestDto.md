# ClientCertificateRekeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replace_in_locations** | **bool** | True to replace renewed certificate in the associated locations | [optional] [default to False]
**request** | **str** | Certificate signing request encoded as Base64 string. If not provided, CSR attributes will be used | [optional] 
**format** | [**CertificateRequestFormat**](CertificateRequestFormat.md) |  | [optional] [default to CertificateRequestFormat.PKCS10]
**key_uuid** | **str** | Key UUID | 
**token_profile_uuid** | **str** | Token Profile UUID | 
**signature_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Signature Attributes. If not provided, existing attributes will be used to generate the new CSR | [optional] 

## Example

```python
from pyCZERTAINLY.models.client_certificate_rekey_request_dto import ClientCertificateRekeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateRekeyRequestDto from a JSON string
client_certificate_rekey_request_dto_instance = ClientCertificateRekeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateRekeyRequestDto.to_json())

# convert the object into a dict
client_certificate_rekey_request_dto_dict = client_certificate_rekey_request_dto_instance.to_dict()
# create an instance of ClientCertificateRekeyRequestDto from a dict
client_certificate_rekey_request_dto_from_dict = ClientCertificateRekeyRequestDto.from_dict(client_certificate_rekey_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


