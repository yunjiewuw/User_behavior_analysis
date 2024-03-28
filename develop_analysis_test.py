import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


# %%
connection= psycopg2.connect(
    host="localhost",
    dbname="spotify_user_database",
    user='postgres',
    password='christinawu',
    port='5432'
)

cursor= connection.cursor()

# code with SQL and python below

# %%
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
subscription_willness_table = pd.DataFrame(cursor.fetchall(), 
                                           columns=['rating', 'willing','overall','ratio'])
#%%
print(subscription_willness_table)
subscription_willness_table['rating'] = subscription_willness_table['rating'].astype(int)

plt.figure(figsize=(8, 8))
subscription_willness_table[['rating', 'ratio']].plot(x='rating',
                                                      y='ratio', kind='bar')
plt.title('Subscription willingness ratio different among recomm_rating')
plt.show()

# %%
get_rating_willingness_groupby_table='''
SELECT
    --music_recc_rating,
    music_recc_rating AS rating, 
    premium_sub_willingness AS willingness, 
    COUNT(*) AS population
FROM
    user_behavior
GROUP BY
    music_recc_rating, premium_sub_willingness
ORDER BY
    music_recc_rating DESC;'''
cursor.execute(get_rating_willingness_groupby_table)
rating_willingness_population_df = pd.DataFrame(cursor.fetchall(), columns=['rating',
                                         'willingness',
                                         'population'])
rating_willingness_population_df['population'] = pd.to_numeric(rating_willingness_population_df['population'], errors='coerce')
print(rating_willingness_population_df)
rating_willingness_population_df.groupby('rating').sum().plot(kind='pie', subplots= True)

# %%
# # in the end
cursor.close()
connection.close()
# %%
