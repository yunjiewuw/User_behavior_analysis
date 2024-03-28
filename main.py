import psycopg2
import pandas as pd
from config import config
subscription_willness_table=pd.DataFrame()

def connect():
    connection = None
    cursor = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        # Create table if not exists
        create_script = '''
        CREATE TABLE IF NOT EXISTS user_behavior (
            Age VARCHAR(1000) NULL,
            Gender VARCHAR(1000) NULL,
            spotify_usage_period VARCHAR(1000) NULL,
            spotify_listening_device VARCHAR(1000) NULL,
            spotify_subscription_plan VARCHAR(1000) NULL,
            premium_sub_willingness VARCHAR(1000) NULL,
            preffered_premium_plan VARCHAR(1000) NULL,
            preferred_listening_content VARCHAR(1000) NULL,
            fav_music_genre VARCHAR(1000) NULL,
            music_time_slot VARCHAR(1000) NULL,
            music_Influencial_mood VARCHAR(1000) NULL,
            music_lis_frequency VARCHAR(1000) NULL,
            music_expl_method VARCHAR(1000) NULL,
            music_recc_rating VARCHAR(1000) NULL,
            pod_lis_frequency VARCHAR(1000) NULL,
            fav_pod_genre VARCHAR(1000) NULL,
            preffered_pod_format VARCHAR(1000) NULL,
            pod_host_preference VARCHAR(1000) NULL,
            preffered_pod_duration VARCHAR(1000) NULL,
            pod_variety_satisfaction VARCHAR(1000) NULL
        )
        '''
        cursor.execute(create_script)
        connection.commit()
        print('Table created')

        # Import data from Excel file
        data_file = pd.read_excel('/Users/christina/Desktop/Data Career/User_Behavior/Spotify_User_Behavior.xlsx')
        for index, row in data_file.iterrows():
            cursor.execute('''
            INSERT INTO user_behavior (
                Age, Gender, spotify_usage_period, spotify_listening_device, spotify_subscription_plan,
                premium_sub_willingness, preffered_premium_plan, preferred_listening_content, fav_music_genre, music_time_slot,
                music_Influencial_mood, music_lis_frequency, music_expl_method, music_recc_rating, pod_lis_frequency,
                fav_pod_genre, preffered_pod_format, pod_host_preference, preffered_pod_duration, pod_variety_satisfaction
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', tuple(row))

        # Commit the transaction
        connection.commit()
        print("Data imported successfully.")
        
        # visualization
        get_subscription_willness_table = '''
        SELECT
            music_recc_rating,
            COUNT(CASE WHEN premium_sub_willingness = 'Yes' THEN 1 END) AS willing,
            COUNT(*) AS overall,
            CASE 
                WHEN COUNT(*) > 0 
                THEN COUNT(CASE WHEN premium_sub_willingness = 'Yes' THEN 1 END)::float / COUNT(*) 
                ELSE 0.0 -- or NULL or any other default value
            END AS willing_ratio
        FROM
            user_behavior
        GROUP BY
            music_recc_rating
        ORDER BY
            music_recc_rating DESC ; '''

        cursor.execute(get_subscription_willness_table)
        subscription_willness_table = pd.DataFrame(cursor.fetchall())
        #subscription_willness_table.plot(kind='pie')

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        print('Database connection terminated.')

if __name__ == "__main__":
    connect()
