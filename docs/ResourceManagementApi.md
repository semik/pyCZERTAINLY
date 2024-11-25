# openapi_client.ResourceManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_resource_events**](ResourceManagementApi.md#list_resource_events) | **GET** /v1/resources/{resource}/events | Retrieve a list of all events that can be triggered by a resource
[**list_resource_rule_filter_fields**](ResourceManagementApi.md#list_resource_rule_filter_fields) | **GET** /v1/resources/{resource}/filters/rules | Retrieve filter fields that can be used for creating rule conditions and actions
[**list_resources**](ResourceManagementApi.md#list_resources) | **GET** /v1/resources | Retrieve list of resources with information and settings


# **list_resource_events**
> List[ResourceEventDto] list_resource_events(resource)

Retrieve a list of all events that can be triggered by a resource

### Example


```python
import openapi_client
from openapi_client.models.resource import Resource
from openapi_client.models.resource_event_dto import ResourceEventDto
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
    api_instance = openapi_client.ResourceManagementApi(api_client)
    resource = openapi_client.Resource() # Resource | Resource

    try:
        # Retrieve a list of all events that can be triggered by a resource
        api_response = api_instance.list_resource_events(resource)
        print("The response of ResourceManagementApi->list_resource_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceManagementApi->list_resource_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)| Resource | 

### Return type

[**List[ResourceEventDto]**](ResourceEventDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**200** | Events retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_rule_filter_fields**
> List[SearchFieldDataByGroupDto] list_resource_rule_filter_fields(resource, settable=settable)

Retrieve filter fields that can be used for creating rule conditions and actions

### Example


```python
import openapi_client
from openapi_client.models.resource import Resource
from openapi_client.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto
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
    api_instance = openapi_client.ResourceManagementApi(api_client)
    resource = openapi_client.Resource() # Resource | Resource
    settable = True # bool |  (optional)

    try:
        # Retrieve filter fields that can be used for creating rule conditions and actions
        api_response = api_instance.list_resource_rule_filter_fields(resource, settable=settable)
        print("The response of ResourceManagementApi->list_resource_rule_filter_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceManagementApi->list_resource_rule_filter_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)| Resource | 
 **settable** | **bool**|  | [optional] 

### Return type

[**List[SearchFieldDataByGroupDto]**](SearchFieldDataByGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Filter fields retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resources**
> List[ResourceDto] list_resources()

Retrieve list of resources with information and settings

### Example


```python
import openapi_client
from openapi_client.models.resource_dto import ResourceDto
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
    api_instance = openapi_client.ResourceManagementApi(api_client)

    try:
        # Retrieve list of resources with information and settings
        api_response = api_instance.list_resources()
        print("The response of ResourceManagementApi->list_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceManagementApi->list_resources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ResourceDto]**](ResourceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Resources retrieved |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

