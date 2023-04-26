# swagger_client.SystemApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_information**](SystemApi.md#get_system_information) | **GET** /api/rest/v1/system-information | Get system information

# **get_system_information**
> InlineResponse20041 get_system_information()

Get system information

This endpoint allows you to get the version and the edition of the PIM. Example of what you can get <table class=\"description-table\"> <thead> <tr> <th align=\"center\">Environment</th> <th align=\"center\">Edition</th> <th align=\"center\">Version</th> </tr> </thead> <tbody> <tr> <td align=\"center\">SaaS EE</td> <td align=\"center\">Serenity</td> <td align=\"center\">v20230112013744</td> </tr> <tr> <td align=\"center\">SaaS CE</td> <td align=\"center\">GE</td> <td align=\"center\">v20210526040645</td> </tr> <tr> <td align=\"center\">PaaS or onPrem EE</td> <td align=\"center\">EE</td> <td align=\"center\">5.0.28</td> </tr> <tr> <td align=\"center\">PaaS or onPrem CE</td> <td align=\"center\">CE</td> <td align=\"center\">5.0.28</td> </tr> </tbody> </table>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Get system information
    api_response = api_instance.get_system_information()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_information: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, version, edition, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

