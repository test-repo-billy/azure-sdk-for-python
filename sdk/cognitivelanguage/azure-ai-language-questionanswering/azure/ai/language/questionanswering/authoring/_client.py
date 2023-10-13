# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.credentials import AzureKeyCredential
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AuthoringClientConfiguration
from ._operations import AuthoringClientOperationsMixin
from ._serialization import Deserializer, Serializer


class AuthoringClient(AuthoringClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """The language service API is a suite of natural language processing (NLP) skills built with
    best-in-class Microsoft machine learning algorithms. The API can be used to analyze
    unstructured text for tasks such as sentiment analysis, key phrase extraction, language
    detection and question answering. Further documentation can be found in
    https://docs.microsoft.com/azure/cognitive-services/text-analytics/overview.

    :param endpoint: Supported Cognitive Services endpoint (e.g.,
     https://:code:`<resource-name>`.api.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :keyword api_version: Api Version. Default value is "2021-10-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(self, endpoint: str, credential: AzureKeyCredential, **kwargs: Any) -> None:
        _endpoint = "{Endpoint}/language"
        self._config = AuthoringClientConfiguration(endpoint=endpoint, credential=credential, **kwargs)
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AuthoringClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
