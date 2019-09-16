# swagger_client.AddressesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_address**](AddressesApi.md#delete_address) | **DELETE** /api/Addresses/{id} | 
[**get_address**](AddressesApi.md#get_address) | **GET** /api/Addresses | 
[**get_address_0**](AddressesApi.md#get_address_0) | **GET** /api/Addresses/{id} | 
[**post_address**](AddressesApi.md#post_address) | **POST** /api/Addresses | 
[**put_address**](AddressesApi.md#put_address) | **PUT** /api/Addresses/{id} | 


# **delete_address**
> delete_address(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 56 # int | 

try:
    api_instance.delete_address(id)
except ApiException as e:
    print("Exception when calling AddressesApi->delete_address: %s\n" % e)
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

# **get_address**
> list[Address] get_address()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()

try:
    api_response = api_instance.get_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Address]**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_0**
> get_address_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 56 # int | 

try:
    api_instance.get_address_0(id)
except ApiException as e:
    print("Exception when calling AddressesApi->get_address_0: %s\n" % e)
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

# **post_address**
> post_address(address=address)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
address = swagger_client.Address() # Address |  (optional)

try:
    api_instance.post_address(address=address)
except ApiException as e:
    print("Exception when calling AddressesApi->post_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](Address.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_address**
> put_address(id, address=address)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddressesApi()
id = 56 # int | 
address = swagger_client.Address() # Address |  (optional)

try:
    api_instance.put_address(id, address=address)
except ApiException as e:
    print("Exception when calling AddressesApi->put_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **address** | [**Address**](Address.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

