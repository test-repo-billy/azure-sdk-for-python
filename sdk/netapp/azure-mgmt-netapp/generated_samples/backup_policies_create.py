# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.netapp import NetAppManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-netapp
# USAGE
    python backup_policies_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetAppManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="D633CC2E-722B-4AE1-B636-BBD9E4C60ED9",
    )

    response = client.backup_policies.begin_create(
        resource_group_name="myRG",
        account_name="account1",
        backup_policy_name="backupPolicyName",
        body={
            "location": "westus",
            "properties": {
                "dailyBackupsToKeep": 10,
                "enabled": True,
                "monthlyBackupsToKeep": 10,
                "weeklyBackupsToKeep": 10,
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/netapp/resource-manager/Microsoft.NetApp/preview/2023-05-01-preview/examples/BackupPolicies_Create.json
if __name__ == "__main__":
    main()
