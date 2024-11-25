# CertificateInLocationDto

List of Certificates in Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_uuid** | **str** | UUID of the Certificate | 
**state** | [**CertificateState**](CertificateState.md) |  | 
**validation_status** | [**CertificateValidationStatus**](CertificateValidationStatus.md) |  | 
**common_name** | **str** | Common Name of the Subject DN field of the Certificate | 
**serial_number** | **str** | Serial number in HEX of the Certificate | 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Metadata of the Certificate in Location | [optional] 
**push_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Applied push attributes | [optional] 
**csr_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Applied issue attributes | [optional] 
**with_key** | **bool** | If the Certificate in Location has associated private key | [optional] [default to False]

## Example

```python
from openapi_client.models.certificate_in_location_dto import CertificateInLocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateInLocationDto from a JSON string
certificate_in_location_dto_instance = CertificateInLocationDto.from_json(json)
# print the JSON string representation of the object
print(CertificateInLocationDto.to_json())

# convert the object into a dict
certificate_in_location_dto_dict = certificate_in_location_dto_instance.to_dict()
# create an instance of CertificateInLocationDto from a dict
certificate_in_location_dto_from_dict = CertificateInLocationDto.from_dict(certificate_in_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


