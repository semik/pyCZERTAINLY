# UpdateScheduledJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** | Cron expression for job schedule | [optional] 

## Example

```python
from openapi_client.models.update_scheduled_job import UpdateScheduledJob

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduledJob from a JSON string
update_scheduled_job_instance = UpdateScheduledJob.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduledJob.to_json())

# convert the object into a dict
update_scheduled_job_dict = update_scheduled_job_instance.to_dict()
# create an instance of UpdateScheduledJob from a dict
update_scheduled_job_from_dict = UpdateScheduledJob.from_dict(update_scheduled_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


