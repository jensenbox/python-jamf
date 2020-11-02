# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TeacherAppApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_teacher_app_get(self, **kwargs):  # noqa: E501
        """Get the Jamf Teacher settings that you have access to see   # noqa: E501

        Get the Jamf Teacher settings that you have access to see.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TeacherSettingsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_teacher_app_get_with_http_info(**kwargs)  # noqa: E501

    def v1_teacher_app_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the Jamf Teacher settings that you have access to see   # noqa: E501

        Get the Jamf Teacher settings that you have access to see.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TeacherSettingsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_teacher_app_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "TeacherSettingsResponse",
        }

        return self.api_client.call_api(
            '/v1/teacher-app', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def v1_teacher_app_history_get(self, **kwargs):  # noqa: E501
        """Get Jamf Teacher app settings history   # noqa: E501

        Gets Jamf Teacher app settings history   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_history_get(async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort: Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is not duplicated for each sort criterion, e.g., ...&sort=name%2Casc,date%2Cdesc
        :type sort: list[str]
        :param filter: Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HistorySearchResults
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_teacher_app_history_get_with_http_info(**kwargs)  # noqa: E501

    def v1_teacher_app_history_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Jamf Teacher app settings history   # noqa: E501

        Gets Jamf Teacher app settings history   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_history_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort: Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is not duplicated for each sort criterion, e.g., ...&sort=name%2Casc,date%2Cdesc
        :type sort: list[str]
        :param filter: Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(HistorySearchResults, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'page',
            'page_size',
            'sort',
            'filter'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_teacher_app_history_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('page-size', local_var_params['page_size']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
            collection_formats['sort'] = 'multi'  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "HistorySearchResults",
        }

        return self.api_client.call_api(
            '/v1/teacher-app/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def v1_teacher_app_history_post(self, object_history_note, **kwargs):  # noqa: E501
        """Add Jamf Teacher app settings history notes   # noqa: E501

        Adds Jamf Teacher app settings history notes   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_history_post(object_history_note, async_req=True)
        >>> result = thread.get()

        :param object_history_note: history notes to create (required)
        :type object_history_note: ObjectHistoryNote
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HrefResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_teacher_app_history_post_with_http_info(object_history_note, **kwargs)  # noqa: E501

    def v1_teacher_app_history_post_with_http_info(self, object_history_note, **kwargs):  # noqa: E501
        """Add Jamf Teacher app settings history notes   # noqa: E501

        Adds Jamf Teacher app settings history notes   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_history_post_with_http_info(object_history_note, async_req=True)
        >>> result = thread.get()

        :param object_history_note: history notes to create (required)
        :type object_history_note: ObjectHistoryNote
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(HrefResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'object_history_note'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_teacher_app_history_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_history_note' is set
        if self.api_client.client_side_validation and ('object_history_note' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_history_note'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_history_note` when calling `v1_teacher_app_history_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'object_history_note' in local_var_params:
            body_params = local_var_params['object_history_note']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            201: "HrefResponse",
            503: "ApiError",
        }

        return self.api_client.call_api(
            '/v1/teacher-app/history', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def v1_teacher_app_put(self, teacher_settings_request, **kwargs):  # noqa: E501
        """Update a Jamf Teacher settings object   # noqa: E501

        Update a Jamf Teacher settings object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_put(teacher_settings_request, async_req=True)
        >>> result = thread.get()

        :param teacher_settings_request: Teacher settings to create. (required)
        :type teacher_settings_request: TeacherSettingsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TeacherSettingsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_teacher_app_put_with_http_info(teacher_settings_request, **kwargs)  # noqa: E501

    def v1_teacher_app_put_with_http_info(self, teacher_settings_request, **kwargs):  # noqa: E501
        """Update a Jamf Teacher settings object   # noqa: E501

        Update a Jamf Teacher settings object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.v1_teacher_app_put_with_http_info(teacher_settings_request, async_req=True)
        >>> result = thread.get()

        :param teacher_settings_request: Teacher settings to create. (required)
        :type teacher_settings_request: TeacherSettingsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TeacherSettingsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'teacher_settings_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_teacher_app_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'teacher_settings_request' is set
        if self.api_client.client_side_validation and ('teacher_settings_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['teacher_settings_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `teacher_settings_request` when calling `v1_teacher_app_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'teacher_settings_request' in local_var_params:
            body_params = local_var_params['teacher_settings_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "TeacherSettingsResponse",
            500: "ApiError",
        }

        return self.api_client.call_api(
            '/v1/teacher-app', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
