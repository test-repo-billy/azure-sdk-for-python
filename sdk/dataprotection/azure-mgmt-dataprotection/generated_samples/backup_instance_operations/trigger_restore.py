# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dataprotection
# USAGE
    python trigger_restore.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataProtectionMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="04cf684a-d41f-4550-9f70-7708a3a2283b",
    )

    response = client.backup_instances.begin_trigger_restore(
        resource_group_name="000pikumar",
        vault_name="PratikPrivatePreviewVault1",
        backup_instance_name="testInstance1",
        parameters={
            "objectType": "AzureBackupRecoveryPointBasedRestoreRequest",
            "recoveryPointId": "hardcodedRP",
            "restoreTargetInfo": {
                "datasourceAuthCredentials": {
                    "objectType": "SecretStoreBasedAuthCredentials",
                    "secretStoreResource": {
                        "secretStoreType": "AzureKeyVault",
                        "uri": "https://samplevault.vault.azure.net/secrets/credentials",
                    },
                },
                "datasourceInfo": {
                    "datasourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "objectType": "Datasource",
                    "resourceID": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/targetdb",
                    "resourceLocation": "",
                    "resourceName": "targetdb",
                    "resourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "resourceUri": "",
                },
                "datasourceSetInfo": {
                    "datasourceType": "Microsoft.DBforPostgreSQL/servers/databases",
                    "objectType": "DatasourceSet",
                    "resourceID": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest",
                    "resourceLocation": "",
                    "resourceName": "viveksipgtest",
                    "resourceType": "Microsoft.DBforPostgreSQL/servers",
                    "resourceUri": "",
                },
                "objectType": "RestoreTargetInfo",
                "recoveryOption": "FailIfExists",
                "restoreLocation": "southeastasia",
            },
            "sourceDataStoreType": "VaultStore",
            "sourceResourceId": "/subscriptions/f75d8d8b-6735-4697-82e1-1a7a3ff0d5d4/resourceGroups/viveksipgtest/providers/Microsoft.DBforPostgreSQL/servers/viveksipgtest/databases/testdb",
        },
    ).result()
    print(response)


# x-ms-original-file: specification/dataprotection/resource-manager/Microsoft.DataProtection/stable/2023-11-01/examples/BackupInstanceOperations/TriggerRestore.json
if __name__ == "__main__":
    main()
