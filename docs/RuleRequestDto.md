# RuleRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the rule | 
**description** | **str** | Description of the rule | [optional] 
**resource** | [**Resource**](Resource.md) |  | 
**conditions_uuids** | **List[str]** | List of UUIDs of existing conditions to add to the rule | 

## Example

```python
from openapi_client.models.rule_request_dto import RuleRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RuleRequestDto from a JSON string
rule_request_dto_instance = RuleRequestDto.from_json(json)
# print the JSON string representation of the object
print(RuleRequestDto.to_json())

# convert the object into a dict
rule_request_dto_dict = rule_request_dto_instance.to_dict()
# create an instance of RuleRequestDto from a dict
rule_request_dto_from_dict = RuleRequestDto.from_dict(rule_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


