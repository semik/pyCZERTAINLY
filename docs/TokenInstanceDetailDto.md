# TokenInstanceDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**connector_name** | **str** | Connector Name | [optional] 
**connector_uuid** | **str** | Connector UUID | [optional] 
**kind** | **str** | Connector Kind | [optional] 
**status** | [**TokenInstanceStatusDetailDto**](TokenInstanceStatusDetailDto.md) |  | 
**token_profiles** | **int** | Number of Token Profiles associated | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Token instance Attributes | 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Token instance Metadata | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Custom Attributes for the Token Instance | [optional] 

## Example

```python
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInstanceDetailDto from a JSON string
token_instance_detail_dto_instance = TokenInstanceDetailDto.from_json(json)
# print the JSON string representation of the object
print(TokenInstanceDetailDto.to_json())

# convert the object into a dict
token_instance_detail_dto_dict = token_instance_detail_dto_instance.to_dict()
# create an instance of TokenInstanceDetailDto from a dict
token_instance_detail_dto_from_dict = TokenInstanceDetailDto.from_dict(token_instance_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


