import pandas as pd
from sqlalchemy import create_engine

# Define your database connection details
host = "localhost"
user = "root"
password = "root"
database = "college"

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Use the engine with pandas to execute the query
df = pd.read_sql_query("SELECT * FROM students", engine)

# Now you can work with the DataFrame
print(df.head())
