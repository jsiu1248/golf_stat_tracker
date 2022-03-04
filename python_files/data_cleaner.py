from decouple import config
from mysql.connector import Error
from datetime import datetime 
import pandas as pd
from sqlalchemy import create_engine
# from File_Reader import File_Reader

class Data_Cleaner():
    def __init__(self,r, fd):

#how to make this into arguments
        # for i in ["rank","stat","pga_player","lpga_player"]:
        # self.rank_dict={}
        # self.rank_list=[]
        self.stat_dict={}
        self.stat_list=[]
        self.pga_player_dict={}
        self.pga_player_list=[]
        self.lpga_player_dict={}
        self.lpga_player_list=[]
        self.lpga_tounament_dict={}
        self.lpga_tounament_list=[]
        self.fd=fd



    # def clean_rank_data(self):
    #     for rank_element in self.fd["ranking_data"]["players"]:
    #         for element in ("id","rank"):
    #             self.rank_dict[element]=rank_element[element]

    #         self.rank_list.append(self.rank_dict.copy())
        # return self.rank_list
        #print(self.rank_list)
    def clean_stat_data(self):
        self.stat="statistics"
        for stat_element in self.fd["stat_data"]["players"]:
            for element in (['id'],(self.stat,'earnings'),(self.stat,'drive_avg'),
            (self.stat,'gir_pct'),(self.stat,'putt_avg'),(self.stat,'sand_saves_pct'),(self.stat,'birdies_per_round'),
            (self.stat,'hole_proximity_avg'),(self.stat,'scrambling_pct'),(self.stat,'world_rank')):
                try:
                    if len(element)==1:
                        self.stat_dict[element[0]]=stat_element[element[0]]
                    elif len(element)==2:
                        self.stat_dict[element[1]]=stat_element[element[0]][element[1]]

                except KeyError: 
                    if len(element)==1:

                        self.stat_dict[element[0]]=None
                    elif len(element)==2:
                        self.stat_dict[element[1]]=None



            self.stat_list.append(self.stat_dict.copy())
        # return self.stat_list


        #print(self.stat_list)
    def clean_pga_player_data(self):
        for pga_player_element in self.fd["pga_player_data"]["players"]:
            for element in (['id'],['first_name'],['last_name'],['height'],['birthday'],['country'],['residence'],['birth_place'],['college']):
                try:
                    if element[0]=="birthday":
                        self.pga_player_dict[element[0]]=datetime.strptime(pga_player_element[element[0]], "%Y-%m-%dT%H:%M:%S+00:00")

                    else:
                        self.pga_player_dict[element[0]]=pga_player_element[element[0]]
                except KeyError: 
                    self.pga_player_dict[element[0]]=None


            self.pga_player_list.append(self.pga_player_dict.copy())
        #return self.pga_player_list
        # print(self.pga_player_list)
    def clean_lpga_player_data(self):
        for lpga_player_element in self.fd["lpga_player_data"]["players"]:
            for element in (['id'],['first_name'],['last_name'],['height'],['birthday'],['country'],['residence'],['birth_place'],['college']):

                try:
                    if element[0]=="birthday":
                        self.lpga_player_dict[element[0]]=datetime.strptime(lpga_player_element[element[0]], "%Y-%m-%dT%H:%M:%S+00:00")

                    else:
                        self.lpga_player_dict[element[0]]=lpga_player_element[element[0]]

                except KeyError: 
                    self.lpga_player_dict[element[0]]=None


            self.lpga_player_list.append(self.lpga_player_dict.copy())
        # return self.lpga_player_list
        # print(self.lpga_player_list)
    def clean_lpga_tournament_data(self):
        for lpga_tournament_element in self.fd["lpga_tournament_data"]["tournaments"]:
            print(lpga_tournament_element)
    # def get_rank_list(self):
    #     return self.rank_list

    def get_stat_list(self):
        return self.stat_list
    def get_pga_player_list(self):
        return self.pga_player_list
    def get_lpga_player_list(self):
        return self.lpga_player_list
        #getters and setters
        #can be encapsulated like properties

