# RangeAttributeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the constraint | [optional] 
**error_message** | **str** | Error message to be displayed for wrong data | [optional] 
**type** | [**AttributeConstraintType**](AttributeConstraintType.md) |  | 
**data** | [**RangeAttributeConstraintData**](RangeAttributeConstraintData.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.range_attribute_constraint import RangeAttributeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of RangeAttributeConstraint from a JSON string
range_attribute_constraint_instance = RangeAttributeConstraint.from_json(json)
# print the JSON string representation of the object
print(RangeAttributeConstraint.to_json())

# convert the object into a dict
range_attribute_constraint_dict = range_attribute_constraint_instance.to_dict()
# create an instance of RangeAttributeConstraint from a dict
range_attribute_constraint_from_dict = RangeAttributeConstraint.from_dict(range_attribute_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


