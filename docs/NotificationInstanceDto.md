# NotificationInstanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Notification instance description | [optional] 
**connector_uuid** | **str** | UUID of Notification provider | 
**connector_name** | **str** | Name of Notification provider | 
**kind** | **str** | Notification Instance Kind | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Notification instance Attributes | 
**attribute_mappings** | [**List[AttributeMappingDto]**](AttributeMappingDto.md) | List of attribute mappings between mapping attributes and (recipient) custom attributes | [optional] 

## Example

```python
from openapi_client.models.notification_instance_dto import NotificationInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInstanceDto from a JSON string
notification_instance_dto_instance = NotificationInstanceDto.from_json(json)
# print the JSON string representation of the object
print(NotificationInstanceDto.to_json())

# convert the object into a dict
notification_instance_dto_dict = notification_instance_dto_instance.to_dict()
# create an instance of NotificationInstanceDto from a dict
notification_instance_dto_from_dict = NotificationInstanceDto.from_dict(notification_instance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


