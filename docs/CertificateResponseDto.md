# CertificateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[CertificateDto]**](CertificateDto.md) | Certificates | 
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 

## Example

```python
from pyCZERTAINLY.models.certificate_response_dto import CertificateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateResponseDto from a JSON string
certificate_response_dto_instance = CertificateResponseDto.from_json(json)
# print the JSON string representation of the object
print(CertificateResponseDto.to_json())

# convert the object into a dict
certificate_response_dto_dict = certificate_response_dto_instance.to_dict()
# create an instance of CertificateResponseDto from a dict
certificate_response_dto_from_dict = CertificateResponseDto.from_dict(certificate_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


