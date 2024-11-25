# openapi_client.AuditLogApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_audit_logs**](AuditLogApi.md#export_audit_logs) | **POST** /v1/auditLogs/export | Export Audit logs
[**get_searchable_field_information5**](AuditLogApi.md#get_searchable_field_information5) | **GET** /v1/auditLogs/search | Get Audit logs searchable fields information
[**list_audit_logs**](AuditLogApi.md#list_audit_logs) | **POST** /v1/auditLogs | List Audit logs
[**purge_audit_logs**](AuditLogApi.md#purge_audit_logs) | **POST** /v1/auditLogs/purge | Purge Audit logs


# **export_audit_logs**
> bytearray export_audit_logs(search_filter_request_dto)

Export Audit logs

### Example


```python
import openapi_client
from openapi_client.models.search_filter_request_dto import SearchFilterRequestDto
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
    api_instance = openapi_client.AuditLogApi(api_client)
    search_filter_request_dto = [openapi_client.SearchFilterRequestDto()] # List[SearchFilterRequestDto] | 

    try:
        # Export Audit logs
        api_response = api_instance.export_audit_logs(search_filter_request_dto)
        print("The response of AuditLogApi->export_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->export_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_filter_request_dto** | [**List[SearchFilterRequestDto]**](SearchFilterRequestDto.md)|  | 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Export of audit logs |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information5**
> List[SearchFieldDataByGroupDto] get_searchable_field_information5()

Get Audit logs searchable fields information

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
    api_instance = openapi_client.AuditLogApi(api_client)

    try:
        # Get Audit logs searchable fields information
        api_response = api_instance.get_searchable_field_information5()
        print("The response of AuditLogApi->get_searchable_field_information5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->get_searchable_field_information5: %s\n" % e)
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
**200** | Audit logs searchable field information retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_logs**
> AuditLogResponseDto list_audit_logs(search_request_dto)

List Audit logs

### Example


```python
import openapi_client
from openapi_client.models.audit_log_response_dto import AuditLogResponseDto
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
    api_instance = openapi_client.AuditLogApi(api_client)
    search_request_dto = openapi_client.SearchRequestDto() # SearchRequestDto | 

    try:
        # List Audit logs
        api_response = api_instance.list_audit_logs(search_request_dto)
        print("The response of AuditLogApi->list_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->list_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**AuditLogResponseDto**](AuditLogResponseDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | List of audit logs |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_audit_logs**
> purge_audit_logs(search_filter_request_dto)

Purge Audit logs

### Example


```python
import openapi_client
from openapi_client.models.search_filter_request_dto import SearchFilterRequestDto
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
    api_instance = openapi_client.AuditLogApi(api_client)
    search_filter_request_dto = [openapi_client.SearchFilterRequestDto()] # List[SearchFilterRequestDto] | 

    try:
        # Purge Audit logs
        api_instance.purge_audit_logs(search_filter_request_dto)
    except Exception as e:
        print("Exception when calling AuditLogApi->purge_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_filter_request_dto** | [**List[SearchFilterRequestDto]**](SearchFilterRequestDto.md)|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Audit logs purged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

