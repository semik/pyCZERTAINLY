# ErrorMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message detail | 

## Example

```python
from openapi_client.models.error_message_dto import ErrorMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessageDto from a JSON string
error_message_dto_instance = ErrorMessageDto.from_json(json)
# print the JSON string representation of the object
print(ErrorMessageDto.to_json())

# convert the object into a dict
error_message_dto_dict = error_message_dto_instance.to_dict()
# create an instance of ErrorMessageDto from a dict
error_message_dto_from_dict = ErrorMessageDto.from_dict(error_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


