# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzStackHCIClusterProperties
from ._models_py3 import AzStackHCIFabricModelCustomProperties
from ._models_py3 import CheckNameAvailabilityModel
from ._models_py3 import CheckNameAvailabilityResponseModel
from ._models_py3 import DeploymentPreflightModel
from ._models_py3 import DeploymentPreflightResource
from ._models_py3 import DraModel
from ._models_py3 import DraModelCollection
from ._models_py3 import DraModelCustomProperties
from ._models_py3 import DraModelProperties
from ._models_py3 import DraModelSystemData
from ._models_py3 import EmailConfigurationModel
from ._models_py3 import EmailConfigurationModelCollection
from ._models_py3 import EmailConfigurationModelProperties
from ._models_py3 import EmailConfigurationModelSystemData
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorModel
from ._models_py3 import ErrorResponse
from ._models_py3 import EventModel
from ._models_py3 import EventModelCollection
from ._models_py3 import EventModelCustomProperties
from ._models_py3 import EventModelProperties
from ._models_py3 import EventModelSystemData
from ._models_py3 import FabricModel
from ._models_py3 import FabricModelCollection
from ._models_py3 import FabricModelCustomProperties
from ._models_py3 import FabricModelProperties
from ._models_py3 import FabricModelSystemData
from ._models_py3 import FabricModelUpdate
from ._models_py3 import FabricModelUpdateSystemData
from ._models_py3 import FailoverProtectedItemProperties
from ._models_py3 import FailoverWorkflowModelCustomProperties
from ._models_py3 import HealthErrorModel
from ._models_py3 import HyperVMigrateFabricModelCustomProperties
from ._models_py3 import HyperVToAzStackHCIDiskInput
from ._models_py3 import HyperVToAzStackHCIEventModelCustomProperties
from ._models_py3 import HyperVToAzStackHCINicInput
from ._models_py3 import HyperVToAzStackHCIPlannedFailoverModelCustomProperties
from ._models_py3 import HyperVToAzStackHCIPolicyModelCustomProperties
from ._models_py3 import HyperVToAzStackHCIProtectedDiskProperties
from ._models_py3 import HyperVToAzStackHCIProtectedItemModelCustomProperties
from ._models_py3 import HyperVToAzStackHCIProtectedNicProperties
from ._models_py3 import HyperVToAzStackHCIRecoveryPointModelCustomProperties
from ._models_py3 import HyperVToAzStackHCIReplicationExtensionModelCustomProperties
from ._models_py3 import IdentityModel
from ._models_py3 import InnerHealthErrorModel
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationModel
from ._models_py3 import OperationModelCollection
from ._models_py3 import OperationModelProperties
from ._models_py3 import OperationStatus
from ._models_py3 import PlannedFailoverModel
from ._models_py3 import PlannedFailoverModelCustomProperties
from ._models_py3 import PlannedFailoverModelProperties
from ._models_py3 import PolicyModel
from ._models_py3 import PolicyModelCollection
from ._models_py3 import PolicyModelCustomProperties
from ._models_py3 import PolicyModelProperties
from ._models_py3 import PolicyModelSystemData
from ._models_py3 import ProtectedItemDynamicMemoryConfig
from ._models_py3 import ProtectedItemJobProperties
from ._models_py3 import ProtectedItemModel
from ._models_py3 import ProtectedItemModelCollection
from ._models_py3 import ProtectedItemModelCustomProperties
from ._models_py3 import ProtectedItemModelProperties
from ._models_py3 import ProtectedItemModelPropertiesCurrentJob
from ._models_py3 import ProtectedItemModelPropertiesLastFailedEnableProtectionJob
from ._models_py3 import ProtectedItemModelPropertiesLastFailedPlannedFailoverJob
from ._models_py3 import ProtectedItemModelPropertiesLastTestFailoverJob
from ._models_py3 import ProtectedItemModelSystemData
from ._models_py3 import RecoveryPointModel
from ._models_py3 import RecoveryPointModelCollection
from ._models_py3 import RecoveryPointModelCustomProperties
from ._models_py3 import RecoveryPointModelProperties
from ._models_py3 import RecoveryPointModelSystemData
from ._models_py3 import ReplicationExtensionModel
from ._models_py3 import ReplicationExtensionModelCollection
from ._models_py3 import ReplicationExtensionModelCustomProperties
from ._models_py3 import ReplicationExtensionModelProperties
from ._models_py3 import ReplicationExtensionModelSystemData
from ._models_py3 import StorageContainerProperties
from ._models_py3 import SystemDataModel
from ._models_py3 import TaskModel
from ._models_py3 import TaskModelCustomProperties
from ._models_py3 import TestFailoverCleanupWorkflowModelCustomProperties
from ._models_py3 import TestFailoverWorkflowModelCustomProperties
from ._models_py3 import VMwareDraModelCustomProperties
from ._models_py3 import VMwareMigrateFabricModelCustomProperties
from ._models_py3 import VMwareToAzStackHCIDiskInput
from ._models_py3 import VMwareToAzStackHCINicInput
from ._models_py3 import VMwareToAzStackHCIPlannedFailoverModelCustomProperties
from ._models_py3 import VMwareToAzStackHCIPolicyModelCustomProperties
from ._models_py3 import VMwareToAzStackHCIProtectedDiskProperties
from ._models_py3 import VMwareToAzStackHCIProtectedItemModelCustomProperties
from ._models_py3 import VMwareToAzStackHCIProtectedNicProperties
from ._models_py3 import VMwareToAzStackHCIReplicationExtensionModelCustomProperties
from ._models_py3 import VaultModel
from ._models_py3 import VaultModelCollection
from ._models_py3 import VaultModelProperties
from ._models_py3 import VaultModelSystemData
from ._models_py3 import VaultModelUpdate
from ._models_py3 import VaultModelUpdateSystemData
from ._models_py3 import WorkflowModel
from ._models_py3 import WorkflowModelCollection
from ._models_py3 import WorkflowModelCustomProperties
from ._models_py3 import WorkflowModelProperties
from ._models_py3 import WorkflowModelSystemData

