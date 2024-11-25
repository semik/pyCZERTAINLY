# DateAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **date** | Date attribute value in format yyyy-MM-dd | 

## Example

```python
from pyCZERTAINLY.models.date_attribute_content import DateAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of DateAttributeContent from a JSON string
date_attribute_content_instance = DateAttributeContent.from_json(json)
# print the JSON string representation of the object
print(DateAttributeContent.to_json())

# convert the object into a dict
date_attribute_content_dict = date_attribute_content_instance.to_dict()
# create an instance of DateAttributeContent from a dict
date_attribute_content_from_dict = DateAttributeContent.from_dict(date_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


