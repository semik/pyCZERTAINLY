# ConnectorRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Connector | 
**url** | **str** | URL of the Connector to connect | 
**auth_type** | [**AuthType**](AuthType.md) |  | 
**auth_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of authentication Attributes. Required if the authentication type is not NONE | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.connector_request_dto import ConnectorRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorRequestDto from a JSON string
connector_request_dto_instance = ConnectorRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConnectorRequestDto.to_json())

# convert the object into a dict
connector_request_dto_dict = connector_request_dto_instance.to_dict()
# create an instance of ConnectorRequestDto from a dict
connector_request_dto_from_dict = ConnectorRequestDto.from_dict(connector_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


