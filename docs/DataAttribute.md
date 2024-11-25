# DataAttribute

Data attribute allows to store and transfer dynamic data. Its content can be edited and send in requests to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute for unique identification | 
**name** | **str** | Name of the Attribute that is used for identification | 
**description** | **str** | Optional description of the Attribute, should contain helper text on what is expected | [optional] 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**properties** | [**DataAttributeProperties**](DataAttributeProperties.md) |  | 
**constraints** | [**List[BaseAttributeConstraint]**](BaseAttributeConstraint.md) | Optional regular expressions and constraints used for validating the Attribute content | [optional] 
**attribute_callback** | [**AttributeCallback**](AttributeCallback.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.data_attribute import DataAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of DataAttribute from a JSON string
data_attribute_instance = DataAttribute.from_json(json)
# print the JSON string representation of the object
print(DataAttribute.to_json())

# convert the object into a dict
data_attribute_dict = data_attribute_instance.to_dict()
# create an instance of DataAttribute from a dict
data_attribute_from_dict = DataAttribute.from_dict(data_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


