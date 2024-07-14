import os
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.sql.models import Server, ServerProperties, Database, DatabaseProperties


TENANT_ID = 'your-tenant-id'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
SUBSCRIPTION_ID = 'your-subscription-id'


RESOURCE_GROUP_NAME = 'your-resource-group-name'
LOCATION = 'your-location'  
SQL_SERVER_NAME = 'your-sql-server-name'
SQL_SERVER_ADMIN_USER = 'your-sql-admin-username'
SQL_SERVER_ADMIN_PASSWORD = 'your-sql-admin-password'
SQL_DATABASE_NAME = 'your-sql-database-name'


credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

# Create clients
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
sql_client = SqlManagementClient(credential, SUBSCRIPTION_ID)

# Create the resource group
resource_group_params = {'location': LOCATION}
resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, resource_group_params)
print(f'Resource group {RESOURCE_GROUP_NAME} created or updated.')

# Create the SQL server
server_params = Server(
    location=LOCATION,
    administrator_login=SQL_SERVER_ADMIN_USER,
    administrator_login_password=SQL_SERVER_ADMIN_PASSWORD,
    version='12.0'
)
sql_client.servers.create_or_update(RESOURCE_GROUP_NAME, SQL_SERVER_NAME, server_params)
print(f'SQL server {SQL_SERVER_NAME} created or updated.')

# Create the SQL database
database_params = Database(
    location=LOCATION,
    properties=DatabaseProperties(collation='SQL_Latin1_General_CP1_CI_AS')
)
sql_client.databases.create_or_update(RESOURCE_GROUP_NAME, SQL_SERVER_NAME, SQL_DATABASE_NAME, database_params)
print(f'SQL database {SQL_DATABASE_NAME} created or updated.')
