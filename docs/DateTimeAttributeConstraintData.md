# DateTimeAttributeConstraintData

DateTime Range Attribute Constraint Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | Start of the datetime for validation | [optional] 
**to** | **datetime** | End of the datetime for validation | [optional] 

## Example

```python
from openapi_client.models.date_time_attribute_constraint_data import DateTimeAttributeConstraintData

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeAttributeConstraintData from a JSON string
date_time_attribute_constraint_data_instance = DateTimeAttributeConstraintData.from_json(json)
# print the JSON string representation of the object
print(DateTimeAttributeConstraintData.to_json())

# convert the object into a dict
date_time_attribute_constraint_data_dict = date_time_attribute_constraint_data_instance.to_dict()
# create an instance of DateTimeAttributeConstraintData from a dict
date_time_attribute_constraint_data_from_dict = DateTimeAttributeConstraintData.from_dict(date_time_attribute_constraint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


