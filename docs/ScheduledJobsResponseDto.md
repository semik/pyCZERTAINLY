# ScheduledJobsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 
**scheduled_jobs** | [**List[ScheduledJobDto]**](ScheduledJobDto.md) | Scheduled jobs | 

## Example

```python
from openapi_client.models.scheduled_jobs_response_dto import ScheduledJobsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJobsResponseDto from a JSON string
scheduled_jobs_response_dto_instance = ScheduledJobsResponseDto.from_json(json)
# print the JSON string representation of the object
print(ScheduledJobsResponseDto.to_json())

# convert the object into a dict
scheduled_jobs_response_dto_dict = scheduled_jobs_response_dto_instance.to_dict()
# create an instance of ScheduledJobsResponseDto from a dict
scheduled_jobs_response_dto_from_dict = ScheduledJobsResponseDto.from_dict(scheduled_jobs_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


