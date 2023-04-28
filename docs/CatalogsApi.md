# swagger_client.CatalogsApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_catalog**](CatalogsApi.md#delete_app_catalog) | **DELETE** /api/rest/v1/catalogs/{id} | Delete a catalog
[**get_app_catalog**](CatalogsApi.md#get_app_catalog) | **GET** /api/rest/v1/catalogs/{id} | Get a catalog
[**get_app_catalogs**](CatalogsApi.md#get_app_catalogs) | **GET** /api/rest/v1/catalogs | Get the list of owned catalogs
[**patch_app_catalog**](CatalogsApi.md#patch_app_catalog) | **PATCH** /api/rest/v1/catalogs/{id} | Update a catalog
[**post_app_catalog**](CatalogsApi.md#post_app_catalog) | **POST** /api/rest/v1/catalogs | Create a new catalog

# **delete_app_catalog**
> delete_app_catalog(id)

Delete a catalog

This endpoint allows you to delete a catalog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID

try:
    # Delete a catalog
    api_instance.delete_app_catalog(id)
except ApiException as e:
    print("Exception when calling CatalogsApi->delete_app_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Catalog ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_catalog**
> InlineResponse2011 get_app_catalog(authorization, id)

Get a catalog

This endpoint allows you to get the information about a catalog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID

try:
    # Get a catalog
    api_response = api_instance.get_app_catalog(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->get_app_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **id** | [**str**](.md)| Catalog ID | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_catalogs**
> Catalogs get_app_catalogs(authorization, page=page, limit=limit)

Get the list of owned catalogs

This endpoint allows you to get the list of catalogs you owned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 100 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 100)

try:
    # Get the list of owned catalogs
    api_response = api_instance.get_app_catalogs(authorization, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->get_app_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100]

### Return type

[**Catalogs**](Catalogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_app_catalog**
> InlineResponse2011 patch_app_catalog(id, body=body)

Update a catalog

This endpoint allows you to update a catalog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID
body = swagger_client.CatalogsIdBody() # CatalogsIdBody |  (optional)

try:
    # Update a catalog
    api_response = api_instance.patch_app_catalog(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->patch_app_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Catalog ID | 
 **body** | [**CatalogsIdBody**](CatalogsIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_app_catalog**
> InlineResponse2011 post_app_catalog(body=body)

Create a new catalog

This endpoint allows you to create a new catalog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
body = swagger_client.V1CatalogsBody() # V1CatalogsBody |  (optional)

try:
    # Create a new catalog
    api_response = api_instance.post_app_catalog(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->post_app_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CatalogsBody**](V1CatalogsBody.md)|  | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

