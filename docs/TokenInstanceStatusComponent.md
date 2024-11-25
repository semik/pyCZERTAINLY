# TokenInstanceStatusComponent

Components of the Token instance status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TokenInstanceStatus**](TokenInstanceStatus.md) |  | 
**details** | **Dict[str, object]** | Token instance component details | [optional] 

## Example

```python
from pyCZERTAINLY.models.token_instance_status_component import TokenInstanceStatusComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInstanceStatusComponent from a JSON string
token_instance_status_component_instance = TokenInstanceStatusComponent.from_json(json)
# print the JSON string representation of the object
print(TokenInstanceStatusComponent.to_json())

# convert the object into a dict
token_instance_status_component_dict = token_instance_status_component_instance.to_dict()
# create an instance of TokenInstanceStatusComponent from a dict
token_instance_status_component_from_dict = TokenInstanceStatusComponent.from_dict(token_instance_status_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


