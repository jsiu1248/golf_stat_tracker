from decouple import config
import os
import json
from datetime import datetime 
from Url import url

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

