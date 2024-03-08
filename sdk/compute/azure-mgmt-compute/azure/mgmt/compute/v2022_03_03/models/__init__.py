# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiError
from ._models_py3 import ApiErrorBase
from ._models_py3 import CommunityGallery
from ._models_py3 import CommunityGalleryImage
from ._models_py3 import CommunityGalleryImageIdentifier
from ._models_py3 import CommunityGalleryImageList
from ._models_py3 import CommunityGalleryImageVersion
from ._models_py3 import CommunityGalleryImageVersionList
from ._models_py3 import CommunityGalleryInfo
from ._models_py3 import DataDiskImageEncryption
from ._models_py3 import Disallowed
from ._models_py3 import DiskImageEncryption
from ._models_py3 import EncryptionImages
from ._models_py3 import ExtendedLocation
from ._models_py3 import Gallery
from ._models_py3 import GalleryApplication
from ._models_py3 import GalleryApplicationCustomAction
from ._models_py3 import GalleryApplicationCustomActionParameter
from ._models_py3 import GalleryApplicationList
from ._models_py3 import GalleryApplicationUpdate
from ._models_py3 import GalleryApplicationVersion
from ._models_py3 import GalleryApplicationVersionList
from ._models_py3 import GalleryApplicationVersionPublishingProfile
from ._models_py3 import GalleryApplicationVersionSafetyProfile
from ._models_py3 import GalleryApplicationVersionUpdate
from ._models_py3 import GalleryArtifactPublishingProfileBase
from ._models_py3 import GalleryArtifactSafetyProfileBase
from ._models_py3 import GalleryArtifactSource
from ._models_py3 import GalleryArtifactVersionFullSource
from ._models_py3 import GalleryArtifactVersionSource
from ._models_py3 import GalleryDataDiskImage
from ._models_py3 import GalleryDiskImage
from ._models_py3 import GalleryDiskImageSource
from ._models_py3 import GalleryExtendedLocation
from ._models_py3 import GalleryIdentifier
from ._models_py3 import GalleryImage
from ._models_py3 import GalleryImageFeature
from ._models_py3 import GalleryImageIdentifier
from ._models_py3 import GalleryImageList
from ._models_py3 import GalleryImageUpdate
from ._models_py3 import GalleryImageVersion
from ._models_py3 import GalleryImageVersionList
from ._models_py3 import GalleryImageVersionPublishingProfile
from ._models_py3 import GalleryImageVersionSafetyProfile
from ._models_py3 import GalleryImageVersionStorageProfile
from ._models_py3 import GalleryImageVersionUpdate
from ._models_py3 import GalleryList
from ._models_py3 import GalleryOSDiskImage
from ._models_py3 import GalleryTargetExtendedLocation
from ._models_py3 import GalleryUpdate
from ._models_py3 import ImagePurchasePlan
from ._models_py3 import InnerError
from ._models_py3 import LatestGalleryImageVersion
from ._models_py3 import ManagedArtifact
from ._models_py3 import OSDiskImageEncryption
from ._models_py3 import OSDiskImageSecurityProfile
from ._models_py3 import PirCommunityGalleryResource
from ._models_py3 import PirResource
from ._models_py3 import PirSharedGalleryResource
from ._models_py3 import PolicyViolation
from ._models_py3 import RecommendedMachineConfiguration
from ._models_py3 import RegionalReplicationStatus
from ._models_py3 import RegionalSharingStatus
from ._models_py3 import ReplicationStatus
from ._models_py3 import Resource
from ._models_py3 import ResourceRange
from ._models_py3 import ResourceWithOptionalLocation
from ._models_py3 import SharedGallery
from ._models_py3 import SharedGalleryDataDiskImage
from ._models_py3 import SharedGalleryDiskImage
from ._models_py3 import SharedGalleryImage
from ._models_py3 import SharedGalleryImageList
from ._models_py3 import SharedGalleryImageVersion
from ._models_py3 import SharedGalleryImageVersionList
from ._models_py3 import SharedGalleryImageVersionStorageProfile
from ._models_py3 import SharedGalleryList
from ._models_py3 import SharedGalleryOSDiskImage
from ._models_py3 import SharingProfile
from ._models_py3 import SharingProfileGroup
from ._models_py3 import SharingStatus
from ._models_py3 import SharingUpdate
from ._models_py3 import SoftDeletePolicy
from ._models_py3 import SubResource
from ._models_py3 import SubResourceReadOnly
from ._models_py3 import SystemData
from ._models_py3 import TargetRegion
from ._models_py3 import UpdateResourceDefinition
from ._models_py3 import UserArtifactManage
from ._models_py3 import UserArtifactSettings
from ._models_py3 import UserArtifactSource
from ._models_py3 import UserAssignedIdentitiesValue

