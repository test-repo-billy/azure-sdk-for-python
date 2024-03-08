# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class FleetMemberProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the last accepted operation."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    JOINING = "Joining"
    """The provisioning state of a member joining a fleet."""
    LEAVING = "Leaving"
    """The provisioning state of a member leaving a fleet."""
    UPDATING = "Updating"
    """The provisioning state of a member being updated."""


class FleetProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the last accepted operation."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    CREATING = "Creating"
    """The provisioning state of a fleet being created."""
    UPDATING = "Updating"
    """The provisioning state of a fleet being updated."""
    DELETING = "Deleting"
    """The provisioning state of a fleet being deleted."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"
