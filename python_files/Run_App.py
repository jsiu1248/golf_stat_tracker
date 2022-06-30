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
from Cli import Cli
from File_Reader import File_Reader
from data_cleaner import Data_Cleaner
from Database import *
from graphs import Graph
def Run_App():


    """
    The file runs all of functions. After all of the pga data is created and inserted, you will be inserting your own data with new practice rounds of 9/18 holes.
    The graphs may not be created without data.
    """
    #pull the data from the Golf Rader API.
    # pull=Api()
    # pull.api()


    r=File_Reader()
    # creates the file paths and then reads the json files
    r.read_files()
    # this just returns the data 
    fd=r.get_file_dict()

    c=Data_Cleaner(r, fd)
    #cleans the respective datasets
    c.clean_stat_data()
#     c.clean_rank_data()
    c.clean_pga_player_data()
    c.clean_lpga_player_data()

    d=Database(c)
    #makes sure that the connection works. 
    ch_1=d.try_connection("localhost", "root", config("mysql_pass"))
    d_2=Database(c)
    d_2.connection(ch_1)
    d_2.create_connection()
    #insert the data into mysql database if list name matches
    d_2.insert_file()


    user_input=int(input("""
    1. Enter round or practice data.
    2. Access my graphs.
    3. Update data from table. (For the future)
    4. Select data from table. (For the future)
    5. Delete data from table. (For the future)
    6. Last goal check.
    """))

# when selected you will either choose to either enter round or practice data through the CLI class.
    if user_input==1:
        me=Cli(ch_1)
        me.session()
        # me.session_type()

        """ 
        the following are unnecessary unless I will change the data to long form instead of wide
        """
        # me.insert_data_practice()
        # me.insert_data_round()

    if user_input==2:
        g=Graph(ch_1)
        graph_input=int(input("""
        Which graph do you want?
        1. Putting Distance Accuracy
        2. Earnings
        3. Greens in Regulation
        4. Drive Averages
        5. Sand Save Percentages
        6. Average Putting
        7. Personal Score Tracking
        """))
        
        if graph_input==1: #working
            g.putting_distance_accuracy()
        elif graph_input==2: # working
            g.earnings()
        elif graph_input==3: #working
            g.gir_pct()
        elif graph_input==4: #working
            g.drive_avg()
        elif graph_input==5: #working
            g.sand_saves_pct()
        elif graph_input==6: #working
            g.avg_putting()
        elif graph_input==7: #working
            g.score()
    
    if user_input==6:
        pass

run=Run_App()

#TODO
#decorator with property, how to loop through variables, indexing, try insert data
        #getters and setters
        #can be encapsulated like properties
    
# date add to the files, think about if it is going to be rerunned. - low

"""

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
        #how to break into smaller pieces of code
        # functions and what it would take
        #json and some structure in turning into a list
        #tricky multiple json things are different structure. 
        #use classes and inheritance
        #composition, design patterns
        #grab json file, single responsibility
        #class that takes json and abstract class process function or method
        #other classes that herit from that abstract class
        #json processor lpga json processor, process to find it needs to do and output to 
        $process the list



"""



#Add data to distance tracking
#do I need stat_type anymore?

# things to practice
# -*arg and **kwags
# decorators
# list comp
# generator
# testing
# inheritance

#testing 
#*args pass a variable positional arguements not list, but tuple
#* unpacks iterables ** unpacks dictionaries


#maybe separate the classes into just the inputs from cli and then class to changing the data



#add data to putt distance
#add data to club distance

#hole_prox_avg,






