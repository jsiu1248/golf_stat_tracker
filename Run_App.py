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

    # d.create_connection()

    me=Cli()
    #me.cli()
    #me.insert_data_practice()
    # me.insert_data_round()

run=Run_App()