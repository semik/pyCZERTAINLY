# pyCZERTAINLY.CertificateInventoryApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_certificate**](CertificateInventoryApi.md#bulk_delete_certificate) | **POST** /v1/certificates/delete | Delete multiple certificates
[**bulk_update_certificate_objects**](CertificateInventoryApi.md#bulk_update_certificate_objects) | **PATCH** /v1/certificates | Update Group and/or Owner for multiple Certificates
[**check_certificates_compliance**](CertificateInventoryApi.md#check_certificates_compliance) | **POST** /v1/certificates/compliance | Initiate Certificate Compliance Check
[**delete_certificate**](CertificateInventoryApi.md#delete_certificate) | **DELETE** /v1/certificates/{uuid} | Delete a certificate
[**download_certificate**](CertificateInventoryApi.md#download_certificate) | **GET** /v1/certificates/{uuid}/{certificateFormat} | Download Certificate
[**download_certificate_chain**](CertificateInventoryApi.md#download_certificate_chain) | **GET** /v1/certificates/{uuid}/chain/{certificateFormat} | Download Certificate Chain in chosen format
[**get_certificate**](CertificateInventoryApi.md#get_certificate) | **GET** /v1/certificates/{uuid} | Get Certificate Details
[**get_certificate_chain**](CertificateInventoryApi.md#get_certificate_chain) | **GET** /v1/certificates/{uuid}/chain | Get certificate chain
[**get_certificate_content**](CertificateInventoryApi.md#get_certificate_content) | **POST** /v1/certificates/content | Get Certificate Content
[**get_certificate_event_history**](CertificateInventoryApi.md#get_certificate_event_history) | **GET** /v1/certificates/{uuid}/history | Get Certificate event history
[**get_certificate_validation_result**](CertificateInventoryApi.md#get_certificate_validation_result) | **GET** /v1/certificates/{uuid}/validate | Get Certificate Validation Result
[**get_csr_generation_attributes**](CertificateInventoryApi.md#get_csr_generation_attributes) | **GET** /v1/certificates/csr/attributes | Get CSR Generation Attributes
[**get_searchable_field_information4**](CertificateInventoryApi.md#get_searchable_field_information4) | **GET** /v1/certificates/search | Get Certificate searchable fields information
[**list_certificate_approvals**](CertificateInventoryApi.md#list_certificate_approvals) | **GET** /v1/certificates/{uuid}/approvals | List Certificates Approvals
[**list_certificate_locations**](CertificateInventoryApi.md#list_certificate_locations) | **GET** /v1/certificates/{certificateUuid}/locations | List of available Locations for the Certificate
[**list_certificates**](CertificateInventoryApi.md#list_certificates) | **POST** /v1/certificates | List Certificates
[**submit_certificate_request**](CertificateInventoryApi.md#submit_certificate_request) | **POST** /v1/certificates/create | Submit certificate request
[**update_certificate_objects**](CertificateInventoryApi.md#update_certificate_objects) | **PATCH** /v1/certificates/{uuid} | Update Certificate Objects
[**upload**](CertificateInventoryApi.md#upload) | **POST** /v1/certificates/upload | Upload a new Certificate


# **bulk_delete_certificate**
> BulkOperationResponse bulk_delete_certificate(remove_certificate_dto)

Delete multiple certificates

In this operation, when the list of Certificate UUIDs are provided and the filter is left as null or undefined, then the change will be applied only to the list of Certificate UUIDs provided. When the filter is provided in the request, the list of UUIDs will be ignored and the change will be applied for the all the certificates that matches the filter criteria. To apply this change for all the Certificates in the inventory, provide an empty array \"[]\" for the value of \"filters\" in the request body

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.bulk_operation_response import BulkOperationResponse
from pyCZERTAINLY.models.remove_certificate_dto import RemoveCertificateDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    remove_certificate_dto = pyCZERTAINLY.RemoveCertificateDto() # RemoveCertificateDto | 

    try:
        # Delete multiple certificates
        api_response = api_instance.bulk_delete_certificate(remove_certificate_dto)
        print("The response of CertificateInventoryApi->bulk_delete_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->bulk_delete_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_certificate_dto** | [**RemoveCertificateDto**](RemoveCertificateDto.md)|  | 

### Return type

[**BulkOperationResponse**](BulkOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificates deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**501** | Certificate objects delete by filters not supported |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_certificate_objects**
> bulk_update_certificate_objects(multiple_certificate_object_update_dto)

Update Group and/or Owner for multiple Certificates

In this operation, when the list of Certificate UUIDs are provided and the filter is left as null or undefined, then the change will be applied only to the list of Certificate UUIDs provided. When the filter is provided in the request, the list of UUIDs will be ignored and the change will be applied for the all the certificates that matches the filter criteria. To apply this change for all the Certificates in the inventory, provide an empty array \"[]\" for the value of \"filters\" in the request body

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.multiple_certificate_object_update_dto import MultipleCertificateObjectUpdateDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    multiple_certificate_object_update_dto = pyCZERTAINLY.MultipleCertificateObjectUpdateDto() # MultipleCertificateObjectUpdateDto | 

    try:
        # Update Group and/or Owner for multiple Certificates
        api_instance.bulk_update_certificate_objects(multiple_certificate_object_update_dto)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->bulk_update_certificate_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_certificate_object_update_dto** | [**MultipleCertificateObjectUpdateDto**](MultipleCertificateObjectUpdateDto.md)|  | 

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
**200** | Certificate objects updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**501** | Certificate objects update by filters not supported |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_certificates_compliance**
> check_certificates_compliance(certificate_compliance_check_dto)

Initiate Certificate Compliance Check

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_compliance_check_dto import CertificateComplianceCheckDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    certificate_compliance_check_dto = pyCZERTAINLY.CertificateComplianceCheckDto() # CertificateComplianceCheckDto | 

    try:
        # Initiate Certificate Compliance Check
        api_instance.check_certificates_compliance(certificate_compliance_check_dto)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->check_certificates_compliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_compliance_check_dto** | [**CertificateComplianceCheckDto**](CertificateComplianceCheckDto.md)|  | 

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
**204** | Compliance check initiated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate**
> delete_certificate(uuid)

Delete a certificate

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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID

    try:
        # Delete a certificate
        api_instance.delete_certificate(uuid)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->delete_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 

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
**204** | Certificate deleted |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_certificate**
> CertificateDownloadResponseDto download_certificate(uuid, certificate_format, encoding)

Download Certificate

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_download_response_dto import CertificateDownloadResponseDto
from pyCZERTAINLY.models.certificate_format import CertificateFormat
from pyCZERTAINLY.models.certificate_format_encoding import CertificateFormatEncoding
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID
    certificate_format = pyCZERTAINLY.CertificateFormat() # CertificateFormat | Certificate format
    encoding = pyCZERTAINLY.CertificateFormatEncoding() # CertificateFormatEncoding | 

    try:
        # Download Certificate
        api_response = api_instance.download_certificate(uuid, certificate_format, encoding)
        print("The response of CertificateInventoryApi->download_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->download_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 
 **certificate_format** | [**CertificateFormat**](.md)| Certificate format | 
 **encoding** | [**CertificateFormatEncoding**](.md)|  | 

### Return type

[**CertificateDownloadResponseDto**](CertificateDownloadResponseDto.md)

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
**200** | Certificate downloaded |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_certificate_chain**
> CertificateChainDownloadResponseDto download_certificate_chain(uuid, certificate_format, encoding, with_end_certificate=with_end_certificate)

Download Certificate Chain in chosen format

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_chain_download_response_dto import CertificateChainDownloadResponseDto
from pyCZERTAINLY.models.certificate_format import CertificateFormat
from pyCZERTAINLY.models.certificate_format_encoding import CertificateFormatEncoding
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID
    certificate_format = pyCZERTAINLY.CertificateFormat() # CertificateFormat | Certificate format
    encoding = pyCZERTAINLY.CertificateFormatEncoding() # CertificateFormatEncoding | 
    with_end_certificate = True # bool |  (optional)

    try:
        # Download Certificate Chain in chosen format
        api_response = api_instance.download_certificate_chain(uuid, certificate_format, encoding, with_end_certificate=with_end_certificate)
        print("The response of CertificateInventoryApi->download_certificate_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->download_certificate_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 
 **certificate_format** | [**CertificateFormat**](.md)| Certificate format | 
 **encoding** | [**CertificateFormatEncoding**](.md)|  | 
 **with_end_certificate** | **bool**|  | [optional] 

### Return type

[**CertificateChainDownloadResponseDto**](CertificateChainDownloadResponseDto.md)

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
**200** | Chain certificates downloaded |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> CertificateDetailDto get_certificate(uuid)

Get Certificate Details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_detail_dto import CertificateDetailDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID

    try:
        # Get Certificate Details
        api_response = api_instance.get_certificate(uuid)
        print("The response of CertificateInventoryApi->get_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 

### Return type

[**CertificateDetailDto**](CertificateDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate detail retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_chain**
> CertificateChainResponseDto get_certificate_chain(uuid, with_end_certificate=with_end_certificate)

Get certificate chain

Get certificate chain for the certificate with the given UUID. The certificate chain is returned in the order of the chain, with the first certificate being the certificate with the given UUID, up to the last identified certificate in the chain. If the certificate with the given UUID has status `NEW` or `REJECTED`, an empty list is returned.

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_chain_response_dto import CertificateChainResponseDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID
    with_end_certificate = True # bool |  (optional)

    try:
        # Get certificate chain
        api_response = api_instance.get_certificate_chain(uuid, with_end_certificate=with_end_certificate)
        print("The response of CertificateInventoryApi->get_certificate_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_certificate_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 
 **with_end_certificate** | **bool**|  | [optional] 

### Return type

[**CertificateChainResponseDto**](CertificateChainResponseDto.md)

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
**200** | Certificate chain retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_content**
> List[CertificateContentDto] get_certificate_content(request_body)

Get Certificate Content

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_content_dto import CertificateContentDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Certificate UUIDs

    try:
        # Get Certificate Content
        api_response = api_instance.get_certificate_content(request_body)
        print("The response of CertificateInventoryApi->get_certificate_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_certificate_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Certificate UUIDs | 

### Return type

[**List[CertificateContentDto]**](CertificateContentDto.md)

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
**200** | Certificate content retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_event_history**
> List[CertificateEventHistoryDto] get_certificate_event_history(uuid)

Get Certificate event history

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_event_history_dto import CertificateEventHistoryDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID

    try:
        # Get Certificate event history
        api_response = api_instance.get_certificate_event_history(uuid)
        print("The response of CertificateInventoryApi->get_certificate_event_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_certificate_event_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 

### Return type

[**List[CertificateEventHistoryDto]**](CertificateEventHistoryDto.md)

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
**200** | Certificate event history retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_validation_result**
> CertificateValidationResultDto get_certificate_validation_result(uuid)

Get Certificate Validation Result

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_validation_result_dto import CertificateValidationResultDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID

    try:
        # Get Certificate Validation Result
        api_response = api_instance.get_certificate_validation_result(uuid)
        print("The response of CertificateInventoryApi->get_certificate_validation_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_certificate_validation_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 

### Return type

[**CertificateValidationResultDto**](CertificateValidationResultDto.md)

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
**200** | Certificate validation detail retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csr_generation_attributes**
> List[BaseAttributeDto] get_csr_generation_attributes()

Get CSR Generation Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)

    try:
        # Get CSR Generation Attributes
        api_response = api_instance.get_csr_generation_attributes()
        print("The response of CertificateInventoryApi->get_csr_generation_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_csr_generation_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BaseAttributeDto]**](BaseAttributeDto.md)

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
**200** | CSR Generation attributes retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information4**
> List[SearchFieldDataByGroupDto] get_searchable_field_information4()

Get Certificate searchable fields information

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)

    try:
        # Get Certificate searchable fields information
        api_response = api_instance.get_searchable_field_information4()
        print("The response of CertificateInventoryApi->get_searchable_field_information4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->get_searchable_field_information4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SearchFieldDataByGroupDto]**](SearchFieldDataByGroupDto.md)

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
**200** | Certificate searchable field information retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_approvals**
> ApprovalResponseDto list_certificate_approvals(uuid, pagination_request_dto)

List Certificates Approvals

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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID
    pagination_request_dto = pyCZERTAINLY.PaginationRequestDto() # PaginationRequestDto | 

    try:
        # List Certificates Approvals
        api_response = api_instance.list_certificate_approvals(uuid, pagination_request_dto)
        print("The response of CertificateInventoryApi->list_certificate_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->list_certificate_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 
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
**200** | List of all approvals for the certificate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_locations**
> List[LocationDto] list_certificate_locations(certificate_uuid)

List of available Locations for the Certificate

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.location_dto import LocationDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID

    try:
        # List of available Locations for the Certificate
        api_response = api_instance.list_certificate_locations(certificate_uuid)
        print("The response of CertificateInventoryApi->list_certificate_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->list_certificate_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_uuid** | **str**| Certificate UUID | 

### Return type

[**List[LocationDto]**](LocationDto.md)

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
**200** | Locations retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates**
> CertificateResponseDto list_certificates(search_request_dto)

List Certificates

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_response_dto import CertificateResponseDto
from pyCZERTAINLY.models.search_request_dto import SearchRequestDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    search_request_dto = pyCZERTAINLY.SearchRequestDto() # SearchRequestDto | 

    try:
        # List Certificates
        api_response = api_instance.list_certificates(search_request_dto)
        print("The response of CertificateInventoryApi->list_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->list_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**CertificateResponseDto**](CertificateResponseDto.md)

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
**200** | List of all the certificates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_certificate_request**
> CertificateDetailDto submit_certificate_request(client_certificate_request_dto)

Submit certificate request

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_detail_dto import CertificateDetailDto
from pyCZERTAINLY.models.client_certificate_request_dto import ClientCertificateRequestDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    client_certificate_request_dto = pyCZERTAINLY.ClientCertificateRequestDto() # ClientCertificateRequestDto | 

    try:
        # Submit certificate request
        api_response = api_instance.submit_certificate_request(client_certificate_request_dto)
        print("The response of CertificateInventoryApi->submit_certificate_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->submit_certificate_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_certificate_request_dto** | [**ClientCertificateRequestDto**](ClientCertificateRequestDto.md)|  | 

### Return type

[**CertificateDetailDto**](CertificateDetailDto.md)

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
**200** | Certificate request submit, certificate created and ready to be issued |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_objects**
> update_certificate_objects(uuid, certificate_update_objects_dto)

Update Certificate Objects

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_update_objects_dto import CertificateUpdateObjectsDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    uuid = 'uuid_example' # str | Certificate UUID
    certificate_update_objects_dto = pyCZERTAINLY.CertificateUpdateObjectsDto() # CertificateUpdateObjectsDto | 

    try:
        # Update Certificate Objects
        api_instance.update_certificate_objects(uuid, certificate_update_objects_dto)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->update_certificate_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Certificate UUID | 
 **certificate_update_objects_dto** | [**CertificateUpdateObjectsDto**](CertificateUpdateObjectsDto.md)|  | 

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
**204** | Certificate objects updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> UuidDto upload(upload_certificate_request_dto)

Upload a new Certificate

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.upload_certificate_request_dto import UploadCertificateRequestDto
from pyCZERTAINLY.models.uuid_dto import UuidDto
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
    api_instance = pyCZERTAINLY.CertificateInventoryApi(api_client)
    upload_certificate_request_dto = pyCZERTAINLY.UploadCertificateRequestDto() # UploadCertificateRequestDto | 

    try:
        # Upload a new Certificate
        api_response = api_instance.upload(upload_certificate_request_dto)
        print("The response of CertificateInventoryApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateInventoryApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_certificate_request_dto** | [**UploadCertificateRequestDto**](UploadCertificateRequestDto.md)|  | 

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
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**201** | Certificate uploaded |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

