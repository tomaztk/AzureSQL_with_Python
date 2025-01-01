## Random py snippet

query = "SELECT * FROM information_schema.tables"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)



## random snippet with connection string

from sqlalchemy import create_engine

connection_string = "mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string.format(
    username=username,
    password=password,
    server=server,
    database=database
))

with engine.connect() as connection:
    result = connection.execute("SELECT * FROM information_schema.tables")
    for row in result:
        print(row)
