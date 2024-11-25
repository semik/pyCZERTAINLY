# SearchFilterRequestDto

Certificate filter input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_source** | [**FilterFieldSource**](FilterFieldSource.md) |  | 
**field_identifier** | **str** | Field identifier of search filter. List of available fields with their identifiers can be retrieved from corresponding endpoint &#x60;GET /v1/{resource}/search&#x60;, e.g.: [**GET /v1/certificates/search**](../core-certificate/#tag/Certificate-Inventory/operation/getSearchableFieldInformation) | 
**condition** | [**FilterConditionOperator**](FilterConditionOperator.md) |  | 
**value** | **object** | Value to match | [optional] 

## Example

```python
from openapi_client.models.search_filter_request_dto import SearchFilterRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilterRequestDto from a JSON string
search_filter_request_dto_instance = SearchFilterRequestDto.from_json(json)
# print the JSON string representation of the object
print(SearchFilterRequestDto.to_json())

# convert the object into a dict
search_filter_request_dto_dict = search_filter_request_dto_instance.to_dict()
# create an instance of SearchFilterRequestDto from a dict
search_filter_request_dto_from_dict = SearchFilterRequestDto.from_dict(search_filter_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


