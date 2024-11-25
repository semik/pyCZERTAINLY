# EditLocationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Location | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes for Location | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] 

## Example

```python
from openapi_client.models.edit_location_request_dto import EditLocationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditLocationRequestDto from a JSON string
edit_location_request_dto_instance = EditLocationRequestDto.from_json(json)
# print the JSON string representation of the object
print(EditLocationRequestDto.to_json())

# convert the object into a dict
edit_location_request_dto_dict = edit_location_request_dto_instance.to_dict()
# create an instance of EditLocationRequestDto from a dict
edit_location_request_dto_from_dict = EditLocationRequestDto.from_dict(edit_location_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


