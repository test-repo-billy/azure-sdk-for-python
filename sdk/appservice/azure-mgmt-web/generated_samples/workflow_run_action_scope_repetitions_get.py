# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-web
# USAGE
    python workflow_run_action_scope_repetitions_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WebSiteManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.workflow_run_action_scope_repetitions.get(
        resource_group_name="testResourceGroup",
        name="test-name",
        workflow_name="testFlow",
        run_name="08586776228332053161046300351",
        action_name="for_each",
        repetition_name="000000",
    )
    print(response)


# x-ms-original-file: specification/web/resource-manager/Microsoft.Web/stable/2023-01-01/examples/WorkflowRunActionScopeRepetitions_Get.json
if __name__ == "__main__":
    main()
