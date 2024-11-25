# ResourceRecord

Affiliated resource that is related to subject resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Resource**](Resource.md) |  | 
**uuids** | **List[str]** |  | [optional] 
**names** | **List[str]** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.resource_record import ResourceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRecord from a JSON string
resource_record_instance = ResourceRecord.from_json(json)
# print the JSON string representation of the object
print(ResourceRecord.to_json())

# convert the object into a dict
resource_record_dict = resource_record_instance.to_dict()
# create an instance of ResourceRecord from a dict
resource_record_from_dict = ResourceRecord.from_dict(resource_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


