# AuditLogDto

Audit log items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Audit log Id | 
**version** | **str** | Log schema version | 
**logged_at** | **datetime** | Time when the audit log is stored | 
**module** | [**Module**](Module.md) |  | 
**actor** | [**ActorRecord**](ActorRecord.md) |  | 
**source** | [**SourceRecord**](SourceRecord.md) |  | [optional] 
**resource** | [**ResourceRecord**](ResourceRecord.md) |  | 
**affiliated_resource** | [**ResourceRecord**](ResourceRecord.md) |  | [optional] 
**operation** | [**Operation**](Operation.md) |  | 
**operation_result** | [**OperationResult**](OperationResult.md) |  | 
**message** | **str** | Additional message | [optional] 
**operation_data** | **object** | Structured data dependent on resource and its operation | [optional] 
**additional_data** | **Dict[str, object]** | Additional data specific to event logged | [optional] 

## Example

```python
from openapi_client.models.audit_log_dto import AuditLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogDto from a JSON string
audit_log_dto_instance = AuditLogDto.from_json(json)
# print the JSON string representation of the object
print(AuditLogDto.to_json())

# convert the object into a dict
audit_log_dto_dict = audit_log_dto_instance.to_dict()
# create an instance of AuditLogDto from a dict
audit_log_dto_from_dict = AuditLogDto.from_dict(audit_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


