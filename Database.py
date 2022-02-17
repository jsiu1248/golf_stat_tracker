from distutils.util import execute
from sqlite3 import OperationalError
from winreg import QueryValueEx
from decouple import config
import mysql.connector
from mysql.connector import MySQLConnection, Error
from sqlalchemy import create_engine
import pymysql
from Data_Cleaner import Data_Cleaner
import os

class Database:
    def __init__(self):
        self.cwd=os.getcwd()
        self.path="Documents\codingnomads\python_capstone"

    def try_connection(self, host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password)
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def try_connection_db(self, host_name, user_name, user_password , db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name)
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection



    def create_connection(self):
        self.cursor_1 = ch_1.cursor() 

    def create_connection_db(self):
        self.cursor_2 = ch_2.cursor()

    def read_file(self):
        file=open(os.path.join(self.cwd, self.path, f"queries.sql"), 'r')
        with open('schema.sql') as f:
            cursor.execute(f.read().decode('utf-8'), multi=True)
        # query_file=file.read()
        # file.close()
        # sqlCommands=query_file.split(";")
        # for command in sqlCommands:
        #     try:
        #         self.cursor_1.execute(command)
        #     except OperationalError as msg:
        #         print(f"Command skipped:  {msg}") 
        # ch_1.commit()


    def insert_file(self):
        file=open(os.path.join(self.cwd, self.path, f"insert_queries_v2.sql"), 'r')
        
        query_file=file.read()
        file.close()

        sqlCommands=query_file.split(";")
        for command in sqlCommands:
            try:
                pass
                # have to make if exists
                # self.cursor_1.execute(command)

        #         # print("x") #why is this printing 3 times?
            except OperationalError as msg:
                print(f"Command skipped:  {msg}") 

        try:
            lpga_insert_query="CALL GOLF.INSERT_LPGA_PLAYER(%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);"
            pga_insert_query="CALL GOLF.INSERT_PGA_PLAYER(%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);"
            stat_insert_query="CALL GOLF.INSERT_STAT(%(id)s, %(earnings)s, %(drive_avg)s, %(gir_pct)s, %(putt_avg)s, %(sand_saves_pct)s, %(birdies_per_round)s, %(hole_proximity_avg)s, %(scrambling_pct)s, %(world_rank)s);"

            for list in (lpga_player_list, pga_player_list, stat_list):
                for element in list:
                    if list==lpga_player_list:
                        self.cursor_1.execute(lpga_insert_query, element)
                    if list==pga_player_list:
                        self.cursor_1.execute(pga_insert_query, element)
                    if list==stat_list:
                        self.cursor_1.execute(stat_insert_query, element)
            ch_1.commit()

        except:
            print("not working")



        #make sure the type is correct to prevent sql injection
        #strings not invalid characters
        #stop it and give me something else
#actually shouldn't do it this way because all of it would execute all of the time. 

            # print(stat_element)

#     def create_database(self):
#         try:
#             self.database_query_create = f"""CREATE DATABASE golf;"""

#             self.cursor_1.execute(self.database_query_create)

#             ch_1.commit()
#         except Error as e:
#             print("The database exists already")

#     def create_table(self):
#         self.rank_query_create = f"""CREATE TABLE IF NOT EXISTS world_rank 
#         (
#         id VARCHAR(255),
#         world_rank INT(10), 
#         PRIMARY KEY(id));"""



#         self.stat_query_create = f"""CREATE TABLE IF NOT EXISTS stat 
#         (
#         id VARCHAR(255),
#         earnings FLOAT(13),
#         drive_avg FLOAT(6), 
#         gir_pct FLOAT(4),
#         putt_avg FLOAT(4),
#         sand_saves_pct FLOAT(4),
#         birdies_per_round FLOAT(4), 
#         hole_proximity_avg VARCHAR(255),
#         scrambling_pct FLOAT(4), 
#         world_rank INT(4),
#         PRIMARY KEY(id));"""


#         self.pga_player_query_create = f"""CREATE TABLE IF NOT EXISTS pga_player 
#         (
#         id VARCHAR(255),
#         first_name VARCHAR(255),
#         last_name VARCHAR(255), 
#         height INT (3),
#         birthday DATETIME,
#         country VARCHAR(255),
#         residence VARCHAR(255), 
#         birth_place VARCHAR(255),
#         college VARCHAR(255), 
#         PRIMARY KEY(id));"""



#         self.lpga_player_query_create = f"""CREATE TABLE IF NOT EXISTS lpga_player 
#         (
#         id VARCHAR(255),
#         first_name VARCHAR(255),
#         last_name VARCHAR(255), 
#         height VARCHAR (255),
#         birthday DATETIME,
#         country VARCHAR(255),
#         residence VARCHAR(255), 
#         birth_place VARCHAR(255),
#         college VARCHAR(255), 
#         PRIMARY KEY(id));"""

#         self.round_query_create = f"""CREATE TABLE IF NOT EXISTS round 
#         (
#         session_id INT(10),
#         hole INT(2),
#         green_reg INT(1),
#         score INT(3),
#         putt INT(1), 
#         fairway INT(1),
#         proximity_to_hole FLOAT(5), 
#         scramble INT(1),
#         PRIMARY KEY(session_id));"""



#         self.practice_query_create = f"""CREATE TABLE IF NOT EXISTS practice 
#         (
#         session_id INT(10),
#         shot_type VARCHAR(255), 
#         success INT(3),
#         total INT(3),
#         distance FLOAT(5),
#         club VARCHAR(255),
#         PRIMARY KEY(session_id));"""


