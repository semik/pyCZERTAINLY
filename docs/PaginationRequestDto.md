# PaginationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | [optional] [default to 10]
**page_number** | **int** | Page number for the request | [optional] [default to 1]

## Example

```python
from openapi_client.models.pagination_request_dto import PaginationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationRequestDto from a JSON string
pagination_request_dto_instance = PaginationRequestDto.from_json(json)
# print the JSON string representation of the object
print(PaginationRequestDto.to_json())

# convert the object into a dict
pagination_request_dto_dict = pagination_request_dto_instance.to_dict()
# create an instance of PaginationRequestDto from a dict
pagination_request_dto_from_dict = PaginationRequestDto.from_dict(pagination_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


