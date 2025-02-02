from sqlalchemy import *
import pyodbc

#sqlalchemy
# SQLite connection string
connection_string = "sqlite:///mydatabase.db"

# Create an engine
engine = create_engine(connection_string)

metadata = MetaData()

# Define the table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

# Create the table in the database
metadata.create_all(engine)

# Inserting a record
with engine.connect() as connection:
    statement = insert(users).values(name="Alice", age=30)
    connection.execute(statement)

# Query all users
with engine.connect() as connection:
    query = select(users)
    result = connection.execute(query)
    for row in result:
        print(row)

# PYODBC
# Connection string
connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=your_server_name;"
    "DATABASE=your_database_name;"
    "UID=your_username;"
    "PWD=your_password;"
)

# Establish a connection
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch results
for row in cursor:
    print(row)

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", "Bob", 25)
conn.commit()  # This is needed to actually push changes, so don't forget it!!