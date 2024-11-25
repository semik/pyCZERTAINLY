# UuidDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 

## Example

```python
from pyCZERTAINLY.models.uuid_dto import UuidDto

# TODO update the JSON string below
json = "{}"
# create an instance of UuidDto from a JSON string
uuid_dto_instance = UuidDto.from_json(json)
# print the JSON string representation of the object
print(UuidDto.to_json())

# convert the object into a dict
uuid_dto_dict = uuid_dto_instance.to_dict()
# create an instance of UuidDto from a dict
uuid_dto_from_dict = UuidDto.from_dict(uuid_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


