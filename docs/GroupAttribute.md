# GroupAttribute

Group attribute and its content represents dynamic list of additional attributes retrieved by callback. Its content can not be edited and is not send in requests to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute for unique identification | 
**name** | **str** | Name of the Attribute that is used for identification | 
**description** | **str** | Optional description of the Attribute, should contain helper text on what is expected | [optional] 
**content** | [**List[BaseAttributeDto]**](BaseAttributeDto.md) | List of all different types of attributes | [optional] 
**type** | [**AttributeType**](AttributeType.md) |  | 
**attribute_callback** | [**AttributeCallback**](AttributeCallback.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_attribute import GroupAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAttribute from a JSON string
group_attribute_instance = GroupAttribute.from_json(json)
# print the JSON string representation of the object
print(GroupAttribute.to_json())

# convert the object into a dict
group_attribute_dict = group_attribute_instance.to_dict()
# create an instance of GroupAttribute from a dict
group_attribute_from_dict = GroupAttribute.from_dict(group_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


