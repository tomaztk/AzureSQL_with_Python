import pyodbc

# Connection details
server = 'MSSQL18Py.database.windows.net'
database = 'SQLDBwithPython'
username = 'tk'
password = 'xxx'

# Connection string
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
cursor = conn.cursor()

# Grant access for service principal
cursor.execute("CREATE USER [your-managed-identity] FROM EXTERNAL PROVIDER;")
cursor.execute("ALTER ROLE db_datareader ADD MEMBER [your-managed-identity];")
cursor.commit()
print("User and permissions configured.")


############################################
# Firewall rule!!! if necessary
sql_client.firewall_rules.begin_create_or_update(
    resource_group_name,
    server_name,
    'AllowAllAzureIps',
    {
        'start_ip_address': '0.0.0.0',
        'end_ip_address': '0.0.0.0',
    }
)
print("Firewall rule added.")



############################################
############################################
### When done, delete the resources
############################################
############################################

# in this order!

# delete a database
sql_client.databases.begin_delete(resource_group_name, server_name, database_name)

# Delete MSSQL server
sql_client.servers.begin_delete(resource_group_name, server_name)

# Delete RG
resource_client.resource_groups.begin_delete(resource_group_name)
