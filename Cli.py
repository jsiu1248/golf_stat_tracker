from decouple import config
import pandas as pd
import uuid
from sqlalchemy import create_engine
import pymysql
# from Database import Database



class Cli:
    def __init__(self):
        pass
    def cli(self):
        self.date=input("What date is it? i.e. 12-12-2021 ")
        self.session=input("Is it a round or a practice? ")
        self.id=uuid.uuid4() # where should I change the id?
        session_list=[]
        session_dict={}
        #session id, course_id, date, notes, goals
        if self.session=="round":
            self.round_list=[]
            self.round_dict={}
            try:
                self.round_course=str(input("What is the name of the course? i.e. Harding Park "))
            except ValueError:
                print("Has to be text.")
            try:
                self.round_num_holes=int(input("How many number of holes did you play? 9 or 18 "))
            except ValueError:
                print("Has to be a number.")

            for self.round_hole in range(1,self.round_num_holes+1):
                try:
                    self.round_drive=int(input("What was the driving distance? i.e 300. "))
                    self.round_green_reg=int(input("What is greens in regulation? i.e. 1 or 0 "))

                    self.round_score=int(input("What was the score? i.e. 59 "))
                    self.round_putt=int(input("How many putts? i.e. 2 "))
                    self.round_fairway=int(input("Did you hit the fairway? i.e. 1 or 0 "))
                    self.round_proximity_to_hole=int(input("What was the promity to the hole in feet? i.e. 39 "))
                    self.round_scramble=int(input("Did you scramble? i.e. 1 or 0 "))
                except ValueError:
                    print("Has to be a number.")
                try:
                    self.round_notes=str(input("Did you have notes? "))
                    self.round_goals=str(input("Did you have goals? "))
                except ValueError:
                    print("Has to be text.")

                self.round_dict["id"]=self.id
                self.round_dict["date"]=self.date
                self.round_dict["round_course"]=self.round_course
                self.round_dict["round_hole"]=self.round_hole
                self.round_dict["round_drive"]=self.round_drive
                self.round_dict["round_green_reg"]=self.round_green_reg
                self.round_dict["round_score"]=self.round_score
                self.round_dict["round_putt"]=self.round_putt
                self.round_dict["round_fairway"]=self.round_fairway
                self.round_dict["round_proximity_to_hole"]=self.round_proximity_to_hole
                self.round_dict["round_scramble"]=self.round_scramble
                self.round_dict["round_notes"]=self.round_notes
                self.round_dict["round_goals"]=self.round_goals
                self.round_list.append(self.round_dict.copy())
            self.df_round=pd.DataFrame(self.round_list)

            #print(df)
            # self.df_round_melt=pd.melt(self.df_round, id_vars=['id','date','round_course','round_hole'],value_vars=['round_drive','round_green_reg','round_score','round_putt','round_fairway','round_proximity_to_hole',
            # 'round_scramble','round_notes','round_goals'])
            # print(self.df_round_melt)

            
# melt the data figure out how to get unique ids

        if self.session=="practice":
            # how do I change the data when I did something wrong?
            try:
                self.num_type=int(input("How many types of shots were you try this time?"))
            except ValueError:
                print("Has to be a number")
            self.practice_list=[]
            self.practice_dict={}
            for num in range(1,self.num_type+1):
                try:
                    self.practice_shot_type=str(input("What is the shot type? ie. chip, drive, putt, pitch, sand, iron "))
                except ValueError:
                    print("Has to be text.")
                try: 
                    self.practice_success=int(input(f"What many times did you success the {self.practice_shot_type} "))
                    self.practice_total=int(input(f"How many total {self.practice_shot_type} did you make? "))
                    self.practice_distance=int(input(f"What was the distance of {self.practice_shot_type} were you trying? "))
                except ValueError:
                    print("Has to be a number")
                try:
                    self.practice_notes=str(input("Did you have notes? "))
                    self.practice_goals=str(input("Did you have goals? "))
                except ValueError:
                    print("Has to be text")

                self.practice_dict["id"]=self.id
                self.practice_dict["date"]=self.date
                self.practice_dict['shot_type']=self.practice_shot_type
                self.practice_dict['success']=self.practice_success
                self.practice_dict['total']=self.practice_total
                self.practice_dict['distance']=self.practice_distance
                self.practice_dict['notes']=self.practice_notes
                self.practice_dict['goals']=self.practice_goals

                self.practice_list.append(self.practice_dict.copy())
            self.df_practice=pd.DataFrame(self.practice_list)

            #print(df)
            # self.df_practice_melt=pd.melt(self.df_practice, id_vars=['id','date'],value_vars=['shot_type','success','total','distance','notes','goals'])
            # print(self.df_practice_melt)
            
    # def insert_data_practice(self):
    #     self.df_practice_melt.to_sql(con=engine, name="practice", if_exists='append')



    # def insert_data_round(self):
    #     self.df_round_melt.to_sql(con=engine, name="round", if_exists='append')






