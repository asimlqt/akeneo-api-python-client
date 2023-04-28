# swagger_client.FamilyApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_families**](FamilyApi.md#get_families) | **GET** /api/rest/v1/families | Get list of families
[**get_families_code**](FamilyApi.md#get_families_code) | **GET** /api/rest/v1/families/{code} | Get a family
[**patch_families**](FamilyApi.md#patch_families) | **PATCH** /api/rest/v1/families | Update/create several families
[**patch_families_code**](FamilyApi.md#patch_families_code) | **PATCH** /api/rest/v1/families/{code} | Update/create a family
[**post_families**](FamilyApi.md#post_families) | **POST** /api/rest/v1/families | Create a new family
[**post_families_family_code_variants**](FamilyApi.md#post_families_family_code_variants) | **POST** /api/rest/v1/families/{family_code}/variants | Create a new family variant

# **get_families**
> Families get_families(authorization, search=search, page=page, limit=limit, with_count=with_count)

Get list of families

This endpoint allows you to get a list of families. Families are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter families, for more details see the <a href=\"/documentation/filter.html#filter-families\">Filters</a> section. (optional)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of families
    api_response = api_instance.get_families(authorization, search=search, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyApi->get_families: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter families, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-families\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**Families**](Families.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_families_code**
> InlineResponse2007 get_families_code(authorization, code)

Get a family

This endpoint allows you to get the information about a given family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a family
    api_response = api_instance.get_families_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyApi->get_families_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_families**
> InlineResponse200 patch_families(body=body)

Update/create several families

This endpoint allows you to update and/or create several families at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
body = swagger_client.V1FamiliesBody1() # V1FamiliesBody1 |  (optional)

try:
    # Update/create several families
    api_response = api_instance.patch_families(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyApi->patch_families: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FamiliesBody1**](V1FamiliesBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_families_code**
> patch_families_code(body, code)

Update/create a family

This endpoint allows you to update a given family. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no family exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
body = swagger_client.FamiliesCodeBody() # FamiliesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a family
    api_instance.patch_families_code(body, code)
except ApiException as e:
    print("Exception when calling FamilyApi->patch_families_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FamiliesCodeBody**](FamiliesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_families**
> post_families(body=body)

Create a new family

This endpoint allows you to create a new family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
body = swagger_client.V1FamiliesBody() # V1FamiliesBody |  (optional)

try:
    # Create a new family
    api_instance.post_families(body=body)
except ApiException as e:
    print("Exception when calling FamilyApi->post_families: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FamiliesBody**](V1FamiliesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_families_family_code_variants**
> post_families_family_code_variants(family_code, body=body)

Create a new family variant

This endpoint allows you to create a family variant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyApi()
family_code = 'family_code_example' # str | Code of the family
body = swagger_client.FamilyCodeVariantsBody() # FamilyCodeVariantsBody |  (optional)

try:
    # Create a new family variant
    api_instance.post_families_family_code_variants(family_code, body=body)
except ApiException as e:
    print("Exception when calling FamilyApi->post_families_family_code_variants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_code** | **str**| Code of the family | 
 **body** | [**FamilyCodeVariantsBody**](FamilyCodeVariantsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

