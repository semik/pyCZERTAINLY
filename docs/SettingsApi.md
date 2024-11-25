# pyCZERTAINLY.SettingsApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications_settings**](SettingsApi.md#get_notifications_settings) | **GET** /v1/settings/notifications | Get notification settings
[**get_platform_settings**](SettingsApi.md#get_platform_settings) | **GET** /v1/settings/platform | Get platform settings
[**update_notifications_settings**](SettingsApi.md#update_notifications_settings) | **PUT** /v1/settings/notifications | Update notifications setting
[**update_platform_settings**](SettingsApi.md#update_platform_settings) | **PUT** /v1/settings/platform | Update platform setting


# **get_notifications_settings**
> NotificationSettingsDto get_notifications_settings()

Get notification settings

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.notification_settings_dto import NotificationSettingsDto
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
    api_instance = pyCZERTAINLY.SettingsApi(api_client)

    try:
        # Get notification settings
        api_response = api_instance.get_notifications_settings()
        print("The response of SettingsApi->get_notifications_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_notifications_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationSettingsDto**](NotificationSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notiifcation settings retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_settings**
> PlatformSettingsDto get_platform_settings()

Get platform settings

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.platform_settings_dto import PlatformSettingsDto
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
    api_instance = pyCZERTAINLY.SettingsApi(api_client)

    try:
        # Get platform settings
        api_response = api_instance.get_platform_settings()
        print("The response of SettingsApi->get_platform_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_platform_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PlatformSettingsDto**](PlatformSettingsDto.md)

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
**200** | Platform settings retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notifications_settings**
> update_notifications_settings(notification_settings_dto)

Update notifications setting

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.notification_settings_dto import NotificationSettingsDto
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
    api_instance = pyCZERTAINLY.SettingsApi(api_client)
    notification_settings_dto = pyCZERTAINLY.NotificationSettingsDto() # NotificationSettingsDto | 

    try:
        # Update notifications setting
        api_instance.update_notifications_settings(notification_settings_dto)
    except Exception as e:
        print("Exception when calling SettingsApi->update_notifications_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_settings_dto** | [**NotificationSettingsDto**](NotificationSettingsDto.md)|  | 

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
**200** | Setting updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_settings**
> update_platform_settings(platform_settings_dto)

Update platform setting

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.platform_settings_dto import PlatformSettingsDto
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
    api_instance = pyCZERTAINLY.SettingsApi(api_client)
    platform_settings_dto = pyCZERTAINLY.PlatformSettingsDto() # PlatformSettingsDto | 

    try:
        # Update platform setting
        api_instance.update_platform_settings(platform_settings_dto)
    except Exception as e:
        print("Exception when calling SettingsApi->update_platform_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_settings_dto** | [**PlatformSettingsDto**](PlatformSettingsDto.md)|  | 

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
**200** | Setting updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

