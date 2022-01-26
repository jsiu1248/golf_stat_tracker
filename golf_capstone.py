import requests
from decouple import config
import mysql.connector
import os
import json
from mysql.connector import Error
from datetime import datetime 
import pandas as pd


#how do I pass a year to the url
year=2021
url= {'ranking':f'https://api.sportradar.us/golf/trial/v3/en/players/wgr/{year}/rankings.json?',
'stat':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/statistics.json?',
'pga_player':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/profiles.json?',
'lpga_player':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/players/profiles.json?',
# 'pga_tournament':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/tournaments/schedule.json?',
'lpga_tournament':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/tournaments/schedule.json?'

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
class File_Reader():
    def __init__(self):
        self.cwd=os.getcwd()
        self.path="Documents\codingnomads\python_capstone"

    def read_files(self):
        self.file_dict={}
        for key, value in url.items(): 
            self.file_path=os.path.join(self.cwd,self.path,f'{key}_data.json')
#how would I include the date?

            with open(self.file_path) as self.json_file:
                self.file_dict[f'{key}_data']=json.load(self.json_file)#.rstrip("\n")
    def get_file_dict(self):
        return self.file_dict



class Data_Cleaner():
    def __init__(self):

#how to make this into arguments
        self.rank_dict={}
        self.rank_list=[]
        self.stat_dict={}
        self.stat_list=[]
        self.pga_player_dict={}
        self.pga_player_list=[]
        self.lpga_player_dict={}
        self.lpga_player_list=[]
        self.lpga_tounament_dict={}
        self.lpga_tounament_list=[]



    def clean_rank_data(self):
        for rank_element in fd["ranking_data"]["players"]:
            for element in ("id","rank"):
                self.rank_dict[element]=rank_element[element]

            # self.rank_dict["id"]=rank_element["id"]
            # self.rank_dict["rank"]=rank_element["rank"]
            self.rank_list.append(self.rank_dict.copy())
        # return self.rank_list
        #print(self.rank_list)
    def clean_stat_data(self):
        for stat_element in fd["stat_data"]["players"]:
            for element in (['id'],('statistics','earnings'),('statistics','drive_avg'),
            ('statistics','gir_pct'),('statistics','putt_avg'),('statistics','sand_saves_pct'),('statistics','birdies_per_round'),('statistics','hole_proximity_avg'),('statistics','scrambling_pct'),('statistics','world_rank')):
                try:
                    if len(element)==1:
                        self.stat_dict[element[0]]=stat_element[element[0]]
                    elif len(element)==2:
                        self.stat_dict[element[1]]=stat_element[element[0]][element[1]]

                # self.stat_dict["id"]=stat_element["id"]
                # self.stat_dict["country"]=stat_element["country"]
                # self.stat_dict["earnings"]=stat_element["statistics"]["earnings"]
                # self.stat_dict["drive_avg"]=stat_element["statistics"]["drive_avg"]
                # self.stat_dict["gir_pct"]=stat_element["statistics"]["gir_pct"]
                # self.stat_dict["putt_avg"]=stat_element["statistics"]["putt_avg"]
                # self.stat_dict["sand_saves_pct"]=stat_element["statistics"]["sand_saves_pct"]
                # self.stat_dict["birdies_per_round"]=stat_element["statistics"]["birdies_per_round"]
                # self.stat_dict["hole_proximity_avg"]=stat_element["statistics"]["hole_proximity_avg"]
                # self.stat_dict["scrambling_pct"]=stat_element["statistics"]["scrambling_pct"]
                # self.stat_dict["rank"]=stat_element["statistics"]["world_rank"]
                except KeyError: 
                    if len(element)==1:

                        self.stat_dict[element[0]]=None
                    elif len(element)==2:
                        self.stat_dict[element[1]]=None



            self.stat_list.append(self.stat_dict.copy())
        # return self.stat_list


        #print(self.stat_list)
    def clean_pga_player_data(self):
        for pga_player_element in fd["pga_player_data"]["players"]:
            for element in (['id'],['first_name'],['last_name'],['height'],['birthday'],['country'],['residence'],['birth_place'],['college']):
                try:
                    if element[0]=="birthday":
                        self.pga_player_dict[element[0]]=datetime.strptime(pga_player_element[element[0]], "%Y-%m-%dT%H:%M:%S+00:00")

                    else:
                        self.pga_player_dict[element[0]]=pga_player_element[element[0]]
                # self.pga_player_dict["id"]=pga_player_element["id"]
                # self.pga_player_dict["first_name"]=pga_player_element["first_name"]
                # self.pga_player_dict["last_name"]=pga_player_element["last_name"]

                # self.pga_player_dict["height"]=pga_player_element["height"]
                # self.pga_player_dict["birthday"]=pga_player_element["birthday"]
                # self.pga_player_dict["country"]=pga_player_element["country"]
                # self.pga_player_dict["residence"]=pga_player_element["residence"]
                # self.pga_player_dict["birth_place"]=pga_player_element["birth_place"]
                # self.pga_player_dict["college"]=pga_player_element["college"]
                except KeyError: 
                    self.pga_player_dict[element[0]]=None


            self.pga_player_list.append(self.pga_player_dict.copy())
        #return self.pga_player_list
        # print(self.pga_player_list)
    def clean_lpga_player_data(self):
        for lpga_player_element in fd["lpga_player_data"]["players"]:
            for element in (['id'],['first_name'],['last_name'],['height'],['birthday'],['country'],['residence'],['birth_place'],['college']):

                try:
                    if element[0]=="birthday":
                        self.lpga_player_dict[element[0]]=datetime.strptime(lpga_player_element[element[0]], "%Y-%m-%dT%H:%M:%S+00:00")

                    else:
                        self.lpga_player_dict[element[0]]=lpga_player_element[element[0]]

                # self.lpga_player_dict["id"]=lpga_player_element["id"]
                # self.lpga_player_dict["first_name"]=lpga_player_element["first_name"]
                # self.lpga_player_dict["last_name"]=lpga_player_element["last_name"]

                # self.lpga_player_dict["height"]=lpga_player_element["height"]
                # self.lpga_player_dict["birthday"]=lpga_player_element["birthday"]
                # self.lpga_player_dict["country"]=lpga_player_element["country"]
                # self.lpga_player_dict["residence"]=lpga_player_element["residence"]
                # self.lpga_player_dict["birth_place"]=lpga_player_element["birth_place"]
                # self.lpga_player_dict["college"]=lpga_player_element["college"]
                except KeyError: 
                    self.lpga_player_dict[element[0]]=None


            self.lpga_player_list.append(self.lpga_player_dict.copy())
        # return self.lpga_player_list
        # print(self.lpga_player_list)
    def clean_lpga_tournament_data(self):
        for lpga_tournament_element in fd["lpga_tournament_data"]["tournaments"]:
            print(lpga_tournament_element)
    def get_rank_list(self):
        return self.rank_list

    def get_stat_list(self):
        return self.stat_list
    def get_pga_player_list(self):
        return self.pga_player_list
    def get_lpga_player_list(self):
        return self.lpga_player_list

    
    #where should I clean practice and round
class Database:
    def __init__(self):
        pass

    def try_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    def create_connection(self):
        #self.ch_1 = try_connection("localhost", "root", config("mysql_pass"), "sakila")
        self.cursor_1 = ch_1.cursor() #checked
        

    def create_database(self):
        try:
            self.database_query_create = f"""CREATE DATABASE golf;"""

            self.cursor_1.execute(self.database_query_create)

            ch_1.commit()
        except Error as e:
            print("The database exists already")

    def create_table(self):
        self.rank_query_create = f"""CREATE TABLE IF NOT EXISTS world_rank 
        (
        id VARCHAR(255),
        world_rank INT(10), 
        PRIMARY KEY(id));"""



        self.stat_query_create = f"""CREATE TABLE IF NOT EXISTS stat 
        (
        id VARCHAR(255),
        earnings FLOAT(13),
        drive_avg FLOAT(6), 
        gir_pct FLOAT(4),
        putt_avg FLOAT(4),
        sand_saves_pct FLOAT(4),
        birdies_per_round FLOAT(4), 
        hole_proximity_avg VARCHAR(255),
        scrambling_pct FLOAT(4), 
        world_rank INT(4),
        PRIMARY KEY(id));"""


        self.pga_player_query_create = f"""CREATE TABLE IF NOT EXISTS pga_player 
        (
        id VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255), 
        height INT (3),
        birthday DATETIME,
        country VARCHAR(255),
        residence VARCHAR(255), 
        birth_place VARCHAR(255),
        college VARCHAR(255), 
        PRIMARY KEY(id));"""



        self.lpga_player_query_create = f"""CREATE TABLE IF NOT EXISTS lpga_player 
        (
        id VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255), 
        height VARCHAR (255),
        birthday DATETIME,
        country VARCHAR(255),
        residence VARCHAR(255), 
        birth_place VARCHAR(255),
        college VARCHAR(255), 
        PRIMARY KEY(id));"""


        try: 
            self.cursor_1.execute(self.rank_query_create)
            self.cursor_1.execute(self.stat_query_create)
            self.cursor_1.execute(self.pga_player_query_create)
            self.cursor_1.execute(self.lpga_player_query_create)


            ch_1.commit()
        except Error as e:
            print("The table exists already")


    def insert_data(self):
        self.rank_query_insert=f"""
            INSERT INTO 
                world_rank
                (id,world_rank)
            VALUES
                (%(id)s, %(rank)s);
        """


        self.stat_query_insert = f""" 
        
            INSERT INTO 
                stat
                (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank)
            VALUES
                (%(id)s, %(earnings)s, %(drive_avg)s, %(gir_pct)s, %(putt_avg)s, %(sand_saves_pct)s, %(birdies_per_round)s, %(hole_proximity_avg)s, %(scrambling_pct)s, %(world_rank)s);
            """     



        self.pga_player_query_insert= f"""
        
            INSERT INTO 
            pga_player
            (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
            VALUES
            (%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);

        """

# {'id': '62320f56-8d9e-4a90-a9db-195629d541d2', 'first_name': 'George', 'last_name': 'McNeill', 'height': 73,
#  'birthday': '1975-10-02T00:00:00+00:00', 'country': 'UNITED STATES', 'residence': 'Fort Myers, FL, USA',
#   'birth_place': 'Naples, FL, USA', 'college': 'Florida State'}

        self.lpga_player_query_insert= f"""
        
            INSERT INTO 
            lpga_player
            (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
            VALUES
            (%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);

        """


        #self.cursor_1.executemany(self.rank_query_insert, rank_list) #change the dataset
        #self.cursor_1.executemany(self.stat_query_insert, stat_list)
        #self.cursor_1.executemany(self.pga_player_query_insert, pga_player_list)
        #self.cursor_1.executemany(self.lpga_player_query_insert, lpga_player_list)


        ch_1.commit()


class Cli:
    def __init__(self):
        pass
    def cli(self):
        self.date=input("What date is it? ex. ")
        self.session=input("Is it a round or a practice?")
        if self.session=="round":
            self.round_list=[]
            self.round_dict={}
            self.round_course=input("What is the name of the course?")
            self.round_num_holes=int(input("How many number of holes did you play?"))
            for self.round_hole in range(1,self.num_holes+1):
                self.round_drive=input("What was the driving distince?")
                self.round_green_reg=input("What is greens in regulation?")
                self.round_score=input("What was the score?")
                self.round_putt=input("How many putts?")
                self.round_fairway=input("Did you hit the fairway?")
                self.round_proximity_to_hole=input("What was the promity to the hole?")
                self.round_scramble=input("Did you scramble?")
                self.round_notes=input("Did you have notes?")
                self.round_goals=input("Did you have goals?")

                self.round_dict["round_hole"]=self.round_hole
                self.round_dict["round_drive"]=self.round_drive
                self.round_dict["round_green_reg"]=self.round_green_reg
                self.round_dict["round_score"]=self.round_score
                self.round_dict["round_putt"]=self.round_putt
                self.round_dict["round_fairway"]=self.round_fairway
                self.round_dict["round_proximity_to_hole"]=self.round_proximity_to_hole
                self.round_dict["round_scramble"]=self.round_scramble
                self.round_dict["round_notes"]=self.round_notes
                self.round_dict["round_goals"]=self.round_goals
                
            self.round_list.append(self.round_dict.copy())

        if self.session=="practice":
            # how do I keep adding loops
            # how do I change the data when I did something wrong?
            self.num_type=int(input("How many types of shots were you try this time?"))
            self.practice_list=[]
            self.practice_dict={}
            for num in range(1,self.num_type+1):
                self.practice_shot_type=input("What is the shot type? ie. chip, drive, putt, pitch, sand, iron")
                self.practice_success=input(f"What many types did you success the {self.shot_type}")
                self.practice_total=input(f"How many total {self.shot_type} did you make?")
                self.practice_distance=input(f"What was the distance of {self.shot_type} were you trying?")
                self.practice_notes=input("Did you have notes?")
                self.practice_goals=input("Did you have goals?")

                self.practice_dict['shot_type']=self.practice_shot_type
                self.practice_dict['success']=self.practice_success
                self.practice_dict['total']=self.practice_total
                self.practice_dict['distance']=self.practice_distance
                self.practice_dict['notes']=self.practice_notes
                self.practice_dict['goals']=self.practice_goals

                self.practice_list.append(self.practice_dict.copy())

            


#I need to save the cli data in a way that can be inserted into database




    


# pull=Api()
# pull.api()

r=File_Reader()
r.read_files()
fd=r.get_file_dict()
#getter or accessor
#argument in method of


c=Data_Cleaner()
rank_list=c.get_rank_list()
stat_list=c.get_stat_list()
pga_player_list=c.get_pga_player_list()
lpga_player_list=c.get_lpga_player_list()

c.clean_rank_data()
c.clean_stat_data()
c.clean_pga_player_data()
c.clean_lpga_player_data()
#c.clean_lpga_tournament_sdata()

d=Database()
ch_1=d.try_connection("localhost", "root", config("mysql_pass"), "golf")
d.create_connection()
d.create_database()
d.create_table()
d.insert_data()

# rank=c.get_rank_list()
# stat=c.get_stat_list()

# cwd=os.getcwd()
# path="Documents\codingnomads\python_capstone"
# stat_file  = open(os.path.join(cwd,path,f"stat_test_data.json"), "w+")
# rank_file  = open(os.path.join(cwd,path,f"rank_test_data.json"), "w+")
# json.dump(stat, stat_file)
# json.dump(rank, rank_file)

"""
class: database
function get connection - done
function create database - done
    see if database exists
function create tables - done
    see if table exists - done
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
class api - done
function pull data player profiles - done
function pull data player statistics - done
pull data players - done
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
is it a round? - done
    CLI - done
    date - done
    stats - done
    notes - done
    store the inputs
is it at the driving range? - done
    CLI - done
    date - done
    stats - done
    notes - done
    store the inputs


things to practice
-*arg and **kwags
decorators
list comp
generator
lambda function
testing
try except - done
inheritance



"""
