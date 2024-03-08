# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._disk_pools_operations import DiskPoolsOperations
from ._disk_pool_zones_operations import DiskPoolZonesOperations
from ._resource_skus_operations import ResourceSkusOperations
from ._iscsi_targets_operations import IscsiTargetsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "DiskPoolsOperations",
    "DiskPoolZonesOperations",
    "ResourceSkusOperations",
    "IscsiTargetsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
