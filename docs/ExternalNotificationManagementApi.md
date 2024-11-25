# openapi_client.ExternalNotificationManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_instance**](ExternalNotificationManagementApi.md#create_notification_instance) | **POST** /v1/notificationInstances | Add Notification instance
[**delete_notification_instance**](ExternalNotificationManagementApi.md#delete_notification_instance) | **DELETE** /v1/notificationInstances/{uuid} | Delete Notification instance
[**edit_notification_instance**](ExternalNotificationManagementApi.md#edit_notification_instance) | **PUT** /v1/notificationInstances/{uuid} | Edit Notification instance
[**get_notification_instance**](ExternalNotificationManagementApi.md#get_notification_instance) | **GET** /v1/notificationInstances/{uuid} | Details of an Notification instance
[**list_mapping_attributes**](ExternalNotificationManagementApi.md#list_mapping_attributes) | **GET** /v1/notificationInstances/attributes/mapping/{connectorUuid}/{kind} | List of mapping attributes
[**list_notification_instances**](ExternalNotificationManagementApi.md#list_notification_instances) | **GET** /v1/notificationInstances | List of available Notification instances


# **create_notification_instance**
> UuidDto create_notification_instance(notification_instance_request_dto)

Add Notification instance

### Example


```python
import openapi_client
from openapi_client.models.notification_instance_request_dto import NotificationInstanceRequestDto
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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)
    notification_instance_request_dto = openapi_client.NotificationInstanceRequestDto() # NotificationInstanceRequestDto | 

    try:
        # Add Notification instance
        api_response = api_instance.create_notification_instance(notification_instance_request_dto)
        print("The response of ExternalNotificationManagementApi->create_notification_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->create_notification_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_instance_request_dto** | [**NotificationInstanceRequestDto**](NotificationInstanceRequestDto.md)|  | 

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
**201** | New Notification instance added |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_instance**
> delete_notification_instance(uuid)

Delete Notification instance

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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)
    uuid = 'uuid_example' # str | Notification instance UUID

    try:
        # Delete Notification instance
        api_instance.delete_notification_instance(uuid)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->delete_notification_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Notification instance UUID | 

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
**204** | Notification instance deleted |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_notification_instance**
> NotificationInstanceDto edit_notification_instance(uuid, notification_instance_update_request_dto)

Edit Notification instance

### Example


```python
import openapi_client
from openapi_client.models.notification_instance_dto import NotificationInstanceDto
from openapi_client.models.notification_instance_update_request_dto import NotificationInstanceUpdateRequestDto
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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)
    uuid = 'uuid_example' # str | Notification instance UUID
    notification_instance_update_request_dto = openapi_client.NotificationInstanceUpdateRequestDto() # NotificationInstanceUpdateRequestDto | 

    try:
        # Edit Notification instance
        api_response = api_instance.edit_notification_instance(uuid, notification_instance_update_request_dto)
        print("The response of ExternalNotificationManagementApi->edit_notification_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->edit_notification_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Notification instance UUID | 
 **notification_instance_update_request_dto** | [**NotificationInstanceUpdateRequestDto**](NotificationInstanceUpdateRequestDto.md)|  | 

### Return type

[**NotificationInstanceDto**](NotificationInstanceDto.md)

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
**200** | Notification instance details updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_instance**
> NotificationInstanceDto get_notification_instance(uuid)

Details of an Notification instance

### Example


```python
import openapi_client
from openapi_client.models.notification_instance_dto import NotificationInstanceDto
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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)
    uuid = 'uuid_example' # str | Notification instance UUID

    try:
        # Details of an Notification instance
        api_response = api_instance.get_notification_instance(uuid)
        print("The response of ExternalNotificationManagementApi->get_notification_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->get_notification_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Notification instance UUID | 

### Return type

[**NotificationInstanceDto**](NotificationInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Notification instance details retrieved |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_attributes**
> List[DataAttribute] list_mapping_attributes(connector_uuid, kind)

List of mapping attributes

### Example


```python
import openapi_client
from openapi_client.models.data_attribute import DataAttribute
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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)
    connector_uuid = 'connector_uuid_example' # str | Connector UUID
    kind = 'kind_example' # str | Kind

    try:
        # List of mapping attributes
        api_response = api_instance.list_mapping_attributes(connector_uuid, kind)
        print("The response of ExternalNotificationManagementApi->list_mapping_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->list_mapping_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **str**| Connector UUID | 
 **kind** | **str**| Kind | 

### Return type

[**List[DataAttribute]**](DataAttribute.md)

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
**200** | List of mapping attributes |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_instances**
> List[NotificationInstanceDto] list_notification_instances()

List of available Notification instances

### Example


```python
import openapi_client
from openapi_client.models.notification_instance_dto import NotificationInstanceDto
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
    api_instance = openapi_client.ExternalNotificationManagementApi(api_client)

    try:
        # List of available Notification instances
        api_response = api_instance.list_notification_instances()
        print("The response of ExternalNotificationManagementApi->list_notification_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalNotificationManagementApi->list_notification_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NotificationInstanceDto]**](NotificationInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Notification instances |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

