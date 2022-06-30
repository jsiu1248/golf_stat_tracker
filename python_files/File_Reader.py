from decouple import config
import os
import json
from datetime import datetime 
from Url import url

""""
Reading the json files
NOTE: May have to change self.path depending on where folders are stored.
"""
class File_Reader():
    def __init__(self):
        self.cwd=os.getcwd()
        self.path="Documents/python_capstone/data"

    def read_files(self):
        self.file_dict={}
        for key, value in url.items():
            self.file_path=os.path.join(self.cwd,self.path,f'{key}_data.json')
#how would I include the date?

# read json files
            with open(self.file_path) as self.json_file:
                self.file_dict[f'{key}_data']=json.load(self.json_file)#.rstrip("\n")
    def get_file_dict(self):
        return self.file_dict

