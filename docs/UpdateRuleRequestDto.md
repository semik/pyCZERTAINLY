# UpdateRuleRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Rule | [optional] 
**conditions_uuids** | **List[str]** | List of UUIDs of existing conditions to add to the rule | 

## Example

```python
from pyCZERTAINLY.models.update_rule_request_dto import UpdateRuleRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleRequestDto from a JSON string
update_rule_request_dto_instance = UpdateRuleRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateRuleRequestDto.to_json())

# convert the object into a dict
update_rule_request_dto_dict = update_rule_request_dto_instance.to_dict()
# create an instance of UpdateRuleRequestDto from a dict
update_rule_request_dto_from_dict = UpdateRuleRequestDto.from_dict(update_rule_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


