# CertificateUpdateObjectsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_uuids** | **List[str]** | Certificate Groups UUIDs (set to empty list to remove certificate from all groups) | [optional] 
**owner_uuid** | **str** | Certificate owner user UUID (set to empty string to remove owner of certificate) | [optional] 
**ra_profile_uuid** | **str** | RA Profile UUID (set to empty string to remove certificate from RA profile) | [optional] 
**trusted_ca** | **bool** | Mark CA certificate as trusted | [optional] 

## Example

```python
from pyCZERTAINLY.models.certificate_update_objects_dto import CertificateUpdateObjectsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateUpdateObjectsDto from a JSON string
certificate_update_objects_dto_instance = CertificateUpdateObjectsDto.from_json(json)
# print the JSON string representation of the object
print(CertificateUpdateObjectsDto.to_json())

# convert the object into a dict
certificate_update_objects_dto_dict = certificate_update_objects_dto_instance.to_dict()
# create an instance of CertificateUpdateObjectsDto from a dict
certificate_update_objects_dto_from_dict = CertificateUpdateObjectsDto.from_dict(certificate_update_objects_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


