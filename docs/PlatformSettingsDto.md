# PlatformSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utils** | [**UtilsSettingsDto**](UtilsSettingsDto.md) |  | 

## Example

```python
from openapi_client.models.platform_settings_dto import PlatformSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformSettingsDto from a JSON string
platform_settings_dto_instance = PlatformSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PlatformSettingsDto.to_json())

# convert the object into a dict
platform_settings_dto_dict = platform_settings_dto_instance.to_dict()
# create an instance of PlatformSettingsDto from a dict
platform_settings_dto_from_dict = PlatformSettingsDto.from_dict(platform_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


