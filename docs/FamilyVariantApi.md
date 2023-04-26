# swagger_client.FamilyVariantApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_families_family_code_variants**](FamilyVariantApi.md#get_families_family_code_variants) | **GET** /api/rest/v1/families/{family_code}/variants | Get list of family variants
[**get_families_family_code_variants_code**](FamilyVariantApi.md#get_families_family_code_variants_code) | **GET** /api/rest/v1/families/{family_code}/variants/{code} | Get a family variant
[**patch_families_family_code_variants**](FamilyVariantApi.md#patch_families_family_code_variants) | **PATCH** /api/rest/v1/families/{family_code}/variants | Update/create several family variants
[**patch_families_family_code_variants_code**](FamilyVariantApi.md#patch_families_family_code_variants_code) | **PATCH** /api/rest/v1/families/{family_code}/variants/{code} | Update/create a family variant

# **get_families_family_code_variants**
> FamilyVariants get_families_family_code_variants(family_code, page=page, limit=limit, with_count=with_count)

Get list of family variants

This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyVariantApi()
family_code = 'family_code_example' # str | Code of the family
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of family variants
    api_response = api_instance.get_families_family_code_variants(family_code, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyVariantApi->get_families_family_code_variants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_code** | **str**| Code of the family | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**FamilyVariants**](FamilyVariants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, labels, variant_attribute_sets, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_families_family_code_variants_code**
> InlineResponse2008 get_families_family_code_variants_code(family_code, code)

Get a family variant

This endpoint allows you to get the information about a given family variant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyVariantApi()
family_code = 'family_code_example' # str | Code of the family
code = 'code_example' # str | Code of the resource

try:
    # Get a family variant
    api_response = api_instance.get_families_family_code_variants_code(family_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyVariantApi->get_families_family_code_variants_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_code** | **str**| Code of the family | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_families_family_code_variants**
> InlineResponse200 patch_families_family_code_variants(family_code, body=body)

Update/create several family variants

This endpoint allows you to update and/or create several family variants at once, for a given family.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyVariantApi()
family_code = 'family_code_example' # str | Code of the family
body = swagger_client.FamilyCodeVariantsBody1() # FamilyCodeVariantsBody1 |  (optional)

try:
    # Update/create several family variants
    api_response = api_instance.patch_families_family_code_variants(family_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamilyVariantApi->patch_families_family_code_variants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family_code** | **str**| Code of the family | 
 **body** | [**FamilyCodeVariantsBody1**](FamilyCodeVariantsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_families_family_code_variants_code**
> patch_families_family_code_variants_code(body, family_code, code)

Update/create a family variant

This endpoint allows you to update a given family variant. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no family variant exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamilyVariantApi()
body = swagger_client.VariantsCodeBody() # VariantsCodeBody | 
family_code = 'family_code_example' # str | Code of the family
code = 'code_example' # str | Code of the resource

try:
    # Update/create a family variant
    api_instance.patch_families_family_code_variants_code(body, family_code, code)
except ApiException as e:
    print("Exception when calling FamilyVariantApi->patch_families_family_code_variants_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariantsCodeBody**](VariantsCodeBody.md)|  | 
 **family_code** | **str**| Code of the family | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

