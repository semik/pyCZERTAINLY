# RegexpAttributeConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the constraint | [optional] 
**error_message** | **str** | Error message to be displayed for wrong data | [optional] 
**type** | [**AttributeConstraintType**](AttributeConstraintType.md) |  | 
**data** | **str** | Regular Expression Attribute Constraint Data | [optional] 

## Example

```python
from openapi_client.models.regexp_attribute_constraint import RegexpAttributeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of RegexpAttributeConstraint from a JSON string
regexp_attribute_constraint_instance = RegexpAttributeConstraint.from_json(json)
# print the JSON string representation of the object
print(RegexpAttributeConstraint.to_json())

# convert the object into a dict
regexp_attribute_constraint_dict = regexp_attribute_constraint_instance.to_dict()
# create an instance of RegexpAttributeConstraint from a dict
regexp_attribute_constraint_from_dict = RegexpAttributeConstraint.from_dict(regexp_attribute_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


