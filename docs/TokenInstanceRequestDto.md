# TokenInstanceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Token Instance | 
**description** | **str** | Token Instance description | [optional] 
**connector_uuid** | **str** | UUID of the Connector | 
**kind** | **str** | Connector Kind | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Custom Attributes | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Attributes for Token Instance | 

## Example

```python
from pyCZERTAINLY.models.token_instance_request_dto import TokenInstanceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInstanceRequestDto from a JSON string
token_instance_request_dto_instance = TokenInstanceRequestDto.from_json(json)
# print the JSON string representation of the object
print(TokenInstanceRequestDto.to_json())

# convert the object into a dict
token_instance_request_dto_dict = token_instance_request_dto_instance.to_dict()
# create an instance of TokenInstanceRequestDto from a dict
token_instance_request_dto_from_dict = TokenInstanceRequestDto.from_dict(token_instance_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


