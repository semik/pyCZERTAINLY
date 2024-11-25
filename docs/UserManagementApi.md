# pyCZERTAINLY.UserManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](UserManagementApi.md#add_role) | **PUT** /v1/users/{userUuid}/roles/{roleUuid} | Add role to User
[**create_user**](UserManagementApi.md#create_user) | **POST** /v1/users | Create User
[**delete_user**](UserManagementApi.md#delete_user) | **DELETE** /v1/users/{userUuid} | Delete User
[**disable_user**](UserManagementApi.md#disable_user) | **PATCH** /v1/users/{userUuid}/disable | Disable User
[**enable_user**](UserManagementApi.md#enable_user) | **PATCH** /v1/users/{userUuid}/enable | Enable User
[**get_permissions**](UserManagementApi.md#get_permissions) | **GET** /v1/users/{userUuid}/permissions | Get User permissions
[**get_user**](UserManagementApi.md#get_user) | **GET** /v1/users/{userUuid} | Get user details
[**get_user_roles**](UserManagementApi.md#get_user_roles) | **GET** /v1/users/{userUuid}/roles | Get User Roles
[**identify_user**](UserManagementApi.md#identify_user) | **POST** /v1/users/identify | Identify User
[**list_users**](UserManagementApi.md#list_users) | **GET** /v1/users | List Users
[**remove_role**](UserManagementApi.md#remove_role) | **DELETE** /v1/users/{userUuid}/roles/{roleUuid} | Remove role from User
[**update_roles**](UserManagementApi.md#update_roles) | **PATCH** /v1/users/{userUuid}/roles | Add roles to User
[**update_user**](UserManagementApi.md#update_user) | **PUT** /v1/users/{userUuid} | Update User


# **add_role**
> UserDetailDto add_role(user_uuid, role_uuid)

Add role to User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Add role to User
        api_response = api_instance.add_role(user_uuid, role_uuid)
        print("The response of UserManagementApi->add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 
 **role_uuid** | **str**| Role UUID | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | User roles updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserDetailDto create_user(add_user_request_dto)

Create User

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.add_user_request_dto import AddUserRequestDto
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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    add_user_request_dto = pyCZERTAINLY.AddUserRequestDto() # AddUserRequestDto | 

    try:
        # Create User
        api_response = api_instance.create_user(add_user_request_dto)
        print("The response of UserManagementApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request_dto** | [**AddUserRequestDto**](AddUserRequestDto.md)|  | 

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
**201** | User details retrieved |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_uuid)

Delete User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Delete User
        api_instance.delete_user(user_uuid)
    except Exception as e:
        print("Exception when calling UserManagementApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

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
**204** | User deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_user**
> UserDetailDto disable_user(user_uuid)

Disable User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Disable User
        api_response = api_instance.disable_user(user_uuid)
        print("The response of UserManagementApi->disable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->disable_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

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
**200** | User disabled |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user**
> UserDetailDto enable_user(user_uuid)

Enable User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Enable User
        api_response = api_instance.enable_user(user_uuid)
        print("The response of UserManagementApi->enable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->enable_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

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
**200** | User enabled |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> SubjectPermissionsDto get_permissions(user_uuid)

Get User permissions

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.subject_permissions_dto import SubjectPermissionsDto
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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Get User permissions
        api_response = api_instance.get_permissions(user_uuid)
        print("The response of UserManagementApi->get_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

### Return type

[**SubjectPermissionsDto**](SubjectPermissionsDto.md)

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
**200** | User permissions removed |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetailDto get_user(user_uuid)

Get user details

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Get user details
        api_response = api_instance.get_user(user_uuid)
        print("The response of UserManagementApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

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
**403** | Forbidden |  -  |
**200** | User details retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> List[RoleDto] get_user_roles(user_uuid)

Get User Roles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_dto import RoleDto
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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID

    try:
        # Get User Roles
        api_response = api_instance.get_user_roles(user_uuid)
        print("The response of UserManagementApi->get_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 

### Return type

[**List[RoleDto]**](RoleDto.md)

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
**200** | User roles retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_user**
> UserDetailDto identify_user(user_identification_request_dto)

Identify User

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.user_detail_dto import UserDetailDto
from pyCZERTAINLY.models.user_identification_request_dto import UserIdentificationRequestDto
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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_identification_request_dto = pyCZERTAINLY.UserIdentificationRequestDto() # UserIdentificationRequestDto | 

    try:
        # Identify User
        api_response = api_instance.identify_user(user_identification_request_dto)
        print("The response of UserManagementApi->identify_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->identify_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_identification_request_dto** | [**UserIdentificationRequestDto**](UserIdentificationRequestDto.md)|  | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | User identified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> List[UserDto] list_users()

List Users

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.user_dto import UserDto
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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)

    try:
        # List Users
        api_response = api_instance.list_users()
        print("The response of UserManagementApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserDto]**](UserDto.md)

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
**200** | List of users fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role**
> UserDetailDto remove_role(user_uuid, role_uuid)

Remove role from User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Remove role from User
        api_response = api_instance.remove_role(user_uuid, role_uuid)
        print("The response of UserManagementApi->remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 
 **role_uuid** | **str**| Role UUID | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | User roles removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_roles**
> UserDetailDto update_roles(user_uuid, request_body)

Add roles to User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Role UUIDs

    try:
        # Add roles to User
        api_response = api_instance.update_roles(user_uuid, request_body)
        print("The response of UserManagementApi->update_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->update_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 
 **request_body** | [**List[str]**](str.md)| Role UUIDs | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | User roles updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> UserDetailDto update_user(user_uuid, update_user_request_dto)

Update User

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
    api_instance = pyCZERTAINLY.UserManagementApi(api_client)
    user_uuid = 'user_uuid_example' # str | User UUID
    update_user_request_dto = pyCZERTAINLY.UpdateUserRequestDto() # UpdateUserRequestDto | 

    try:
        # Update User
        api_response = api_instance.update_user(user_uuid, update_user_request_dto)
        print("The response of UserManagementApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| User UUID | 
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
**200** | User details updated |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

