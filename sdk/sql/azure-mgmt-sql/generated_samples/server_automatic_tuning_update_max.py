# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python server_automatic_tuning_update_max.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="c3aa9078-0000-0000-0000-e36f151182d7",
    )

    response = client.server_automatic_tuning.update(
        resource_group_name="default-sql-onebox",
        server_name="testsvr11",
        parameters={
            "properties": {
                "desiredState": "Auto",
                "options": {
                    "createIndex": {"desiredState": "Off"},
                    "dropIndex": {"desiredState": "On"},
                    "forceLastGoodPlan": {"desiredState": "Default"},
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2020-11-01-preview/examples/ServerAutomaticTuningUpdateMax.json
if __name__ == "__main__":
    main()
