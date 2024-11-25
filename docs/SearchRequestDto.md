# SearchRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[SearchFilterRequestDto]**](SearchFilterRequestDto.md) | Certificate filter input | [optional] 
**items_per_page** | **int** | Number of entries per page | [optional] [default to 10]
**page_number** | **int** | Page number for the request | [optional] [default to 1]

## Example

```python
from openapi_client.models.search_request_dto import SearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestDto from a JSON string
search_request_dto_instance = SearchRequestDto.from_json(json)
# print the JSON string representation of the object
print(SearchRequestDto.to_json())

# convert the object into a dict
search_request_dto_dict = search_request_dto_instance.to_dict()
# create an instance of SearchRequestDto from a dict
search_request_dto_from_dict = SearchRequestDto.from_dict(search_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


