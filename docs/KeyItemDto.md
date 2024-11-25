# KeyItemDto

Cryptographic Keys

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Key | 
**creation_time** | **datetime** | Creation time of the Key. If the key is discovered from the connector, then it will be returned | 
**key_wrapper_uuid** | **str** | UUID of the wrapper object | 
**token_profile_uuid** | **str** | UUID of the Token Profile | [optional] 
**token_profile_name** | **str** | Name of the Token Profile | [optional] 
**token_instance_uuid** | **str** | Token Instance UUID | 
**token_instance_name** | **str** | Token Instance Name | 
**owner** | **str** | Owner of the Key | [optional] 
**owner_uuid** | **str** | UUID of the owner of the Key | [optional] 
**groups** | [**List[GroupDto]**](GroupDto.md) | Groups associated to the Key | [optional] 
**associations** | **int** | Number of associated objects | [optional] 
**key_reference_uuid** | **str** | UUID of the key item in the Connector | 
**type** | [**KeyType**](KeyType.md) |  | 
**key_algorithm** | [**KeyAlgorithm**](KeyAlgorithm.md) |  | 
**format** | [**KeyFormat**](KeyFormat.md) |  | [optional] 
**length** | **int** | Key Length | [optional] 
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Key Usages | 
**enabled** | **bool** | Boolean describing if the key is enabled or not | 
**state** | [**KeyState**](KeyState.md) |  | 

## Example

```python
from pyCZERTAINLY.models.key_item_dto import KeyItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyItemDto from a JSON string
key_item_dto_instance = KeyItemDto.from_json(json)
# print the JSON string representation of the object
print(KeyItemDto.to_json())

# convert the object into a dict
key_item_dto_dict = key_item_dto_instance.to_dict()
# create an instance of KeyItemDto from a dict
key_item_dto_from_dict = KeyItemDto.from_dict(key_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


