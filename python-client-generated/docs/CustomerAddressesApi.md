# swagger_client.CustomerAddressesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_address**](CustomerAddressesApi.md#delete_customer_address) | **DELETE** /api/CustomerAddresses/{id} | 
[**get_customer_address**](CustomerAddressesApi.md#get_customer_address) | **GET** /api/CustomerAddresses | 
[**get_customer_address_0**](CustomerAddressesApi.md#get_customer_address_0) | **GET** /api/CustomerAddresses/{id} | 
[**post_customer_address**](CustomerAddressesApi.md#post_customer_address) | **POST** /api/CustomerAddresses | 
[**put_customer_address**](CustomerAddressesApi.md#put_customer_address) | **PUT** /api/CustomerAddresses/{id} | 


# **delete_customer_address**
> delete_customer_address(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressesApi()
id = 56 # int | 

try:
    api_instance.delete_customer_address(id)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->delete_customer_address: %s\n" % e)
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

# **get_customer_address**
> list[CustomerAddress] get_customer_address()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressesApi()

try:
    api_response = api_instance.get_customer_address()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->get_customer_address: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomerAddress]**](CustomerAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_address_0**
> get_customer_address_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressesApi()
id = 56 # int | 

try:
    api_instance.get_customer_address_0(id)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->get_customer_address_0: %s\n" % e)
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

# **post_customer_address**
> post_customer_address(customer_address=customer_address)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressesApi()
customer_address = swagger_client.CustomerAddress() # CustomerAddress |  (optional)

try:
    api_instance.post_customer_address(customer_address=customer_address)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->post_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_address** | [**CustomerAddress**](CustomerAddress.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_customer_address**
> put_customer_address(id, customer_address=customer_address)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressesApi()
id = 56 # int | 
customer_address = swagger_client.CustomerAddress() # CustomerAddress |  (optional)

try:
    api_instance.put_customer_address(id, customer_address=customer_address)
except ApiException as e:
    print("Exception when calling CustomerAddressesApi->put_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **customer_address** | [**CustomerAddress**](CustomerAddress.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

