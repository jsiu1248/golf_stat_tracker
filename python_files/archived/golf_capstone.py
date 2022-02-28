from distutils.util import execute
import requests
from decouple import config
import mysql.connector
import os
import json
from mysql.connector import Error
from datetime import datetime 
import pandas as pd
import uuid
from sqlalchemy import create_engine
import pymysql



year=2021
url= {'ranking':f'https://api.sportradar.us/golf/trial/v3/en/players/wgr/{year}/rankings.json?',
'stat':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/statistics.json?',
'pga_player':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/players/profiles.json?',
'lpga_player':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/players/profiles.json?',
# 'pga_tournament':f'https://api.sportradar.us/golf/trial/pga/v3/en/{year}/tournaments/schedule.json?',
'lpga_tournament':f'https://api.sportradar.us/golf/trial/lpga/v3/en/{year}/tournaments/schedule.json?'

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
        # for i in ["rank","stat","pga_player","lpga_player"]:
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

            self.rank_list.append(self.rank_dict.copy())
        # return self.rank_list
        #print(self.rank_list)
    def clean_stat_data(self):
        self.stat="statistics"
        for stat_element in fd["stat_data"]["players"]:
            for element in (['id'],(self.stat,'earnings'),(self.stat,'drive_avg'),
            (self.stat,'gir_pct'),(self.stat,'putt_avg'),(self.stat,'sand_saves_pct'),(self.stat,'birdies_per_round'),
            (self.stat,'hole_proximity_avg'),(self.stat,'scrambling_pct'),(self.stat,'world_rank')):
                try:
                    if len(element)==1:
                        self.stat_dict[element[0]]=stat_element[element[0]]
                    elif len(element)==2:
                        self.stat_dict[element[1]]=stat_element[element[0]][element[1]]

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
        #getters and setters
        #can be encapsulated like properties

    
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
        self.cursor_1 = ch_1.cursor() 
        

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

        self.round_query_create = f"""CREATE TABLE IF NOT EXISTS round 
        (
        session_id INT(10),
        hole INT(2),
        green_reg INT(1),
        score INT(3),
        putt INT(1), 
        fairway INT(1),
        proximity_to_hole FLOAT(5), 
        scramble INT(1),
        PRIMARY KEY(session_id));"""



        self.practice_query_create = f"""CREATE TABLE IF NOT EXISTS practice 
        (
        session_id INT(10),
        shot_type VARCHAR(255), 
        success INT(3),
        total INT(3),
        distance FLOAT(5),
        club VARCHAR(255),
        PRIMARY KEY(session_id));"""


        self.golf_course_query_create = f"""CREATE TABLE IF NOT EXISTS golf_course 
        (
        id INT(5) AUTO_INCREMENT,
        course_name VARCHAR(255),
        hole INT(2), 
        PRIMARY KEY(id));"""

        self.session_query_create = f"""CREATE TABLE IF NOT EXISTS session
        (
            session_id INT(10), 
            session_type_id INT(2), 
            course_id INT(10), 
            date DATETIME, 
            notes LONGTEXT, 
            goals LONGTEXT, 
            PRIMARY KEY(session_id));
        
        
        
        """

        self.session_type_query_create = f"""CREATE TABLE IF NOT EXISTS session_type 
        (
        session_type_id INT(2) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(session_type_id));
        """


        self.stat_type_query_create = f"""CREATE TABLE IF NOT EXISTS stat_type 
        (
        stat_id INT(4) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(stat_id));
        """

        self.swing_type_query_create = f"""CREATE TABLE IF NOT EXISTS swing_type 
        (
        swing_id INT(3) AUTO_INCREMENT,
        name VARCHAR(255), 
        UNIQUE(name),
        PRIMARY KEY(swing_id));
        """

        self.distance_tracking_query_create = f"""CREATE TABLE IF NOT EXISTS distance_tracking
        (
        id INT(7) AUTO_INCREMENT,
        date DATETIME,
        club VARCHAR(255),
        distance FLOAT(5),

        PRIMARY KEY(id));
        """




        try: 
            for element in [self.rank_query_create, self.stat_query_create, self.pga_player_query_create, self.lpga_player_query_create, 
                self.round_query_create, self.practice_query_create, self.golf_course_query_create, 
            self.session_query_create, self.session_type_query_create, self.swing_type_query_create, self.distance_tracking_query_create]:
                self.cursor_1.execute(element)


#list of queries can it be automatic or manual?
#loop and grab query run through execute then try block



            ch_1.commit()
        except Error as e: #f"{e}":
            print(f"The {element}_query_create table exists already")


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


        self.lpga_player_query_insert= f"""
        
            INSERT INTO 
            lpga_player
            (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
            VALUES
            (%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);

        """


        self.swing_type_query_insert=f"""
        
        INSERT INTO 
        swing_type
        (name)
        VALUES
        ('sand'), ('chip'), ('pitch'), ('drive'), ('iron'), ('putt')
        """

        self.session_type_query_insert="""
        INSERT INTO 
        session_type
        (name)
        VALUES
        ('round'),('practice')"""




        try:
            for data in ((self.rank_query_insert, rank_list),(self.stat_query_insert, stat_list), (self.pga_player_query_insert, pga_player_list), (self.lpga_player_query_insert, lpga_player_list)):
                self.cursor_1.executemany(data[0],data[1]) 
                ch_1.commit()

        except Error as e: #f"{e}":
                print(f"The {data}'s data exists already")
        
        try:
            for d in (self.swing_type_query_insert, self.session_type_query_insert):
                self.cursor_1.execute(d)
                ch_1.commit()

        except Error as e:
            print(f"The {d}'s data exists already")



class Cli:
    def __init__(self):
        pass
    def cli(self):
        self.date=input("What date is it? i.e. 12-12-2021 ")
        self.session=input("Is it a round or a practice? ")
        self.id=uuid.uuid4() # where should I change the id?
        session_list=[]
        session_dict={}
        #session id, course_id, date, notes, goals
        if self.session=="round":
            self.round_list=[]
            self.round_dict={}
            try:
                self.round_course=str(input("What is the name of the course? i.e. Harding Park "))
            except ValueError:
                print("Has to be text.")
            try:
                self.round_num_holes=int(input("How many number of holes did you play? 9 or 18 "))
            except ValueError:
                print("Has to be a number.")

            for self.round_hole in range(1,self.round_num_holes+1):
                try:
                    self.round_drive=int(input("What was the driving distance? i.e 300. "))
                    self.round_green_reg=int(input("What is greens in regulation? i.e. 1 or 0 "))

                    self.round_score=int(input("What was the score? i.e. 59 "))
                    self.round_putt=int(input("How many putts? i.e. 2 "))
                    self.round_fairway=int(input("Did you hit the fairway? i.e. 1 or 0 "))
                    self.round_proximity_to_hole=int(input("What was the promity to the hole in feet? i.e. 39 "))
                    self.round_scramble=int(input("Did you scramble? i.e. 1 or 0 "))
                except ValueError:
                    print("Has to be a number.")
                try:
                    self.round_notes=str(input("Did you have notes? "))
                    self.round_goals=str(input("Did you have goals? "))
                except ValueError:
                    print("Has to be text.")

                self.round_dict["id"]=self.id
                self.round_dict["date"]=self.date
                self.round_dict["round_course"]=self.round_course
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
            self.df_round=pd.DataFrame(self.round_list)

            #print(df)
            # self.df_round_melt=pd.melt(self.df_round, id_vars=['id','date','round_course','round_hole'],value_vars=['round_drive','round_green_reg','round_score','round_putt','round_fairway','round_proximity_to_hole',
            # 'round_scramble','round_notes','round_goals'])
            # print(self.df_round_melt)

            
# melt the data figure out how to get unique ids

        if self.session=="practice":
            # how do I change the data when I did something wrong?
            try:
                self.num_type=int(input("How many types of shots were you try this time?"))
            except ValueError:
                print("Has to be a number")
            self.practice_list=[]
            self.practice_dict={}
            for num in range(1,self.num_type+1):
                try:
                    self.practice_shot_type=str(input("What is the shot type? ie. chip, drive, putt, pitch, sand, iron "))
                except ValueError:
                    print("Has to be text.")
                try: 
                    self.practice_success=int(input(f"What many times did you success the {self.practice_shot_type} "))
                    self.practice_total=int(input(f"How many total {self.practice_shot_type} did you make? "))
                    self.practice_distance=int(input(f"What was the distance of {self.practice_shot_type} were you trying? "))
                except ValueError:
                    print("Has to be a number")
                try:
                    self.practice_notes=str(input("Did you have notes? "))
                    self.practice_goals=str(input("Did you have goals? "))
                except ValueError:
                    print("Has to be text")

                self.practice_dict["id"]=self.id
                self.practice_dict["date"]=self.date
                self.practice_dict['shot_type']=self.practice_shot_type
                self.practice_dict['success']=self.practice_success
                self.practice_dict['total']=self.practice_total
                self.practice_dict['distance']=self.practice_distance
                self.practice_dict['notes']=self.practice_notes
                self.practice_dict['goals']=self.practice_goals

                self.practice_list.append(self.practice_dict.copy())
            self.df_practice=pd.DataFrame(self.practice_list)

            #print(df)
            # self.df_practice_melt=pd.melt(self.df_practice, id_vars=['id','date'],value_vars=['shot_type','success','total','distance','notes','goals'])
            # print(self.df_practice_melt)
            
    # def insert_data_practice(self):
    #     self.df_practice_melt.to_sql(con=engine, name="practice", if_exists='append')



    # def insert_data_round(self):
    #     self.df_round_melt.to_sql(con=engine, name="round", if_exists='append')







    


# pull=Api()
# pull.api()

r=File_Reader()
r.read_files()
fd=r.get_file_dict()


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
engine = create_engine(f"mysql+pymysql://root:{config('mysql_pass')}@localhost/golf")
# con=engine.connect()
d.create_connection()
d.create_database()
d.create_table()
d.insert_data()

me=Cli()
#me.cli()
#me.insert_data_practice()
# me.insert_data_round()

#functions and arguments?
#more general? Would I have multiple data cleaners?


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
store the data - done

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
    store the inputs - done
is it at the driving range? - done
    CLI - done
    date - done
    stats - done
    notes - done
    store the inputs - done


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
