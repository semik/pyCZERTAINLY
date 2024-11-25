# RuleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Rule | [optional] 
**resource** | [**Resource**](Resource.md) |  | 

## Example

```python
from pyCZERTAINLY.models.rule_dto import RuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDto from a JSON string
rule_dto_instance = RuleDto.from_json(json)
# print the JSON string representation of the object
print(RuleDto.to_json())

# convert the object into a dict
rule_dto_dict = rule_dto_instance.to_dict()
# create an instance of RuleDto from a dict
rule_dto_from_dict = RuleDto.from_dict(rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


