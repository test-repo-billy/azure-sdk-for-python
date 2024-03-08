# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python private_endpoint_create_with_asg.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.private_endpoints.begin_create_or_update(
        resource_group_name="rg1",
        private_endpoint_name="testPe",
        parameters={
            "location": "eastus2euap",
            "properties": {
                "applicationSecurityGroups": [
                    {
                        "id": "/subscriptions/subId/resourceGroups/rg1/provders/Microsoft.Network/applicationSecurityGroup/asg1"
                    }
                ],
                "privateLinkServiceConnections": [
                    {
                        "properties": {
                            "groupIds": ["groupIdFromResource"],
                            "privateLinkServiceId": "/subscriptions/subId/resourceGroups/rg1/providers/Microsoft.Network/privateLinkServices/testPls",
                            "requestMessage": "Please approve my connection.",
                        }
                    }
                ],
                "subnet": {
                    "id": "/subscriptions/subId/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/myVnet/subnets/mySubnet"
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-09-01/examples/PrivateEndpointCreateWithASG.json
if __name__ == "__main__":
    main()
