# NotificationDto

Notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Notification UUID | 
**message** | **str** | Notification message | 
**detail** | **str** | Notification message detail | [optional] 
**read_at** | **datetime** | Notification read date | [optional] 
**sent_at** | **datetime** | Notification sent date | 
**target_object_type** | [**Resource**](Resource.md) |  | [optional] 
**target_object_identification** | **List[str]** | Target object identification (UUID) | [optional] 

## Example

```python
from pyCZERTAINLY.models.notification_dto import NotificationDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDto from a JSON string
notification_dto_instance = NotificationDto.from_json(json)
# print the JSON string representation of the object
print(NotificationDto.to_json())

# convert the object into a dict
notification_dto_dict = notification_dto_instance.to_dict()
# create an instance of NotificationDto from a dict
notification_dto_from_dict = NotificationDto.from_dict(notification_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


