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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ReportsOperations(object):
    """ReportsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2019-11-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-11-01"

        self.config = config

    def get_latency_scorecards(
            self, resource_group_name, profile_name, experiment_name, aggregation_interval, end_date_time_utc=None, country=None, custom_headers=None, raw=False, **operation_config):
        """Gets a Latency Scorecard for a given Experiment.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: The Profile identifier associated with the Tenant
         and Partner
        :type profile_name: str
        :param experiment_name: The Experiment identifier associated with the
         Experiment
        :type experiment_name: str
        :param aggregation_interval: The aggregation interval of the Latency
         Scorecard. Possible values include: 'Daily', 'Weekly', 'Monthly'
        :type aggregation_interval: str or
         ~azure.mgmt.frontdoor.models.LatencyScorecardAggregationInterval
        :param end_date_time_utc: The end DateTime of the Latency Scorecard in
         UTC
        :type end_date_time_utc: str
        :param country: The country associated with the Latency Scorecard.
         Values are country ISO codes as specified here-
         https://www.iso.org/iso-3166-country-codes.html
        :type country: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LatencyScorecard or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.frontdoor.models.LatencyScorecard or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_latency_scorecards.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str', pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'experimentName': self._serialize.url("experiment_name", experiment_name, 'str', pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if end_date_time_utc is not None:
            query_parameters['endDateTimeUTC'] = self._serialize.query("end_date_time_utc", end_date_time_utc, 'str')
        if country is not None:
            query_parameters['country'] = self._serialize.query("country", country, 'str')
        query_parameters['aggregationInterval'] = self._serialize.query("aggregation_interval", aggregation_interval, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LatencyScorecard', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_latency_scorecards.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/LatencyScorecard'}

    def get_timeseries(
            self, resource_group_name, profile_name, experiment_name, start_date_time_utc, end_date_time_utc, aggregation_interval, timeseries_type, endpoint=None, country=None, custom_headers=None, raw=False, **operation_config):
        """Gets a Timeseries for a given Experiment.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param profile_name: The Profile identifier associated with the Tenant
         and Partner
        :type profile_name: str
        :param experiment_name: The Experiment identifier associated with the
         Experiment
        :type experiment_name: str
        :param start_date_time_utc: The start DateTime of the Timeseries in
         UTC
        :type start_date_time_utc: datetime
        :param end_date_time_utc: The end DateTime of the Timeseries in UTC
        :type end_date_time_utc: datetime
        :param aggregation_interval: The aggregation interval of the
         Timeseries. Possible values include: 'Hourly', 'Daily'
        :type aggregation_interval: str or
         ~azure.mgmt.frontdoor.models.TimeseriesAggregationInterval
        :param timeseries_type: The type of Timeseries. Possible values
         include: 'MeasurementCounts', 'LatencyP50', 'LatencyP75', 'LatencyP95'
        :type timeseries_type: str or
         ~azure.mgmt.frontdoor.models.TimeseriesType
        :param endpoint: The specific endpoint
        :type endpoint: str
        :param country: The country associated with the Timeseries. Values are
         country ISO codes as specified here-
         https://www.iso.org/iso-3166-country-codes.html
        :type country: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Timeseries or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.frontdoor.models.Timeseries or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_timeseries.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=80, min_length=1, pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'profileName': self._serialize.url("profile_name", profile_name, 'str', pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$'),
            'experimentName': self._serialize.url("experiment_name", experiment_name, 'str', pattern=r'^[a-zA-Z0-9_\-\(\)\.]*[^\.]$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        query_parameters['startDateTimeUTC'] = self._serialize.query("start_date_time_utc", start_date_time_utc, 'iso-8601')
        query_parameters['endDateTimeUTC'] = self._serialize.query("end_date_time_utc", end_date_time_utc, 'iso-8601')
        query_parameters['aggregationInterval'] = self._serialize.query("aggregation_interval", aggregation_interval, 'str')
        query_parameters['timeseriesType'] = self._serialize.query("timeseries_type", timeseries_type, 'str')
        if endpoint is not None:
            query_parameters['endpoint'] = self._serialize.query("endpoint", endpoint, 'str')
        if country is not None:
            query_parameters['country'] = self._serialize.query("country", country, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Timeseries', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_timeseries.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/Timeseries'}
