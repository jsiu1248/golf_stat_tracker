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
from Database import *
def Run_App():
    pass

    me=Cli()

    me.session()
    #me.session_type()
    #me.insert_data_practice()
    # me.insert_data_round()

run=Run_App()

#TODO
#decorator with property, how to loop through variables, indexing, try insert data
#club id and name table
        #getters and setters
        #can be encapsulated like properties
# date add to the files, think about if it is going to be rerunned. - low

#plotly - low
"""
How to put the database instances in the right place? - low 

How to insert the data and call it? - low 
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

#add views now and joining data
#need view for averaged data for practice and round
#need to figure out how to compare data


#join all of my data and make my own stats
#clean up the cli code into functions

#run view script
#Add data to distance tracking
#table for clubs?
#do I need stat_type anymore?
#shot_type_id
#club_id

#how to make that if duplicate then don't kick error
# 1062 (23000): Duplicate entry '4e1d40b0-e8e5-4f00-aa67-6962561fd43f' for key 'lpga_player.PRIMARY'
# 1062 (23000): Duplicate entry 'sand' for key 'shot_type.name'
#change read file to be generalized and passing parameter