# NotificationResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 
**items** | [**List[NotificationDto]**](NotificationDto.md) | Notifications | 

## Example

```python
from openapi_client.models.notification_response_dto import NotificationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationResponseDto from a JSON string
notification_response_dto_instance = NotificationResponseDto.from_json(json)
# print the JSON string representation of the object
print(NotificationResponseDto.to_json())

# convert the object into a dict
notification_response_dto_dict = notification_response_dto_instance.to_dict()
# create an instance of NotificationResponseDto from a dict
notification_response_dto_from_dict = NotificationResponseDto.from_dict(notification_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


