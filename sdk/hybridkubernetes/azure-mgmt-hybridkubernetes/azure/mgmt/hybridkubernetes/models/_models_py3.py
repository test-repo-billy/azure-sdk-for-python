# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class ConnectedCluster(TrackedResource):  # pylint: disable=too-many-instance-attributes
    """Represents a connected cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar identity: The identity of the connected cluster. Required.
    :vartype identity: ~azure.mgmt.hybridkubernetes.models.ConnectedClusterIdentity
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.hybridkubernetes.models.SystemData
    :ivar agent_public_key_certificate: Base64 encoded public certificate used by the agent to do
     the initial handshake to the backend services in Azure. Required.
    :vartype agent_public_key_certificate: str
    :ivar kubernetes_version: The Kubernetes version of the connected cluster resource.
    :vartype kubernetes_version: str
    :ivar total_node_count: Number of nodes present in the connected cluster resource.
    :vartype total_node_count: int
    :ivar total_core_count: Number of CPU cores present in the connected cluster resource.
    :vartype total_core_count: int
    :ivar agent_version: Version of the agent running on the connected cluster resource.
    :vartype agent_version: str
    :ivar provisioning_state: Provisioning state of the connected cluster resource. Known values
     are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.mgmt.hybridkubernetes.models.ProvisioningState
    :ivar distribution: The Kubernetes distribution running on this connected cluster.
    :vartype distribution: str
    :ivar infrastructure: The infrastructure on which the Kubernetes cluster represented by this
     connected cluster is running on.
    :vartype infrastructure: str
    :ivar offering: Connected cluster offering.
    :vartype offering: str
    :ivar managed_identity_certificate_expiration_time: Expiration time of the managed identity
     certificate.
    :vartype managed_identity_certificate_expiration_time: ~datetime.datetime
    :ivar last_connectivity_time: Time representing the last instance when heart beat was received
     from the cluster.
    :vartype last_connectivity_time: ~datetime.datetime
    :ivar connectivity_status: Represents the connectivity status of the connected cluster. Known
     values are: "Connecting", "Connected", "Offline", and "Expired".
    :vartype connectivity_status: str or ~azure.mgmt.hybridkubernetes.models.ConnectivityStatus
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "identity": {"required": True},
        "system_data": {"readonly": True},
        "agent_public_key_certificate": {"required": True},
        "kubernetes_version": {"readonly": True},
        "total_node_count": {"readonly": True},
        "total_core_count": {"readonly": True},
        "agent_version": {"readonly": True},
        "offering": {"readonly": True},
        "managed_identity_certificate_expiration_time": {"readonly": True},
        "last_connectivity_time": {"readonly": True},
        "connectivity_status": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "identity": {"key": "identity", "type": "ConnectedClusterIdentity"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "agent_public_key_certificate": {"key": "properties.agentPublicKeyCertificate", "type": "str"},
        "kubernetes_version": {"key": "properties.kubernetesVersion", "type": "str"},
        "total_node_count": {"key": "properties.totalNodeCount", "type": "int"},
        "total_core_count": {"key": "properties.totalCoreCount", "type": "int"},
        "agent_version": {"key": "properties.agentVersion", "type": "str"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "distribution": {"key": "properties.distribution", "type": "str"},
        "infrastructure": {"key": "properties.infrastructure", "type": "str"},
        "offering": {"key": "properties.offering", "type": "str"},
        "managed_identity_certificate_expiration_time": {
            "key": "properties.managedIdentityCertificateExpirationTime",
            "type": "iso-8601",
        },
        "last_connectivity_time": {"key": "properties.lastConnectivityTime", "type": "iso-8601"},
        "connectivity_status": {"key": "properties.connectivityStatus", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        identity: "_models.ConnectedClusterIdentity",
        agent_public_key_certificate: str,
        tags: Optional[Dict[str, str]] = None,
        provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = None,
        distribution: Optional[str] = None,
        infrastructure: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword identity: The identity of the connected cluster. Required.
        :paramtype identity: ~azure.mgmt.hybridkubernetes.models.ConnectedClusterIdentity
        :keyword agent_public_key_certificate: Base64 encoded public certificate used by the agent to
         do the initial handshake to the backend services in Azure. Required.
        :paramtype agent_public_key_certificate: str
        :keyword provisioning_state: Provisioning state of the connected cluster resource. Known values
         are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
        :paramtype provisioning_state: str or ~azure.mgmt.hybridkubernetes.models.ProvisioningState
        :keyword distribution: The Kubernetes distribution running on this connected cluster.
        :paramtype distribution: str
        :keyword infrastructure: The infrastructure on which the Kubernetes cluster represented by this
         connected cluster is running on.
        :paramtype infrastructure: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.identity = identity
        self.system_data = None
        self.agent_public_key_certificate = agent_public_key_certificate
        self.kubernetes_version = None
        self.total_node_count = None
        self.total_core_count = None
        self.agent_version = None
        self.provisioning_state = provisioning_state
        self.distribution = distribution
        self.infrastructure = infrastructure
        self.offering = None
        self.managed_identity_certificate_expiration_time = None
        self.last_connectivity_time = None
        self.connectivity_status = None


class ConnectedClusterIdentity(_serialization.Model):
    """Identity for the connected cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar principal_id: The principal id of connected cluster identity. This property will only be
     provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the connected cluster. This property will only
     be provided for a system assigned identity.
    :vartype tenant_id: str
    :ivar type: The type of identity used for the connected cluster. The type 'SystemAssigned,
     includes a system created identity. The type 'None' means no identity is assigned to the
     connected cluster. Known values are: "None" and "SystemAssigned".
    :vartype type: str or ~azure.mgmt.hybridkubernetes.models.ResourceIdentityType
    """

    _validation = {
        "principal_id": {"readonly": True},
        "tenant_id": {"readonly": True},
        "type": {"required": True},
    }

    _attribute_map = {
        "principal_id": {"key": "principalId", "type": "str"},
        "tenant_id": {"key": "tenantId", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, *, type: Union[str, "_models.ResourceIdentityType"] = "SystemAssigned", **kwargs):
        """
        :keyword type: The type of identity used for the connected cluster. The type 'SystemAssigned,
         includes a system created identity. The type 'None' means no identity is assigned to the
         connected cluster. Known values are: "None" and "SystemAssigned".
        :paramtype type: str or ~azure.mgmt.hybridkubernetes.models.ResourceIdentityType
        """
        super().__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class ConnectedClusterList(_serialization.Model):
    """The paginated list of connected Clusters.

    :ivar value: The list of connected clusters.
    :vartype value: list[~azure.mgmt.hybridkubernetes.models.ConnectedCluster]
    :ivar next_link: The link to fetch the next page of connected cluster.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[ConnectedCluster]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.ConnectedCluster"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: The list of connected clusters.
        :paramtype value: list[~azure.mgmt.hybridkubernetes.models.ConnectedCluster]
        :keyword next_link: The link to fetch the next page of connected cluster.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ConnectedClusterPatch(_serialization.Model):
    """Object containing updates for patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: Describes the connected cluster resource properties that can be updated
     during PATCH operation.
    :vartype properties: JSON
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "properties": {"key": "properties", "type": "object"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, properties: Optional[JSON] = None, **kwargs):
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword properties: Describes the connected cluster resource properties that can be updated
         during PATCH operation.
        :paramtype properties: JSON
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.properties = properties


class CredentialResult(_serialization.Model):
    """The credential result response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the credential.
    :vartype name: str
    :ivar value: Base64-encoded Kubernetes configuration file.
    :vartype value: bytes
    """

    _validation = {
        "name": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "value": {"key": "value", "type": "bytearray"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.name = None
        self.value = None


class CredentialResults(_serialization.Model):
    """The list of credential result response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar hybrid_connection_config: Contains the REP (rendezvous endpoint) and “Sender” access
     token.
    :vartype hybrid_connection_config: ~azure.mgmt.hybridkubernetes.models.HybridConnectionConfig
    :ivar kubeconfigs: Base64-encoded Kubernetes configuration file.
    :vartype kubeconfigs: list[~azure.mgmt.hybridkubernetes.models.CredentialResult]
    """

    _validation = {
        "hybrid_connection_config": {"readonly": True},
        "kubeconfigs": {"readonly": True},
    }

    _attribute_map = {
        "hybrid_connection_config": {"key": "hybridConnectionConfig", "type": "HybridConnectionConfig"},
        "kubeconfigs": {"key": "kubeconfigs", "type": "[CredentialResult]"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.hybrid_connection_config = None
        self.kubeconfigs = None


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.hybridkubernetes.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.hybridkubernetes.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.hybridkubernetes.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs):
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.hybridkubernetes.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class HybridConnectionConfig(_serialization.Model):
    """Contains the REP (rendezvous endpoint) and “Sender” access token.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar expiration_time: Timestamp when this token will be expired.
    :vartype expiration_time: int
    :ivar hybrid_connection_name: Name of the connection.
    :vartype hybrid_connection_name: str
    :ivar relay: Name of the relay.
    :vartype relay: str
    :ivar token: Sender access token.
    :vartype token: str
    """

    _validation = {
        "expiration_time": {"readonly": True},
        "hybrid_connection_name": {"readonly": True},
        "relay": {"readonly": True},
        "token": {"readonly": True},
    }

    _attribute_map = {
        "expiration_time": {"key": "expirationTime", "type": "int"},
        "hybrid_connection_name": {"key": "hybridConnectionName", "type": "str"},
        "relay": {"key": "relay", "type": "str"},
        "token": {"key": "token", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.expiration_time = None
        self.hybrid_connection_name = None
        self.relay = None
        self.token = None


class ListClusterUserCredentialProperties(_serialization.Model):
    """ListClusterUserCredentialProperties.

    All required parameters must be populated in order to send to Azure.

    :ivar authentication_method: The mode of client authentication. Required. Known values are:
     "Token" and "AAD".
    :vartype authentication_method: str or ~azure.mgmt.hybridkubernetes.models.AuthenticationMethod
    :ivar client_proxy: Boolean value to indicate whether the request is for client side proxy or
     not. Required.
    :vartype client_proxy: bool
    """

    _validation = {
        "authentication_method": {"required": True},
        "client_proxy": {"required": True},
    }

    _attribute_map = {
        "authentication_method": {"key": "authenticationMethod", "type": "str"},
        "client_proxy": {"key": "clientProxy", "type": "bool"},
    }

    def __init__(
        self, *, authentication_method: Union[str, "_models.AuthenticationMethod"], client_proxy: bool, **kwargs
    ):
        """
        :keyword authentication_method: The mode of client authentication. Required. Known values are:
         "Token" and "AAD".
        :paramtype authentication_method: str or
         ~azure.mgmt.hybridkubernetes.models.AuthenticationMethod
        :keyword client_proxy: Boolean value to indicate whether the request is for client side proxy
         or not. Required.
        :paramtype client_proxy: bool
        """
        super().__init__(**kwargs)
        self.authentication_method = authentication_method
        self.client_proxy = client_proxy


class Operation(_serialization.Model):
    """The Connected cluster API operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {Microsoft.Kubernetes}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that represents the operation.
    :vartype display: ~azure.mgmt.hybridkubernetes.models.OperationDisplay
    """

    _validation = {
        "name": {"readonly": True},
        "display": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "OperationDisplay"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.name = None
        self.display = None


class OperationDisplay(_serialization.Model):
    """The object that represents the operation.

    :ivar provider: Service provider: Microsoft.connectedClusters.
    :vartype provider: str
    :ivar resource: Connected Cluster Resource on which the operation is performed.
    :vartype resource: str
    :ivar operation: Operation type: Read, write, delete, etc.
    :vartype operation: str
    :ivar description: Description of the operation.
    :vartype description: str
    """

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword provider: Service provider: Microsoft.connectedClusters.
        :paramtype provider: str
        :keyword resource: Connected Cluster Resource on which the operation is performed.
        :paramtype resource: str
        :keyword operation: Operation type: Read, write, delete, etc.
        :paramtype operation: str
        :keyword description: Description of the operation.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(_serialization.Model):
    """The paginated list of connected cluster API operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The list of connected cluster API operations.
    :vartype value: list[~azure.mgmt.hybridkubernetes.models.Operation]
    :ivar next_link: The link to fetch the next page of connected cluster API operations.
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, next_link: Optional[str] = None, **kwargs):
        """
        :keyword next_link: The link to fetch the next page of connected cluster API operations.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = next_link


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.hybridkubernetes.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.hybridkubernetes.models.LastModifiedByType
    :ivar last_modified_at: The timestamp of resource modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.LastModifiedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.hybridkubernetes.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.hybridkubernetes.models.LastModifiedByType
        :keyword last_modified_at: The timestamp of resource modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
