# NotificationInstanceUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Notification instance description | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Notification instance Attributes | 
**attribute_mappings** | [**List[AttributeMappingDto]**](AttributeMappingDto.md) | List of attribute mappings between mapping attributes and (recipient) custom attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.notification_instance_update_request_dto import NotificationInstanceUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInstanceUpdateRequestDto from a JSON string
notification_instance_update_request_dto_instance = NotificationInstanceUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(NotificationInstanceUpdateRequestDto.to_json())

# convert the object into a dict
notification_instance_update_request_dto_dict = notification_instance_update_request_dto_instance.to_dict()
# create an instance of NotificationInstanceUpdateRequestDto from a dict
notification_instance_update_request_dto_from_dict = NotificationInstanceUpdateRequestDto.from_dict(notification_instance_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


