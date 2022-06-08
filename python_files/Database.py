from distutils.util import execute
from sqlite3 import OperationalError
from decouple import config
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import pymysql
# from Data_Cleaner import Data_Cleaner
import os


"""
Connecting to database and then inserting data
"""
class Database:
    def __init__(self,c):
        self.cwd=os.getcwd()
        self.path="Documents\codingnomads\python_capstone"
        
        # getting the clean data from the data cleaner
        # self.rank_list=c.get_rank_list()
        self.stat_list=c.get_stat_list()
        self.pga_player_list=c.get_pga_player_list()
        self.lpga_player_list=c.get_lpga_player_list()
        

# testing the connection
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

#creating this as a class method
    @classmethod
    def connection(cls,ch_1 ):
        cls.ch_1=ch_1



    # def try_connection_db(self, host_name, user_name, user_password , db_name):
    #     connection = None
    #     try:
    #         connection = mysql.connector.connect(
    #             host=host_name,
    #             user=user_name,
    #             passwd=user_password,
    #             database=db_name)
    #         print("Connection to MySQL DB successful")
    #     except Error as e:
    #         print(f"The error '{e}' occurred")

    #     return connection



    def create_connection(self):
        self.cursor_1 = self.ch_1.cursor() 

    # def create_connection_db(self):
    #     self.cursor_2 = self.ch_2.cursor()


        """
        Inserting data through paramenters and calling the queries through procedures
        """
    def insert_file(self):

        try: #don't need this
            lpga_insert_query="CALL GOLF.INSERT_LPGA_PLAYER(%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);"
            pga_insert_query="CALL GOLF.INSERT_PGA_PLAYER(%(id)s, %(first_name)s, %(last_name)s, %(height)s, %(birthday)s, %(country)s, %(residence)s, %(birth_place)s, %(college)s);"
            stat_insert_query="CALL GOLF.INSERT_STAT(%(id)s, %(earnings)s, %(drive_avg)s, %(gir_pct)s, %(putt_avg)s, %(sand_saves_pct)s, %(birdies_per_round)s, %(hole_proximity_avg)s, %(scrambling_pct)s, %(world_rank)s, %(scoring_avg)s);"
            golf_course_insert_query="CALL GOLF.INSERT_GOLF_COURSE(%(course_name)s, %(hole)s);"

            session_type_insert_query="CALL GOLF.INSERT_SESSION_TYPE;"
            stat_type_insert_query="CALL GOLF.INSERT_STAT_TYPE;"
            shot_type_insert_query="CALL GOLF.INSERT_SHOT_TYPE;"
            club_insert_query="CALL GOLF.INSERT_CLUB;"




        # going through the tuple of lists of data and if it equals the name then the data would insert and if it has the data already then it won't kick back an error

            for list in (self.lpga_player_list, self.pga_player_list, self.stat_list):
                for element in list: #put try except here
                    if list==self.lpga_player_list:
                        self.cursor_1.execute(lpga_insert_query, element)
                    if list==self.pga_player_list:
                        self.cursor_1.execute(pga_insert_query, element)
                    if list==self.stat_list:
                        self.cursor_1.execute(stat_insert_query, element)
            self.ch_1.commit()
        except mysql.connector.Error as err: # try to find a more specific error 
            print(err) # maybe general database error. look for the type of expection

        try:
            #list comprehension maybe
            #In this case: maybe. It may work for calling the execute function multiple times for your queries, but usually list comp is used for lists of things and not for calling something a bunch of times.

#I would stick with a standard for loop
            
            #inserting data for club, shot_type, and stat_type. All of these are reference tables. 
            for query in (club_insert_query, shot_type_insert_query, stat_type_insert_query, 
            session_type_insert_query):
                self.cursor_1.execute(query)
                self.ch_1.commit()
        except mysql.connector.Error as err:
            print(err)



        #make sure the type is correct to prevent sql injection
        #strings not invalid characters
        #stop it and give me something else
#actually shouldn't do it this way because all of it would execute all of the time. 







