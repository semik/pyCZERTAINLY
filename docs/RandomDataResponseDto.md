# RandomDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Base64 encoded random data | 

## Example

```python
from pyCZERTAINLY.models.random_data_response_dto import RandomDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RandomDataResponseDto from a JSON string
random_data_response_dto_instance = RandomDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(RandomDataResponseDto.to_json())

# convert the object into a dict
random_data_response_dto_dict = random_data_response_dto_instance.to_dict()
# create an instance of RandomDataResponseDto from a dict
random_data_response_dto_from_dict = RandomDataResponseDto.from_dict(random_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


