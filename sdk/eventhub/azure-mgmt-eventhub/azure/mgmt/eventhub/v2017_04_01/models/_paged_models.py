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


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.eventhub.v2017_04_01.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class EHNamespacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`EHNamespace <azure.mgmt.eventhub.v2017_04_01.models.EHNamespace>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EHNamespace]'}
    }

    def __init__(self, *args, **kwargs):

        super(EHNamespacePaged, self).__init__(*args, **kwargs)
class AuthorizationRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AuthorizationRule <azure.mgmt.eventhub.v2017_04_01.models.AuthorizationRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AuthorizationRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(AuthorizationRulePaged, self).__init__(*args, **kwargs)
class NetworkRuleSetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkRuleSet <azure.mgmt.eventhub.v2017_04_01.models.NetworkRuleSet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkRuleSet]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkRuleSetPaged, self).__init__(*args, **kwargs)
class ArmDisasterRecoveryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ArmDisasterRecovery <azure.mgmt.eventhub.v2017_04_01.models.ArmDisasterRecovery>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ArmDisasterRecovery]'}
    }

    def __init__(self, *args, **kwargs):

        super(ArmDisasterRecoveryPaged, self).__init__(*args, **kwargs)
class EventhubPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Eventhub <azure.mgmt.eventhub.v2017_04_01.models.Eventhub>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Eventhub]'}
    }

    def __init__(self, *args, **kwargs):

        super(EventhubPaged, self).__init__(*args, **kwargs)
class ConsumerGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ConsumerGroup <azure.mgmt.eventhub.v2017_04_01.models.ConsumerGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ConsumerGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConsumerGroupPaged, self).__init__(*args, **kwargs)
class MessagingRegionsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`MessagingRegions <azure.mgmt.eventhub.v2017_04_01.models.MessagingRegions>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MessagingRegions]'}
    }

    def __init__(self, *args, **kwargs):

        super(MessagingRegionsPaged, self).__init__(*args, **kwargs)
