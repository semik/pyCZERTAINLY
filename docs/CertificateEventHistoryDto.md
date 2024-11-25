# CertificateEventHistoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the event | 
**certificate_uuid** | **str** | UUID of the Certificate | 
**created** | **datetime** | Event creation time | 
**created_by** | **str** | Created By | 
**event** | **str** | Event type | 
**status** | **str** | Event result | 
**message** | **str** | Event message | 
**additional_information** | **Dict[str, object]** | Additional information for the event | [optional] 

## Example

```python
from openapi_client.models.certificate_event_history_dto import CertificateEventHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateEventHistoryDto from a JSON string
certificate_event_history_dto_instance = CertificateEventHistoryDto.from_json(json)
# print the JSON string representation of the object
print(CertificateEventHistoryDto.to_json())

# convert the object into a dict
certificate_event_history_dto_dict = certificate_event_history_dto_instance.to_dict()
# create an instance of CertificateEventHistoryDto from a dict
certificate_event_history_dto_from_dict = CertificateEventHistoryDto.from_dict(certificate_event_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


