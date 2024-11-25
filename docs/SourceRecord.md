# SourceRecord

Source of log record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**path** | **str** |  | 
**content_type** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.source_record import SourceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRecord from a JSON string
source_record_instance = SourceRecord.from_json(json)
# print the JSON string representation of the object
print(SourceRecord.to_json())

# convert the object into a dict
source_record_dict = source_record_instance.to_dict()
# create an instance of SourceRecord from a dict
source_record_from_dict = SourceRecord.from_dict(source_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


