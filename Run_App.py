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

    #me=Cli()
    #me.session()
    #me.session_type()
    #me.insert_data_practice()
    # me.insert_data_round()

run=Run_App()

#TODO
#have to correct the database to create and kick an error if it isn't created
#how to insert the data
#decorator with property, how to loop through variables, indexing, try insert data, make data back into wide
#club id and name table
        #getters and setters
        #can be encapsulated like properties
# date add to the files, think about if it is going to be rerunned.
# figure out session tables and the logic for figuring out the joining

#plotly
#try to put Database instances here
#export