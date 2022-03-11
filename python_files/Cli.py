from socket import create_connection
from decouple import config
import pandas as pd
import uuid
from sqlalchemy import create_engine
import pymysql
from Database import *



class Cli:
    def __init__(self,ch_1):
        self.ch_1=ch_1
        #You can pass a few things here to set some of the classes self variables ####
    # maybe some things can be added to the constructor
    #clean up not everything self
    #set self at the end of method
    #cli that only gets questions
    #then another class to use the data 
    #having individual roles lets me put all of the pieces together

    # user ability for graphs and changing data
    #update sql statment
    # ONLY  access to self tables
    #grab id to edit this
    #how to reuse class already
    #can reuse for inputting data 


    def session(self): 
        # *arg and **kwags maybe here
        #This is a possibility, but I'd like to hear from you what you think can be *args/**kwargs in this function :)
        self.cursor_1 = self.ch_1.cursor() 
        try:
            self.round_course=str(input("What is the name of the course? i.e. Harding Park "))
        except ValueError:
            print("Has to be text.")


        session_type_name=input("Is it a round or a practice? ")
        new_course=input("Is it a new course? yes or no.")
        if new_course == "yes":
            self.hole=input("How many holes? 9 or 18?")
            golf_course_insert_query="CALL GOLF.INSERT_GOLF_COURSE(%(course_name)s, %(hole)s);"
            self.golf_course_dict={}
            self.golf_course_dict["course_name"]=self.round_course
            self.golf_course_dict["hole"]=self.hole
            self.cursor_1.execute(golf_course_insert_query, self.golf_course_dict)
            self.ch_1.commit()


        elif new_course == "no":
            pass
        self.session_dict={}
        self.session_dict["date"]=input("What date is it? i.e. 2021-12-30")
        try:
            self.session_dict["notes"]=str(input("Did you have notes? "))
            self.session_dict["goals"]=str(input("Did you have goals? "))
        except ValueError:
            print("Has to be text.")

        


        session_type_code_query="SELECT DISTINCT session_type_id from golf.session_type WHERE name=%s;"



        self.cursor_1.execute(session_type_code_query, (session_type_name,  ))
        session_type_record=self.cursor_1.fetchall()
        self.session_type_id=session_type_record[0][0]

        #Some of your session_dict and other dictionary additions could possibly be consolidated into a function that takes user input, 
        # and if it gets an invalid format, can tell the user such and then try again without stopping the whole CLI. I noticed this in line ~46 that a try/except would just skip goals and notes.

#This function could be general and take arguments like a **kwargs where each key is the key in the dict you want to return results for,
#  and the value might be a tuple of (prompt, type_expected) like ("Did you have notes? ", str). We can talk about this more on the next call

        course_id_query="SELECT DISTINCT id from golf.golf_course WHERE course_name=%s;"


        self.cursor_1.execute(course_id_query, (self.round_course, ))

        course_id_record=self.cursor_1.fetchall()
        self.course_id_record=course_id_record[0][0]


        self.session_dict["course_id"]=self.course_id
        self.session_dict["session_type_id"]=self.session_type_id


        try:
            session_insert_query="CALL GOLF.INSERT_SESSION(%(session_type_id)s, %(course_id)s, %(date)s, %(notes)s, %(goals)s);"
            self.cursor_1.execute(session_insert_query, self.session_dict)
            self.ch_1.commit()
        except mysql.connector.Error as err:
            print(err)

#Yes, I think so! What might that look like? list comp
        try:
            session_id_query="SELECT DISTINCT session_id from golf.self_session WHERE session_id=(SELECT MAX(session_id) FROM GOLF.SELF_SESSION);"
            self.cursor_1.execute(session_id_query)

            session_id_record=self.cursor_1.fetchall()
            self.session_id=session_id_record[0][0]

            print(f"{self.session_id} is the session id")
            self.ch_1.commit()
        except mysql.connector.Error as err:
            print(err)
        if session_type_name=="round":
            Cli.round(self)
        if session_type_name=="practice":
            Cli.practice(self)


#invalid use of group gunction


#how to get session_id to go to round and practice?
#cascade to create a new row if round or practice
# update the new row using update with data here in python - pretty sure this part is almost done unless I need to use update vs insert

    def round(self):
        #*arg and **kwags maybe here
            self.round_list=[]
            self.round_dict={}
            try:
                self.round_num_holes=int(input("How many number of holes did you play? 9 or 18 "))
            except ValueError:
                print("Has to be a number.")

            for self.round_hole in range(1,self.round_num_holes+1):
                try:
                    # self.round_drive=int(input("What was the driving distance? i.e 300. "))
                    self.round_green_reg=int(input("What is greens in regulation? i.e. 1 or 0 "))

                    self.round_score=int(input("What was the score? i.e. 5 "))
                    self.round_putt=int(input("How many putts? i.e. 2 "))
                    self.round_fairway=int(input("Did you hit the fairway? i.e. 1 or 0 "))
                    self.round_proximity_to_hole=int(input("What was the promity to the hole in feet? i.e. 39 "))
                    self.round_scramble=int(input("Did you scramble? i.e. 1 or 0 "))
                except ValueError:
                    print("Has to be a number.")

                self.round_dict["session_id"]=self.session_id
                self.round_dict["hole"]=self.round_hole
                self.round_dict["green_reg"]=self.round_green_reg
                self.round_dict["score"]=self.round_score
                self.round_dict["putt"]=self.round_putt
                self.round_dict["fairway"]=self.round_fairway
                self.round_dict["proximity_to_hole"]=self.round_proximity_to_hole
                self.round_dict["scramble"]=self.round_scramble
                self.round_list.append(self.round_dict.copy())
            try:
                round_insert_query="CALL GOLF.insert_ROUND(%(session_id)s, %(hole)s, %(green_reg)s, %(score)s, %(putt)s, %(fairway)s, %(proximity_to_hole)s, %(scramble)s);"
                for element in self.round_list:
                        self.cursor_1.execute(round_insert_query, element)
                self.ch_1.commit()
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
    def practice(self): # can use arguements here if I want to
        #*arg and **kwags maybe here
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
                self.practice_dict["session_id"]=self.session_id


                shot_type_query="SELECT DISTINCT shot_id from golf.shot_type WHERE name=%s;"


                self.cursor_1.execute(shot_type_query, (self.practice_shot_type, ))

                shot_type_record=self.cursor_1.fetchall()

                #not sure where to put a lambda. But, I can probably put this as a list comp again
                self.practice_shot_type_id=shot_type_record[0][0]

                self.session_dict["course_id"]=self.course_id

                
                self.practice_dict['shot_type_id']=self.practice_shot_type_id


                self.practice_dict['success']=self.practice_success
                self.practice_dict['total']=self.practice_total
                self.practice_dict['distance']=self.practice_distance

                club_query="SELECT DISTINCT club_id from golf.club WHERE name=%s;"
                self.cursor_1.execute(club_query, (self.practice_club, ))

                club_record=self.cursor_1.fetchall()
                self.practice_club_id=club_record[0][0]


                self.practice_dict['club_id']=self.practice_club_id
                #need to change this to the id

                self.practice_list.append(self.practice_dict.copy())
            try:
                    practice_insert_query="CALL GOLF.insert_PRACTICE(%(session_id)s, %(shot_type_id)s, %(success)s, %(total)s, %(distance)s, %(club_id)s);"
                    for element in self.practice_list:
                        self.cursor_1.execute(practice_insert_query, element)
                    self.ch_1.commit()
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



