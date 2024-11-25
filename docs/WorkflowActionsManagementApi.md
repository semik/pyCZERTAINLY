# pyCZERTAINLY.WorkflowActionsManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_action**](WorkflowActionsManagementApi.md#create_action) | **POST** /v1/workflows/actions | Create Action
[**create_execution**](WorkflowActionsManagementApi.md#create_execution) | **POST** /v1/workflows/executions | Create Execution
[**delete_action**](WorkflowActionsManagementApi.md#delete_action) | **DELETE** /v1/workflows/actions/{actionUuid} | Delete Action
[**delete_execution**](WorkflowActionsManagementApi.md#delete_execution) | **DELETE** /v1/workflows/executions/{executionUuid} | Delete Execution
[**get_action**](WorkflowActionsManagementApi.md#get_action) | **GET** /v1/workflows/actions/{actionUuid} | Get Action Details
[**get_execution**](WorkflowActionsManagementApi.md#get_execution) | **GET** /v1/workflows/executions/{executionUuid} | Get Execution Details
[**list_actions**](WorkflowActionsManagementApi.md#list_actions) | **GET** /v1/workflows/actions | List Actions
[**list_executions**](WorkflowActionsManagementApi.md#list_executions) | **GET** /v1/workflows/executions | List executions
[**update_action**](WorkflowActionsManagementApi.md#update_action) | **PUT** /v1/workflows/actions/{actionUuid} | Update Action
[**update_execution**](WorkflowActionsManagementApi.md#update_execution) | **PUT** /v1/workflows/executions/{executionUuid} | Update Execution


# **create_action**
> ActionDetailDto create_action(action_request_dto)

Create Action

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.action_detail_dto import ActionDetailDto
from pyCZERTAINLY.models.action_request_dto import ActionRequestDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    action_request_dto = pyCZERTAINLY.ActionRequestDto() # ActionRequestDto | 

    try:
        # Create Action
        api_response = api_instance.create_action(action_request_dto)
        print("The response of WorkflowActionsManagementApi->create_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->create_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_request_dto** | [**ActionRequestDto**](ActionRequestDto.md)|  | 

### Return type

[**ActionDetailDto**](ActionDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**201** | Action created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_execution**
> ExecutionDto create_execution(execution_request_dto)

Create Execution

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.execution_dto import ExecutionDto
from pyCZERTAINLY.models.execution_request_dto import ExecutionRequestDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    execution_request_dto = pyCZERTAINLY.ExecutionRequestDto() # ExecutionRequestDto | 

    try:
        # Create Execution
        api_response = api_instance.create_execution(execution_request_dto)
        print("The response of WorkflowActionsManagementApi->create_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->create_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_request_dto** | [**ExecutionRequestDto**](ExecutionRequestDto.md)|  | 

### Return type

[**ExecutionDto**](ExecutionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**201** | Execution created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_action**
> delete_action(action_uuid)

Delete Action

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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    action_uuid = 'action_uuid_example' # str | Action UUID

    try:
        # Delete Action
        api_instance.delete_action(action_uuid)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->delete_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_uuid** | **str**| Action UUID | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Action deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_execution**
> delete_execution(execution_uuid)

Delete Execution

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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    execution_uuid = 'execution_uuid_example' # str | Execution UUID

    try:
        # Delete Execution
        api_instance.delete_execution(execution_uuid)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->delete_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_uuid** | **str**| Execution UUID | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Execution deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action**
> ActionDetailDto get_action(action_uuid)

Get Action Details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.action_detail_dto import ActionDetailDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    action_uuid = 'action_uuid_example' # str | Action UUID

    try:
        # Get Action Details
        api_response = api_instance.get_action(action_uuid)
        print("The response of WorkflowActionsManagementApi->get_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->get_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_uuid** | **str**| Action UUID | 

### Return type

[**ActionDetailDto**](ActionDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Action details retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> ExecutionDto get_execution(execution_uuid)

Get Execution Details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.execution_dto import ExecutionDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    execution_uuid = 'execution_uuid_example' # str | Execution UUID

    try:
        # Get Execution Details
        api_response = api_instance.get_execution(execution_uuid)
        print("The response of WorkflowActionsManagementApi->get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->get_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_uuid** | **str**| Execution UUID | 

### Return type

[**ExecutionDto**](ExecutionDto.md)

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
**200** | Execution details retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_actions**
> List[ActionDto] list_actions(resource=resource)

List Actions

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.action_dto import ActionDto
from pyCZERTAINLY.models.resource import Resource
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    resource = pyCZERTAINLY.Resource() # Resource |  (optional)

    try:
        # List Actions
        api_response = api_instance.list_actions(resource=resource)
        print("The response of WorkflowActionsManagementApi->list_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->list_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)|  | [optional] 

### Return type

[**List[ActionDto]**](ActionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | List of actions fetched |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_executions**
> List[ExecutionDto] list_executions(resource=resource)

List executions

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.execution_dto import ExecutionDto
from pyCZERTAINLY.models.resource import Resource
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    resource = pyCZERTAINLY.Resource() # Resource |  (optional)

    try:
        # List executions
        api_response = api_instance.list_executions(resource=resource)
        print("The response of WorkflowActionsManagementApi->list_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->list_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)|  | [optional] 

### Return type

[**List[ExecutionDto]**](ExecutionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | List of executions fetched |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_action**
> ActionDetailDto update_action(action_uuid, update_action_request_dto)

Update Action

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.action_detail_dto import ActionDetailDto
from pyCZERTAINLY.models.update_action_request_dto import UpdateActionRequestDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    action_uuid = 'action_uuid_example' # str | Action UUID
    update_action_request_dto = pyCZERTAINLY.UpdateActionRequestDto() # UpdateActionRequestDto | 

    try:
        # Update Action
        api_response = api_instance.update_action(action_uuid, update_action_request_dto)
        print("The response of WorkflowActionsManagementApi->update_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->update_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_uuid** | **str**| Action UUID | 
 **update_action_request_dto** | [**UpdateActionRequestDto**](UpdateActionRequestDto.md)|  | 

### Return type

[**ActionDetailDto**](ActionDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Action updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_execution**
> ExecutionDto update_execution(execution_uuid, update_execution_request_dto)

Update Execution

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.execution_dto import ExecutionDto
from pyCZERTAINLY.models.update_execution_request_dto import UpdateExecutionRequestDto
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
    api_instance = pyCZERTAINLY.WorkflowActionsManagementApi(api_client)
    execution_uuid = 'execution_uuid_example' # str | Execution UUID
    update_execution_request_dto = pyCZERTAINLY.UpdateExecutionRequestDto() # UpdateExecutionRequestDto | 

    try:
        # Update Execution
        api_response = api_instance.update_execution(execution_uuid, update_execution_request_dto)
        print("The response of WorkflowActionsManagementApi->update_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsManagementApi->update_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_uuid** | **str**| Execution UUID | 
 **update_execution_request_dto** | [**UpdateExecutionRequestDto**](UpdateExecutionRequestDto.md)|  | 

### Return type

[**ExecutionDto**](ExecutionDto.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Execution updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

