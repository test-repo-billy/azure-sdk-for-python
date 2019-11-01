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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class AaaaRecord(Model):
    """An AAAA record.

    :param ipv6_address: The IPv6 address of this AAAA record.
    :type ipv6_address: str
    """

    _attribute_map = {
        'ipv6_address': {'key': 'ipv6Address', 'type': 'str'},
    }

    def __init__(self, *, ipv6_address: str=None, **kwargs) -> None:
        super(AaaaRecord, self).__init__(**kwargs)
        self.ipv6_address = ipv6_address


class ARecord(Model):
    """An A record.

    :param ipv4_address: The IPv4 address of this A record.
    :type ipv4_address: str
    """

    _attribute_map = {
        'ipv4_address': {'key': 'ipv4Address', 'type': 'str'},
    }

    def __init__(self, *, ipv4_address: str=None, **kwargs) -> None:
        super(ARecord, self).__init__(**kwargs)
        self.ipv4_address = ipv4_address


class CloudError(Model):
    """An error message.

    :param error: The error message body
    :type error: ~azure.mgmt.privatedns.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """The body of an error message.

    :param code: The error code
    :type code: str
    :param message: A description of what caused the error
    :type message: str
    :param target: The target resource of the error message
    :type target: str
    :param details: Extra error information
    :type details: list[~azure.mgmt.privatedns.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class CnameRecord(Model):
    """A CNAME record.

    :param cname: The canonical name for this CNAME record.
    :type cname: str
    """

    _attribute_map = {
        'cname': {'key': 'cname', 'type': 'str'},
    }

    def __init__(self, *, cname: str=None, **kwargs) -> None:
        super(CnameRecord, self).__init__(**kwargs)
        self.cname = cname


class MxRecord(Model):
    """An MX record.

    :param preference: The preference value for this MX record.
    :type preference: int
    :param exchange: The domain name of the mail host for this MX record.
    :type exchange: str
    """

    _attribute_map = {
        'preference': {'key': 'preference', 'type': 'int'},
        'exchange': {'key': 'exchange', 'type': 'str'},
    }

    def __init__(self, *, preference: int=None, exchange: str=None, **kwargs) -> None:
        super(MxRecord, self).__init__(**kwargs)
        self.preference = preference
        self.exchange = exchange


class Resource(Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class PrivateZone(TrackedResource):
    """Describes a Private DNS zone.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param etag: The ETag of the zone.
    :type etag: str
    :ivar max_number_of_record_sets: The maximum number of record sets that
     can be created in this Private DNS zone. This is a read-only property and
     any attempt to set this value will be ignored.
    :vartype max_number_of_record_sets: long
    :ivar number_of_record_sets: The current number of record sets in this
     Private DNS zone. This is a read-only property and any attempt to set this
     value will be ignored.
    :vartype number_of_record_sets: long
    :ivar max_number_of_virtual_network_links: The maximum number of virtual
     networks that can be linked to this Private DNS zone. This is a read-only
     property and any attempt to set this value will be ignored.
    :vartype max_number_of_virtual_network_links: long
    :ivar number_of_virtual_network_links: The current number of virtual
     networks that are linked to this Private DNS zone. This is a read-only
     property and any attempt to set this value will be ignored.
    :vartype number_of_virtual_network_links: long
    :ivar max_number_of_virtual_network_links_with_registration: The maximum
     number of virtual networks that can be linked to this Private DNS zone
     with registration enabled. This is a read-only property and any attempt to
     set this value will be ignored.
    :vartype max_number_of_virtual_network_links_with_registration: long
    :ivar number_of_virtual_network_links_with_registration: The current
     number of virtual networks that are linked to this Private DNS zone with
     registration enabled. This is a read-only property and any attempt to set
     this value will be ignored.
    :vartype number_of_virtual_network_links_with_registration: long
    :ivar provisioning_state: The provisioning state of the resource. This is
     a read-only property and any attempt to set this value will be ignored.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.privatedns.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'max_number_of_record_sets': {'readonly': True},
        'number_of_record_sets': {'readonly': True},
        'max_number_of_virtual_network_links': {'readonly': True},
        'number_of_virtual_network_links': {'readonly': True},
        'max_number_of_virtual_network_links_with_registration': {'readonly': True},
        'number_of_virtual_network_links_with_registration': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'max_number_of_record_sets': {'key': 'properties.maxNumberOfRecordSets', 'type': 'long'},
        'number_of_record_sets': {'key': 'properties.numberOfRecordSets', 'type': 'long'},
        'max_number_of_virtual_network_links': {'key': 'properties.maxNumberOfVirtualNetworkLinks', 'type': 'long'},
        'number_of_virtual_network_links': {'key': 'properties.numberOfVirtualNetworkLinks', 'type': 'long'},
        'max_number_of_virtual_network_links_with_registration': {'key': 'properties.maxNumberOfVirtualNetworkLinksWithRegistration', 'type': 'long'},
        'number_of_virtual_network_links_with_registration': {'key': 'properties.numberOfVirtualNetworkLinksWithRegistration', 'type': 'long'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, etag: str=None, **kwargs) -> None:
        super(PrivateZone, self).__init__(tags=tags, location=location, **kwargs)
        self.etag = etag
        self.max_number_of_record_sets = None
        self.number_of_record_sets = None
        self.max_number_of_virtual_network_links = None
        self.number_of_virtual_network_links = None
        self.max_number_of_virtual_network_links_with_registration = None
        self.number_of_virtual_network_links_with_registration = None
        self.provisioning_state = None


class ProxyResource(Resource):
    """The resource model definition for an ARM proxy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class PtrRecord(Model):
    """A PTR record.

    :param ptrdname: The PTR target domain name for this PTR record.
    :type ptrdname: str
    """

    _attribute_map = {
        'ptrdname': {'key': 'ptrdname', 'type': 'str'},
    }

    def __init__(self, *, ptrdname: str=None, **kwargs) -> None:
        super(PtrRecord, self).__init__(**kwargs)
        self.ptrdname = ptrdname


class RecordSet(ProxyResource):
    """Describes a DNS record set (a collection of DNS records with the same name
    and type) in a Private DNS zone.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    :param etag: The ETag of the record set.
    :type etag: str
    :param metadata: The metadata attached to the record set.
    :type metadata: dict[str, str]
    :param ttl: The TTL (time-to-live) of the records in the record set.
    :type ttl: long
    :ivar fqdn: Fully qualified domain name of the record set.
    :vartype fqdn: str
    :ivar is_auto_registered: Is the record set auto-registered in the Private
     DNS zone through a virtual network link?
    :vartype is_auto_registered: bool
    :param a_records: The list of A records in the record set.
    :type a_records: list[~azure.mgmt.privatedns.models.ARecord]
    :param aaaa_records: The list of AAAA records in the record set.
    :type aaaa_records: list[~azure.mgmt.privatedns.models.AaaaRecord]
    :param cname_record: The CNAME record in the record set.
    :type cname_record: ~azure.mgmt.privatedns.models.CnameRecord
    :param mx_records: The list of MX records in the record set.
    :type mx_records: list[~azure.mgmt.privatedns.models.MxRecord]
    :param ptr_records: The list of PTR records in the record set.
    :type ptr_records: list[~azure.mgmt.privatedns.models.PtrRecord]
    :param soa_record: The SOA record in the record set.
    :type soa_record: ~azure.mgmt.privatedns.models.SoaRecord
    :param srv_records: The list of SRV records in the record set.
    :type srv_records: list[~azure.mgmt.privatedns.models.SrvRecord]
    :param txt_records: The list of TXT records in the record set.
    :type txt_records: list[~azure.mgmt.privatedns.models.TxtRecord]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'fqdn': {'readonly': True},
        'is_auto_registered': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'ttl': {'key': 'properties.ttl', 'type': 'long'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'is_auto_registered': {'key': 'properties.isAutoRegistered', 'type': 'bool'},
        'a_records': {'key': 'properties.aRecords', 'type': '[ARecord]'},
        'aaaa_records': {'key': 'properties.aaaaRecords', 'type': '[AaaaRecord]'},
        'cname_record': {'key': 'properties.cnameRecord', 'type': 'CnameRecord'},
        'mx_records': {'key': 'properties.mxRecords', 'type': '[MxRecord]'},
        'ptr_records': {'key': 'properties.ptrRecords', 'type': '[PtrRecord]'},
        'soa_record': {'key': 'properties.soaRecord', 'type': 'SoaRecord'},
        'srv_records': {'key': 'properties.srvRecords', 'type': '[SrvRecord]'},
        'txt_records': {'key': 'properties.txtRecords', 'type': '[TxtRecord]'},
    }

    def __init__(self, *, etag: str=None, metadata=None, ttl: int=None, a_records=None, aaaa_records=None, cname_record=None, mx_records=None, ptr_records=None, soa_record=None, srv_records=None, txt_records=None, **kwargs) -> None:
        super(RecordSet, self).__init__(**kwargs)
        self.etag = etag
        self.metadata = metadata
        self.ttl = ttl
        self.fqdn = None
        self.is_auto_registered = None
        self.a_records = a_records
        self.aaaa_records = aaaa_records
        self.cname_record = cname_record
        self.mx_records = mx_records
        self.ptr_records = ptr_records
        self.soa_record = soa_record
        self.srv_records = srv_records
        self.txt_records = txt_records


class SoaRecord(Model):
    """An SOA record.

    :param host: The domain name of the authoritative name server for this SOA
     record.
    :type host: str
    :param email: The email contact for this SOA record.
    :type email: str
    :param serial_number: The serial number for this SOA record.
    :type serial_number: long
    :param refresh_time: The refresh value for this SOA record.
    :type refresh_time: long
    :param retry_time: The retry time for this SOA record.
    :type retry_time: long
    :param expire_time: The expire time for this SOA record.
    :type expire_time: long
    :param minimum_ttl: The minimum value for this SOA record. By convention
     this is used to determine the negative caching duration.
    :type minimum_ttl: long
    """

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'serial_number': {'key': 'serialNumber', 'type': 'long'},
        'refresh_time': {'key': 'refreshTime', 'type': 'long'},
        'retry_time': {'key': 'retryTime', 'type': 'long'},
        'expire_time': {'key': 'expireTime', 'type': 'long'},
        'minimum_ttl': {'key': 'minimumTtl', 'type': 'long'},
    }

    def __init__(self, *, host: str=None, email: str=None, serial_number: int=None, refresh_time: int=None, retry_time: int=None, expire_time: int=None, minimum_ttl: int=None, **kwargs) -> None:
        super(SoaRecord, self).__init__(**kwargs)
        self.host = host
        self.email = email
        self.serial_number = serial_number
        self.refresh_time = refresh_time
        self.retry_time = retry_time
        self.expire_time = expire_time
        self.minimum_ttl = minimum_ttl


class SrvRecord(Model):
    """An SRV record.

    :param priority: The priority value for this SRV record.
    :type priority: int
    :param weight: The weight value for this SRV record.
    :type weight: int
    :param port: The port value for this SRV record.
    :type port: int
    :param target: The target domain name for this SRV record.
    :type target: str
    """

    _attribute_map = {
        'priority': {'key': 'priority', 'type': 'int'},
        'weight': {'key': 'weight', 'type': 'int'},
        'port': {'key': 'port', 'type': 'int'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, *, priority: int=None, weight: int=None, port: int=None, target: str=None, **kwargs) -> None:
        super(SrvRecord, self).__init__(**kwargs)
        self.priority = priority
        self.weight = weight
        self.port = port
        self.target = target


class SubResource(Model):
    """Reference to another subresource.

    :param id: Resource ID.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(SubResource, self).__init__(**kwargs)
        self.id = id


class TxtRecord(Model):
    """A TXT record.

    :param value: The text value of this TXT record.
    :type value: list[str]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(TxtRecord, self).__init__(**kwargs)
        self.value = value


class VirtualNetworkLink(TrackedResource):
    """Describes a link to virtual network for a Private DNS zone.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param etag: The ETag of the virtual network link.
    :type etag: str
    :param virtual_network: The reference of the virtual network.
    :type virtual_network: ~azure.mgmt.privatedns.models.SubResource
    :param registration_enabled: Is auto-registration of virtual machine
     records in the virtual network in the Private DNS zone enabled?
    :type registration_enabled: bool
    :ivar virtual_network_link_state: The status of the virtual network link
     to the Private DNS zone. Possible values are 'InProgress' and 'Done'. This
     is a read-only property and any attempt to set this value will be ignored.
     Possible values include: 'InProgress', 'Completed'
    :vartype virtual_network_link_state: str or
     ~azure.mgmt.privatedns.models.VirtualNetworkLinkState
    :ivar provisioning_state: The provisioning state of the resource. This is
     a read-only property and any attempt to set this value will be ignored.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.privatedns.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_network_link_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'SubResource'},
        'registration_enabled': {'key': 'properties.registrationEnabled', 'type': 'bool'},
        'virtual_network_link_state': {'key': 'properties.virtualNetworkLinkState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, etag: str=None, virtual_network=None, registration_enabled: bool=None, **kwargs) -> None:
        super(VirtualNetworkLink, self).__init__(tags=tags, location=location, **kwargs)
        self.etag = etag
        self.virtual_network = virtual_network
        self.registration_enabled = registration_enabled
        self.virtual_network_link_state = None
        self.provisioning_state = None
