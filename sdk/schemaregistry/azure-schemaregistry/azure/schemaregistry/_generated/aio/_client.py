# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import AzureSchemaRegistryConfiguration
from .operations import SchemaOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class AzureSchemaRegistry:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Schema Registry is as a central schema repository, with support for versioning,
    management, compatibility checking, and RBAC.

    :ivar schema: SchemaOperations operations
    :vartype schema: azure.schemaregistry._generated.aio.operations.SchemaOperations
    :param endpoint: The Schema Registry service endpoint, for example
     my-namespace.servicebus.windows.net. Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword api_version: Api Version. Default value is "2023-07-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, endpoint: str, credential: "AsyncTokenCredential", **kwargs: Any) -> None:
        _endpoint = "https://{endpoint}"
        self._config = AzureSchemaRegistryConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client: AsyncPipelineClient = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.schema = SchemaOperations(self._client, self._config, self._serialize, self._deserialize)

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
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureSchemaRegistry":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
