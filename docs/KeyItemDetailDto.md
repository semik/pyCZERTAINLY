# KeyItemDetailDto

Key Objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**key_reference_uuid** | **str** | UUID of the key item in the Connector | 
**type** | [**KeyType**](KeyType.md) |  | 
**key_algorithm** | [**KeyAlgorithm**](KeyAlgorithm.md) |  | 
**format** | [**KeyFormat**](KeyFormat.md) |  | [optional] 
**key_data** | **str** | Key Data | [optional] 
**length** | **int** | Key Length | [optional] 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Metadata for the key | [optional] 
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Key Usages | 
**enabled** | **bool** | Boolean describing if the key is enabled or not | 
**state** | [**KeyState**](KeyState.md) |  | 
**reason** | [**KeyCompromiseReason**](KeyCompromiseReason.md) |  | [optional] 

## Example

```python
from openapi_client.models.key_item_detail_dto import KeyItemDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyItemDetailDto from a JSON string
key_item_detail_dto_instance = KeyItemDetailDto.from_json(json)
# print the JSON string representation of the object
print(KeyItemDetailDto.to_json())

# convert the object into a dict
key_item_detail_dto_dict = key_item_detail_dto_instance.to_dict()
# create an instance of KeyItemDetailDto from a dict
key_item_detail_dto_from_dict = KeyItemDetailDto.from_dict(key_item_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


