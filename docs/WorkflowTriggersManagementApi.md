# pyCZERTAINLY.WorkflowTriggersManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger**](WorkflowTriggersManagementApi.md#create_trigger) | **POST** /v1/workflows/triggers | Create Trigger
[**delete_trigger**](WorkflowTriggersManagementApi.md#delete_trigger) | **DELETE** /v1/workflows/triggers/{triggerUuid} | Delete Trigger
[**get_trigger**](WorkflowTriggersManagementApi.md#get_trigger) | **GET** /v1/workflows/triggers/{triggerUuid} | Get Trigger details
[**get_trigger_history**](WorkflowTriggersManagementApi.md#get_trigger_history) | **GET** /v1/workflows/triggers/{triggerUuid}/history/{associationObjectUuid} | Get Trigger History
[**get_trigger_history_summary**](WorkflowTriggersManagementApi.md#get_trigger_history_summary) | **GET** /v1/workflows/triggers/history/{associationObjectUuid} | Get Trigger History Summary
[**list_triggers**](WorkflowTriggersManagementApi.md#list_triggers) | **GET** /v1/workflows/triggers | List Triggers
[**update_trigger**](WorkflowTriggersManagementApi.md#update_trigger) | **PUT** /v1/workflows/triggers/{triggerUuid} | Update Trigger


# **create_trigger**
> TriggerDetailDto create_trigger(trigger_request_dto)

Create Trigger

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.trigger_detail_dto import TriggerDetailDto
from pyCZERTAINLY.models.trigger_request_dto import TriggerRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    trigger_request_dto = pyCZERTAINLY.TriggerRequestDto() # TriggerRequestDto | 

    try:
        # Create Trigger
        api_response = api_instance.create_trigger(trigger_request_dto)
        print("The response of WorkflowTriggersManagementApi->create_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->create_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_request_dto** | [**TriggerRequestDto**](TriggerRequestDto.md)|  | 

### Return type

[**TriggerDetailDto**](TriggerDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**201** | Trigger created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trigger**
> delete_trigger(trigger_uuid)

Delete Trigger

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    trigger_uuid = 'trigger_uuid_example' # str | Trigger UUID

    try:
        # Delete Trigger
        api_instance.delete_trigger(trigger_uuid)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->delete_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| Trigger UUID | 

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
**204** | Trigger deleted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger**
> TriggerDetailDto get_trigger(trigger_uuid)

Get Trigger details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.trigger_detail_dto import TriggerDetailDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    trigger_uuid = 'trigger_uuid_example' # str | Trigger UUID

    try:
        # Get Trigger details
        api_response = api_instance.get_trigger(trigger_uuid)
        print("The response of WorkflowTriggersManagementApi->get_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->get_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| Trigger UUID | 

### Return type

[**TriggerDetailDto**](TriggerDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Trigger details retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_history**
> List[TriggerHistoryDto] get_trigger_history(trigger_uuid, association_object_uuid)

Get Trigger History

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.trigger_history_dto import TriggerHistoryDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    trigger_uuid = 'trigger_uuid_example' # str | Trigger UUID
    association_object_uuid = 'association_object_uuid_example' # str | Trigger Association Object UUID

    try:
        # Get Trigger History
        api_response = api_instance.get_trigger_history(trigger_uuid, association_object_uuid)
        print("The response of WorkflowTriggersManagementApi->get_trigger_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->get_trigger_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| Trigger UUID | 
 **association_object_uuid** | **str**| Trigger Association Object UUID | 

### Return type

[**List[TriggerHistoryDto]**](TriggerHistoryDto.md)

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
**404** | Not Found |  -  |
**200** | Trigger History retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_history_summary**
> TriggerHistorySummaryDto get_trigger_history_summary(association_object_uuid)

Get Trigger History Summary

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.trigger_history_summary_dto import TriggerHistorySummaryDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    association_object_uuid = 'association_object_uuid_example' # str | Trigger Association Object UUID

    try:
        # Get Trigger History Summary
        api_response = api_instance.get_trigger_history_summary(association_object_uuid)
        print("The response of WorkflowTriggersManagementApi->get_trigger_history_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->get_trigger_history_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_object_uuid** | **str**| Trigger Association Object UUID | 

### Return type

[**TriggerHistorySummaryDto**](TriggerHistorySummaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Trigger History Summary retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_triggers**
> List[TriggerDto] list_triggers(resource=resource, event_resource=event_resource)

List Triggers

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.resource import Resource
from pyCZERTAINLY.models.trigger_dto import TriggerDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    resource = pyCZERTAINLY.Resource() # Resource |  (optional)
    event_resource = pyCZERTAINLY.Resource() # Resource |  (optional)

    try:
        # List Triggers
        api_response = api_instance.list_triggers(resource=resource, event_resource=event_resource)
        print("The response of WorkflowTriggersManagementApi->list_triggers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->list_triggers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)|  | [optional] 
 **event_resource** | [**Resource**](.md)|  | [optional] 

### Return type

[**List[TriggerDto]**](TriggerDto.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | List of triggers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trigger**
> TriggerDetailDto update_trigger(trigger_uuid, update_trigger_request_dto)

Update Trigger

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.trigger_detail_dto import TriggerDetailDto
from pyCZERTAINLY.models.update_trigger_request_dto import UpdateTriggerRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.WorkflowTriggersManagementApi(api_client)
    trigger_uuid = 'trigger_uuid_example' # str | Trigger UUID
    update_trigger_request_dto = pyCZERTAINLY.UpdateTriggerRequestDto() # UpdateTriggerRequestDto | 

    try:
        # Update Trigger
        api_response = api_instance.update_trigger(trigger_uuid, update_trigger_request_dto)
        print("The response of WorkflowTriggersManagementApi->update_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggersManagementApi->update_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_uuid** | **str**| Trigger UUID | 
 **update_trigger_request_dto** | [**UpdateTriggerRequestDto**](UpdateTriggerRequestDto.md)|  | 

### Return type

[**TriggerDetailDto**](TriggerDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Trigger updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

