# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._workspaces_operations import WorkspacesOperations
from ._usages_operations import UsagesOperations
from ._virtual_machine_sizes_operations import VirtualMachineSizesOperations
from ._quotas_operations import QuotasOperations
from ._compute_operations import ComputeOperations
from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._workspace_connections_operations import WorkspaceConnectionsOperations
from ._registry_code_containers_operations import RegistryCodeContainersOperations
from ._registry_code_versions_operations import RegistryCodeVersionsOperations
from ._registry_component_containers_operations import RegistryComponentContainersOperations
from ._registry_component_versions_operations import RegistryComponentVersionsOperations
from ._registry_data_containers_operations import RegistryDataContainersOperations
from ._registry_data_versions_operations import RegistryDataVersionsOperations
from ._registry_environment_containers_operations import RegistryEnvironmentContainersOperations
from ._registry_environment_versions_operations import RegistryEnvironmentVersionsOperations
from ._registry_model_containers_operations import RegistryModelContainersOperations
from ._registry_model_versions_operations import RegistryModelVersionsOperations
from ._batch_endpoints_operations import BatchEndpointsOperations
from ._batch_deployments_operations import BatchDeploymentsOperations
from ._code_containers_operations import CodeContainersOperations
from ._code_versions_operations import CodeVersionsOperations
from ._component_containers_operations import ComponentContainersOperations
from ._component_versions_operations import ComponentVersionsOperations
from ._data_containers_operations import DataContainersOperations
from ._data_versions_operations import DataVersionsOperations
from ._datastores_operations import DatastoresOperations
from ._environment_containers_operations import EnvironmentContainersOperations
from ._environment_versions_operations import EnvironmentVersionsOperations
from ._jobs_operations import JobsOperations
from ._model_containers_operations import ModelContainersOperations
from ._model_versions_operations import ModelVersionsOperations
from ._online_endpoints_operations import OnlineEndpointsOperations
from ._online_deployments_operations import OnlineDeploymentsOperations
from ._schedules_operations import SchedulesOperations
from ._registries_operations import RegistriesOperations
from ._workspace_features_operations import WorkspaceFeaturesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "WorkspacesOperations",
    "UsagesOperations",
    "VirtualMachineSizesOperations",
    "QuotasOperations",
    "ComputeOperations",
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "WorkspaceConnectionsOperations",
    "RegistryCodeContainersOperations",
    "RegistryCodeVersionsOperations",
    "RegistryComponentContainersOperations",
    "RegistryComponentVersionsOperations",
    "RegistryDataContainersOperations",
    "RegistryDataVersionsOperations",
    "RegistryEnvironmentContainersOperations",
    "RegistryEnvironmentVersionsOperations",
    "RegistryModelContainersOperations",
    "RegistryModelVersionsOperations",
    "BatchEndpointsOperations",
    "BatchDeploymentsOperations",
    "CodeContainersOperations",
    "CodeVersionsOperations",
    "ComponentContainersOperations",
    "ComponentVersionsOperations",
    "DataContainersOperations",
    "DataVersionsOperations",
    "DatastoresOperations",
    "EnvironmentContainersOperations",
    "EnvironmentVersionsOperations",
    "JobsOperations",
    "ModelContainersOperations",
    "ModelVersionsOperations",
    "OnlineEndpointsOperations",
    "OnlineDeploymentsOperations",
    "SchedulesOperations",
    "RegistriesOperations",
    "WorkspaceFeaturesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
