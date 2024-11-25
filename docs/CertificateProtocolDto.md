# CertificateProtocolDto

Information about protocol used to issue the certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**CertificateProtocol**](CertificateProtocol.md) |  | 
**protocol_profile_uuid** | **str** | UUID of the protocol | 
**additional_protocol_uuid** | **str** | Additional UUID for use of the protocol, for example ACME Account UUID in case of ACME protocol | [optional] 

## Example

```python
from openapi_client.models.certificate_protocol_dto import CertificateProtocolDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateProtocolDto from a JSON string
certificate_protocol_dto_instance = CertificateProtocolDto.from_json(json)
# print the JSON string representation of the object
print(CertificateProtocolDto.to_json())

# convert the object into a dict
certificate_protocol_dto_dict = certificate_protocol_dto_instance.to_dict()
# create an instance of CertificateProtocolDto from a dict
certificate_protocol_dto_from_dict = CertificateProtocolDto.from_dict(certificate_protocol_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


