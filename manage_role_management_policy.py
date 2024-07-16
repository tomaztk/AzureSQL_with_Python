
import os
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient


def main():

    sub_id = os.environ.get("SUBSCRIPTION_ID", None)

    client = AuthorizationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=sub_id,
    )

    result = client.role_management_policies.list_for_scope(
        scope=f"providers/Microsoft.Subscription/subscriptions/{sub_id}"
    )

    for item in result:
        print(json.dumps(item.serialize()))


if __name__ == "__main__":
    main()