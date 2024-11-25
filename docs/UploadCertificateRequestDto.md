# UploadCertificateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Base64 Content of the Certificate | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Custom Attributes for the Certificate | 

## Example

```python
from openapi_client.models.upload_certificate_request_dto import UploadCertificateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadCertificateRequestDto from a JSON string
upload_certificate_request_dto_instance = UploadCertificateRequestDto.from_json(json)
# print the JSON string representation of the object
print(UploadCertificateRequestDto.to_json())

# convert the object into a dict
upload_certificate_request_dto_dict = upload_certificate_request_dto_instance.to_dict()
# create an instance of UploadCertificateRequestDto from a dict
upload_certificate_request_dto_from_dict = UploadCertificateRequestDto.from_dict(upload_certificate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


