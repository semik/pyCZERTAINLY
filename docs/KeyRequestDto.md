# KeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Cryptographic Key | 
**description** | **str** | Description of the Cryptographic Key | 
**group_uuids** | **List[str]** | UUIDs of the groups to associate with key | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to create a Key | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Custom Attributes for the key | [optional] 
**enabled** | **bool** | Enabled status of created key. True &#x3D; Enabled, False &#x3D; Disabled | [optional] [default to False]

## Example

```python
from pyCZERTAINLY.models.key_request_dto import KeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRequestDto from a JSON string
key_request_dto_instance = KeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(KeyRequestDto.to_json())

# convert the object into a dict
key_request_dto_dict = key_request_dto_instance.to_dict()
# create an instance of KeyRequestDto from a dict
key_request_dto_from_dict = KeyRequestDto.from_dict(key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


