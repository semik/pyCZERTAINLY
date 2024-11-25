# AttributeCallback

Optional definition of callback for getting the content of the Attribute based on the action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_context** | **str** | Context part of callback URL | 
**callback_method** | **str** | HTTP method of the callback | 
**mappings** | [**List[AttributeCallbackMapping]**](AttributeCallbackMapping.md) | Mappings for the callback method | 

## Example

```python
from pyCZERTAINLY.models.attribute_callback import AttributeCallback

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeCallback from a JSON string
attribute_callback_instance = AttributeCallback.from_json(json)
# print the JSON string representation of the object
print(AttributeCallback.to_json())

# convert the object into a dict
attribute_callback_dict = attribute_callback_instance.to_dict()
# create an instance of AttributeCallback from a dict
attribute_callback_from_dict = AttributeCallback.from_dict(attribute_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


