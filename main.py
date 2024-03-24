import psycopg2
from config import config 


#conventional way
#connection= psycopg2.connect(host="localhost", port="5432",database="spotify_user_data", user="postgresql",password="christinawu")

def connect():
    connection = None #non-object- no value object
    try: 
        params= config()
        print('Connecting to the postgreSQL database...')
        connection = psycopg2.connect(**params) #kwargs- extract elements inside db

        #create a cursor
        crsr= connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
             #connection and cursor is the way python files communicates
            print('Database connection terminated.')

if __name__ == "__main__":
    connect()