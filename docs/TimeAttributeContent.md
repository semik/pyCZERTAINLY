# TimeAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **str** | Time attribute value in format HH:mm:ss | 

## Example

```python
from openapi_client.models.time_attribute_content import TimeAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAttributeContent from a JSON string
time_attribute_content_instance = TimeAttributeContent.from_json(json)
# print the JSON string representation of the object
print(TimeAttributeContent.to_json())

# convert the object into a dict
time_attribute_content_dict = time_attribute_content_instance.to_dict()
# create an instance of TimeAttributeContent from a dict
time_attribute_content_from_dict = TimeAttributeContent.from_dict(time_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


