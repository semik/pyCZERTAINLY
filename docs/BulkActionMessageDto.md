# BulkActionMessageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**message** | **str** | Message describing the associations of the Objects which is preventing the bulk operation | 

## Example

```python
from pyCZERTAINLY.models.bulk_action_message_dto import BulkActionMessageDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkActionMessageDto from a JSON string
bulk_action_message_dto_instance = BulkActionMessageDto.from_json(json)
# print the JSON string representation of the object
print(BulkActionMessageDto.to_json())

# convert the object into a dict
bulk_action_message_dto_dict = bulk_action_message_dto_instance.to_dict()
# create an instance of BulkActionMessageDto from a dict
bulk_action_message_dto_from_dict = BulkActionMessageDto.from_dict(bulk_action_message_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


