# openapi_client.ScheduledJobsManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_scheduled_job**](ScheduledJobsManagementApi.md#delete_scheduled_job) | **DELETE** /v1/scheduler/jobs/{uuid} | Delete Scheduled job
[**disable_scheduled_job**](ScheduledJobsManagementApi.md#disable_scheduled_job) | **PATCH** /v1/scheduler/jobs/{uuid}/disable | Disabling of Scheduled job
[**enable_scheduled_job**](ScheduledJobsManagementApi.md#enable_scheduled_job) | **PATCH** /v1/scheduler/jobs/{uuid}/enable | Enabling of Scheduled job
[**get_scheduled_job_detail**](ScheduledJobsManagementApi.md#get_scheduled_job_detail) | **GET** /v1/scheduler/jobs/{uuid} | Scheduled job detail
[**get_scheduled_job_history**](ScheduledJobsManagementApi.md#get_scheduled_job_history) | **GET** /v1/scheduler/jobs/{uuid}/history | Scheduled job history
[**list_scheduled_jobs**](ScheduledJobsManagementApi.md#list_scheduled_jobs) | **GET** /v1/scheduler/jobs | List of scheduled jobs
[**update_scheduled_job**](ScheduledJobsManagementApi.md#update_scheduled_job) | **PUT** /v1/scheduler/jobs/{uuid} | Edit Scheduled job


# **delete_scheduled_job**
> delete_scheduled_job(uuid)

Delete Scheduled job

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    uuid = 'uuid_example' # str | Scheduled job UUID

    try:
        # Delete Scheduled job
        api_instance.delete_scheduled_job(uuid)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->delete_scheduled_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Scheduled job UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Scheduled job deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_scheduled_job**
> disable_scheduled_job(uuid)

Disabling of Scheduled job

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    uuid = 'uuid_example' # str | Scheduled job UUID

    try:
        # Disabling of Scheduled job
        api_instance.disable_scheduled_job(uuid)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->disable_scheduled_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Scheduled job UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Scheduled job disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_scheduled_job**
> enable_scheduled_job(uuid)

Enabling of Scheduled job

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    uuid = 'uuid_example' # str | Scheduled job UUID

    try:
        # Enabling of Scheduled job
        api_instance.enable_scheduled_job(uuid)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->enable_scheduled_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Scheduled job UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Scheduled job enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_job_detail**
> ScheduledJobDetailDto get_scheduled_job_detail(uuid)

Scheduled job detail

### Example


```python
import openapi_client
from openapi_client.models.scheduled_job_detail_dto import ScheduledJobDetailDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    uuid = 'uuid_example' # str | Scheduled job UUID

    try:
        # Scheduled job detail
        api_response = api_instance.get_scheduled_job_detail(uuid)
        print("The response of ScheduledJobsManagementApi->get_scheduled_job_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->get_scheduled_job_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Scheduled job UUID | 

### Return type

[**ScheduledJobDetailDto**](ScheduledJobDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled job detail retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_job_history**
> ScheduledJobHistoryResponseDto get_scheduled_job_history(pagination, uuid)

Scheduled job history

### Example


```python
import openapi_client
from openapi_client.models.pagination_request_dto import PaginationRequestDto
from openapi_client.models.scheduled_job_history_response_dto import ScheduledJobHistoryResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    pagination = openapi_client.PaginationRequestDto() # PaginationRequestDto | 
    uuid = 'uuid_example' # str | Scheduled job UUID

    try:
        # Scheduled job history
        api_response = api_instance.get_scheduled_job_history(pagination, uuid)
        print("The response of ScheduledJobsManagementApi->get_scheduled_job_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->get_scheduled_job_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationRequestDto**](.md)|  | 
 **uuid** | **str**| Scheduled job UUID | 

### Return type

[**ScheduledJobHistoryResponseDto**](ScheduledJobHistoryResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled job history retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scheduled_jobs**
> ScheduledJobsResponseDto list_scheduled_jobs(pagination)

List of scheduled jobs

### Example


```python
import openapi_client
from openapi_client.models.pagination_request_dto import PaginationRequestDto
from openapi_client.models.scheduled_jobs_response_dto import ScheduledJobsResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    pagination = openapi_client.PaginationRequestDto() # PaginationRequestDto | 

    try:
        # List of scheduled jobs
        api_response = api_instance.list_scheduled_jobs(pagination)
        print("The response of ScheduledJobsManagementApi->list_scheduled_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->list_scheduled_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationRequestDto**](.md)|  | 

### Return type

[**ScheduledJobsResponseDto**](ScheduledJobsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of scheduled jobs fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scheduled_job**
> ScheduledJobDetailDto update_scheduled_job(uuid, update_scheduled_job)

Edit Scheduled job

### Example


```python
import openapi_client
from openapi_client.models.scheduled_job_detail_dto import ScheduledJobDetailDto
from openapi_client.models.update_scheduled_job import UpdateScheduledJob
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ScheduledJobsManagementApi(api_client)
    uuid = 'uuid_example' # str | Scheduled job UUID
    update_scheduled_job = openapi_client.UpdateScheduledJob() # UpdateScheduledJob | 

    try:
        # Edit Scheduled job
        api_response = api_instance.update_scheduled_job(uuid, update_scheduled_job)
        print("The response of ScheduledJobsManagementApi->update_scheduled_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobsManagementApi->update_scheduled_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Scheduled job UUID | 
 **update_scheduled_job** | [**UpdateScheduledJob**](UpdateScheduledJob.md)|  | 

### Return type

[**ScheduledJobDetailDto**](ScheduledJobDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduled job updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

