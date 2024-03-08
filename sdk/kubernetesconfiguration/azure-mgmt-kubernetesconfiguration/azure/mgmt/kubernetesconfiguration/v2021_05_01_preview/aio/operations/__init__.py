# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._extensions_operations import ExtensionsOperations
from ._operation_status_operations import OperationStatusOperations
from ._cluster_extension_type_operations import ClusterExtensionTypeOperations
from ._cluster_extension_types_operations import ClusterExtensionTypesOperations
from ._extension_type_versions_operations import ExtensionTypeVersionsOperations
from ._location_extension_types_operations import LocationExtensionTypesOperations
from ._source_control_configurations_operations import SourceControlConfigurationsOperations
from ._operations import Operations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ExtensionsOperations",
    "OperationStatusOperations",
    "ClusterExtensionTypeOperations",
    "ClusterExtensionTypesOperations",
    "ExtensionTypeVersionsOperations",
    "LocationExtensionTypesOperations",
    "SourceControlConfigurationsOperations",
    "Operations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
