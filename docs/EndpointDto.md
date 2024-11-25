# EndpointDto

List of end points related to functional group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**context** | **str** | Context of the Endpoint | 
**method** | **str** | Method to be used for the Endpoint | 
**required** | **bool** | True if the Endpoint is required for implementation | 

## Example

```python
from pyCZERTAINLY.models.endpoint_dto import EndpointDto

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDto from a JSON string
endpoint_dto_instance = EndpointDto.from_json(json)
# print the JSON string representation of the object
print(EndpointDto.to_json())

# convert the object into a dict
endpoint_dto_dict = endpoint_dto_instance.to_dict()
# create an instance of EndpointDto from a dict
endpoint_dto_from_dict = EndpointDto.from_dict(endpoint_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


