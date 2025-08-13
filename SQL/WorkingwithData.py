import pandas as pd
df = pd.read_csv("DataSets/spotify_history.csv")
print(df.head())

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345612", db="ecommerce")
cursor = conn.cursor()

create_table_query = """
CREATE TABLE spotify_history (
    spotify_track_uri VARCHAR(50),
    ts DATETIME,
    platform VARCHAR(50),
    ms_played INT,
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    album_name VARCHAR(255),
    reason_start VARCHAR(50),
    reason_end VARCHAR(50),
    shuffle BOOLEAN,
    skipped BOOLEAN
);
"""

cursor.execute(create_table_query)
print("Table 'spotify_history' created successfully!")


df = df.where(pd.notnull(df), None)

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO spotify_history 
        (spotify_track_uri, ts, platform, ms_played, track_name, artist_name, album_name, reason_start, reason_end, shuffle, skipped)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("CSV data inserted into spotify_history table!")
