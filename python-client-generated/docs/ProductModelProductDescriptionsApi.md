# swagger_client.ProductModelProductDescriptionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_model_product_description**](ProductModelProductDescriptionsApi.md#delete_product_model_product_description) | **DELETE** /api/ProductModelProductDescriptions/{id} | 
[**get_product_model_product_description**](ProductModelProductDescriptionsApi.md#get_product_model_product_description) | **GET** /api/ProductModelProductDescriptions | 
[**get_product_model_product_description_0**](ProductModelProductDescriptionsApi.md#get_product_model_product_description_0) | **GET** /api/ProductModelProductDescriptions/{id} | 
[**post_product_model_product_description**](ProductModelProductDescriptionsApi.md#post_product_model_product_description) | **POST** /api/ProductModelProductDescriptions | 
[**put_product_model_product_description**](ProductModelProductDescriptionsApi.md#put_product_model_product_description) | **PUT** /api/ProductModelProductDescriptions/{id} | 


# **delete_product_model_product_description**
> delete_product_model_product_description(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelProductDescriptionsApi()
id = 56 # int | 

try:
    api_instance.delete_product_model_product_description(id)
except ApiException as e:
    print("Exception when calling ProductModelProductDescriptionsApi->delete_product_model_product_description: %s\n" % e)
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

# **get_product_model_product_description**
> list[ProductModelProductDescription] get_product_model_product_description()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelProductDescriptionsApi()

try:
    api_response = api_instance.get_product_model_product_description()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductModelProductDescriptionsApi->get_product_model_product_description: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductModelProductDescription]**](ProductModelProductDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_model_product_description_0**
> get_product_model_product_description_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelProductDescriptionsApi()
id = 56 # int | 

try:
    api_instance.get_product_model_product_description_0(id)
except ApiException as e:
    print("Exception when calling ProductModelProductDescriptionsApi->get_product_model_product_description_0: %s\n" % e)
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

# **post_product_model_product_description**
> post_product_model_product_description(product_model_product_description=product_model_product_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelProductDescriptionsApi()
product_model_product_description = swagger_client.ProductModelProductDescription() # ProductModelProductDescription |  (optional)

try:
    api_instance.post_product_model_product_description(product_model_product_description=product_model_product_description)
except ApiException as e:
    print("Exception when calling ProductModelProductDescriptionsApi->post_product_model_product_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_model_product_description** | [**ProductModelProductDescription**](ProductModelProductDescription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_model_product_description**
> put_product_model_product_description(id, product_model_product_description=product_model_product_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelProductDescriptionsApi()
id = 56 # int | 
product_model_product_description = swagger_client.ProductModelProductDescription() # ProductModelProductDescription |  (optional)

try:
    api_instance.put_product_model_product_description(id, product_model_product_description=product_model_product_description)
except ApiException as e:
    print("Exception when calling ProductModelProductDescriptionsApi->put_product_model_product_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **product_model_product_description** | [**ProductModelProductDescription**](ProductModelProductDescription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

