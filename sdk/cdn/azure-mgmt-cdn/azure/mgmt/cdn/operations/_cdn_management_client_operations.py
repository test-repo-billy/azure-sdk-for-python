# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import CdnManagementClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_check_endpoint_name_availability_request(
    resource_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/checkEndpointNameAvailability",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_check_name_availability_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.Cdn/checkNameAvailability")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_check_name_availability_with_subscription_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/checkNameAvailability")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_validate_probe_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/validateProbe")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class CdnManagementClientOperationsMixin(CdnManagementClientMixinABC):
    @overload
    def check_endpoint_name_availability(
        self,
        resource_group_name: str,
        check_endpoint_name_availability_input: _models.CheckEndpointNameAvailabilityInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckEndpointNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a afdx endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param check_endpoint_name_availability_input: Input to check. Required.
        :type check_endpoint_name_availability_input:
         ~azure.mgmt.cdn.models.CheckEndpointNameAvailabilityInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckEndpointNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckEndpointNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_endpoint_name_availability(
        self,
        resource_group_name: str,
        check_endpoint_name_availability_input: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckEndpointNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a afdx endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param check_endpoint_name_availability_input: Input to check. Required.
        :type check_endpoint_name_availability_input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckEndpointNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckEndpointNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_endpoint_name_availability(
        self,
        resource_group_name: str,
        check_endpoint_name_availability_input: Union[_models.CheckEndpointNameAvailabilityInput, IO],
        **kwargs: Any
    ) -> _models.CheckEndpointNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a afdx endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param check_endpoint_name_availability_input: Input to check. Is either a
         CheckEndpointNameAvailabilityInput type or a IO type. Required.
        :type check_endpoint_name_availability_input:
         ~azure.mgmt.cdn.models.CheckEndpointNameAvailabilityInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckEndpointNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckEndpointNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CheckEndpointNameAvailabilityOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_endpoint_name_availability_input, (IOBase, bytes)):
            _content = check_endpoint_name_availability_input
        else:
            _json = self._serialize.body(check_endpoint_name_availability_input, "CheckEndpointNameAvailabilityInput")

        request = build_check_endpoint_name_availability_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_endpoint_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckEndpointNameAvailabilityOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_endpoint_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/checkEndpointNameAvailability"
    }

    @overload
    def check_name_availability(
        self,
        check_name_availability_input: _models.CheckNameAvailabilityInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: ~azure.mgmt.cdn.models.CheckNameAvailabilityInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_name_availability(
        self, check_name_availability_input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_name_availability(
        self, check_name_availability_input: Union[_models.CheckNameAvailabilityInput, IO], **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Is either a CheckNameAvailabilityInput
         type or a IO type. Required.
        :type check_name_availability_input: ~azure.mgmt.cdn.models.CheckNameAvailabilityInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CheckNameAvailabilityOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_input, (IOBase, bytes)):
            _content = check_name_availability_input
        else:
            _json = self._serialize.body(check_name_availability_input, "CheckNameAvailabilityInput")

        request = build_check_name_availability_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {"url": "/providers/Microsoft.Cdn/checkNameAvailability"}

    @overload
    def check_name_availability_with_subscription(
        self,
        check_name_availability_input: _models.CheckNameAvailabilityInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: ~azure.mgmt.cdn.models.CheckNameAvailabilityInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_name_availability_with_subscription(
        self, check_name_availability_input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Required.
        :type check_name_availability_input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_name_availability_with_subscription(
        self, check_name_availability_input: Union[_models.CheckNameAvailabilityInput, IO], **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the availability of a resource name. This is needed for resources where name is globally
        unique, such as a CDN endpoint.

        :param check_name_availability_input: Input to check. Is either a CheckNameAvailabilityInput
         type or a IO type. Required.
        :type check_name_availability_input: ~azure.mgmt.cdn.models.CheckNameAvailabilityInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CheckNameAvailabilityOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability_input, (IOBase, bytes)):
            _content = check_name_availability_input
        else:
            _json = self._serialize.body(check_name_availability_input, "CheckNameAvailabilityInput")

        request = build_check_name_availability_with_subscription_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability_with_subscription.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability_with_subscription.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/checkNameAvailability"
    }

    @overload
    def validate_probe(
        self, validate_probe_input: _models.ValidateProbeInput, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ValidateProbeOutput:
        """Check if the probe path is a valid path and the file can be accessed. Probe path is the path to
        a file hosted on the origin server to help accelerate the delivery of dynamic content via the
        CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

        :param validate_probe_input: Input to check. Required.
        :type validate_probe_input: ~azure.mgmt.cdn.models.ValidateProbeInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidateProbeOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.ValidateProbeOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def validate_probe(
        self, validate_probe_input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ValidateProbeOutput:
        """Check if the probe path is a valid path and the file can be accessed. Probe path is the path to
        a file hosted on the origin server to help accelerate the delivery of dynamic content via the
        CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

        :param validate_probe_input: Input to check. Required.
        :type validate_probe_input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidateProbeOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.ValidateProbeOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def validate_probe(
        self, validate_probe_input: Union[_models.ValidateProbeInput, IO], **kwargs: Any
    ) -> _models.ValidateProbeOutput:
        """Check if the probe path is a valid path and the file can be accessed. Probe path is the path to
        a file hosted on the origin server to help accelerate the delivery of dynamic content via the
        CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

        :param validate_probe_input: Input to check. Is either a ValidateProbeInput type or a IO type.
         Required.
        :type validate_probe_input: ~azure.mgmt.cdn.models.ValidateProbeInput or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ValidateProbeOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.ValidateProbeOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ValidateProbeOutput] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(validate_probe_input, (IOBase, bytes)):
            _content = validate_probe_input
        else:
            _json = self._serialize.body(validate_probe_input, "ValidateProbeInput")

        request = build_validate_probe_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.validate_probe.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ValidateProbeOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    validate_probe.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/validateProbe"}
