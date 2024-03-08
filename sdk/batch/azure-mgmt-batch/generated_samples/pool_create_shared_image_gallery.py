# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.batch import BatchManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-batch
# USAGE
    python pool_create_shared_image_gallery.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = BatchManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.pool.create(
        resource_group_name="default-azurebatch-japaneast",
        account_name="sampleacct",
        pool_name="testpool",
        parameters={
            "properties": {
                "deploymentConfiguration": {
                    "virtualMachineConfiguration": {
                        "imageReference": {
                            "id": "/subscriptions/subid/resourceGroups/networking-group/providers/Microsoft.Compute/galleries/testgallery/images/testimagedef/versions/0.0.1"
                        },
                        "nodeAgentSkuId": "batch.node.ubuntu 18.04",
                    }
                },
                "vmSize": "STANDARD_D4",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/batch/resource-manager/Microsoft.Batch/stable/2023-11-01/examples/PoolCreate_SharedImageGallery.json
if __name__ == "__main__":
    main()
