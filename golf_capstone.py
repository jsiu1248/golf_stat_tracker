import requests
from decouple import config
import mysql.connector
import os
import json


url= {'ranking':'https://api.sportradar.us/golf/trial/v3/en/players/wgr/2021/rankings.json?',
'stat':'https://api.sportradar.us/golf/trial/pga/v3/en/2021/players/statistics.json?',
'pga_player':'https://api.sportradar.us/golf/trial/pga/v3/en/2021/players/profiles.json?',
'lpga_player':'https://api.sportradar.us/golf/trial/lpga/v3/en/2021/players/profiles.json?',
'pga_tournament':'https://api.sportradar.us/golf/trial/pga/v3/en/2021/tournaments/schedule.json?',
'lpga_tournament':'https://api.sportradar.us/golf/trial/lpga/v3/en/2021/tournaments/schedule.json?'

#,'player_profile':'https://api.sportradar.us/golf/trial/v3/en/players/a7041051-eb25-40b9-acb3-dab88cae69c0/profile.json?'
    } #have to edit id

# if I have multiple methods in each class then it would make sense to put in constructor

class Api:
    def __init__(self):
        self.cwd=os.getcwd()
        self.path="Documents\codingnomads\python_capstone"

    def api(self):
# often data don't need. class method and static methods used more
#class methods can have class variables. 
#staff transformer class maintains state.
    #figure out how to pass a list of links
    #passing in the url instead of being hard-coded
    #having the map be a module for import better for testing. sort of a config file
    # date add to the files, think about if it is going to be rerunned.
        for key,value in url.items():
            self.response=requests.get(value, params={"api_key":config("golf_demo")})

            self.status=self.response.status_code
            # #how to edit out the url part and then add data to the end part
            self.file  = open(os.path.join(self.cwd,self.path,f"{key}_data.json"), "w+")

            self.golf_data=self.response.json()
            json.dump(self.golf_data, self.file)

            # print(status)
            # # print(_data)

            # #pipe all of the variable names here
            # #have to store the data here
            #file.write(f"{golf_data}")
            self.file.close()

#instance variable for object in a different class
class Read_Files():
    def __init__(self):
        self.cwd=os.getcwd()
        self.path="Documents\codingnomads\python_capstone"

    def read_files(self):
        self.file_dict={}
        for key, value in url.items(): # without the asterisk means just gimme the tuple
            self.file_path=os.path.join(self.cwd,self.path,f'{key}_data.json')
#how would I include the date?

            #file=open(file_path, "r", encoding="utf-8")
            with open(self.file_path) as self.json_file:
                # data = json.load(json_file)
            # print(file.read())
                self.file_dict[f'{key}_data']=json.load(self.json_file)#.rstrip("\n")
    def get_file_dict(self):
        return self.file_dict


# do you need to separate read, clean, 
#read_file can return the data
#get_file_dict

class Clean_Data():
    def __init__(self):
        self.rank_dict={}
        self.rank_list=[]

    def clean_rank_data(self):
        for element in fd["ranking_data"]["players"]:
            self.rank_dict["id"]=element["id"]
            self.rank_dict["first_name"]=element["first_name"]
            self.rank_dict["last_name"]=element["last_name"]
            self.rank_dict["country"]=element["country"]
            self.rank_dict["rank"]=element["rank"]
            self.rank_list.append(self.rank_dict.copy())
        print(self.rank_list)

#probably make this into another function def clean data 
    # for element in file_dict["ranking_data"]["players"]:
    #     print(element)
    # print(file_dict["stat_data"])
    # print(file_dict["pga_player_data"])
    # print(file_dict["lpga_player_data"])
    # print(file_dict["pga_tournament_data"])
    # print(file_dict["lpga_tournament_data"])
    # print(file_dict["player_profile_data"])

#pull=Api()
#pull.api()

r=Read_Files()
r.read_files()
# fd=r.get_file_dict()
#getter or accessor
#argument in method of


# c=Clean_Data()

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


#mostly done
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



#add reference table?
#Expected should all tables have primary keys 


"""
