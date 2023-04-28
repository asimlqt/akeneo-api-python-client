# swagger_client.AssetApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_assets_code**](AssetApi.md#delete_assets_code) | **DELETE** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Delete an asset
[**get_assets**](AssetApi.md#get_assets) | **GET** /api/rest/v1/asset-families/{asset_family_code}/assets | Get the list of the assets of a given asset family
[**get_assets_code**](AssetApi.md#get_assets_code) | **GET** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Get an asset of a given asset family
[**patch_asset_code**](AssetApi.md#patch_asset_code) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Update/create an asset
[**patch_assets**](AssetApi.md#patch_assets) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/assets | Update/create several assets

# **delete_assets_code**
> delete_assets_code(asset_family_code, code)

Delete an asset

This endpoint allows you to delete a given asset. This endpoint is case sensitive on the asset family code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
code = 'code_example' # str | Code of the resource

try:
    # Delete an asset
    api_instance.delete_assets_code(asset_family_code, code)
except ApiException as e:
    print("Exception when calling AssetApi->delete_assets_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_family_code** | **str**| Code of the asset family | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> Asset get_assets(authorization, asset_family_code, search=search, channel=channel, locales=locales, search_after=search_after)

Get the list of the assets of a given asset family

This endpoint allows you to get a list of assets of a given asset family. Assets are paginated. This endpoint is case sensitive on the asset family code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
search = 'search_example' # str | Filter assets, for more details see the <a href=\"/documentation/filter.html#filter-assets\">Asset filters</a> section (optional)
channel = 'channel_example' # str | Filter asset values to return scopable asset attributes for the given channel as well as the non localizable/non scopable asset attributes, for more details see the <a href=\"/documentation/filter.html#asset-values-by-channel\">Filter asset values by channel</a> section (optional)
locales = 'locales_example' # str | Filter asset values to return localizable attributes for the given locales as well as the non localizable/non scopable asset attributes, for more details see the <a href=\"/documentation/filter.html#asset-values-by-locale\">Filter asset values by locale</a> section (optional)
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)

try:
    # Get the list of the assets of a given asset family
    api_response = api_instance.get_assets(authorization, asset_family_code, search=search, channel=channel, locales=locales, search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_family_code** | **str**| Code of the asset family | 
 **search** | **str**| Filter assets, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-assets\&quot;&gt;Asset filters&lt;/a&gt; section | [optional] 
 **channel** | **str**| Filter asset values to return scopable asset attributes for the given channel as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-channel\&quot;&gt;Filter asset values by channel&lt;/a&gt; section | [optional] 
 **locales** | **str**| Filter asset values to return localizable attributes for the given locales as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-locale\&quot;&gt;Filter asset values by locale&lt;/a&gt; section | [optional] 
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_code**
> InlineResponse20032 get_assets_code(authorization, asset_family_code, code)

Get an asset of a given asset family

This endpoint allows you to get the information about a given asset for a given asset family. This endpoint is case sensitive on the asset family code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
code = 'code_example' # str | Code of the resource

try:
    # Get an asset of a given asset family
    api_response = api_instance.get_assets_code(authorization, asset_family_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->get_assets_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **asset_family_code** | **str**| Code of the asset family | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_asset_code**
> patch_asset_code(body, asset_family_code, code)

Update/create an asset

This endpoint allows you to update a given asset of a given asset family. Learn more about the <a href=\"/documentation/update.html#patch-asset-attribute-values\">Update behavior</a>. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
body = swagger_client.AssetsCodeBody() # AssetsCodeBody | 
asset_family_code = 'asset_family_code_example' # str | Code of the asset family
code = 'code_example' # str | Code of the resource

try:
    # Update/create an asset
    api_instance.patch_asset_code(body, asset_family_code, code)
except ApiException as e:
    print("Exception when calling AssetApi->patch_asset_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetsCodeBody**](AssetsCodeBody.md)|  | 
 **asset_family_code** | **str**| Code of the asset family | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_assets**
> list[InlineResponse20025] patch_assets(body, asset_family_code)

Update/create several assets

This endpoint allows you to update and/or create several assets of one given asset family at once. Learn more about the <a href=\"/documentation/update.html#patch-asset-attribute-values\">Update behavior</a>. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetApi()
body = [swagger_client.AssetFamilyCodeAssetsBody()] # list[AssetFamilyCodeAssetsBody] | 
asset_family_code = 'asset_family_code_example' # str | Code of the asset family

try:
    # Update/create several assets
    api_response = api_instance.patch_assets(body, asset_family_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetApi->patch_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AssetFamilyCodeAssetsBody]**](AssetFamilyCodeAssetsBody.md)|  | 
 **asset_family_code** | **str**| Code of the asset family | 

### Return type

[**list[InlineResponse20025]**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

