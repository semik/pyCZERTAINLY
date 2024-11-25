# NotificationSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications_mapping** | **Dict[str, str]** | Type settings of the notification | 

## Example

```python
from openapi_client.models.notification_settings_dto import NotificationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettingsDto from a JSON string
notification_settings_dto_instance = NotificationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(NotificationSettingsDto.to_json())

# convert the object into a dict
notification_settings_dto_dict = notification_settings_dto_instance.to_dict()
# create an instance of NotificationSettingsDto from a dict
notification_settings_dto_from_dict = NotificationSettingsDto.from_dict(notification_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


