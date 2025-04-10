import os
import sys
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from the .env file
load_dotenv()

# Retrieve connection details from environment variables
host = 'localhost'  #os.getenv('host')  # The host of your MySQL database
user =  'root'   #os.getenv('user')  # The username for your MySQL database
password = 'root'     #os.getenv('password')  # The password for the database
db =  'college'  #os.getenv('db')  # The name of the database you want to access

def read_sql_data():
    """
    This function connects to a MySQL database, retrieves data from the 'students' table, and returns it as a DataFrame.
    It logs the progress and handles exceptions appropriately.
    """
    logging.info('Reading data from SQL started...')

    try:
        # Create a SQLAlchemy engine for the MySQL connection
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')

        # Log that the connection to the database was successful
        logging.info("Connection established successfully.")

        # Use pandas to execute a SQL query and retrieve the data from the 'students' table
        df = pd.read_sql_query("SELECT * FROM students", engine)

        # Log that the data retrieval was successful
        logging.info("Data retrieved successfully from the 'students' table.")

        # Print the first few rows of the dataframe to verify the data
        logging.info(f"First 5 rows of the data:\n{df.head()}")

        # Return the dataframe to be used by other parts of the application
        return df

    except Exception as ex:
        # Log the exception and raise a custom exception with error details
        logging.error(f"An error occurred while reading data: {str(ex)}")
        raise CustomException(ex, sys)
