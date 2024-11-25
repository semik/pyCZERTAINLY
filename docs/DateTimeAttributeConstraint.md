# DateTimeAttributeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the constraint | [optional] 
**error_message** | **str** | Error message to be displayed for wrong data | [optional] 
**type** | [**AttributeConstraintType**](AttributeConstraintType.md) |  | 
**data** | [**DateTimeAttributeConstraintData**](DateTimeAttributeConstraintData.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.date_time_attribute_constraint import DateTimeAttributeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeAttributeConstraint from a JSON string
date_time_attribute_constraint_instance = DateTimeAttributeConstraint.from_json(json)
# print the JSON string representation of the object
print(DateTimeAttributeConstraint.to_json())

# convert the object into a dict
date_time_attribute_constraint_dict = date_time_attribute_constraint_instance.to_dict()
# create an instance of DateTimeAttributeConstraint from a dict
date_time_attribute_constraint_from_dict = DateTimeAttributeConstraint.from_dict(date_time_attribute_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


