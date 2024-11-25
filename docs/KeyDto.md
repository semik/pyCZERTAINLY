# KeyDto

Key Pair of the certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Key | 
**creation_time** | **datetime** | Creation time of the Key. If the key is discovered from the connector, then it will be returned | 
**token_profile_uuid** | **str** | UUID of the Token Profile | [optional] 
**token_profile_name** | **str** | Name of the Token Profile | [optional] 
**token_instance_uuid** | **str** | Token Instance UUID | 
**token_instance_name** | **str** | Token Instance Name | 
**owner** | **str** | Owner of the Key | [optional] 
**owner_uuid** | **str** | UUID of the owner of the Key | [optional] 
**groups** | [**List[GroupDto]**](GroupDto.md) | Groups associated to the key | [optional] 
**items** | [**List[KeyItemDto]**](KeyItemDto.md) | Key Items | 
**associations** | **int** | Number of associated objects | [optional] 

## Example

```python
from pyCZERTAINLY.models.key_dto import KeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyDto from a JSON string
key_dto_instance = KeyDto.from_json(json)
# print the JSON string representation of the object
print(KeyDto.to_json())

# convert the object into a dict
key_dto_dict = key_dto_instance.to_dict()
# create an instance of KeyDto from a dict
key_dto_from_dict = KeyDto.from_dict(key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


