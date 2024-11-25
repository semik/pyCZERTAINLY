# DateTimeAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **datetime** | DateTime attribute value in format yyyy-MM-ddTHH:mm:ss.SSSXXX | 

## Example

```python
from openapi_client.models.date_time_attribute_content import DateTimeAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of DateTimeAttributeContent from a JSON string
date_time_attribute_content_instance = DateTimeAttributeContent.from_json(json)
# print the JSON string representation of the object
print(DateTimeAttributeContent.to_json())

# convert the object into a dict
date_time_attribute_content_dict = date_time_attribute_content_instance.to_dict()
# create an instance of DateTimeAttributeContent from a dict
date_time_attribute_content_from_dict = DateTimeAttributeContent.from_dict(date_time_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


