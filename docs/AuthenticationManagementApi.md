# pyCZERTAINLY.AuthenticationManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_resources**](AuthenticationManagementApi.md#get_auth_resources) | **GET** /v1/auth/resources | Get Auth Resources
[**get_objects_for_resource**](AuthenticationManagementApi.md#get_objects_for_resource) | **GET** /v1/auth/resources/{resourceName}/objects | Get List of objects for Object Access
[**profile**](AuthenticationManagementApi.md#profile) | **GET** /v1/auth/profile | Profile Authorization
[**update_user_profile**](AuthenticationManagementApi.md#update_user_profile) | **PUT** /v1/auth/profile | Update User Profile


# **get_auth_resources**
> List[AuthResourceDto] get_auth_resources()

Get Auth Resources

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.auth_resource_dto import AuthResourceDto
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
    api_instance = pyCZERTAINLY.AuthenticationManagementApi(api_client)

    try:
        # Get Auth Resources
        api_response = api_instance.get_auth_resources()
        print("The response of AuthenticationManagementApi->get_auth_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->get_auth_resources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AuthResourceDto]**](AuthResourceDto.md)

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
**200** | Resources retrieved successfully |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects_for_resource**
> List[NameAndUuidDto] get_objects_for_resource(resource_name)

Get List of objects for Object Access

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.name_and_uuid_dto import NameAndUuidDto
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
    api_instance = pyCZERTAINLY.AuthenticationManagementApi(api_client)
    resource_name = pyCZERTAINLY.Resource() # Resource | Resource Name

    try:
        # Get List of objects for Object Access
        api_response = api_instance.get_objects_for_resource(resource_name)
        print("The response of AuthenticationManagementApi->get_objects_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->get_objects_for_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | [**Resource**](.md)| Resource Name | 

### Return type

[**List[NameAndUuidDto]**](NameAndUuidDto.md)

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
**200** | Objects retrieved |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> UserDetailDto profile()

Profile Authorization

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.user_detail_dto import UserDetailDto
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
    api_instance = pyCZERTAINLY.AuthenticationManagementApi(api_client)

    try:
        # Profile Authorization
        api_response = api_instance.profile()
        print("The response of AuthenticationManagementApi->profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDetailDto**](UserDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Authenticate a user |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> UserDetailDto update_user_profile(update_user_request_dto)

Update User Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.update_user_request_dto import UpdateUserRequestDto
from pyCZERTAINLY.models.user_detail_dto import UserDetailDto
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
    api_instance = pyCZERTAINLY.AuthenticationManagementApi(api_client)
    update_user_request_dto = pyCZERTAINLY.UpdateUserRequestDto() # UpdateUserRequestDto | 

    try:
        # Update User Profile
        api_response = api_instance.update_user_profile(update_user_request_dto)
        print("The response of AuthenticationManagementApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationManagementApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request_dto** | [**UpdateUserRequestDto**](UpdateUserRequestDto.md)|  | 

### Return type

[**UserDetailDto**](UserDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Authenticate a user |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

