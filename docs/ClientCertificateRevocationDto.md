# ClientCertificateRevocationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**CertificateRevocationReason**](CertificateRevocationReason.md) |  | [optional] [default to UNSPECIFIED]
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to revoke Certificate | 
**destroy_key** | **bool** | Destroy Key upon successful revocation | [optional] [default to False]

## Example

```python
from pyCZERTAINLY.models.client_certificate_revocation_dto import ClientCertificateRevocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateRevocationDto from a JSON string
client_certificate_revocation_dto_instance = ClientCertificateRevocationDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateRevocationDto.to_json())

# convert the object into a dict
client_certificate_revocation_dto_dict = client_certificate_revocation_dto_instance.to_dict()
# create an instance of ClientCertificateRevocationDto from a dict
client_certificate_revocation_dto_from_dict = ClientCertificateRevocationDto.from_dict(client_certificate_revocation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


