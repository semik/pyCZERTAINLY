# CertificateDownloadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**CertificateFormat**](CertificateFormat.md) |  | 
**encoding** | [**CertificateFormatEncoding**](CertificateFormatEncoding.md) |  | 
**content** | **str** | Base64 encoded content in the specified format and encoding | 

## Example

```python
from pyCZERTAINLY.models.certificate_download_response_dto import CertificateDownloadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateDownloadResponseDto from a JSON string
certificate_download_response_dto_instance = CertificateDownloadResponseDto.from_json(json)
# print the JSON string representation of the object
print(CertificateDownloadResponseDto.to_json())

# convert the object into a dict
certificate_download_response_dto_dict = certificate_download_response_dto_instance.to_dict()
# create an instance of CertificateDownloadResponseDto from a dict
certificate_download_response_dto_from_dict = CertificateDownloadResponseDto.from_dict(certificate_download_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


