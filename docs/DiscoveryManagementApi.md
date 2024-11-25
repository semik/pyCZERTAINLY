# openapi_client.DiscoveryManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_discovery**](DiscoveryManagementApi.md#bulk_delete_discovery) | **DELETE** /v1/discoveries | Delete Multiple Discoveries
[**create_discovery**](DiscoveryManagementApi.md#create_discovery) | **POST** /v1/discoveries | Create Discovery
[**delete_discovery**](DiscoveryManagementApi.md#delete_discovery) | **DELETE** /v1/discoveries/{uuid} | Delete Discovery
[**get_discovery**](DiscoveryManagementApi.md#get_discovery) | **GET** /v1/discoveries/{uuid} | Discovery Details
[**get_discovery_certificates**](DiscoveryManagementApi.md#get_discovery_certificates) | **GET** /v1/discoveries/{uuid}/certificates | Discovery Details
[**get_searchable_field_information3**](DiscoveryManagementApi.md#get_searchable_field_information3) | **GET** /v1/discoveries/search | Get Discovery searchable fields information
[**list_discoveries**](DiscoveryManagementApi.md#list_discoveries) | **POST** /v1/discoveries/list | List Discovery
[**schedule_discovery**](DiscoveryManagementApi.md#schedule_discovery) | **POST** /v1/discoveries/schedule | Schedule Discovery


# **bulk_delete_discovery**
> bulk_delete_discovery(request_body)

Delete Multiple Discoveries

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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Discovery UUIDs

    try:
        # Delete Multiple Discoveries
        api_instance.bulk_delete_discovery(request_body)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->bulk_delete_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Discovery UUIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Discoveries deleted |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_discovery**
> UuidDto create_discovery(discovery_dto)

Create Discovery

### Example


```python
import openapi_client
from openapi_client.models.discovery_dto import DiscoveryDto
from openapi_client.models.uuid_dto import UuidDto
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    discovery_dto = openapi_client.DiscoveryDto() # DiscoveryDto | 

    try:
        # Create Discovery
        api_response = api_instance.create_discovery(discovery_dto)
        print("The response of DiscoveryManagementApi->create_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->create_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discovery_dto** | [**DiscoveryDto**](DiscoveryDto.md)|  | 

### Return type

[**UuidDto**](UuidDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**201** | Discovery Created |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_discovery**
> delete_discovery(uuid)

Delete Discovery

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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    uuid = 'uuid_example' # str | Discovery UUID

    try:
        # Delete Discovery
        api_instance.delete_discovery(uuid)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->delete_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Discovery UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | Discovery deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery**
> DiscoveryHistoryDetailDto get_discovery(uuid)

Discovery Details

### Example


```python
import openapi_client
from openapi_client.models.discovery_history_detail_dto import DiscoveryHistoryDetailDto
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    uuid = 'uuid_example' # str | Discovery UUID

    try:
        # Discovery Details
        api_response = api_instance.get_discovery(uuid)
        print("The response of DiscoveryManagementApi->get_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->get_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Discovery UUID | 

### Return type

[**DiscoveryHistoryDetailDto**](DiscoveryHistoryDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Discovery details retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery_certificates**
> DiscoveryCertificateResponseDto get_discovery_certificates(uuid, newly_discovered=newly_discovered, items_per_page=items_per_page, page_number=page_number)

Discovery Details

### Example


```python
import openapi_client
from openapi_client.models.discovery_certificate_response_dto import DiscoveryCertificateResponseDto
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    uuid = 'uuid_example' # str | Discovery UUID
    newly_discovered = True # bool |  (optional)
    items_per_page = 10 # int |  (optional) (default to 10)
    page_number = 0 # int |  (optional) (default to 0)

    try:
        # Discovery Details
        api_response = api_instance.get_discovery_certificates(uuid, newly_discovered=newly_discovered, items_per_page=items_per_page, page_number=page_number)
        print("The response of DiscoveryManagementApi->get_discovery_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->get_discovery_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Discovery UUID | 
 **newly_discovered** | **bool**|  | [optional] 
 **items_per_page** | **int**|  | [optional] [default to 10]
 **page_number** | **int**|  | [optional] [default to 0]

### Return type

[**DiscoveryCertificateResponseDto**](DiscoveryCertificateResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Discovery details retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information3**
> List[SearchFieldDataByGroupDto] get_searchable_field_information3()

Get Discovery searchable fields information

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)

    try:
        # Get Discovery searchable fields information
        api_response = api_instance.get_searchable_field_information3()
        print("The response of DiscoveryManagementApi->get_searchable_field_information3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->get_searchable_field_information3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**200** | Discovery searchable field information retrieved |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discoveries**
> DiscoveryResponseDto list_discoveries(search_request_dto)

List Discovery

### Example


```python
import openapi_client
from openapi_client.models.discovery_response_dto import DiscoveryResponseDto
from openapi_client.models.search_request_dto import SearchRequestDto
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    search_request_dto = openapi_client.SearchRequestDto() # SearchRequestDto | 

    try:
        # List Discovery
        api_response = api_instance.list_discoveries(search_request_dto)
        print("The response of DiscoveryManagementApi->list_discoveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->list_discoveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**DiscoveryResponseDto**](DiscoveryResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | List of available Discoveries |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_discovery**
> UuidDto schedule_discovery(schedule_discovery_dto)

Schedule Discovery

### Example


```python
import openapi_client
from openapi_client.models.schedule_discovery_dto import ScheduleDiscoveryDto
from openapi_client.models.uuid_dto import UuidDto
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
    api_instance = openapi_client.DiscoveryManagementApi(api_client)
    schedule_discovery_dto = openapi_client.ScheduleDiscoveryDto() # ScheduleDiscoveryDto | 

    try:
        # Schedule Discovery
        api_response = api_instance.schedule_discovery(schedule_discovery_dto)
        print("The response of DiscoveryManagementApi->schedule_discovery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryManagementApi->schedule_discovery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_discovery_dto** | [**ScheduleDiscoveryDto**](ScheduleDiscoveryDto.md)|  | 

### Return type

[**UuidDto**](UuidDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**201** | Discovery Scheduled |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

