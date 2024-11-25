# NotificationInstanceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Notification instance description | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Notification instance Attributes | 
**attribute_mappings** | [**List[AttributeMappingDto]**](AttributeMappingDto.md) | List of attribute mappings between mapping attributes and (recipient) custom attributes | [optional] 
**name** | **str** | Notification instance name | 
**connector_uuid** | **str** | UUID of Notification provider | 
**kind** | **str** | Notification instance Kind | 

## Example

```python
from pyCZERTAINLY.models.notification_instance_request_dto import NotificationInstanceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInstanceRequestDto from a JSON string
notification_instance_request_dto_instance = NotificationInstanceRequestDto.from_json(json)
# print the JSON string representation of the object
print(NotificationInstanceRequestDto.to_json())

# convert the object into a dict
notification_instance_request_dto_dict = notification_instance_request_dto_instance.to_dict()
# create an instance of NotificationInstanceRequestDto from a dict
notification_instance_request_dto_from_dict = NotificationInstanceRequestDto.from_dict(notification_instance_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


