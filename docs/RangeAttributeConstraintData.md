# RangeAttributeConstraintData

Integer Range Attribute Constraint Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Start of the range for validation | [optional] 
**to** | **int** | End of the range for validation | [optional] 

## Example

```python
from pyCZERTAINLY.models.range_attribute_constraint_data import RangeAttributeConstraintData

# TODO update the JSON string below
json = "{}"
# create an instance of RangeAttributeConstraintData from a JSON string
range_attribute_constraint_data_instance = RangeAttributeConstraintData.from_json(json)
# print the JSON string representation of the object
print(RangeAttributeConstraintData.to_json())

# convert the object into a dict
range_attribute_constraint_data_dict = range_attribute_constraint_data_instance.to_dict()
# create an instance of RangeAttributeConstraintData from a dict
range_attribute_constraint_data_from_dict = RangeAttributeConstraintData.from_dict(range_attribute_constraint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


