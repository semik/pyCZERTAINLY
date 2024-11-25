# ClientCertificateRenewRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replace_in_locations** | **bool** | True to replace renewed certificate in the associated locations | [optional] [default to False]
**request** | **str** | Certificate signing request encoded as Base64 string. If not provided, Existing CSR will be used | [optional] 
**format** | [**CertificateRequestFormat**](CertificateRequestFormat.md) |  | [optional] [default to CertificateRequestFormat.PKCS10]

## Example

```python
from openapi_client.models.client_certificate_renew_request_dto import ClientCertificateRenewRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateRenewRequestDto from a JSON string
client_certificate_renew_request_dto_instance = ClientCertificateRenewRequestDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateRenewRequestDto.to_json())

# convert the object into a dict
client_certificate_renew_request_dto_dict = client_certificate_renew_request_dto_instance.to_dict()
# create an instance of ClientCertificateRenewRequestDto from a dict
client_certificate_renew_request_dto_from_dict = ClientCertificateRenewRequestDto.from_dict(client_certificate_renew_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


