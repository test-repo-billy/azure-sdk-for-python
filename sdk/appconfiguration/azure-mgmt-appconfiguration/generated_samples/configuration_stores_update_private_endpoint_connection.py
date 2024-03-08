# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.appconfiguration import AppConfigurationManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appconfiguration
# USAGE
    python configuration_stores_update_private_endpoint_connection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AppConfigurationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="c80fb759-c965-4c6a-9110-9b2b2d038882",
    )

    response = client.private_endpoint_connections.begin_create_or_update(
        resource_group_name="myResourceGroup",
        config_store_name="contoso",
        private_endpoint_connection_name="myConnection",
        private_endpoint_connection={
            "properties": {"privateLinkServiceConnectionState": {"description": "Auto-Approved", "status": "Approved"}}
        },
    ).result()
    print(response)


# x-ms-original-file: specification/appconfiguration/resource-manager/Microsoft.AppConfiguration/stable/2023-03-01/examples/ConfigurationStoresUpdatePrivateEndpointConnection.json
if __name__ == "__main__":
    main()
