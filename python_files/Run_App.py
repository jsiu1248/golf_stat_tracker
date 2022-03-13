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
    pass
    # pull=Api()
    # pull.api()
    r=File_Reader()
    r.read_files()
    fd=r.get_file_dict()

    c=Data_Cleaner(r, fd)
    c.clean_stat_data()
#     c.clean_rank_data()
    c.clean_pga_player_data()
    c.clean_lpga_player_data()

    d=Database(c)
    ch_1=d.try_connection("localhost", "root", config("mysql_pass"))
    d_2=Database(c)
    d_2.connection(ch_1)
    d_2.create_connection()
    d_2.insert_file()

    me=Cli(ch_1)

#     me.session()
    #me.session_type()
    #me.insert_data_practice()
    # me.insert_data_round()


    g=Graph(ch_1)
    g.putting_distance_accuracy()
    # g.earnings()
    # g.gir_pct()
    # g.drive_avg()
    # g.sand_saves_pct()
    # g.avg_putting()
    # g.score()

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

#need to figure out how to compare data
#do I want to average all of the players?

#join all of my data and make my own stats
#clean up the cli code into functions

#run view script
#Add data to distance tracking
#do I need stat_type anymore?

# things to practice
# -*arg and **kwags
# decorators
# list comp
# generator
# testing
# inheritance

#pull request
#testing 
#static method - don't use self or cls
#*args pass a variable positional arguements not list, but tuple
#* unpacks iterables ** unpacks dictionaries

#add putter to club_id

#maybe allow the user to make the app do different things
#maybe add a golf hole table so that can analyze the averages later.
#maybe separate the classes into just the inputs from cli and then class to changing the data


#finish compare self
#avg
#skip sort
# figure out improvement more
#exit survey