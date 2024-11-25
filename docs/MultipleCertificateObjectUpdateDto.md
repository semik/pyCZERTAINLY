# MultipleCertificateObjectUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_uuids** | **List[str]** | Certificate Groups UUIDs (set to empty list to remove certificate from all groups) | [optional] 
**owner_uuid** | **str** | Certificate owner user UUID (set to empty string to remove owner of certificate) | [optional] 
**ra_profile_uuid** | **str** | RA Profile UUID (set to empty string to remove certificate from RA profile) | [optional] 
**certificate_uuids** | **List[str]** | List of Certificate UUIDs | [optional] 
**filters** | [**List[SearchFilterRequestDto]**](SearchFilterRequestDto.md) | Certificate filter input | [optional] 

## Example

```python
from pyCZERTAINLY.models.multiple_certificate_object_update_dto import MultipleCertificateObjectUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleCertificateObjectUpdateDto from a JSON string
multiple_certificate_object_update_dto_instance = MultipleCertificateObjectUpdateDto.from_json(json)
# print the JSON string representation of the object
print(MultipleCertificateObjectUpdateDto.to_json())

# convert the object into a dict
multiple_certificate_object_update_dto_dict = multiple_certificate_object_update_dto_instance.to_dict()
# create an instance of MultipleCertificateObjectUpdateDto from a dict
multiple_certificate_object_update_dto_from_dict = MultipleCertificateObjectUpdateDto.from_dict(multiple_certificate_object_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


