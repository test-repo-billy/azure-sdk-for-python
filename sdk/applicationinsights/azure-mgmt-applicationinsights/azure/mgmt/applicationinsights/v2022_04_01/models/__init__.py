# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import Resource
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import Workbook
from ._models_py3 import WorkbookError
from ._models_py3 import WorkbookErrorDefinition
from ._models_py3 import WorkbookInnerErrorTrace
from ._models_py3 import WorkbookResource
from ._models_py3 import WorkbookResourceIdentity
from ._models_py3 import WorkbookUpdateParameters
from ._models_py3 import WorkbooksListResult

from ._application_insights_management_client_enums import CategoryType
from ._application_insights_management_client_enums import CreatedByType
from ._application_insights_management_client_enums import ManagedServiceIdentityType
from ._application_insights_management_client_enums import WorkbookSharedTypeKind
from ._application_insights_management_client_enums import WorkbookUpdateSharedTypeKind
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ManagedServiceIdentity",
    "Resource",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "Workbook",
    "WorkbookError",
    "WorkbookErrorDefinition",
    "WorkbookInnerErrorTrace",
    "WorkbookResource",
    "WorkbookResourceIdentity",
    "WorkbookUpdateParameters",
    "WorkbooksListResult",
    "CategoryType",
    "CreatedByType",
    "ManagedServiceIdentityType",
    "WorkbookSharedTypeKind",
    "WorkbookUpdateSharedTypeKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
