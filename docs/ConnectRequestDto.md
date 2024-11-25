# ConnectRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the Connector to connect | 
**uuid** | **str** | UUID of the Connector. Mandatory if connection is needed for the same Connector | [optional] 
**auth_type** | [**AuthType**](AuthType.md) |  | 
**auth_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of authentication Attributes. Required if the authentication type is not NONE | [optional] 

## Example

```python
from openapi_client.models.connect_request_dto import ConnectRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectRequestDto from a JSON string
connect_request_dto_instance = ConnectRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConnectRequestDto.to_json())

# convert the object into a dict
connect_request_dto_dict = connect_request_dto_instance.to_dict()
# create an instance of ConnectRequestDto from a dict
connect_request_dto_from_dict = ConnectRequestDto.from_dict(connect_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


