# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"

user_table_drop = "DROP table IF EXISTS users"

song_table_drop = "DROP table IF EXISTS songs"

artist_table_drop = "DROP table IF EXISTS artists"

time_table_drop = "DROP table IF EXISTS timetable"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY,
    user_id VARCHAR NOT NULL, 
    song_id VARCHAR,
    artist_id VARCHAR, 
    session_id INT, 
    location VARCHAR,
    user_agent VARCHAR,
    start_time TIMESTAMP NOT NULL,
    level VARCHAR)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(user_id VARCHAR PRIMARY KEY,
     first_n VARCHAR,
     last_n VARCHAR,
     gender VARCHAR,
     level VARCHAR)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(song_id VARCHAR PRIMARY KEY,
    artist_id VARCHAR,
    title VARCHAR,
    duration FLOAT,
    year INT)
    """)

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(artist_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    location VARCHAR,
    latitude FLOAT,
    longitude FLOAT)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS timetable (start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT, 
    month INT,
    year INT,
    weekday INT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays 
    (user_id, song_id, artist_id, start_time, session_id, location, user_agent, level)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT songplays_pkey
    DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_n, last_n,gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT users_pkey
    DO UPDATE SET level=EXCLUDED.level 
""")

song_table_insert = ("""
INSERT INTO songs (song_id, artist_id, title, duration, year)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT songs_pkey
    DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists \
    (artist_id, name, location, latitude, longitude)\
    VALUES(%s, %s, %s, %s, %s)\
    ON CONFLICT ON CONSTRAINT artists_pkey\
    DO NOTHING
""")


time_table_insert = ("""
INSERT INTO timetable (year, week, month, day, hour, weekday, start_time)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT ON CONSTRAINT timetable_pkey
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id
FROM songs s JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s AND a.name = %s AND s.duration = %s

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]