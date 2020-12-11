# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays(
songplay_id SERIAL PRIMARY KEY,
start_time BIGINT,
user_id varchar,
level varchar,
song_id varchar,
artist_id varchar,
session_id varchar,
location varchar,
user_agent varchar)
""")

user_table_create = ("""
CREATE TABLE users(
user_id varchar PRIMARY KEY,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
gender varchar NOT NULL,
level varchar NOT NULL)
""")

song_table_create = ("""
CREATE TABLE songs(
song_id varchar PRIMARY KEY,
title varchar NOT NULL,
artist_id varchar NOT NULL,
year int,
duration float)
""")

artist_table_create = ("""
CREATE TABLE artists(
artist_id varchar PRIMARY KEY,
name varchar NOT NULL,
location varchar NOT NULL,
latitude float,
longitude float)
""")

time_table_create = ("""
CREATE TABLE time(
start_time BIGINT PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id,
                           location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]