from ._recovery_services_data_replication_mgmt_client_enums import ActionType
from ._recovery_services_data_replication_mgmt_client_enums import HealthStatus
from ._recovery_services_data_replication_mgmt_client_enums import Origin
from ._recovery_services_data_replication_mgmt_client_enums import ProtectedItemActiveLocation
from ._recovery_services_data_replication_mgmt_client_enums import ProtectionState
from ._recovery_services_data_replication_mgmt_client_enums import ProvisioningState
from ._recovery_services_data_replication_mgmt_client_enums import RecoveryPointType
from ._recovery_services_data_replication_mgmt_client_enums import ReplicationVaultType
from ._recovery_services_data_replication_mgmt_client_enums import ResynchronizationState
from ._recovery_services_data_replication_mgmt_client_enums import TaskState
from ._recovery_services_data_replication_mgmt_client_enums import TestFailoverState
from ._recovery_services_data_replication_mgmt_client_enums import VMNicSelection
from ._recovery_services_data_replication_mgmt_client_enums import VMwareToAzureMigrateResyncState
from ._recovery_services_data_replication_mgmt_client_enums import WorkflowObjectType
from ._recovery_services_data_replication_mgmt_client_enums import WorkflowState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzStackHCIClusterProperties",
    "AzStackHCIFabricModelCustomProperties",
    "CheckNameAvailabilityModel",
    "CheckNameAvailabilityResponseModel",
    "DeploymentPreflightModel",
    "DeploymentPreflightResource",
    "DraModel",
    "DraModelCollection",
    "DraModelCustomProperties",
    "DraModelProperties",
    "DraModelSystemData",
    "EmailConfigurationModel",
    "EmailConfigurationModelCollection",
    "EmailConfigurationModelProperties",
    "EmailConfigurationModelSystemData",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorModel",
    "ErrorResponse",
    "EventModel",
    "EventModelCollection",
    "EventModelCustomProperties",
    "EventModelProperties",
    "EventModelSystemData",
    "FabricModel",
    "FabricModelCollection",
    "FabricModelCustomProperties",
    "FabricModelProperties",
    "FabricModelSystemData",
    "FabricModelUpdate",
    "FabricModelUpdateSystemData",
    "FailoverProtectedItemProperties",
    "FailoverWorkflowModelCustomProperties",
    "HealthErrorModel",
    "HyperVMigrateFabricModelCustomProperties",
    "HyperVToAzStackHCIDiskInput",
    "HyperVToAzStackHCIEventModelCustomProperties",
    "HyperVToAzStackHCINicInput",
    "HyperVToAzStackHCIPlannedFailoverModelCustomProperties",
    "HyperVToAzStackHCIPolicyModelCustomProperties",
    "HyperVToAzStackHCIProtectedDiskProperties",
    "HyperVToAzStackHCIProtectedItemModelCustomProperties",
    "HyperVToAzStackHCIProtectedNicProperties",
    "HyperVToAzStackHCIRecoveryPointModelCustomProperties",
    "HyperVToAzStackHCIReplicationExtensionModelCustomProperties",
    "IdentityModel",
    "InnerHealthErrorModel",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationModel",
    "OperationModelCollection",
    "OperationModelProperties",
    "OperationStatus",
    "PlannedFailoverModel",
    "PlannedFailoverModelCustomProperties",
    "PlannedFailoverModelProperties",
    "PolicyModel",
    "PolicyModelCollection",
    "PolicyModelCustomProperties",
    "PolicyModelProperties",
    "PolicyModelSystemData",
    "ProtectedItemDynamicMemoryConfig",
    "ProtectedItemJobProperties",
    "ProtectedItemModel",
    "ProtectedItemModelCollection",
    "ProtectedItemModelCustomProperties",
    "ProtectedItemModelProperties",
    "ProtectedItemModelPropertiesCurrentJob",
    "ProtectedItemModelPropertiesLastFailedEnableProtectionJob",
    "ProtectedItemModelPropertiesLastFailedPlannedFailoverJob",
    "ProtectedItemModelPropertiesLastTestFailoverJob",
    "ProtectedItemModelSystemData",
    "RecoveryPointModel",
    "RecoveryPointModelCollection",
    "RecoveryPointModelCustomProperties",
    "RecoveryPointModelProperties",
    "RecoveryPointModelSystemData",
    "ReplicationExtensionModel",
    "ReplicationExtensionModelCollection",
    "ReplicationExtensionModelCustomProperties",
    "ReplicationExtensionModelProperties",
    "ReplicationExtensionModelSystemData",
    "StorageContainerProperties",
    "SystemDataModel",
    "TaskModel",
    "TaskModelCustomProperties",
    "TestFailoverCleanupWorkflowModelCustomProperties",
    "TestFailoverWorkflowModelCustomProperties",
    "VMwareDraModelCustomProperties",
    "VMwareMigrateFabricModelCustomProperties",
    "VMwareToAzStackHCIDiskInput",
    "VMwareToAzStackHCINicInput",
    "VMwareToAzStackHCIPlannedFailoverModelCustomProperties",
    "VMwareToAzStackHCIPolicyModelCustomProperties",
    "VMwareToAzStackHCIProtectedDiskProperties",
    "VMwareToAzStackHCIProtectedItemModelCustomProperties",
    "VMwareToAzStackHCIProtectedNicProperties",
    "VMwareToAzStackHCIReplicationExtensionModelCustomProperties",
    "VaultModel",
    "VaultModelCollection",
    "VaultModelProperties",
    "VaultModelSystemData",
    "VaultModelUpdate",
    "VaultModelUpdateSystemData",
    "WorkflowModel",
    "WorkflowModelCollection",
    "WorkflowModelCustomProperties",
    "WorkflowModelProperties",
    "WorkflowModelSystemData",
    "ActionType",
    "HealthStatus",
    "Origin",
    "ProtectedItemActiveLocation",
    "ProtectionState",
    "ProvisioningState",
    "RecoveryPointType",
    "ReplicationVaultType",
    "ResynchronizationState",
    "TaskState",
    "TestFailoverState",
    "VMNicSelection",
    "VMwareToAzureMigrateResyncState",
    "WorkflowObjectType",
    "WorkflowState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
