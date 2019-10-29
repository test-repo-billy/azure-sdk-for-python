# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class ProfilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Profile <azure.mgmt.cdn.models.Profile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Profile]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProfilePaged, self).__init__(*args, **kwargs)
class ResourceUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceUsage <azure.mgmt.cdn.models.ResourceUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceUsagePaged, self).__init__(*args, **kwargs)
class EndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Endpoint <azure.mgmt.cdn.models.Endpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Endpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(EndpointPaged, self).__init__(*args, **kwargs)
class OriginPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Origin <azure.mgmt.cdn.models.Origin>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Origin]'}
    }

    def __init__(self, *args, **kwargs):

        super(OriginPaged, self).__init__(*args, **kwargs)
class OriginGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`OriginGroup <azure.mgmt.cdn.models.OriginGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OriginGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(OriginGroupPaged, self).__init__(*args, **kwargs)
class CustomDomainPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CustomDomain <azure.mgmt.cdn.models.CustomDomain>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CustomDomain]'}
    }

    def __init__(self, *args, **kwargs):

        super(CustomDomainPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.cdn.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class EdgeNodePaged(Paged):
    """
    A paging container for iterating over a list of :class:`EdgeNode <azure.mgmt.cdn.models.EdgeNode>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EdgeNode]'}
    }

    def __init__(self, *args, **kwargs):

        super(EdgeNodePaged, self).__init__(*args, **kwargs)
