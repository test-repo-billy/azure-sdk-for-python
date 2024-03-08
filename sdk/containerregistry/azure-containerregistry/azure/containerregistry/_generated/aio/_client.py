# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.7, generator: @autorest/python@6.7.8)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ContainerRegistryConfiguration
from .operations import AuthenticationOperations, ContainerRegistryBlobOperations, ContainerRegistryOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ContainerRegistry:  # pylint: disable=client-accepts-api-version-keyword
    """Metadata API definition for the Azure Container Registry runtime.

    :ivar container_registry: ContainerRegistryOperations operations
    :vartype container_registry: container_registry.aio.operations.ContainerRegistryOperations
    :ivar container_registry_blob: ContainerRegistryBlobOperations operations
    :vartype container_registry_blob:
     container_registry.aio.operations.ContainerRegistryBlobOperations
    :ivar authentication: AuthenticationOperations operations
    :vartype authentication: container_registry.aio.operations.AuthenticationOperations
    :param url: Registry login URL. Required.
    :type url: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2021-07-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, url: str, credential: "AsyncTokenCredential", **kwargs: Any) -> None:
        _endpoint = "{url}"
        self._config = ContainerRegistryConfiguration(url=url, credential=credential, **kwargs)
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models._models.__dict__.items() if isinstance(v, type)}
        client_models.update({k: v for k, v in _models.__dict__.items() if isinstance(v, type)})
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.container_registry = ContainerRegistryOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.container_registry_blob = ContainerRegistryBlobOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.authentication = AuthenticationOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "url": self._serialize.url("self._config.url", self._config.url, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerRegistry":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
