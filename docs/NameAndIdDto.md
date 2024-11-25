# NameAndIdDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Object identifier | 
**name** | **str** | Object name | 

## Example

```python
from pyCZERTAINLY.models.name_and_id_dto import NameAndIdDto

# TODO update the JSON string below
json = "{}"
# create an instance of NameAndIdDto from a JSON string
name_and_id_dto_instance = NameAndIdDto.from_json(json)
# print the JSON string representation of the object
print(NameAndIdDto.to_json())

# convert the object into a dict
name_and_id_dto_dict = name_and_id_dto_instance.to_dict()
# create an instance of NameAndIdDto from a dict
name_and_id_dto_from_dict = NameAndIdDto.from_dict(name_and_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


