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

from enum import Enum


class SkuName(str, Enum):

    standard_verizon = "Standard_Verizon"
    premium_verizon = "Premium_Verizon"
    custom_verizon = "Custom_Verizon"
    standard_akamai = "Standard_Akamai"
    standard_china_cdn = "Standard_ChinaCdn"
    standard_microsoft = "Standard_Microsoft"
    premium_china_cdn = "Premium_ChinaCdn"


class ProfileResourceState(str, Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"
    disabled = "Disabled"


class OptimizationType(str, Enum):

    general_web_delivery = "GeneralWebDelivery"
    general_media_streaming = "GeneralMediaStreaming"
    video_on_demand_media_streaming = "VideoOnDemandMediaStreaming"
    large_file_download = "LargeFileDownload"
    dynamic_site_acceleration = "DynamicSiteAcceleration"


class HealthProbeRequestType(str, Enum):

    not_set = "NotSet"
    get = "GET"
    head = "HEAD"


class ProbeProtocol(str, Enum):

    not_set = "NotSet"
    http = "Http"
    https = "Https"


class ResponseBasedDetectedErrorTypes(str, Enum):

    none = "None"
    tcp_errors_only = "TcpErrorsOnly"
    tcp_and_http_errors = "TcpAndHttpErrors"


class EndpointResourceState(str, Enum):

    creating = "Creating"
    deleting = "Deleting"
    running = "Running"
    starting = "Starting"
    stopped = "Stopped"
    stopping = "Stopping"


class QueryStringCachingBehavior(str, Enum):

    ignore_query_string = "IgnoreQueryString"
    bypass_caching = "BypassCaching"
    use_query_string = "UseQueryString"
    not_set = "NotSet"


class GeoFilterActions(str, Enum):

    block = "Block"
    allow = "Allow"


class RemoteAddressOperator(str, Enum):

    any = "Any"
    ip_match = "IPMatch"
    geo_match = "GeoMatch"


class Transform(str, Enum):

    lowercase = "Lowercase"
    uppercase = "Uppercase"


class QueryStringOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class PostArgsOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class RequestUriOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class RequestHeaderOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class RequestBodyOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class UrlPathOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"
    wildcard = "Wildcard"


class UrlFileExtensionOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class UrlFileNameOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class CookiesOperator(str, Enum):

    any = "Any"
    equal = "Equal"
    contains = "Contains"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"


class RedirectType(str, Enum):

    moved = "Moved"
    found = "Found"
    temporary_redirect = "TemporaryRedirect"
    permanent_redirect = "PermanentRedirect"


class DestinationProtocol(str, Enum):

    match_request = "MatchRequest"
    http = "Http"
    https = "Https"


class HeaderAction(str, Enum):

    append = "Append"
    overwrite = "Overwrite"
    delete = "Delete"


class CacheBehavior(str, Enum):

    bypass_cache = "BypassCache"
    override = "Override"
    set_if_missing = "SetIfMissing"


class QueryStringBehavior(str, Enum):

    include = "Include"
    include_all = "IncludeAll"
    exclude = "Exclude"
    exclude_all = "ExcludeAll"


class OriginResourceState(str, Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"


class OriginGroupResourceState(str, Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"


class CustomDomainResourceState(str, Enum):

    creating = "Creating"
    active = "Active"
    deleting = "Deleting"


class CustomHttpsProvisioningState(str, Enum):

    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    failed = "Failed"


class CustomHttpsProvisioningSubstate(str, Enum):

    submitting_domain_control_validation_request = "SubmittingDomainControlValidationRequest"
    pending_domain_control_validation_request_approval = "PendingDomainControlValidationREquestApproval"
    domain_control_validation_request_approved = "DomainControlValidationRequestApproved"
    domain_control_validation_request_rejected = "DomainControlValidationRequestRejected"
    domain_control_validation_request_timed_out = "DomainControlValidationRequestTimedOut"
    issuing_certificate = "IssuingCertificate"
    deploying_certificate = "DeployingCertificate"
    certificate_deployed = "CertificateDeployed"
    deleting_certificate = "DeletingCertificate"
    certificate_deleted = "CertificateDeleted"


class ProtocolType(str, Enum):

    server_name_indication = "ServerNameIndication"
    ip_based = "IPBased"


class MinimumTlsVersion(str, Enum):

    none = "None"
    tls10 = "TLS10"
    tls12 = "TLS12"


class CertificateType(str, Enum):

    shared = "Shared"
    dedicated = "Dedicated"


class ResourceType(str, Enum):

    microsoft_cdn_profiles_endpoints = "Microsoft.Cdn/Profiles/Endpoints"
