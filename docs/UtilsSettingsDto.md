# UtilsSettingsDto

Utils settings of the platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utils_service_url** | **str** | URL of the Util Service | [optional] 

## Example

```python
from pyCZERTAINLY.models.utils_settings_dto import UtilsSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UtilsSettingsDto from a JSON string
utils_settings_dto_instance = UtilsSettingsDto.from_json(json)
# print the JSON string representation of the object
print(UtilsSettingsDto.to_json())

# convert the object into a dict
utils_settings_dto_dict = utils_settings_dto_instance.to_dict()
# create an instance of UtilsSettingsDto from a dict
utils_settings_dto_from_dict = UtilsSettingsDto.from_dict(utils_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


