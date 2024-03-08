# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.storagecache import StorageCacheManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagecache
# USAGE
    python caches_start.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageCacheManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    client.caches.begin_start(
        resource_group_name="scgroup",
        cache_name="sc",
    ).result()


# x-ms-original-file: specification/storagecache/resource-manager/Microsoft.StorageCache/preview/2023-11-01-preview/examples/Caches_Start.json
if __name__ == "__main__":
    main()
