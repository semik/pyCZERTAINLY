# AuditLogResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 
**items** | [**List[AuditLogDto]**](AuditLogDto.md) | Audit log items | 

## Example

```python
from openapi_client.models.audit_log_response_dto import AuditLogResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogResponseDto from a JSON string
audit_log_response_dto_instance = AuditLogResponseDto.from_json(json)
# print the JSON string representation of the object
print(AuditLogResponseDto.to_json())

# convert the object into a dict
audit_log_response_dto_dict = audit_log_response_dto_instance.to_dict()
# create an instance of AuditLogResponseDto from a dict
audit_log_response_dto_from_dict = AuditLogResponseDto.from_dict(audit_log_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


