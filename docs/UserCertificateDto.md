# UserCertificateDto

User Certificate details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the certificate | 
**fingerprint** | **str** | Fingerprint of the certificate | 

## Example

```python
from pyCZERTAINLY.models.user_certificate_dto import UserCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserCertificateDto from a JSON string
user_certificate_dto_instance = UserCertificateDto.from_json(json)
# print the JSON string representation of the object
print(UserCertificateDto.to_json())

# convert the object into a dict
user_certificate_dto_dict = user_certificate_dto_instance.to_dict()
# create an instance of UserCertificateDto from a dict
user_certificate_dto_from_dict = UserCertificateDto.from_dict(user_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


