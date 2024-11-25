# openapi_client.WorkflowRulesManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_condition**](WorkflowRulesManagementApi.md#create_condition) | **POST** /v1/workflows/conditions | Create Condition
[**create_rule**](WorkflowRulesManagementApi.md#create_rule) | **POST** /v1/workflows/rules | Create Rule
[**delete_condition**](WorkflowRulesManagementApi.md#delete_condition) | **DELETE** /v1/workflows/conditions/{conditionUuid} | Delete Condition
[**delete_rule**](WorkflowRulesManagementApi.md#delete_rule) | **DELETE** /v1/workflows/rules/{ruleUuid} | Delete Rule
[**get_condition**](WorkflowRulesManagementApi.md#get_condition) | **GET** /v1/workflows/conditions/{conditionUuid} | Get Condition details
[**get_rule**](WorkflowRulesManagementApi.md#get_rule) | **GET** /v1/workflows/rules/{ruleUuid} | Get Rule details
[**list_conditions**](WorkflowRulesManagementApi.md#list_conditions) | **GET** /v1/workflows/conditions | List Conditions
[**list_rules**](WorkflowRulesManagementApi.md#list_rules) | **GET** /v1/workflows/rules | List Rules
[**update_condition**](WorkflowRulesManagementApi.md#update_condition) | **PUT** /v1/workflows/conditions/{conditionUuid} | Update Condition
[**update_rule**](WorkflowRulesManagementApi.md#update_rule) | **PUT** /v1/workflows/rules/{ruleUuid} | Update Rule


# **create_condition**
> ConditionDto create_condition(condition_request_dto)

Create Condition

### Example


```python
import openapi_client
from openapi_client.models.condition_dto import ConditionDto
from openapi_client.models.condition_request_dto import ConditionRequestDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    condition_request_dto = openapi_client.ConditionRequestDto() # ConditionRequestDto | 

    try:
        # Create Condition
        api_response = api_instance.create_condition(condition_request_dto)
        print("The response of WorkflowRulesManagementApi->create_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->create_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_request_dto** | [**ConditionRequestDto**](ConditionRequestDto.md)|  | 

### Return type

[**ConditionDto**](ConditionDto.md)

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
**201** | Condition created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> RuleDetailDto create_rule(rule_request_dto)

Create Rule

### Example


```python
import openapi_client
from openapi_client.models.rule_detail_dto import RuleDetailDto
from openapi_client.models.rule_request_dto import RuleRequestDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    rule_request_dto = openapi_client.RuleRequestDto() # RuleRequestDto | 

    try:
        # Create Rule
        api_response = api_instance.create_rule(rule_request_dto)
        print("The response of WorkflowRulesManagementApi->create_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->create_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_request_dto** | [**RuleRequestDto**](RuleRequestDto.md)|  | 

### Return type

[**RuleDetailDto**](RuleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**201** | Rule created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_condition**
> delete_condition(condition_uuid)

Delete Condition

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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    condition_uuid = 'condition_uuid_example' # str | Condition UUID

    try:
        # Delete Condition
        api_instance.delete_condition(condition_uuid)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->delete_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_uuid** | **str**| Condition UUID | 

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
**204** | Condition deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(rule_uuid)

Delete Rule

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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    rule_uuid = 'rule_uuid_example' # str | Rule UUID

    try:
        # Delete Rule
        api_instance.delete_rule(rule_uuid)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->delete_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_uuid** | **str**| Rule UUID | 

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
**204** | Rule deleted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_condition**
> ConditionDto get_condition(condition_uuid)

Get Condition details

### Example


```python
import openapi_client
from openapi_client.models.condition_dto import ConditionDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    condition_uuid = 'condition_uuid_example' # str | Condition UUID

    try:
        # Get Condition details
        api_response = api_instance.get_condition(condition_uuid)
        print("The response of WorkflowRulesManagementApi->get_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->get_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_uuid** | **str**| Condition UUID | 

### Return type

[**ConditionDto**](ConditionDto.md)

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
**200** | Condition details retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> RuleDetailDto get_rule(rule_uuid)

Get Rule details

### Example


```python
import openapi_client
from openapi_client.models.rule_detail_dto import RuleDetailDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    rule_uuid = 'rule_uuid_example' # str | Rule UUID

    try:
        # Get Rule details
        api_response = api_instance.get_rule(rule_uuid)
        print("The response of WorkflowRulesManagementApi->get_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->get_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_uuid** | **str**| Rule UUID | 

### Return type

[**RuleDetailDto**](RuleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Rule details retrieved |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conditions**
> List[ConditionDto] list_conditions(resource=resource)

List Conditions

### Example


```python
import openapi_client
from openapi_client.models.condition_dto import ConditionDto
from openapi_client.models.resource import Resource
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    resource = openapi_client.Resource() # Resource |  (optional)

    try:
        # List Conditions
        api_response = api_instance.list_conditions(resource=resource)
        print("The response of WorkflowRulesManagementApi->list_conditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->list_conditions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)|  | [optional] 

### Return type

[**List[ConditionDto]**](ConditionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | List of conditions fetched |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rules**
> List[RuleDto] list_rules(resource=resource)

List Rules

### Example


```python
import openapi_client
from openapi_client.models.resource import Resource
from openapi_client.models.rule_dto import RuleDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    resource = openapi_client.Resource() # Resource |  (optional)

    try:
        # List Rules
        api_response = api_instance.list_rules(resource=resource)
        print("The response of WorkflowRulesManagementApi->list_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->list_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)|  | [optional] 

### Return type

[**List[RuleDto]**](RuleDto.md)

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
**200** | List of rules fetched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_condition**
> ConditionDto update_condition(condition_uuid, update_condition_request_dto)

Update Condition

### Example


```python
import openapi_client
from openapi_client.models.condition_dto import ConditionDto
from openapi_client.models.update_condition_request_dto import UpdateConditionRequestDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    condition_uuid = 'condition_uuid_example' # str | Condition UUID
    update_condition_request_dto = openapi_client.UpdateConditionRequestDto() # UpdateConditionRequestDto | 

    try:
        # Update Condition
        api_response = api_instance.update_condition(condition_uuid, update_condition_request_dto)
        print("The response of WorkflowRulesManagementApi->update_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->update_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **condition_uuid** | **str**| Condition UUID | 
 **update_condition_request_dto** | [**UpdateConditionRequestDto**](UpdateConditionRequestDto.md)|  | 

### Return type

[**ConditionDto**](ConditionDto.md)

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
**200** | Condition updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleDetailDto update_rule(rule_uuid, update_rule_request_dto)

Update Rule

### Example


```python
import openapi_client
from openapi_client.models.rule_detail_dto import RuleDetailDto
from openapi_client.models.update_rule_request_dto import UpdateRuleRequestDto
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
    api_instance = openapi_client.WorkflowRulesManagementApi(api_client)
    rule_uuid = 'rule_uuid_example' # str | Rule UUID
    update_rule_request_dto = openapi_client.UpdateRuleRequestDto() # UpdateRuleRequestDto | 

    try:
        # Update Rule
        api_response = api_instance.update_rule(rule_uuid, update_rule_request_dto)
        print("The response of WorkflowRulesManagementApi->update_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowRulesManagementApi->update_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_uuid** | **str**| Rule UUID | 
 **update_rule_request_dto** | [**UpdateRuleRequestDto**](UpdateRuleRequestDto.md)|  | 

### Return type

[**RuleDetailDto**](RuleDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Rule details updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

