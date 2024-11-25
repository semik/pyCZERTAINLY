# TokenInstanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**status** | [**TokenInstanceStatus**](TokenInstanceStatus.md) |  | 
**token_profiles** | **int** | Number of Token Profiles associated | 
**connector_name** | **str** | Connector Name | [optional] 
**connector_uuid** | **str** | Connector UUID | [optional] 
**kind** | **str** | Connector Kind | [optional] 

## Example

```python
from pyCZERTAINLY.models.token_instance_dto import TokenInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInstanceDto from a JSON string
token_instance_dto_instance = TokenInstanceDto.from_json(json)
# print the JSON string representation of the object
print(TokenInstanceDto.to_json())

# convert the object into a dict
token_instance_dto_dict = token_instance_dto_instance.to_dict()
# create an instance of TokenInstanceDto from a dict
token_instance_dto_from_dict = TokenInstanceDto.from_dict(token_instance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


