# TokenInstanceStatusDetailDto

Status Of the Token Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TokenInstanceStatus**](TokenInstanceStatus.md) |  | 
**components** | [**Dict[str, TokenInstanceStatusComponent]**](TokenInstanceStatusComponent.md) | Components of the Token instance status | [optional] 

## Example

```python
from openapi_client.models.token_instance_status_detail_dto import TokenInstanceStatusDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInstanceStatusDetailDto from a JSON string
token_instance_status_detail_dto_instance = TokenInstanceStatusDetailDto.from_json(json)
# print the JSON string representation of the object
print(TokenInstanceStatusDetailDto.to_json())

# convert the object into a dict
token_instance_status_detail_dto_dict = token_instance_status_detail_dto_instance.to_dict()
# create an instance of TokenInstanceStatusDetailDto from a dict
token_instance_status_detail_dto_from_dict = TokenInstanceStatusDetailDto.from_dict(token_instance_status_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


