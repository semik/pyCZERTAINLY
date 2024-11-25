# AddLocationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Location name | 
**description** | **str** | Location description | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to register Location | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] [default to False]

## Example

```python
from openapi_client.models.add_location_request_dto import AddLocationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddLocationRequestDto from a JSON string
add_location_request_dto_instance = AddLocationRequestDto.from_json(json)
# print the JSON string representation of the object
print(AddLocationRequestDto.to_json())

# convert the object into a dict
add_location_request_dto_dict = add_location_request_dto_instance.to_dict()
# create an instance of AddLocationRequestDto from a dict
add_location_request_dto_from_dict = AddLocationRequestDto.from_dict(add_location_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