#         self.golf_course_query_create = f"""CREATE TABLE IF NOT EXISTS golf_course 
#         (
#         id INT(5) AUTO_INCREMENT,
#         course_name VARCHAR(255),
#         hole INT(2), 
#         PRIMARY KEY(id));"""

#         self.session_query_create = f"""CREATE TABLE IF NOT EXISTS session
#         (
#             session_id INT(10), 
#             session_type_id INT(2), 
#             course_id INT(10), 
#             date DATETIME, 
#             notes LONGTEXT, 
#             goals LONGTEXT, 
#             PRIMARY KEY(session_id));
        
        
        
#         """

#         self.session_type_query_create = f"""CREATE TABLE IF NOT EXISTS session_type 
#         (
#         session_type_id INT(2) AUTO_INCREMENT,
#         name VARCHAR(255), 
#         UNIQUE(name),
#         PRIMARY KEY(session_type_id));
#         """


#         self.stat_type_query_create = f"""CREATE TABLE IF NOT EXISTS stat_type 
#         (
#         stat_id INT(4) AUTO_INCREMENT,
#         name VARCHAR(255), 
#         UNIQUE(name),
#         PRIMARY KEY(stat_id));
#         """

#         self.swing_type_query_create = f"""CREATE TABLE IF NOT EXISTS swing_type 
#         (
#         swing_id INT(3) AUTO_INCREMENT,
#         name VARCHAR(255), 
#         UNIQUE(name),
#         PRIMARY KEY(swing_id));
#         """

#         self.distance_tracking_query_create = f"""CREATE TABLE IF NOT EXISTS distance_tracking
#         (
#         id INT(7) AUTO_INCREMENT,
#         date DATETIME,
#         club VARCHAR(255),
#         distance FLOAT(5),

#         PRIMARY KEY(id));
#         """




#         try: 
#             for element in [self.rank_query_create, self.stat_query_create, self.pga_player_query_create, self.lpga_player_query_create, 
#                 self.round_query_create, self.practice_query_create, self.golf_course_query_create, self.session_query_create,
#                 self.session_type_query_create, self.swing_type_query_create, self.distance_tracking_query_create]:

#                 self.cursor_2.execute(element)


# #list of queries can it be automatic or manual?
# #loop and grab query run through execute then try block



#             ch_2.commit()
#         except Error as e: #f"{e}":
#             print(f"The {element}_query_create table exists already")


    # def insert_data(self):
    #     self.rank_query_insert=f"""
    #         INSERT INTO 
    #             world_rank
    #             (id,world_rank)
    #         VALUES
    #             (%(id)s, %(rank)s);
    #     """


    #     self.stat_query_insert = f""" 
        
    #         INSERT INTO 
    #             stat
    #             (id,earnings, drive_avg, gir_pct, putt_avg, sand_saves_pct, birdies_per_round, hole_proximity_avg, scrambling_pct, world_rank)
    #         VALUES
    #             (%(id)s, %(earnings)s, %(drive_avg)s, %(gir_pct)s, %(putt_avg)s, %(sand_saves_pct)s, %(birdies_per_round)s, %(hole_proximity_avg)s, %(scrambling_pct)s, %(world_rank)s);
    #         """     



    #     self.pga_player_query_insert= f"""
        
    #         INSERT INTO 
    #         pga_player
    #         (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
    #         VALUES
    #         (%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);

    #     """


    #     self.lpga_player_query_insert= f"""
        
    #         INSERT INTO 
    #         lpga_player
    #         (id, first_name, last_name, height, birthday, country, residence, birth_place, college)
    #         VALUES
    #         (%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);

    #     """


    #     self.swing_type_query_insert=f"""
        
    #     INSERT INTO 
    #     swing_type
    #     (name)
    #     VALUES
    #     ('sand'), ('chip'), ('pitch'), ('drive'), ('iron'), ('putt')
    #     """

    #     self.session_type_query_insert="""
    #     INSERT INTO 
    #     session_type
    #     (name)
    #     VALUES
    #     ('round'),('practice')"""




    #     try:
    #         for data in ((self.rank_query_insert, rank_list),(self.stat_query_insert, stat_list), (self.pga_player_query_insert, pga_player_list), (self.lpga_player_query_insert, lpga_player_list)):
    #             self.cursor_2.executemany(data[0],data[1]) 
    #             ch_2.commit()

    #     except Error as e: #f"{e}":
    #             print(f"The insert data exists already")
        
    #     try:
    #         for d in (self.swing_type_query_insert, self.session_type_query_insert):
    #             ch_2.commit()

    #     except Error as e:
    #         print(f"The {d}'s data exists already")

c=Data_Cleaner()
c.clean_stat_data()
c.clean_rank_data()
c.clean_pga_player_data()
c.clean_lpga_player_data()

rank_list=c.get_rank_list()
stat_list=c.get_stat_list()
pga_player_list=c.get_pga_player_list()
lpga_player_list=c.get_lpga_player_list()

d=Database()

ch_1=d.try_connection("localhost", "root", config("mysql_pass"))
# ch_2=d.try_connection_db("localhost", "root", config("mysql_pass"), "golf")

# engine = create_engine(f"mysql+pymysql://root:{config('mysql_pass')}@localhost/golf")
d.create_connection()
# d.create_connection_db()
# d.read_file()
d.insert_file()
#d.create_database()
#d.create_table()
#d.insert_data()
