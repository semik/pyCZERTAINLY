# openapi_client.InternalNotificationApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_notification**](InternalNotificationApi.md#bulk_delete_notification) | **DELETE** /v1/notifications | Delete a list of notifications for logged user
[**bulk_mark_notification_as_read**](InternalNotificationApi.md#bulk_mark_notification_as_read) | **PATCH** /v1/notifications | Mark a list of notifications as read for logged user
[**delete_notification**](InternalNotificationApi.md#delete_notification) | **DELETE** /v1/notifications/{uuid} | Delete a notification for logged user
[**list_notifications**](InternalNotificationApi.md#list_notifications) | **GET** /v1/notifications | List notifications for logged user
[**mark_notification_as_read**](InternalNotificationApi.md#mark_notification_as_read) | **PATCH** /v1/notifications/{uuid} | Mark notification as read for logged user


# **bulk_delete_notification**
> bulk_delete_notification(request_body)

Delete a list of notifications for logged user

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
    api_instance = openapi_client.InternalNotificationApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Notifications UUIDs

    try:
        # Delete a list of notifications for logged user
        api_instance.bulk_delete_notification(request_body)
    except Exception as e:
        print("Exception when calling InternalNotificationApi->bulk_delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Notifications UUIDs | 

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
**204** | Notifications deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_mark_notification_as_read**
> bulk_mark_notification_as_read(request_body)

Mark a list of notifications as read for logged user

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
    api_instance = openapi_client.InternalNotificationApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Notifications UUIDs

    try:
        # Mark a list of notifications as read for logged user
        api_instance.bulk_mark_notification_as_read(request_body)
    except Exception as e:
        print("Exception when calling InternalNotificationApi->bulk_mark_notification_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Notifications UUIDs | 

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
**204** | Notifications marked as read |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> delete_notification(uuid)

Delete a notification for logged user

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
    api_instance = openapi_client.InternalNotificationApi(api_client)
    uuid = 'uuid_example' # str | Notification UUID

    try:
        # Delete a notification for logged user
        api_instance.delete_notification(uuid)
    except Exception as e:
        print("Exception when calling InternalNotificationApi->delete_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Notification UUID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Notification deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> NotificationResponseDto list_notifications(request)

List notifications for logged user

### Example


```python
import openapi_client
from openapi_client.models.notification_request_dto import NotificationRequestDto
from openapi_client.models.notification_response_dto import NotificationResponseDto
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
    api_instance = openapi_client.InternalNotificationApi(api_client)
    request = openapi_client.NotificationRequestDto() # NotificationRequestDto | Show only unread notifications

    try:
        # List notifications for logged user
        api_response = api_instance.list_notifications(request)
        print("The response of InternalNotificationApi->list_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalNotificationApi->list_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**NotificationRequestDto**](.md)| Show only unread notifications | 

### Return type

[**NotificationResponseDto**](NotificationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | List of notifications |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> mark_notification_as_read(uuid)

Mark notification as read for logged user

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
    api_instance = openapi_client.InternalNotificationApi(api_client)
    uuid = 'uuid_example' # str | Notification UUID

    try:
        # Mark notification as read for logged user
        api_instance.mark_notification_as_read(uuid)
    except Exception as e:
        print("Exception when calling InternalNotificationApi->mark_notification_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Notification UUID | 

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
**204** | Notification marked as read |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

