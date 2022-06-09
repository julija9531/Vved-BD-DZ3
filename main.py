import sqlalchemy
from pprint import pprint

from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from datetime import datetime

engine = sqlalchemy.create_engine('postgresql://julija:@localhost:5432/bazadannih')

engine

connection = engine.connect()

'''запрос № 1'''
zap1 = connection.execute(
"""
SELECT title, year_of_issue FROM albums
WHERE year_of_issue = 2018;
""").fetchall()

'''запрос № 2'''
zap2 = connection.execute(
"""
SELECT trek_name, duration FROM treks 
ORDER BY duration DESC
LIMIT 1;
""").fetchall()

'''запрос № 3'''
zap3 = connection.execute(
"""
SELECT trek_name FROM treks 
WHERE duration >= 210;
""").fetchall()

'''запрос № 4'''
zap4 = connection.execute(
"""
SELECT name FROM collection 
WHERE year_of_issue BETWEEN 2018 and 2020;
""").fetchall()

'''запрос № 5'''
zap5 = connection.execute(
"""
SELECT performers_name FROM performers 
WHERE performers_name NOT LIKE ('%% %%');
""").fetchall()

'''запрос № 6'''
zap6 = connection.execute(
"""
SELECT trek_name FROM treks 
WHERE lower(trek_name) LIKE ('%%мой%%') 
OR lower(trek_name) LIKE ('%%my%%');
""").fetchall()
pprint(zap6)



perf = connection.execute(
"""
SELECT * FROM performers;
""").fetchall()

genres = connection.execute(
"""
SELECT * FROM genres;
""").fetchall()

albums = connection.execute(
"""
SELECT * FROM albums;
""").fetchall()

treks = connection.execute(
"""
SELECT * FROM treks;
""").fetchall()

collection = connection.execute(
"""
SELECT * FROM collection;
""").fetchall()

