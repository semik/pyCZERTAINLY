# CertificateChainDownloadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**CertificateFormat**](CertificateFormat.md) |  | 
**encoding** | [**CertificateFormatEncoding**](CertificateFormatEncoding.md) |  | 
**content** | **str** | Base64 encoded content in the specified format and encoding | 
**complete_chain** | **bool** | Indicator whether the chain returned is complete | 

## Example

```python
from openapi_client.models.certificate_chain_download_response_dto import CertificateChainDownloadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainDownloadResponseDto from a JSON string
certificate_chain_download_response_dto_instance = CertificateChainDownloadResponseDto.from_json(json)
# print the JSON string representation of the object
print(CertificateChainDownloadResponseDto.to_json())

# convert the object into a dict
certificate_chain_download_response_dto_dict = certificate_chain_download_response_dto_instance.to_dict()
# create an instance of CertificateChainDownloadResponseDto from a dict
certificate_chain_download_response_dto_from_dict = CertificateChainDownloadResponseDto.from_dict(certificate_chain_download_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


