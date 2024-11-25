# RemoveCertificateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of Certificate UUIDs | [optional] 
**filters** | [**List[SearchFilterRequestDto]**](SearchFilterRequestDto.md) | Certificate filter input | [optional] 

## Example

```python
from openapi_client.models.remove_certificate_dto import RemoveCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCertificateDto from a JSON string
remove_certificate_dto_instance = RemoveCertificateDto.from_json(json)
# print the JSON string representation of the object
print(RemoveCertificateDto.to_json())

# convert the object into a dict
remove_certificate_dto_dict = remove_certificate_dto_instance.to_dict()
# create an instance of RemoveCertificateDto from a dict
remove_certificate_dto_from_dict = RemoveCertificateDto.from_dict(remove_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


