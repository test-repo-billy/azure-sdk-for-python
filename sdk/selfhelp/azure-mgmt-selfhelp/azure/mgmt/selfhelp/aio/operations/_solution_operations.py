# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._solution_operations import build_create_request, build_get_request, build_update_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SolutionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.selfhelp.aio.SelfHelpMgmtClient`'s
        :attr:`solution` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_initial(
        self,
        scope: str,
        solution_resource_name: str,
        solution_request_body: Optional[Union[_models.SolutionResource, IO]] = None,
        **kwargs: Any
    ) -> _models.SolutionResource:
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
        cls: ClsType[_models.SolutionResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(solution_request_body, (IOBase, bytes)):
            _content = solution_request_body
        else:
            if solution_request_body is not None:
                _json = self._serialize.body(solution_request_body, "SolutionResource")
            else:
                _json = None

        request = build_create_request(
            scope=scope,
            solution_resource_name=solution_resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_initial.metadata["url"],
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("SolutionResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SolutionResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    _create_initial.metadata = {"url": "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}"}

    @overload
    async def begin_create(
        self,
        scope: str,
        solution_resource_name: str,
        solution_request_body: Optional[_models.SolutionResource] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId
        and requiredInputs’ from discovery solutions. :code:`<br/>` Azure solutions comprise a
        comprehensive library of self-help resources that have been thoughtfully curated by Azure
        engineers to aid customers in resolving typical troubleshooting issues. These solutions
        encompass (1.) dynamic and context-aware diagnostics, guided troubleshooting wizards, and data
        visualizations, (2.) rich instructional video tutorials and illustrative diagrams and images,
        and (3.) thoughtfully assembled textual troubleshooting instructions. All these components are
        seamlessly converged into unified solutions tailored to address a specific support problem
        area. Each solution type may require one or more ‘requiredParameters’ that are required to
        execute the individual solution component. In the absence of the ‘requiredParameters’ it is
        likely that some of the solutions might fail execution, and you might see an empty response.
        :code:`<br/>`:code:`<br/>` :code:`<b>Note:</b>`  :code:`<br/>`1. ‘requiredInputs’ from
        Discovery solutions response must be passed via ‘parameters’ in the request body of Solutions
        API. :code:`<br/>`2. ‘requiredParameters’ from the Solutions response is the same as ‘
        additionalParameters’ in the request for diagnostics :code:`<br/>`3. ‘requiredParameters’ from
        the Solutions response is the same as ‘properties.parameters’ in the request for
        Troubleshooters.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_request_body: The required request body for this solution resource creation.
         Default value is None.
        :type solution_request_body: ~azure.mgmt.selfhelp.models.SolutionResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        scope: str,
        solution_resource_name: str,
        solution_request_body: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId
        and requiredInputs’ from discovery solutions. :code:`<br/>` Azure solutions comprise a
        comprehensive library of self-help resources that have been thoughtfully curated by Azure
        engineers to aid customers in resolving typical troubleshooting issues. These solutions
        encompass (1.) dynamic and context-aware diagnostics, guided troubleshooting wizards, and data
        visualizations, (2.) rich instructional video tutorials and illustrative diagrams and images,
        and (3.) thoughtfully assembled textual troubleshooting instructions. All these components are
        seamlessly converged into unified solutions tailored to address a specific support problem
        area. Each solution type may require one or more ‘requiredParameters’ that are required to
        execute the individual solution component. In the absence of the ‘requiredParameters’ it is
        likely that some of the solutions might fail execution, and you might see an empty response.
        :code:`<br/>`:code:`<br/>` :code:`<b>Note:</b>`  :code:`<br/>`1. ‘requiredInputs’ from
        Discovery solutions response must be passed via ‘parameters’ in the request body of Solutions
        API. :code:`<br/>`2. ‘requiredParameters’ from the Solutions response is the same as ‘
        additionalParameters’ in the request for diagnostics :code:`<br/>`3. ‘requiredParameters’ from
        the Solutions response is the same as ‘properties.parameters’ in the request for
        Troubleshooters.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_request_body: The required request body for this solution resource creation.
         Default value is None.
        :type solution_request_body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        scope: str,
        solution_resource_name: str,
        solution_request_body: Optional[Union[_models.SolutionResource, IO]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId
        and requiredInputs’ from discovery solutions. :code:`<br/>` Azure solutions comprise a
        comprehensive library of self-help resources that have been thoughtfully curated by Azure
        engineers to aid customers in resolving typical troubleshooting issues. These solutions
        encompass (1.) dynamic and context-aware diagnostics, guided troubleshooting wizards, and data
        visualizations, (2.) rich instructional video tutorials and illustrative diagrams and images,
        and (3.) thoughtfully assembled textual troubleshooting instructions. All these components are
        seamlessly converged into unified solutions tailored to address a specific support problem
        area. Each solution type may require one or more ‘requiredParameters’ that are required to
        execute the individual solution component. In the absence of the ‘requiredParameters’ it is
        likely that some of the solutions might fail execution, and you might see an empty response.
        :code:`<br/>`:code:`<br/>` :code:`<b>Note:</b>`  :code:`<br/>`1. ‘requiredInputs’ from
        Discovery solutions response must be passed via ‘parameters’ in the request body of Solutions
        API. :code:`<br/>`2. ‘requiredParameters’ from the Solutions response is the same as ‘
        additionalParameters’ in the request for diagnostics :code:`<br/>`3. ‘requiredParameters’ from
        the Solutions response is the same as ‘properties.parameters’ in the request for
        Troubleshooters.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_request_body: The required request body for this solution resource creation. Is
         either a SolutionResource type or a IO type. Default value is None.
        :type solution_request_body: ~azure.mgmt.selfhelp.models.SolutionResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SolutionResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                scope=scope,
                solution_resource_name=solution_resource_name,
                solution_request_body=solution_request_body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("SolutionResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_create.metadata = {"url": "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}"}

    @distributed_trace_async
    async def get(self, scope: str, solution_resource_name: str, **kwargs: Any) -> _models.SolutionResource:
        """Get the solution using the applicable solutionResourceName while creating the solution.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SolutionResource or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.SolutionResource
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.SolutionResource] = kwargs.pop("cls", None)

        request = build_get_request(
            scope=scope,
            solution_resource_name=solution_resource_name,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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

        deserialized = self._deserialize("SolutionResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}"}

    async def _update_initial(
        self,
        scope: str,
        solution_resource_name: str,
        solution_patch_request_body: Optional[Union[_models.SolutionPatchRequestBody, IO]] = None,
        **kwargs: Any
    ) -> _models.SolutionResource:
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
        cls: ClsType[_models.SolutionResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(solution_patch_request_body, (IOBase, bytes)):
            _content = solution_patch_request_body
        else:
            if solution_patch_request_body is not None:
                _json = self._serialize.body(solution_patch_request_body, "SolutionPatchRequestBody")
            else:
                _json = None

        request = build_update_request(
            scope=scope,
            solution_resource_name=solution_resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._update_initial.metadata["url"],
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

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("SolutionResource", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("SolutionResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    _update_initial.metadata = {"url": "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}"}

    @overload
    async def begin_update(
        self,
        scope: str,
        solution_resource_name: str,
        solution_patch_request_body: Optional[_models.SolutionPatchRequestBody] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Update the requiredInputs or additional information needed to execute the solution.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_patch_request_body: The required request body for updating a solution resource.
         Default value is None.
        :type solution_patch_request_body: ~azure.mgmt.selfhelp.models.SolutionPatchRequestBody
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        scope: str,
        solution_resource_name: str,
        solution_patch_request_body: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Update the requiredInputs or additional information needed to execute the solution.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_patch_request_body: The required request body for updating a solution resource.
         Default value is None.
        :type solution_patch_request_body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        scope: str,
        solution_resource_name: str,
        solution_patch_request_body: Optional[Union[_models.SolutionPatchRequestBody, IO]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SolutionResource]:
        """Update the requiredInputs or additional information needed to execute the solution.

        :param scope: scope = resourceUri of affected resource.:code:`<br/>` For example:
         /subscriptions/0d0fcd2e-c4fd-4349-8497-200edb3923c6/resourcegroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read.
         Required.
        :type scope: str
        :param solution_resource_name: Solution resource Name. Required.
        :type solution_resource_name: str
        :param solution_patch_request_body: The required request body for updating a solution resource.
         Is either a SolutionPatchRequestBody type or a IO type. Default value is None.
        :type solution_patch_request_body: ~azure.mgmt.selfhelp.models.SolutionPatchRequestBody or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either SolutionResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.selfhelp.models.SolutionResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SolutionResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                scope=scope,
                solution_resource_name=solution_resource_name,
                solution_patch_request_body=solution_patch_request_body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("SolutionResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_update.metadata = {"url": "/{scope}/providers/Microsoft.Help/solutions/{solutionResourceName}"}
