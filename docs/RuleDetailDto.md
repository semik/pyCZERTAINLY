# RuleDetailDto

List of Rules in the Rule Trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Rule | [optional] 
**resource** | [**Resource**](Resource.md) |  | 
**conditions** | [**List[ConditionDto]**](ConditionDto.md) | List of conditions in the Rule | 

## Example

```python
from pyCZERTAINLY.models.rule_detail_dto import RuleDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDetailDto from a JSON string
rule_detail_dto_instance = RuleDetailDto.from_json(json)
# print the JSON string representation of the object
print(RuleDetailDto.to_json())

# convert the object into a dict
rule_detail_dto_dict = rule_detail_dto_instance.to_dict()
# create an instance of RuleDetailDto from a dict
rule_detail_dto_from_dict = RuleDetailDto.from_dict(rule_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


