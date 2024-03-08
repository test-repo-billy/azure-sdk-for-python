# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.voiceservices import VoiceServicesMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-voiceservices
# USAGE
    python communications_gateways_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = VoiceServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.communications_gateways.begin_create_or_update(
        resource_group_name="testrg",
        communications_gateway_name="myname",
        resource={
            "location": "useast",
            "properties": {
                "autoGeneratedDomainNameLabelScope": "NoReuse",
                "codecs": ["PCMA"],
                "connectivity": "PublicAddress",
                "e911Type": "Standard",
                "platforms": ["OperatorConnect"],
                "serviceLocations": [
                    {
                        "name": "useast",
                        "primaryRegionProperties": {
                            "allowedMediaSourceAddressPrefixes": ["10.1.2.0/24"],
                            "allowedSignalingSourceAddressPrefixes": ["10.1.1.0/24"],
                            "operatorAddresses": ["198.51.100.1"],
                        },
                    },
                    {
                        "name": "useast2",
                        "primaryRegionProperties": {
                            "allowedMediaSourceAddressPrefixes": ["10.2.2.0/24"],
                            "allowedSignalingSourceAddressPrefixes": ["10.2.1.0/24"],
                            "operatorAddresses": ["198.51.100.2"],
                        },
                    },
                ],
                "teamsVoicemailPilotNumber": "1234567890",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/voiceservices/resource-manager/Microsoft.VoiceServices/stable/2023-01-31/examples/CommunicationsGateways_CreateOrUpdate.json
if __name__ == "__main__":
    main()
