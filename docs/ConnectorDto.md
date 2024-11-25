# ConnectorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**function_groups** | [**List[FunctionGroupDto]**](FunctionGroupDto.md) | List of Function Groups implemented by the Connector | 
**url** | **str** | URL of the Connector | 
**auth_type** | [**AuthType**](AuthType.md) |  | 
**auth_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes for the authentication type | [optional] 
**status** | [**ConnectorStatus**](ConnectorStatus.md) |  | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.connector_dto import ConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorDto from a JSON string
connector_dto_instance = ConnectorDto.from_json(json)
# print the JSON string representation of the object
print(ConnectorDto.to_json())

# convert the object into a dict
connector_dto_dict = connector_dto_instance.to_dict()
# create an instance of ConnectorDto from a dict
connector_dto_from_dict = ConnectorDto.from_dict(connector_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


