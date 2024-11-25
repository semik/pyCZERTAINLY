# ActorRecord

Actor of log record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ActorType**](ActorType.md) |  | 
**auth_method** | [**AuthMethod**](AuthMethod.md) |  | 
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.actor_record import ActorRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ActorRecord from a JSON string
actor_record_instance = ActorRecord.from_json(json)
# print the JSON string representation of the object
print(ActorRecord.to_json())

# convert the object into a dict
actor_record_dict = actor_record_instance.to_dict()
# create an instance of ActorRecord from a dict
actor_record_from_dict = ActorRecord.from_dict(actor_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


