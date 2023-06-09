# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LocaleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_locales(self, authorization, **kwargs):  # noqa: E501
        """Get a list of locales  # noqa: E501

        This endpoint allows you to get a list of locales. Locales are paginated and sorted by code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locales(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str search: Filter locales, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
        :param int page: Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
        :param int limit: Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
        :param bool with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
        :return: Locales
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_locales_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_locales_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_locales_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Get a list of locales  # noqa: E501

        This endpoint allows you to get a list of locales. Locales are paginated and sorted by code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locales_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str search: Filter locales, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
        :param int page: Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
        :param int limit: Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
        :param bool with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
        :return: Locales
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'search', 'page', 'limit', 'with_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_locales" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_locales`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'with_count' in params:
            query_params.append(('with_count', params['with_count']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '_links', 'current_page', '_embedded', 'code', 'message'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/locales', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Locales',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_locales_code(self, authorization, code, **kwargs):  # noqa: E501
        """Get a locale  # noqa: E501

        This endpoint allows you to get the information about a given locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locales_code(authorization, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_locales_code_with_http_info(authorization, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_locales_code_with_http_info(authorization, code, **kwargs)  # noqa: E501
            return data

    def get_locales_code_with_http_info(self, authorization, code, **kwargs):  # noqa: E501
        """Get a locale  # noqa: E501

        This endpoint allows you to get the information about a given locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_locales_code_with_http_info(authorization, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_locales_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_locales_code`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_locales_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/locales/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
