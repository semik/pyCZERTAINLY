# NotificationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | [optional] [default to 10]
**page_number** | **int** | Page number for the request | [optional] [default to 1]
**unread** | **bool** | Show only unread notifications | [optional] [default to False]

## Example

```python
from openapi_client.models.notification_request_dto import NotificationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRequestDto from a JSON string
notification_request_dto_instance = NotificationRequestDto.from_json(json)
# print the JSON string representation of the object
print(NotificationRequestDto.to_json())

# convert the object into a dict
notification_request_dto_dict = notification_request_dto_instance.to_dict()
# create an instance of NotificationRequestDto from a dict
notification_request_dto_from_dict = NotificationRequestDto.from_dict(notification_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


