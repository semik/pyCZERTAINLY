# pyCZERTAINLY.RoleManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_permission_objects**](RoleManagementApi.md#add_resource_permission_objects) | **POST** /v1/roles/{roleUuid}/permissions/{resourceUuid}/objects | Add Resource Objects to a Role
[**create_role**](RoleManagementApi.md#create_role) | **POST** /v1/roles | Create Role
[**delete_role**](RoleManagementApi.md#delete_role) | **DELETE** /v1/roles/{roleUuid} | Delete Role
[**get_resource_permission_objects**](RoleManagementApi.md#get_resource_permission_objects) | **GET** /v1/roles/{roleUuid}/permissions/{resourceUuid}/objects | Get Resource Objects of a Role
[**get_role**](RoleManagementApi.md#get_role) | **GET** /v1/roles/{roleUuid} | Get role details
[**get_role_permissions**](RoleManagementApi.md#get_role_permissions) | **GET** /v1/roles/{roleUuid}/permissions | Get Permissions of a Role
[**get_role_resource_permissions**](RoleManagementApi.md#get_role_resource_permissions) | **GET** /v1/roles/{roleUuid}/permissions/{resourceUuid} | Get Resources of a Role
[**get_role_users**](RoleManagementApi.md#get_role_users) | **GET** /v1/roles/{roleUuid}/users | Get Role Users
[**list_roles**](RoleManagementApi.md#list_roles) | **GET** /v1/roles | List Roles
[**remove_resource_permission_objects**](RoleManagementApi.md#remove_resource_permission_objects) | **DELETE** /v1/roles/{roleUuid}/permissions/{resourceUuid}/objects/{objectUuid} | Update Resource Objects to a Role
[**save_permissions**](RoleManagementApi.md#save_permissions) | **POST** /v1/roles/{roleUuid}/permissions | Add permissions to Role
[**update_resource_permission_objects**](RoleManagementApi.md#update_resource_permission_objects) | **PUT** /v1/roles/{roleUuid}/permissions/{resourceUuid}/objects/{objectUuid} | Update Resource Objects to a Role
[**update_role**](RoleManagementApi.md#update_role) | **PUT** /v1/roles/{roleUuid} | Update Role
[**update_users**](RoleManagementApi.md#update_users) | **PATCH** /v1/roles/{roleUuid}/users | Add users to Role


# **add_resource_permission_objects**
> add_resource_permission_objects(role_uuid, resource_uuid, object_permissions_request_dto)

Add Resource Objects to a Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.object_permissions_request_dto import ObjectPermissionsRequestDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    resource_uuid = 'resource_uuid_example' # str | Resource UUID
    object_permissions_request_dto = [pyCZERTAINLY.ObjectPermissionsRequestDto()] # List[ObjectPermissionsRequestDto] | 

    try:
        # Add Resource Objects to a Role
        api_instance.add_resource_permission_objects(role_uuid, resource_uuid, object_permissions_request_dto)
    except Exception as e:
        print("Exception when calling RoleManagementApi->add_resource_permission_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **resource_uuid** | **str**| Resource UUID | 
 **object_permissions_request_dto** | [**List[ObjectPermissionsRequestDto]**](ObjectPermissionsRequestDto.md)|  | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Resource Objects added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleDetailDto create_role(role_request_dto)

Create Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_detail_dto import RoleDetailDto
from pyCZERTAINLY.models.role_request_dto import RoleRequestDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_request_dto = pyCZERTAINLY.RoleRequestDto() # RoleRequestDto | 

    try:
        # Create Role
        api_response = api_instance.create_role(role_request_dto)
        print("The response of RoleManagementApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_request_dto** | [**RoleRequestDto**](RoleRequestDto.md)|  | 

### Return type

[**RoleDetailDto**](RoleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Role created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_uuid)

Delete Role

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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Delete Role
        api_instance.delete_role(role_uuid)
    except Exception as e:
        print("Exception when calling RoleManagementApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 

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
**403** | Forbidden |  -  |
**204** | Role deleted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_permission_objects**
> List[ObjectPermissionsDto] get_resource_permission_objects(role_uuid, resource_uuid)

Get Resource Objects of a Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.object_permissions_dto import ObjectPermissionsDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    resource_uuid = 'resource_uuid_example' # str | Resource UUID

    try:
        # Get Resource Objects of a Role
        api_response = api_instance.get_resource_permission_objects(role_uuid, resource_uuid)
        print("The response of RoleManagementApi->get_resource_permission_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->get_resource_permission_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **resource_uuid** | **str**| Resource UUID | 

### Return type

[**List[ObjectPermissionsDto]**](ObjectPermissionsDto.md)

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
**200** | Resource Objects retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleDetailDto get_role(role_uuid)

Get role details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_detail_dto import RoleDetailDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Get role details
        api_response = api_instance.get_role(role_uuid)
        print("The response of RoleManagementApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 

### Return type

[**RoleDetailDto**](RoleDetailDto.md)

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
**200** | Role details retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions**
> SubjectPermissionsDto get_role_permissions(role_uuid)

Get Permissions of a Role

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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Get Permissions of a Role
        api_response = api_instance.get_role_permissions(role_uuid)
        print("The response of RoleManagementApi->get_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->get_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Role permissions retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_resource_permissions**
> ResourcePermissionsDto get_role_resource_permissions(role_uuid, resource_uuid)

Get Resources of a Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.resource_permissions_dto import ResourcePermissionsDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    resource_uuid = 'resource_uuid_example' # str | Resource UUID

    try:
        # Get Resources of a Role
        api_response = api_instance.get_role_resource_permissions(role_uuid, resource_uuid)
        print("The response of RoleManagementApi->get_role_resource_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->get_role_resource_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **resource_uuid** | **str**| Resource UUID | 

### Return type

[**ResourcePermissionsDto**](ResourcePermissionsDto.md)

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
**200** | Role resources retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_users**
> List[UserDto] get_role_users(role_uuid)

Get Role Users

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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID

    try:
        # Get Role Users
        api_response = api_instance.get_role_users(role_uuid)
        print("The response of RoleManagementApi->get_role_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->get_role_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 

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
**200** | Role users retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> List[RoleDto] list_roles()

List Roles

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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)

    try:
        # List Roles
        api_response = api_instance.list_roles()
        print("The response of RoleManagementApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->list_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | List of roles fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_resource_permission_objects**
> remove_resource_permission_objects(role_uuid, resource_uuid, object_uuid)

Update Resource Objects to a Role

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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    resource_uuid = 'resource_uuid_example' # str | Resource UUID
    object_uuid = 'object_uuid_example' # str | Object UUID

    try:
        # Update Resource Objects to a Role
        api_instance.remove_resource_permission_objects(role_uuid, resource_uuid, object_uuid)
    except Exception as e:
        print("Exception when calling RoleManagementApi->remove_resource_permission_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **resource_uuid** | **str**| Resource UUID | 
 **object_uuid** | **str**| Object UUID | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Resource Objects added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_permissions**
> SubjectPermissionsDto save_permissions(role_uuid, role_permissions_request_dto)

Add permissions to Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_permissions_request_dto import RolePermissionsRequestDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    role_permissions_request_dto = pyCZERTAINLY.RolePermissionsRequestDto() # RolePermissionsRequestDto | 

    try:
        # Add permissions to Role
        api_response = api_instance.save_permissions(role_uuid, role_permissions_request_dto)
        print("The response of RoleManagementApi->save_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->save_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **role_permissions_request_dto** | [**RolePermissionsRequestDto**](RolePermissionsRequestDto.md)|  | 

### Return type

[**SubjectPermissionsDto**](SubjectPermissionsDto.md)

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

# **update_resource_permission_objects**
> update_resource_permission_objects(role_uuid, resource_uuid, object_uuid, object_permissions_request_dto)

Update Resource Objects to a Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.object_permissions_request_dto import ObjectPermissionsRequestDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    resource_uuid = 'resource_uuid_example' # str | Resource UUID
    object_uuid = 'object_uuid_example' # str | Object UUID
    object_permissions_request_dto = pyCZERTAINLY.ObjectPermissionsRequestDto() # ObjectPermissionsRequestDto | 

    try:
        # Update Resource Objects to a Role
        api_instance.update_resource_permission_objects(role_uuid, resource_uuid, object_uuid, object_permissions_request_dto)
    except Exception as e:
        print("Exception when calling RoleManagementApi->update_resource_permission_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **resource_uuid** | **str**| Resource UUID | 
 **object_uuid** | **str**| Object UUID | 
 **object_permissions_request_dto** | [**ObjectPermissionsRequestDto**](ObjectPermissionsRequestDto.md)|  | 

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
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Resource Objects added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleDetailDto update_role(role_uuid, role_request_dto)

Update Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_detail_dto import RoleDetailDto
from pyCZERTAINLY.models.role_request_dto import RoleRequestDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    role_request_dto = pyCZERTAINLY.RoleRequestDto() # RoleRequestDto | 

    try:
        # Update Role
        api_response = api_instance.update_role(role_uuid, role_request_dto)
        print("The response of RoleManagementApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **role_request_dto** | [**RoleRequestDto**](RoleRequestDto.md)|  | 

### Return type

[**RoleDetailDto**](RoleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Role details updated |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> RoleDetailDto update_users(role_uuid, request_body)

Add users to Role

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.role_detail_dto import RoleDetailDto
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
    api_instance = pyCZERTAINLY.RoleManagementApi(api_client)
    role_uuid = 'role_uuid_example' # str | Role UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | User UUIDs

    try:
        # Add users to Role
        api_response = api_instance.update_users(role_uuid, request_body)
        print("The response of RoleManagementApi->update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleManagementApi->update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_uuid** | **str**| Role UUID | 
 **request_body** | [**List[str]**](str.md)| User UUIDs | 

### Return type

[**RoleDetailDto**](RoleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Role users updated |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

