import requests
from decouple import config
import mysql.connector

#url='http://api.sportradar.us/beachvolleyball/trial/v2/en/competitors/sr:competitor:1/profile.json?'
#118926
# url='http://api.sportradar.us/nba/trial/v7/en/players/ab532a66-9314-4d57-ade7-bb54a70c65ad/profile.json?'
url='http://api.sportradar.us/nba/trial/v7/en/players/:/profile.json?'

#response=requests.get(url, params={"api_key":config("beach_app")})
response=requests.get(url, params={"api_key":config("nba_call")})

status=response.status_code
beach_data=response.json()
print(status)
print(beach_data)

"""
class: database
function get connection
function create database
    see if database exists
function create tables
    see if table exists
fuction insert personal 9/18 data
    check if data inserted
    check not duplicated data
function insert personal practice data
    check if data inserted
    check not duplicated data
function insert player profiles data
    check if data inserted
    check not duplicated data
function insert player statistics data
    check if data inserted
    check not duplicated data
function insert players data
    check if data inserted
    check not duplicated data

function query merge api with my data SQL 
function extract data - fetchall



class api
function pull data player profiles
function pull data player statistics
pull data players
store the data

class clean data
function clean player profiles
    create calculated columns like averages and totals
function clean player statistics
    create calculated columns like averages and totals
function clean my stat
    create calculated columns
    from all sessions?

class ask_me_for_data
is it a round?
    CLI 
    date
    stats
    notes
    store the inputs
is it at the driving range?
    CLI 
    date
    stats
    notes
    store the inputs


things to practice
-*arg and **kwags
decorators
list comp
generator
lambda function
testing
try except
inheritance






"""