from ._compute_management_client_enums import AggregatedReplicationState
from ._compute_management_client_enums import Architecture
from ._compute_management_client_enums import ConfidentialVMEncryptionType
from ._compute_management_client_enums import EdgeZoneStorageAccountType
from ._compute_management_client_enums import ExtendedLocationTypes
from ._compute_management_client_enums import GalleryApplicationCustomActionParameterType
from ._compute_management_client_enums import GalleryExpandParams
from ._compute_management_client_enums import GalleryExtendedLocationType
from ._compute_management_client_enums import GalleryProvisioningState
from ._compute_management_client_enums import GallerySharingPermissionTypes
from ._compute_management_client_enums import HostCaching
from ._compute_management_client_enums import HyperVGeneration
from ._compute_management_client_enums import OperatingSystemStateTypes
from ._compute_management_client_enums import OperatingSystemTypes
from ._compute_management_client_enums import PolicyViolationCategory
from ._compute_management_client_enums import ReplicationMode
from ._compute_management_client_enums import ReplicationState
from ._compute_management_client_enums import ReplicationStatusTypes
from ._compute_management_client_enums import SelectPermissions
from ._compute_management_client_enums import SharedGalleryHostCaching
from ._compute_management_client_enums import SharedToValues
from ._compute_management_client_enums import SharingProfileGroupTypes
from ._compute_management_client_enums import SharingState
from ._compute_management_client_enums import SharingUpdateOperationTypes
from ._compute_management_client_enums import StorageAccountType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiError",
    "ApiErrorBase",
    "CommunityGallery",
    "CommunityGalleryImage",
    "CommunityGalleryImageIdentifier",
    "CommunityGalleryImageList",
    "CommunityGalleryImageVersion",
    "CommunityGalleryImageVersionList",
    "CommunityGalleryInfo",
    "DataDiskImageEncryption",
    "Disallowed",
    "DiskImageEncryption",
    "EncryptionImages",
    "ExtendedLocation",
    "Gallery",
    "GalleryApplication",
    "GalleryApplicationCustomAction",
    "GalleryApplicationCustomActionParameter",
    "GalleryApplicationList",
    "GalleryApplicationUpdate",
    "GalleryApplicationVersion",
    "GalleryApplicationVersionList",
    "GalleryApplicationVersionPublishingProfile",
    "GalleryApplicationVersionSafetyProfile",
    "GalleryApplicationVersionUpdate",
    "GalleryArtifactPublishingProfileBase",
    "GalleryArtifactSafetyProfileBase",
    "GalleryArtifactSource",
    "GalleryArtifactVersionFullSource",
    "GalleryArtifactVersionSource",
    "GalleryDataDiskImage",
    "GalleryDiskImage",
    "GalleryDiskImageSource",
    "GalleryExtendedLocation",
    "GalleryIdentifier",
    "GalleryImage",
    "GalleryImageFeature",
    "GalleryImageIdentifier",
    "GalleryImageList",
    "GalleryImageUpdate",
    "GalleryImageVersion",
    "GalleryImageVersionList",
    "GalleryImageVersionPublishingProfile",
    "GalleryImageVersionSafetyProfile",
    "GalleryImageVersionStorageProfile",
    "GalleryImageVersionUpdate",
    "GalleryList",
    "GalleryOSDiskImage",
    "GalleryTargetExtendedLocation",
    "GalleryUpdate",
    "ImagePurchasePlan",
    "InnerError",
    "LatestGalleryImageVersion",
    "ManagedArtifact",
    "OSDiskImageEncryption",
    "OSDiskImageSecurityProfile",
    "PirCommunityGalleryResource",
    "PirResource",
    "PirSharedGalleryResource",
    "PolicyViolation",
    "RecommendedMachineConfiguration",
    "RegionalReplicationStatus",
    "RegionalSharingStatus",
    "ReplicationStatus",
    "Resource",
    "ResourceRange",
    "ResourceWithOptionalLocation",
    "SharedGallery",
    "SharedGalleryDataDiskImage",
    "SharedGalleryDiskImage",
    "SharedGalleryImage",
    "SharedGalleryImageList",
    "SharedGalleryImageVersion",
    "SharedGalleryImageVersionList",
    "SharedGalleryImageVersionStorageProfile",
    "SharedGalleryList",
    "SharedGalleryOSDiskImage",
    "SharingProfile",
    "SharingProfileGroup",
    "SharingStatus",
    "SharingUpdate",
    "SoftDeletePolicy",
    "SubResource",
    "SubResourceReadOnly",
    "SystemData",
    "TargetRegion",
    "UpdateResourceDefinition",
    "UserArtifactManage",
    "UserArtifactSettings",
    "UserArtifactSource",
    "UserAssignedIdentitiesValue",
    "AggregatedReplicationState",
    "Architecture",
    "ConfidentialVMEncryptionType",
    "EdgeZoneStorageAccountType",
    "ExtendedLocationTypes",
    "GalleryApplicationCustomActionParameterType",
    "GalleryExpandParams",
    "GalleryExtendedLocationType",
    "GalleryProvisioningState",
    "GallerySharingPermissionTypes",
    "HostCaching",
    "HyperVGeneration",
    "OperatingSystemStateTypes",
    "OperatingSystemTypes",
    "PolicyViolationCategory",
    "ReplicationMode",
    "ReplicationState",
    "ReplicationStatusTypes",
    "SelectPermissions",
    "SharedGalleryHostCaching",
    "SharedToValues",
    "SharingProfileGroupTypes",
    "SharingState",
    "SharingUpdateOperationTypes",
    "StorageAccountType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
