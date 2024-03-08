# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AuthorizationManagementClientConfiguration
from .operations import (
    EligibleChildResourcesOperations,
    RoleAssignmentScheduleInstancesOperations,
    RoleAssignmentScheduleRequestsOperations,
    RoleAssignmentSchedulesOperations,
    RoleAssignmentsOperations,
    RoleEligibilityScheduleInstancesOperations,
    RoleEligibilityScheduleRequestsOperations,
    RoleEligibilitySchedulesOperations,
    RoleManagementPoliciesOperations,
    RoleManagementPolicyAssignmentsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AuthorizationManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Role based access control provides you a way to apply granular level policy administration down
    to individual resources or resource groups. These operations enable you to manage role
    assignments. A role assignment grants access to Azure Active Directory users.

    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentsOperations
    :ivar eligible_child_resources: EligibleChildResourcesOperations operations
    :vartype eligible_child_resources:
     azure.mgmt.authorization.v2020_10_01_preview.operations.EligibleChildResourcesOperations
    :ivar role_assignment_schedules: RoleAssignmentSchedulesOperations operations
    :vartype role_assignment_schedules:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentSchedulesOperations
    :ivar role_assignment_schedule_instances: RoleAssignmentScheduleInstancesOperations operations
    :vartype role_assignment_schedule_instances:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentScheduleInstancesOperations
    :ivar role_assignment_schedule_requests: RoleAssignmentScheduleRequestsOperations operations
    :vartype role_assignment_schedule_requests:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentScheduleRequestsOperations
    :ivar role_eligibility_schedules: RoleEligibilitySchedulesOperations operations
    :vartype role_eligibility_schedules:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilitySchedulesOperations
    :ivar role_eligibility_schedule_instances: RoleEligibilityScheduleInstancesOperations
     operations
    :vartype role_eligibility_schedule_instances:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilityScheduleInstancesOperations
    :ivar role_eligibility_schedule_requests: RoleEligibilityScheduleRequestsOperations operations
    :vartype role_eligibility_schedule_requests:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilityScheduleRequestsOperations
    :ivar role_management_policies: RoleManagementPoliciesOperations operations
    :vartype role_management_policies:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleManagementPoliciesOperations
    :ivar role_management_policy_assignments: RoleManagementPolicyAssignmentsOperations operations
    :vartype role_management_policy_assignments:
     azure.mgmt.authorization.v2020_10_01_preview.operations.RoleManagementPolicyAssignmentsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-10-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AuthorizationManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.eligible_child_resources = EligibleChildResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_assignment_schedules = RoleAssignmentSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_assignment_schedule_instances = RoleAssignmentScheduleInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_assignment_schedule_requests = RoleAssignmentScheduleRequestsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_eligibility_schedules = RoleEligibilitySchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_eligibility_schedule_instances = RoleEligibilityScheduleInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_eligibility_schedule_requests = RoleEligibilityScheduleRequestsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_management_policies = RoleManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )
        self.role_management_policy_assignments = RoleManagementPolicyAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2020-10-01-preview"
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AuthorizationManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
