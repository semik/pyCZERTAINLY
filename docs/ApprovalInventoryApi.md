# pyCZERTAINLY.ApprovalInventoryApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_approval**](ApprovalInventoryApi.md#approve_approval) | **PATCH** /v1/approvals/{uuid}/approve | Approving of the Approval
[**approve_approval_recipient**](ApprovalInventoryApi.md#approve_approval_recipient) | **PATCH** /v1/approvals/{uuid}/approveRecipient | Approving of Recipient of the Approval
[**get_approval**](ApprovalInventoryApi.md#get_approval) | **GET** /v1/approvals/{uuid} | Get Approval Detail
[**list_approvals**](ApprovalInventoryApi.md#list_approvals) | **GET** /v1/approvals | List of Approvals
[**list_user_approvals**](ApprovalInventoryApi.md#list_user_approvals) | **GET** /v1/approvals/user | List of User&#39;s Approvals
[**reject_approval**](ApprovalInventoryApi.md#reject_approval) | **PATCH** /v1/approvals/{uuid}/reject | Rejecting of the Approval
[**reject_approval_recipient**](ApprovalInventoryApi.md#reject_approval_recipient) | **PATCH** /v1/approvals/{uuid}/rejectRecipient | Rejecting of Recipient of the Approval


# **approve_approval**
> approve_approval(uuid)

Approving of the Approval

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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval UUID

    try:
        # Approving of the Approval
        api_instance.approve_approval(uuid)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->approve_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Approval approved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_approval_recipient**
> approve_approval_recipient(uuid, user_approval_dto)

Approving of Recipient of the Approval

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.user_approval_dto import UserApprovalDto
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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval UUID
    user_approval_dto = pyCZERTAINLY.UserApprovalDto() # UserApprovalDto | 

    try:
        # Approving of Recipient of the Approval
        api_instance.approve_approval_recipient(uuid, user_approval_dto)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->approve_approval_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval UUID | 
 **user_approval_dto** | [**UserApprovalDto**](UserApprovalDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Approval Recipient approved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval**
> ApprovalDetailDto get_approval(uuid)

Get Approval Detail

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_detail_dto import ApprovalDetailDto
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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval UUID

    try:
        # Get Approval Detail
        api_response = api_instance.get_approval(uuid)
        print("The response of ApprovalInventoryApi->get_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->get_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval UUID | 

### Return type

[**ApprovalDetailDto**](ApprovalDetailDto.md)

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
**200** | Approval detail retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approvals**
> ApprovalResponseDto list_approvals(pagination_request_dto)

List of Approvals

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_response_dto import ApprovalResponseDto
from pyCZERTAINLY.models.pagination_request_dto import PaginationRequestDto
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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    pagination_request_dto = pyCZERTAINLY.PaginationRequestDto() # PaginationRequestDto | 

    try:
        # List of Approvals
        api_response = api_instance.list_approvals(pagination_request_dto)
        print("The response of ApprovalInventoryApi->list_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->list_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_dto** | [**PaginationRequestDto**](.md)|  | 

### Return type

[**ApprovalResponseDto**](ApprovalResponseDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | List of all approvals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_approvals**
> ApprovalResponseDto list_user_approvals(pagination_request_dto, approval_user_dto)

List of User's Approvals

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_response_dto import ApprovalResponseDto
from pyCZERTAINLY.models.approval_user_dto import ApprovalUserDto
from pyCZERTAINLY.models.pagination_request_dto import PaginationRequestDto
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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    pagination_request_dto = pyCZERTAINLY.PaginationRequestDto() # PaginationRequestDto | 
    approval_user_dto = pyCZERTAINLY.ApprovalUserDto() # ApprovalUserDto | Select if you want to list all history of approvals by user

    try:
        # List of User's Approvals
        api_response = api_instance.list_user_approvals(pagination_request_dto, approval_user_dto)
        print("The response of ApprovalInventoryApi->list_user_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->list_user_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_dto** | [**PaginationRequestDto**](.md)|  | 
 **approval_user_dto** | [**ApprovalUserDto**](.md)| Select if you want to list all history of approvals by user | 

### Return type

[**ApprovalResponseDto**](ApprovalResponseDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | List of all approvals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_approval**
> reject_approval(uuid)

Rejecting of the Approval

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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval UUID

    try:
        # Rejecting of the Approval
        api_instance.reject_approval(uuid)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->reject_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**204** | Approval rejected |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_approval_recipient**
> reject_approval_recipient(uuid, user_approval_dto)

Rejecting of Recipient of the Approval

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.user_approval_dto import UserApprovalDto
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
    api_instance = pyCZERTAINLY.ApprovalInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval UUID
    user_approval_dto = pyCZERTAINLY.UserApprovalDto() # UserApprovalDto | 

    try:
        # Rejecting of Recipient of the Approval
        api_instance.reject_approval_recipient(uuid, user_approval_dto)
    except Exception as e:
        print("Exception when calling ApprovalInventoryApi->reject_approval_recipient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval UUID | 
 **user_approval_dto** | [**UserApprovalDto**](UserApprovalDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Approval Recipient rejected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

