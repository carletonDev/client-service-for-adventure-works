# swagger_client.ErrorLogsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_error_log**](ErrorLogsApi.md#delete_error_log) | **DELETE** /api/ErrorLogs/{id} | 
[**get_error_log**](ErrorLogsApi.md#get_error_log) | **GET** /api/ErrorLogs | 
[**get_error_log_0**](ErrorLogsApi.md#get_error_log_0) | **GET** /api/ErrorLogs/{id} | 
[**post_error_log**](ErrorLogsApi.md#post_error_log) | **POST** /api/ErrorLogs | 
[**put_error_log**](ErrorLogsApi.md#put_error_log) | **PUT** /api/ErrorLogs/{id} | 


# **delete_error_log**
> delete_error_log(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ErrorLogsApi()
id = 56 # int | 

try:
    api_instance.delete_error_log(id)
except ApiException as e:
    print("Exception when calling ErrorLogsApi->delete_error_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_error_log**
> list[ErrorLog] get_error_log()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ErrorLogsApi()

try:
    api_response = api_instance.get_error_log()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorLogsApi->get_error_log: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ErrorLog]**](ErrorLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_error_log_0**
> get_error_log_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ErrorLogsApi()
id = 56 # int | 

try:
    api_instance.get_error_log_0(id)
except ApiException as e:
    print("Exception when calling ErrorLogsApi->get_error_log_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_error_log**
> post_error_log(error_log=error_log)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ErrorLogsApi()
error_log = swagger_client.ErrorLog() # ErrorLog |  (optional)

try:
    api_instance.post_error_log(error_log=error_log)
except ApiException as e:
    print("Exception when calling ErrorLogsApi->post_error_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_log** | [**ErrorLog**](ErrorLog.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_error_log**
> put_error_log(id, error_log=error_log)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ErrorLogsApi()
id = 56 # int | 
error_log = swagger_client.ErrorLog() # ErrorLog |  (optional)

try:
    api_instance.put_error_log(id, error_log=error_log)
except ApiException as e:
    print("Exception when calling ErrorLogsApi->put_error_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **error_log** | [**ErrorLog**](ErrorLog.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

