# %%
import psycopg2
import pandas as pd
from config import config

a= [0,2,1,3,4,5]
def connect():
    connection = None
    cursor = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        print('Database connection terminated.')

if  __name__ == "__main__":
    connect()

# %%
