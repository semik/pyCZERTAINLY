# CertificateContentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Certificate | 
**common_name** | **str** | Certificate common name | 
**serial_number** | **str** | Certificate serial number | 
**certificate_content** | **str** | Base64 encoded Certificate content | 

## Example

```python
from pyCZERTAINLY.models.certificate_content_dto import CertificateContentDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateContentDto from a JSON string
certificate_content_dto_instance = CertificateContentDto.from_json(json)
# print the JSON string representation of the object
print(CertificateContentDto.to_json())

# convert the object into a dict
certificate_content_dto_dict = certificate_content_dto_instance.to_dict()
# create an instance of CertificateContentDto from a dict
certificate_content_dto_from_dict = CertificateContentDto.from_dict(certificate_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


