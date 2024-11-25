# RequestAttributeCallback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | [optional] 
**name** | **str** | Name of the Attribute | 
**path_variable** | **Dict[str, object]** | Map of path variables supported by the callback method | [optional] 
**request_parameter** | **Dict[str, object]** | Map of the query parameters supported by the callback method | [optional] 
**body** | **Dict[str, object]** | Request body for the callback method | [optional] 

## Example

```python
from pyCZERTAINLY.models.request_attribute_callback import RequestAttributeCallback

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAttributeCallback from a JSON string
request_attribute_callback_instance = RequestAttributeCallback.from_json(json)
# print the JSON string representation of the object
print(RequestAttributeCallback.to_json())

# convert the object into a dict
request_attribute_callback_dict = request_attribute_callback_instance.to_dict()
# create an instance of RequestAttributeCallback from a dict
request_attribute_callback_from_dict = RequestAttributeCallback.from_dict(request_attribute_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


