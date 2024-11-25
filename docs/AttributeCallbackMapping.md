# AttributeCallbackMapping

Mappings for the callback method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Name of the attribute whose value is to be used as value of path variable or request param or body field.It is optional and must be set only if value is not set. | [optional] 
**attribute_type** | [**AttributeType**](AttributeType.md) |  | [optional] 
**attribute_content_type** | [**AttributeContentType**](AttributeContentType.md) |  | [optional] 
**to** | **str** | Name of the path variable or request param or body field which is to be used to assign value of attribute | 
**targets** | [**List[AttributeValueTarget]**](AttributeValueTarget.md) | Set of targets for propagating value. | 
**value** | **object** | Static value to be propagated to targets. It is optional and is set only if the value is known at attribute creation time. | [optional] 

## Example

```python
from pyCZERTAINLY.models.attribute_callback_mapping import AttributeCallbackMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeCallbackMapping from a JSON string
attribute_callback_mapping_instance = AttributeCallbackMapping.from_json(json)
# print the JSON string representation of the object
print(AttributeCallbackMapping.to_json())

# convert the object into a dict
attribute_callback_mapping_dict = attribute_callback_mapping_instance.to_dict()
# create an instance of AttributeCallbackMapping from a dict
attribute_callback_mapping_from_dict = AttributeCallbackMapping.from_dict(attribute_callback_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


