# swagger_client.CategoryApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories**](CategoryApi.md#get_categories) | **GET** /api/rest/v1/categories | Get list of categories
[**get_categories_code**](CategoryApi.md#get_categories_code) | **GET** /api/rest/v1/categories/{code} | Get a category
[**get_category_media_files_code_download**](CategoryApi.md#get_category_media_files_code_download) | **GET** /api/rest/v1/category-media-files/{code}/download | Download a category media file
[**patch_categories**](CategoryApi.md#patch_categories) | **PATCH** /api/rest/v1/categories | Update/create several categories
[**patch_categories_code**](CategoryApi.md#patch_categories_code) | **PATCH** /api/rest/v1/categories/{code} | Update/create a category
[**post_categories**](CategoryApi.md#post_categories) | **POST** /api/rest/v1/categories | Create a new category

# **get_categories**
> Categories get_categories(authorization, search=search, page=page, limit=limit, with_count=with_count, with_position=with_position, with_enriched_attributes=with_enriched_attributes)

Get list of categories

This endpoint allows you to get a list of categories. Categories are paginated and sorted by `root/left`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter categories, for more details see the <a href=\"/documentation/filter.html#filter-categories\">Filters</a> section. (optional)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)
with_position = true # bool | Return information about category position into its category tree (only available since the 7.0 version) (optional)
with_enriched_attributes = true # bool | Return attribute values of the category (only available on SaaS platforms) (optional)

try:
    # Get list of categories
    api_response = api_instance.get_categories(authorization, search=search, page=page, limit=limit, with_count=with_count, with_position=with_position, with_enriched_attributes=with_enriched_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter categories, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-categories\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **with_position** | **bool**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] 
 **with_enriched_attributes** | **bool**| Return attribute values of the category (only available on SaaS platforms) | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_code**
> InlineResponse20015 get_categories_code(authorization, code, with_position=with_position, with_enriched_attributes=with_enriched_attributes)

Get a category

This endpoint allows you to get the information about a given category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource
with_position = true # bool | Return information about category position into its category tree (only available since the 7.0 version) (optional)
with_enriched_attributes = true # bool | Return attribute values of the category (only available on SaaS platforms) (optional)

try:
    # Get a category
    api_response = api_instance.get_categories_code(authorization, code, with_position=with_position, with_enriched_attributes=with_enriched_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_categories_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 
 **with_position** | **bool**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] 
 **with_enriched_attributes** | **bool**| Return attribute values of the category (only available on SaaS platforms) | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_media_files_code_download**
> get_category_media_files_code_download(authorization, code)

Download a category media file

This endpoint allows you to download a given media file that is used as an attribute value of a enriched category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Download a category media file
    api_instance.get_category_media_files_code_download(authorization, code)
except ApiException as e:
    print("Exception when calling CategoryApi->get_category_media_files_code_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_categories**
> InlineResponse200 patch_categories(body=body)

Update/create several categories

This endpoint allows you to update several categories at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
body = swagger_client.V1CategoriesBody1() # V1CategoriesBody1 |  (optional)

try:
    # Update/create several categories
    api_response = api_instance.patch_categories(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->patch_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CategoriesBody1**](V1CategoriesBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_categories_code**
> patch_categories_code(body, code)

Update/create a category

This endpoint allows you to update a given category. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no category exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
body = swagger_client.CategoriesCodeBody() # CategoriesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a category
    api_instance.patch_categories_code(body, code)
except ApiException as e:
    print("Exception when calling CategoryApi->patch_categories_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoriesCodeBody**](CategoriesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_categories**
> post_categories(body=body)

Create a new category

This endpoint allows you to create a new category.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoryApi()
body = swagger_client.V1CategoriesBody() # V1CategoriesBody |  (optional)

try:
    # Create a new category
    api_instance.post_categories(body=body)
except ApiException as e:
    print("Exception when calling CategoryApi->post_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CategoriesBody**](V1CategoriesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

