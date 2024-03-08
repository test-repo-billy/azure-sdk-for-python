# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._file_system_operations import (
    build_create_request,
    build_delete_request,
    build_get_properties_request,
    build_list_blob_hierarchy_segment_request,
    build_list_paths_request,
    build_set_properties_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FileSystemOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.filedatalake.aio.AzureDataLakeStorageRESTAPI`'s
        :attr:`file_system` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create(  # pylint: disable=inconsistent-return-statements
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        properties: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Create FileSystem.

        Create a FileSystem rooted at the specified location. If the FileSystem already exists, the
        operation fails.  This operation does not support conditional HTTP requests.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_create_request(
            url=self._config.url,
            request_id_parameter=request_id_parameter,
            timeout=timeout,
            properties=properties,
            resource=self._config.resource,
            version=self._config.version,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["x-ms-namespace-enabled"] = self._deserialize(
            "str", response.headers.get("x-ms-namespace-enabled")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)

    create.metadata = {"url": "{url}"}

    @distributed_trace_async
    async def set_properties(  # pylint: disable=inconsistent-return-statements
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        properties: Optional[str] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        """Set FileSystem Properties.

        Set properties for the FileSystem.  This operation supports conditional HTTP requests.  For
        more information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param properties: Optional. User-defined properties to be stored with the filesystem, in the
         format of a comma-separated list of name and value pairs "n1=v1, n2=v2, ...", where each value
         is a base64 encoded string. Note that the string may only contain ASCII characters in the
         ISO-8859-1 character set.  If the filesystem exists, any properties not included in the list
         will be removed.  All properties are removed if the header is omitted.  To merge new and
         existing properties, first get all existing properties and the current E-Tag, then make a
         conditional request with the E-Tag and include values for all properties. Default value is
         None.
        :type properties: str
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _if_modified_since = None
        _if_unmodified_since = None
        if modified_access_conditions is not None:
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_unmodified_since = modified_access_conditions.if_unmodified_since

        request = build_set_properties_request(
            url=self._config.url,
            request_id_parameter=request_id_parameter,
            timeout=timeout,
            properties=properties,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            resource=self._config.resource,
            version=self._config.version,
            template_url=self.set_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {"url": "{url}"}

    @distributed_trace_async
    async def get_properties(  # pylint: disable=inconsistent-return-statements
        self, request_id_parameter: Optional[str] = None, timeout: Optional[int] = None, **kwargs: Any
    ) -> None:
        """Get FileSystem Properties.

        All system and user-defined filesystem properties are specified in the response headers.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_get_properties_request(
            url=self._config.url,
            request_id_parameter=request_id_parameter,
            timeout=timeout,
            resource=self._config.resource,
            version=self._config.version,
            template_url=self.get_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["x-ms-properties"] = self._deserialize("str", response.headers.get("x-ms-properties"))
        response_headers["x-ms-namespace-enabled"] = self._deserialize(
            "str", response.headers.get("x-ms-namespace-enabled")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)

    get_properties.metadata = {"url": "{url}"}

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        modified_access_conditions: Optional[_models.ModifiedAccessConditions] = None,
        **kwargs: Any
    ) -> None:
        """Delete FileSystem.

        Marks the FileSystem for deletion.  When a FileSystem is deleted, a FileSystem with the same
        identifier cannot be created for at least 30 seconds. While the filesystem is being deleted,
        attempts to create a filesystem with the same identifier will fail with status code 409
        (Conflict), with the service returning additional error information indicating that the
        filesystem is being deleted. All other operations, including operations on any files or
        directories within the filesystem, will fail with status code 404 (Not Found) while the
        filesystem is being deleted. This operation supports conditional HTTP requests.  For more
        information, see `Specifying Conditional Headers for Blob Service Operations
        <https://docs.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations>`_.

        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param modified_access_conditions: Parameter group. Default value is None.
        :type modified_access_conditions: ~azure.storage.filedatalake.models.ModifiedAccessConditions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _if_modified_since = None
        _if_unmodified_since = None
        if modified_access_conditions is not None:
            _if_modified_since = modified_access_conditions.if_modified_since
            _if_unmodified_since = modified_access_conditions.if_unmodified_since

        request = build_delete_request(
            url=self._config.url,
            request_id_parameter=request_id_parameter,
            timeout=timeout,
            if_modified_since=_if_modified_since,
            if_unmodified_since=_if_unmodified_since,
            resource=self._config.resource,
            version=self._config.version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {"url": "{url}"}

    @distributed_trace_async
    async def list_paths(
        self,
        recursive: bool,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        continuation: Optional[str] = None,
        path: Optional[str] = None,
        max_results: Optional[int] = None,
        upn: Optional[bool] = None,
        **kwargs: Any
    ) -> _models.PathList:
        """List Paths.

        List FileSystem paths and their properties.

        :param recursive: Required. Required.
        :type recursive: bool
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory. Default value is None.
        :type continuation: str
        :param path: Optional.  Filters results to paths within the specified directory. An error
         occurs if the directory does not exist. Default value is None.
        :type path: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param upn: Optional. Valid only when Hierarchical Namespace is enabled for the account. If
         "true", the user identity values returned in the x-ms-owner, x-ms-group, and x-ms-acl response
         headers will be transformed from Azure Active Directory Object IDs to User Principal Names.  If
         "false", the values will be returned as Azure Active Directory Object IDs. The default value is
         false. Note that group and application Object IDs are not translated because they do not have
         unique friendly names. Default value is None.
        :type upn: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PathList or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.PathList
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PathList] = kwargs.pop("cls", None)

        request = build_list_paths_request(
            url=self._config.url,
            recursive=recursive,
            request_id_parameter=request_id_parameter,
            timeout=timeout,
            continuation=continuation,
            path=path,
            max_results=max_results,
            upn=upn,
            resource=self._config.resource,
            version=self._config.version,
            template_url=self.list_paths.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["x-ms-continuation"] = self._deserialize("str", response.headers.get("x-ms-continuation"))

        deserialized = self._deserialize("PathList", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    list_paths.metadata = {"url": "{url}"}

    @distributed_trace_async
    async def list_blob_hierarchy_segment(
        self,
        prefix: Optional[str] = None,
        delimiter: Optional[str] = None,
        marker: Optional[str] = None,
        max_results: Optional[int] = None,
        include: Optional[List[Union[str, _models.ListBlobsIncludeItem]]] = None,
        showonly: Literal["deleted"] = "deleted",
        timeout: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ListBlobsHierarchySegmentResponse:
        """The List Blobs operation returns a list of the blobs under the specified container.

        :param prefix: Filters results to filesystems within the specified prefix. Default value is
         None.
        :type prefix: str
        :param delimiter: When the request includes this parameter, the operation returns a BlobPrefix
         element in the response body that acts as a placeholder for all blobs whose names begin with
         the same substring up to the appearance of the delimiter character. The delimiter may be a
         single character or a string. Default value is None.
        :type delimiter: str
        :param marker: A string value that identifies the portion of the list of containers to be
         returned with the next listing operation. The operation returns the NextMarker value within the
         response body if the listing operation did not return all containers remaining to be listed
         with the current page. The NextMarker value can be used as the value for the marker parameter
         in a subsequent call to request the next page of list items. The marker value is opaque to the
         client. Default value is None.
        :type marker: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items. Default value is
         None.
        :type max_results: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.filedatalake.models.ListBlobsIncludeItem]
        :param showonly: Include this parameter to specify one or more datasets to include in the
         response. Known values are "deleted" and None. Default value is "deleted".
        :type showonly: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-timeouts-for-blob-service-operations">Setting
         Timeouts for Blob Service Operations.</a>`. Default value is None.
        :type timeout: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled. Default
         value is None.
        :type request_id_parameter: str
        :keyword restype: restype. Default value is "container". Note that overriding this default
         value may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListBlobsHierarchySegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.filedatalake.models.ListBlobsHierarchySegmentResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype: Literal["container"] = kwargs.pop("restype", _params.pop("restype", "container"))
        comp: Literal["list"] = kwargs.pop("comp", _params.pop("comp", "list"))
        cls: ClsType[_models.ListBlobsHierarchySegmentResponse] = kwargs.pop("cls", None)

        request = build_list_blob_hierarchy_segment_request(
            url=self._config.url,
            prefix=prefix,
            delimiter=delimiter,
            marker=marker,
            max_results=max_results,
            include=include,
            showonly=showonly,
            timeout=timeout,
            request_id_parameter=request_id_parameter,
            restype=restype,
            comp=comp,
            version=self._config.version,
            template_url=self.list_blob_hierarchy_segment.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
        response_headers["x-ms-client-request-id"] = self._deserialize(
            "str", response.headers.get("x-ms-client-request-id")
        )
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))
        response_headers["Date"] = self._deserialize("rfc-1123", response.headers.get("Date"))

        deserialized = self._deserialize("ListBlobsHierarchySegmentResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    list_blob_hierarchy_segment.metadata = {"url": "{url}"}
