# RandomDataRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Number of random bytes to generate | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Random generator Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.random_data_request_dto import RandomDataRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RandomDataRequestDto from a JSON string
random_data_request_dto_instance = RandomDataRequestDto.from_json(json)
# print the JSON string representation of the object
print(RandomDataRequestDto.to_json())

# convert the object into a dict
random_data_request_dto_dict = random_data_request_dto_instance.to_dict()
# create an instance of RandomDataRequestDto from a dict
random_data_request_dto_from_dict = RandomDataRequestDto.from_dict(random_data_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


