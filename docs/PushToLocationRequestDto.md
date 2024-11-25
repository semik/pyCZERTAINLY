# PushToLocationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of push Attributes for Location | 

## Example

```python
from pyCZERTAINLY.models.push_to_location_request_dto import PushToLocationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PushToLocationRequestDto from a JSON string
push_to_location_request_dto_instance = PushToLocationRequestDto.from_json(json)
# print the JSON string representation of the object
print(PushToLocationRequestDto.to_json())

# convert the object into a dict
push_to_location_request_dto_dict = push_to_location_request_dto_instance.to_dict()
# create an instance of PushToLocationRequestDto from a dict
push_to_location_request_dto_from_dict = PushToLocationRequestDto.from_dict(push_to_location_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


