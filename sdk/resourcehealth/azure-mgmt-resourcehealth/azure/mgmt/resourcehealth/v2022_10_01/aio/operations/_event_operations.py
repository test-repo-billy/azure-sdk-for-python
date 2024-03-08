# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._event_operations import (
    build_fetch_details_by_subscription_id_and_tracking_id_request,
    build_fetch_details_by_tenant_id_and_tracking_id_request,
    build_get_by_subscription_id_and_tracking_id_request,
    build_get_by_tenant_id_and_tracking_id_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class EventOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.resourcehealth.v2022_10_01.aio.ResourceHealthMgmtClient`'s
        :attr:`event` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def get_by_subscription_id_and_tracking_id(
        self,
        event_tracking_id: str,
        filter: Optional[str] = None,
        query_start_time: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Event:
        """Service health event in the subscription by event tracking id.

        :param event_tracking_id: Event Id which uniquely identifies ServiceHealth event. Required.
        :type event_tracking_id: str
        :param filter: The filter to apply on the operation. For more information please see
         https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN. Default value
         is None.
        :type filter: str
        :param query_start_time: Specifies from when to return events, based on the lastUpdateTime
         property. For example, queryStartTime = 7/24/2020 OR queryStartTime=7%2F24%2F2020. Default
         value is None.
        :type query_start_time: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event or the result of cls(response)
        :rtype: ~azure.mgmt.resourcehealth.v2022_10_01.models.Event
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-10-01"))
        cls: ClsType[_models.Event] = kwargs.pop("cls", None)

        request = build_get_by_subscription_id_and_tracking_id_request(
            event_tracking_id=event_tracking_id,
            subscription_id=self._config.subscription_id,
            filter=filter,
            query_start_time=query_start_time,
            api_version=api_version,
            template_url=self.get_by_subscription_id_and_tracking_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_subscription_id_and_tracking_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events/{eventTrackingId}"
    }

    @distributed_trace_async
    async def fetch_details_by_subscription_id_and_tracking_id(
        self, event_tracking_id: str, **kwargs: Any
    ) -> _models.Event:
        """Service health event details in the subscription by event tracking id. This can be used to
        fetch sensitive properties for Security Advisory events.

        :param event_tracking_id: Event Id which uniquely identifies ServiceHealth event. Required.
        :type event_tracking_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event or the result of cls(response)
        :rtype: ~azure.mgmt.resourcehealth.v2022_10_01.models.Event
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-10-01"))
        cls: ClsType[_models.Event] = kwargs.pop("cls", None)

        request = build_fetch_details_by_subscription_id_and_tracking_id_request(
            event_tracking_id=event_tracking_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.fetch_details_by_subscription_id_and_tracking_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    fetch_details_by_subscription_id_and_tracking_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events/{eventTrackingId}/fetchEventDetails"
    }

    @distributed_trace_async
    async def get_by_tenant_id_and_tracking_id(
        self,
        event_tracking_id: str,
        filter: Optional[str] = None,
        query_start_time: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Event:
        """Service health event in the tenant by event tracking id.

        :param event_tracking_id: Event Id which uniquely identifies ServiceHealth event. Required.
        :type event_tracking_id: str
        :param filter: The filter to apply on the operation. For more information please see
         https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN. Default value
         is None.
        :type filter: str
        :param query_start_time: Specifies from when to return events, based on the lastUpdateTime
         property. For example, queryStartTime = 7/24/2020 OR queryStartTime=7%2F24%2F2020. Default
         value is None.
        :type query_start_time: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event or the result of cls(response)
        :rtype: ~azure.mgmt.resourcehealth.v2022_10_01.models.Event
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-10-01"))
        cls: ClsType[_models.Event] = kwargs.pop("cls", None)

        request = build_get_by_tenant_id_and_tracking_id_request(
            event_tracking_id=event_tracking_id,
            filter=filter,
            query_start_time=query_start_time,
            api_version=api_version,
            template_url=self.get_by_tenant_id_and_tracking_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_tenant_id_and_tracking_id.metadata = {"url": "/providers/Microsoft.ResourceHealth/events/{eventTrackingId}"}

    @distributed_trace_async
    async def fetch_details_by_tenant_id_and_tracking_id(self, event_tracking_id: str, **kwargs: Any) -> _models.Event:
        """Service health event details in the tenant by event tracking id. This can be used to fetch
        sensitive properties for Security Advisory events.

        :param event_tracking_id: Event Id which uniquely identifies ServiceHealth event. Required.
        :type event_tracking_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Event or the result of cls(response)
        :rtype: ~azure.mgmt.resourcehealth.v2022_10_01.models.Event
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2022-10-01"))
        cls: ClsType[_models.Event] = kwargs.pop("cls", None)

        request = build_fetch_details_by_tenant_id_and_tracking_id_request(
            event_tracking_id=event_tracking_id,
            api_version=api_version,
            template_url=self.fetch_details_by_tenant_id_and_tracking_id.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Event", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    fetch_details_by_tenant_id_and_tracking_id.metadata = {
        "url": "/providers/Microsoft.ResourceHealth/events/{eventTrackingId}/fetchEventDetails"
    }
