# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import RedisManagementClientConfiguration
from .operations import (
    AccessPolicyAssignmentOperations,
    AccessPolicyOperations,
    AsyncOperationStatusOperations,
    FirewallRulesOperations,
    LinkedServerOperations,
    Operations,
    PatchSchedulesOperations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    RedisOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class RedisManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """REST API for Azure Redis Cache Service.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.redis.aio.operations.Operations
    :ivar redis: RedisOperations operations
    :vartype redis: azure.mgmt.redis.aio.operations.RedisOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.redis.aio.operations.FirewallRulesOperations
    :ivar patch_schedules: PatchSchedulesOperations operations
    :vartype patch_schedules: azure.mgmt.redis.aio.operations.PatchSchedulesOperations
    :ivar linked_server: LinkedServerOperations operations
    :vartype linked_server: azure.mgmt.redis.aio.operations.LinkedServerOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.redis.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.redis.aio.operations.PrivateLinkResourcesOperations
    :ivar async_operation_status: AsyncOperationStatusOperations operations
    :vartype async_operation_status: azure.mgmt.redis.aio.operations.AsyncOperationStatusOperations
    :ivar access_policy: AccessPolicyOperations operations
    :vartype access_policy: azure.mgmt.redis.aio.operations.AccessPolicyOperations
    :ivar access_policy_assignment: AccessPolicyAssignmentOperations operations
    :vartype access_policy_assignment:
     azure.mgmt.redis.aio.operations.AccessPolicyAssignmentOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-08-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = RedisManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.redis = RedisOperations(self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.patch_schedules = PatchSchedulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.linked_server = LinkedServerOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.async_operation_status = AsyncOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.access_policy = AccessPolicyOperations(self._client, self._config, self._serialize, self._deserialize)
        self.access_policy_assignment = AccessPolicyAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "RedisManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
