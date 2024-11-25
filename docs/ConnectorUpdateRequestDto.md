# ConnectorUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the Connector to connect | [optional] 
**auth_type** | [**AuthType**](AuthType.md) |  | [optional] 
**auth_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of authentication Attributes. Required if the authentication type is not NONE | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.connector_update_request_dto import ConnectorUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorUpdateRequestDto from a JSON string
connector_update_request_dto_instance = ConnectorUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConnectorUpdateRequestDto.to_json())

# convert the object into a dict
connector_update_request_dto_dict = connector_update_request_dto_instance.to_dict()
# create an instance of ConnectorUpdateRequestDto from a dict
connector_update_request_dto_from_dict = ConnectorUpdateRequestDto.from_dict(connector_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


