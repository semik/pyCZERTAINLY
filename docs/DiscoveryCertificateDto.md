# DiscoveryCertificateDto

Certificates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Certificate | 
**inventory_uuid** | **str** | UUID of the Certificate in Certificate inventory | [optional] 
**common_name** | **str** | Certificate common name | 
**serial_number** | **str** | Certificate Serial Number | 
**issuer_common_name** | **str** | Issuer common name | 
**not_before** | **datetime** | Certificate validity start date | 
**not_after** | **datetime** | Certificate expiration date | 
**fingerprint** | **str** | SHA256 thumbprint of the certificate | 
**certificate_content** | **str** | Base64 encoded Certificate content | 
**newly_discovered** | **bool** | Boolean representing if the certificate is newly discovered. True - Certificate is newly discoveredfalse - Certificate was already available in the inventory | 
**processed** | **bool** | Indicator whether the discovery certificate has already been processed. | 
**processed_error** | **str** | Error message in case of failed processing of the discovery certificate. | [optional] 

## Example

```python
from openapi_client.models.discovery_certificate_dto import DiscoveryCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryCertificateDto from a JSON string
discovery_certificate_dto_instance = DiscoveryCertificateDto.from_json(json)
# print the JSON string representation of the object
print(DiscoveryCertificateDto.to_json())

# convert the object into a dict
discovery_certificate_dto_dict = discovery_certificate_dto_instance.to_dict()
# create an instance of DiscoveryCertificateDto from a dict
discovery_certificate_dto_from_dict = DiscoveryCertificateDto.from_dict(discovery_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


