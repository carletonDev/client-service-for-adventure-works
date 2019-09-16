# swagger_client.ProductDescriptionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_description**](ProductDescriptionsApi.md#delete_product_description) | **DELETE** /api/ProductDescriptions/{id} | 
[**get_product_description**](ProductDescriptionsApi.md#get_product_description) | **GET** /api/ProductDescriptions | 
[**get_product_description_0**](ProductDescriptionsApi.md#get_product_description_0) | **GET** /api/ProductDescriptions/{id} | 
[**post_product_description**](ProductDescriptionsApi.md#post_product_description) | **POST** /api/ProductDescriptions | 
[**put_product_description**](ProductDescriptionsApi.md#put_product_description) | **PUT** /api/ProductDescriptions/{id} | 


# **delete_product_description**
> delete_product_description(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductDescriptionsApi()
id = 56 # int | 

try:
    api_instance.delete_product_description(id)
except ApiException as e:
    print("Exception when calling ProductDescriptionsApi->delete_product_description: %s\n" % e)
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

# **get_product_description**
> list[ProductDescription] get_product_description()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductDescriptionsApi()

try:
    api_response = api_instance.get_product_description()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductDescriptionsApi->get_product_description: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductDescription]**](ProductDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_description_0**
> get_product_description_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductDescriptionsApi()
id = 56 # int | 

try:
    api_instance.get_product_description_0(id)
except ApiException as e:
    print("Exception when calling ProductDescriptionsApi->get_product_description_0: %s\n" % e)
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

# **post_product_description**
> post_product_description(product_description=product_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductDescriptionsApi()
product_description = swagger_client.ProductDescription() # ProductDescription |  (optional)

try:
    api_instance.post_product_description(product_description=product_description)
except ApiException as e:
    print("Exception when calling ProductDescriptionsApi->post_product_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_description** | [**ProductDescription**](ProductDescription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_description**
> put_product_description(id, product_description=product_description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductDescriptionsApi()
id = 56 # int | 
product_description = swagger_client.ProductDescription() # ProductDescription |  (optional)

try:
    api_instance.put_product_description(id, product_description=product_description)
except ApiException as e:
    print("Exception when calling ProductDescriptionsApi->put_product_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **product_description** | [**ProductDescription**](ProductDescription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

