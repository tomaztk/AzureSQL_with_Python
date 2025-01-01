from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient

# Authenticate with Azure and add your subscription ID
credential = DefaultAzureCredential()
subscription_id = 'xxx'


resource_client = ResourceManagementClient(credential, subscription_id)
sql_client = SqlManagementClient(credential, subscription_id)


resource_group_name = 'RG_SQLPython'
location = 'westeurope'

resource_client.resource_groups.create_or_update(
    resource_group_name,
    {'location': location}
)

server_name = 'MSSQL18Py'
admin_user = 'tk'
admin_password = 'xx'

sql_client.servers.begin_create_or_update(
    resource_group_name,
    server_name,
    {
        'location': location,
        'administrator_login': admin_user,
        'administrator_login_password': admin_password,
    }
)

database_name = 'SQLDBwithPython'

sql_client.databases.begin_create_or_update(
    resource_group_name,
    server_name,
    database_name,
    {
        'location': location,
        'sku': {'name': 'Basic', 'tier': 'Basic'}
    }
)
print(f"Database {database_name} provisioned successfully.")
