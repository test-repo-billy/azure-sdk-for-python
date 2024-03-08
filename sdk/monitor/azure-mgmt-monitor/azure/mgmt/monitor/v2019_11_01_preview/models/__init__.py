# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureMonitorMetricsDestination
from ._models_py3 import DataCollectionRule
from ._models_py3 import DataCollectionRuleAssociation
from ._models_py3 import DataCollectionRuleAssociationProxyOnlyResource
from ._models_py3 import DataCollectionRuleAssociationProxyOnlyResourceListResult
from ._models_py3 import DataCollectionRuleAssociationProxyOnlyResourceProperties
from ._models_py3 import DataCollectionRuleDataSources
from ._models_py3 import DataCollectionRuleDestinations
from ._models_py3 import DataCollectionRuleResource
from ._models_py3 import DataCollectionRuleResourceListResult
from ._models_py3 import DataCollectionRuleResourceProperties
from ._models_py3 import DataFlow
from ._models_py3 import DataSourcesSpec
from ._models_py3 import DestinationsSpec
from ._models_py3 import DestinationsSpecAzureMonitorMetrics
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExtensionDataSource
from ._models_py3 import LogAnalyticsDestination
from ._models_py3 import PerfCounterDataSource
from ._models_py3 import ResourceForUpdate
from ._models_py3 import SyslogDataSource
from ._models_py3 import WindowsEventLogDataSource

from ._monitor_management_client_enums import KnownDataCollectionRuleAssociationProvisioningState
from ._monitor_management_client_enums import KnownDataCollectionRuleProvisioningState
from ._monitor_management_client_enums import KnownDataCollectionRuleResourceKind
from ._monitor_management_client_enums import KnownDataFlowStreams
from ._monitor_management_client_enums import KnownExtensionDataSourceStreams
from ._monitor_management_client_enums import KnownPerfCounterDataSourceStreams
from ._monitor_management_client_enums import KnownSyslogDataSourceFacilityNames
from ._monitor_management_client_enums import KnownSyslogDataSourceLogLevels
from ._monitor_management_client_enums import KnownSyslogDataSourceStreams
from ._monitor_management_client_enums import KnownWindowsEventLogDataSourceStreams
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureMonitorMetricsDestination",
    "DataCollectionRule",
    "DataCollectionRuleAssociation",
    "DataCollectionRuleAssociationProxyOnlyResource",
    "DataCollectionRuleAssociationProxyOnlyResourceListResult",
    "DataCollectionRuleAssociationProxyOnlyResourceProperties",
    "DataCollectionRuleDataSources",
    "DataCollectionRuleDestinations",
    "DataCollectionRuleResource",
    "DataCollectionRuleResourceListResult",
    "DataCollectionRuleResourceProperties",
    "DataFlow",
    "DataSourcesSpec",
    "DestinationsSpec",
    "DestinationsSpecAzureMonitorMetrics",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtensionDataSource",
    "LogAnalyticsDestination",
    "PerfCounterDataSource",
    "ResourceForUpdate",
    "SyslogDataSource",
    "WindowsEventLogDataSource",
    "KnownDataCollectionRuleAssociationProvisioningState",
    "KnownDataCollectionRuleProvisioningState",
    "KnownDataCollectionRuleResourceKind",
    "KnownDataFlowStreams",
    "KnownExtensionDataSourceStreams",
    "KnownPerfCounterDataSourceStreams",
    "KnownSyslogDataSourceFacilityNames",
    "KnownSyslogDataSourceLogLevels",
    "KnownSyslogDataSourceStreams",
    "KnownWindowsEventLogDataSourceStreams",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
