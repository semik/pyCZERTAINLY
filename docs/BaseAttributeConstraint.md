# BaseAttributeConstraint

Optional regular expressions and constraints used for validating the Attribute content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the constraint | [optional] 
**error_message** | **str** | Error message to be displayed for wrong data | [optional] 
**type** | [**AttributeConstraintType**](AttributeConstraintType.md) |  | 
**data** | **object** | Attribute Constraint Data | 

## Example

```python
from openapi_client.models.base_attribute_constraint import BaseAttributeConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAttributeConstraint from a JSON string
base_attribute_constraint_instance = BaseAttributeConstraint.from_json(json)
# print the JSON string representation of the object
print(BaseAttributeConstraint.to_json())

# convert the object into a dict
base_attribute_constraint_dict = base_attribute_constraint_instance.to_dict()
# create an instance of BaseAttributeConstraint from a dict
base_attribute_constraint_from_dict = BaseAttributeConstraint.from_dict(base_attribute_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


