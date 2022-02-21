from socket import create_connection
from decouple import config
import pandas as pd
import uuid
from sqlalchemy import create_engine
import pymysql
from Database import *



class Cli:
    def __init__(self):
        pass
    def session(self):
        """trying to not call self.cursor_1 here again"""
        # d_2=Database()
        # ch_1=d_2.try_connection("localhost", "root", config("mysql_pass"))
        # d_2.create_connection()
        self.cursor_1 = ch_1.cursor() 
        try:
            self.round_course=str(input("What is the name of the course? i.e. Harding Park "))
        except ValueError:
            print("Has to be text.")


        self.session_type_name=input("Is it a round or a practice? ")
        self.new_course=input("Is it a new course? yes or no.")
        self.hole=input("How many holes? 9 or 18?")
        if self.new_course is "yes":
            golf_course_insert_query="CALL GOLF.INSERT_GOLF_COURSE(%(course_name)s, %(hole)s);"
            self.golf_course_dict={}
            self.golf_course_dict["course_name"]=self.round_course
            self.golf_course_dict["hole"]=self.hole
            self.cursor_1.execute(golf_course_insert_query, self.golf_course_dict)
            ch_1.commit()


        elif self.new_course is "no":
            pass
        self.session_dict={}
        self.session_dict["date"]=input("What date is it? i.e. 12-12-2021 ")
        try:
            self.session_dict["notes"]=str(input("Did you have notes? "))
            self.session_dict["goals"]=str(input("Did you have goals? "))
        except ValueError:
            print("Has to be text.")

        


#fix this to use th variable
        # session_type_code_query="SELECT DISTINCT session_type_id from golf.session_type WHERE name=%(name)s;"

        # self.cursor_1.execute(session_type_code_query, self.session)

        session_type_code_query="SELECT DISTINCT session_type_id from golf.session_type WHERE name='practice';" #self.session_id
        session_type_code_query="SELECT DISTINCT session_type_id from golf.session_type WHERE name='round';"

        self.cursor_1.execute(session_type_code_query)

        record=self.cursor_1.fetchall()
        for i in record:
            self.session_type_id=i[0]


        course_id_query="SELECT DISTINCT course_id from golf.golf_course WHERE course_name='harding';"

        # self.cursor_1.execute(session_type_code_query, self.session)
        self.cursor_1.execute(course_id_query)

        record=self.cursor_1.fetchall()
        for i in record:
            self.course_id=i[0]
        self.session_dict["course_id"]=self.course_id
        self.session_dict["session_type_id"]=self.session_type_id


        #start making session_table
        try:
            session_insert_query="CALL GOLF.INSERT_SESSION(%(session_type_id)s, %(course_id)s, %(date)s, %(notes)s, %(goals)s);"
            self.cursor_1.execute(session_insert_query, self.session_dict)
            for element in self.session_list:
                    self.cursor_1.execute(session_insert_query, element)
            ch_1.commit()
        except mysql.connector.Error as err:
            print(err)




    #session id, type_id, course_id, 
    # done date, notes, goal

        if self.session_type_name=="round":
            self.round_list=[]
            self.round_dict={}
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

                # self.round_dict["id"]=self.id
                self.round_dict["hole"]=self.round_hole
                self.round_dict["green_reg"]=self.round_green_reg
                self.round_dict["score"]=self.round_score
                self.round_dict["putt"]=self.round_putt
                self.round_dict["fairway"]=self.round_fairway
                self.round_dict["proximity_to_hole"]=self.round_proximity_to_hole
                self.round_dict["scramble"]=self.round_scramble
                self.round_list.append(self.round_dict.copy())
            try:
                round_insert_query="CALL GOLF.INSERT_ROUND(%(hole)s, %(green_reg)s, %(score)s, %(putt)s, %(fairway)s, %(proximity_to_hole)s, %(scramble)s);"
                self.cursor_1.execute(round_insert_query, self.round_list)
                for element in self.round_list:
                        self.cursor_1.execute(round_insert_query, element)
                ch_1.commit()
            except mysql.connector.Error as err:
                print(err)

            self.df_round=pd.DataFrame(self.round_list)

            #print(df)
            # self.df_round_melt=pd.melt(self.df_round, id_vars=['id','date','round_course','round_hole'],value_vars=['round_drive','round_green_reg','round_score','round_putt','round_fairway','round_proximity_to_hole',
            # 'round_scramble','round_notes','round_goals'])
            # print(self.df_round_melt)
            # melt the data figure out how to get unique ids
            
            #insert data here if round
            # id should be cascaded here
            #round would have a number that would be in this table

        if self.session_type_name=="practice":
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
                    self.practice_club=input(f"What club did you use for the {self.practice_shot_type}? ")
                except ValueError:
                    print("Has to be a number")
                self.practice_distance=int(input(f"What was the distance of {self.practice_shot_type} were you trying? "))
                # self.practice_dict["id"]=self.id
                self.practice_dict['shot_type']=self.practice_shot_type
                self.practice_dict['success']=self.practice_success
                self.practice_dict['total']=self.practice_total
                self.practice_dict['distance']=self.practice_distance
                self.practice_dict['club']=self.practice_club

                self.practice_list.append(self.practice_dict.copy())
            try:
                    practice_insert_query="CALL GOLF.INSERT_PRACTICE(%(shot_type)s, %(success)s, %(total)s, %(distance)s, %(club)s);"
                    for element in self.practice_list:
                        self.cursor_1.execute(practice_insert_query, element)
                    ch_1.commit()
            except mysql.connector.Error as err:
                print(err)

            self.df_practice=pd.DataFrame(self.practice_list)





            #print(df)
            # self.df_practice_melt=pd.melt(self.df_practice, id_vars=['id','date'],value_vars=['shot_type','success','total','distance','notes','goals'])
            # print(self.df_practice_melt)
            
    # def insert_data_practice(self):
    #     self.df_practice_melt.to_sql(con=engine, name="practice", if_exists='append')



    # def insert_data_round(self):
    #     self.df_round_melt.to_sql(con=engine, name="round", if_exists='append')



            #insert data here if round
            # id should be cascaded here
            #session would have a number that would be in this table


# for name in dir():
#     value = globals()[name]
#     print(name, type(value), value)
