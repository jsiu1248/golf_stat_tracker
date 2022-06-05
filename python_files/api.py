import requests
from decouple import config
import os
import json
from Url import url

""""
looping through the links and then write the content into a json file.
NOTE: the self.path may need to be changed depending on where and how you store your folder. 

"""
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

        """
        We are looping through the keys and values of the dictionary called url. self.response is the get request. Remember to set up your env file to have the api_key.
        """
        for key,value in url.items():
            self.response=requests.get(value, params={"api_key":config("golf_demo")})

            self.status=self.response.status_code
            #make the files with the json paths
            self.file  = open(os.path.join(self.cwd,self.path,f"{key}_data.json"), "w+")

            #get the text of the response
            self.golf_data=self.response.json()

            #dump the data into the files
            json.dump(self.golf_data, self.file)


            #file.write(f"{golf_data}")
            self.file.close()



