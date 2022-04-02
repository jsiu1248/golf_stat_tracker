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
        self.cursor_1 = self.ch_1.cursor() 

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


    """
    creating a session for each round or practice. It gets removed later it the round or practice round doesn't go through.
    """
    def session(self): 
        # *arg and **kwags maybe here
        try:
            self.round_course=str(input("What is the name of the course? i.e. Harding Park "))
        except ValueError:
            print("Has to be text.")

        """
        If it is a new course, we are also inserting the number of holes.
        """
        session_type_name=input("Is it a round or a practice? ")
        new_course=input("Is it a new course? yes or no.")
        self.session_dict={}

        if new_course == "yes":
            hole_list=[]
            hole_dict={}
            self.hole=int(input("How many holes? 9 or 18?"))
            golf_course_insert_query="CALL GOLF.INSERT_GOLF_COURSE(%(course_name)s, %(hole)s);"
            self.golf_course_dict={}
            self.golf_course_dict["course_name"]=self.round_course
            self.golf_course_dict["hole"]=self.hole
            self.cursor_1.execute(golf_course_insert_query, self.golf_course_dict)
            self.ch_1.commit()

            # add a loop to ask for what par is each hole
            #call query insert data


            """
            We are doing a lookup for the course_id of the course_name.
            """
            course_id_query="SELECT DISTINCT id from golf.golf_course WHERE course_name=%s;"


            self.cursor_1.execute(course_id_query, (self.round_course, ))

            course_id_record=self.cursor_1.fetchall()
            self.course_id=course_id_record[0][0]


            self.session_dict["course_id"]=self.course_id


            """
            The user is asked the par for each hole. Then, the data is inserted. 
            """
            for hole_num in range(1,self.hole+1):
                hole_dict["golf_course_id"]=self.session_dict["course_id"]
                par=input(f"What was the par for hole number {hole_num}")
                hole_dict["hole_num"]=hole_num
                hole_dict["par"]=par
                hole_list.append(hole_dict.copy())
                hole_insert_query="CALL GOLF.INSERT_HOLE(%(golf_course_id)s,%(hole_num)s, %(par)s);"
            for element in hole_list:
                self.cursor_1.execute(hole_insert_query, element)
            self.ch_1.commit()

        elif new_course == "no":
            pass

#I'm repeating these lines. How can I not repeat them?
            course_id_query="SELECT DISTINCT id from golf.golf_course WHERE course_name=%s;"


            self.cursor_1.execute(course_id_query, (self.round_course, ))

            course_id_record=self.cursor_1.fetchall()
            self.course_id=course_id_record[0][0]


            self.session_dict["course_id"]=self.course_id

        """
        The date, note, and goal is entered by the user. 
        """

        self.session_dict["date"]=input("What date is it? i.e. 2021-12-30")
        try:
            self.session_dict["notes"]=str(input("Did you have notes? "))
            self.session_dict["goals"]=str(input("Did you have goals? "))
        except ValueError:
            print("Has to be text.")

        

        """
        Doing a lookup of the session_type_id where the name is either a round or practice. 
        """
        session_type_code_query="SELECT DISTINCT session_type_id from golf.session_type WHERE name=%s;"



        self.cursor_1.execute(session_type_code_query, (session_type_name,  ))
        session_type_record=self.cursor_1.fetchall()
        self.session_type_id=session_type_record[0][0]

        #Some of your session_dict and other dictionary additions could possibly be consolidated into a function that takes user input, 
        # and if it gets an invalid format, can tell the user such and then try again without stopping the whole CLI. I noticed this in line ~46 that a try/except would just skip goals and notes.

#This function could be general and take arguments like a **kwargs where each key is the key in the dict you want to return results for,
#  and the value might be a tuple of (prompt, type_expected) like ("Did you have notes? ", str). We can talk about this more on the next call



        self.session_dict["session_type_id"]=self.session_type_id


        try:
            session_insert_query="CALL GOLF.INSERT_SESSION(%(session_type_id)s, %(course_id)s, %(date)s, %(notes)s, %(goals)s);"
            self.cursor_1.execute(session_insert_query, self.session_dict)
            self.ch_1.commit()
        except mysql.connector.Error as err:
            print(err)

        try:
            session_id_query="SELECT DISTINCT session_id from golf.self_session WHERE session_id=(SELECT MAX(session_id) FROM GOLF.SELF_SESSION);"
            self.cursor_1.execute(session_id_query)

            session_id_record=self.cursor_1.fetchall()
            self.session_id=session_id_record[0][0]

            print(f"{self.session_id} is the session id")
            self.ch_1.commit()
        except mysql.connector.Error as err:
            print(err)
        
        
        """
        If the session type name equals round or practice, then run the function.
        """
        if session_type_name=="round":
            Cli.round(self)
        if session_type_name=="practice":
            Cli.practice(self)




    """
    
    """
    def round(self):
        #*arg and **kwags maybe here
            self.round_list=[]
            self.round_dict={}
            #call query that gets the lowest score and the highest score
            old_max_score_query="SELECT MAX(total_score) from golf.round_data_summary;"
            old_min_score_query="SELECT MIN(total_score) from golf.round_data_summary;"
            new_max_score_query= old_max_score_query
            new_min_score_query=old_min_score_query


            old_max_score_df=pd.read_sql(old_max_score_query, self.ch_1)
            old_max_score_df_value=old_max_score_df.iloc[0][0]

            old_min_score_df=pd.read_sql(old_min_score_query, self.ch_1)
            old_min_score_df_value=old_min_score_df.iloc[0][0]

            old_query="SELECT DRIVE_AVG, GIR_PCT, SAND_SAVES_PCT, BIRDIES_PER_ROUND, HOLE_PROXIMITY_AVG, SCRAMBLING_PCT, SCORING_AVG, PUTT_AVG FROM GOLF.STAT WHERE ID='00000000-0000-0000-0000-000000000001'"
            new_query=old_query
            old_df=pd.read_sql(old_query,self.ch_1)


            #so only this line needs to change for each variable. 
            old_drive_avg_df_value=old_df.iloc[0][0]
            old_gir_pct_df_value=old_df.iloc[0][1]
            old_sand_saves_pct_df_value=old_df.iloc[0][2]
            old_scrambling_pct_df_value=old_df.iloc[0][5]
            old_avg_score_df_value=old_df.iloc[0][6]
            old_putt_avg_df_value=old_df.iloc[0][7]



            try:
                self.round_num_holes=int(input("How many number of holes did you play? 9 or 18 "))
            except ValueError:
                print("Has to be a number.")
                self.ch_1.rollback()

            for self.round_hole in range(1,self.round_num_holes+1):
                try:
                    # self.round_drive=int(input("What was the driving distance? i.e 300. "))
                    self.round_green_reg=int(input("What is greens in regulation? i.e. 1 or 0 "))

                    self.round_score=int(input("What was the score? i.e. 5 "))
                    self.round_putt=int(input("How many putts? i.e. 2 "))
                    self.round_fairway=int(input("Did you hit the fairway? i.e. 1 or 0 "))
                    self.round_proximity_to_hole=int(input("What was the proximity to the hole in yards? i.e. 39 "))
                    self.round_scramble=int(input("Did you scramble? i.e. 1 or 0 "))
                    self.round_sand_success=int(input("How many sand successes did you have? i.e. 2 "))
                    self.round_sand_total=int(input("How many total sand shots did you have? i.e. 4 "))

                except ValueError:
                    print("Has to be a number.")
                    self.ch_1.rollback()
                self.round_dict["player_id"]='00000000-0000-0000-0000-000000000001'
                self.round_dict["session_id"]=self.session_id
                self.round_dict["hole"]=self.round_hole
                self.round_dict["green_reg"]=self.round_green_reg
                self.round_dict["score"]=self.round_score
                self.round_dict["putt"]=self.round_putt
                self.round_dict["fairway"]=self.round_fairway
                self.round_dict["proximity_to_hole"]=self.round_proximity_to_hole
                self.round_dict["scramble"]=self.round_scramble
                self.round_dict["sand_success"]=self.round_sand_success
                self.round_dict["sand_total"]=self.round_sand_total


                self.round_list.append(self.round_dict.copy())
            try:
                round_insert_query="CALL GOLF.insert_ROUND(%(player_id)s,%(session_id)s, %(hole)s, %(green_reg)s, %(score)s, %(putt)s, %(fairway)s, %(proximity_to_hole)s, %(scramble)s, %(sand_success)s, %(sand_total)s);"
                for element in self.round_list:
                        self.cursor_1.execute(round_insert_query, element)
                self.ch_1.commit()
            except mysql.connector.Error as err:
                print(err)

            self.df_round=pd.DataFrame(self.round_list)

            new_max_score_df=pd.read_sql(new_max_score_query, self.ch_1)
            new_max_score_df_value=new_max_score_df.iloc[0][0]

            new_min_score_df=pd.read_sql(new_min_score_query, self.ch_1)
            new_min_score_df_value=new_min_score_df.iloc[0][0]



            new_df=pd.read_sql(new_query, self.ch_1)
            new_drive_avg_df_value=new_df.iloc[0][0]
            new_gir_pct_df_value=new_df.iloc[0][1]
            new_sand_saves_pct_df_value=new_df.iloc[0][2]
            new_scrambling_pct_df_value=new_df.iloc[0][5]
            new_avg_score_df_value=new_df.iloc[0][6]
            new_putt_avg_df_value=new_df.iloc[0][7]

            #which avg score should I use?



            if old_max_score_df_value<new_max_score_df_value:
                print(f"Aw. You you have a new high score from {old_max_score_df_value} to {new_max_score_df_value} for your total score. Keep practicing.")
            if old_min_score_df_value>new_min_score_df_value:
                print(f"Yay. You improved from {old_min_score_df_value} to {new_min_score_df_value} for your total score. A {(new_min_score_df_value-old_min_score_df_value)/old_min_score_df_value*100}% decrease.")
            if old_avg_score_df_value>new_avg_score_df_value:
                print(f"Yay. You improved from {old_avg_score_df_value} to {new_avg_score_df_value} for your average score. A {(new_avg_score_df_value-old_avg_score_df_value)/old_avg_score_df_value*100}% decrease.")


            if old_drive_avg_df_value<new_avg_score_df_value:
                print(f"Yay. You improved from {old_drive_avg_df_value} to {new_drive_avg_df_value} for your drive average. A {(new_drive_avg_df_value - old_drive_avg_df_value)/old_drive_avg_df_value*100}% increase.")
            if old_gir_pct_df_value<new_gir_pct_df_value:
                print(f"Yay. You improved from {old_gir_pct_df_value} to {new_gir_pct_df_value} for your greens in regulation pct. A {(new_gir_pct_df_value - old_gir_pct_df_value)/old_gir_pct_df_value*100}% increase.")
            if old_scrambling_pct_df_value<new_scrambling_pct_df_value:
                print(f"Yay. You improved from {old_scrambling_pct_df_value} to {new_scrambling_pct_df_value} for your scrambling pct. A {(new_scrambling_pct_df_value - old_scrambling_pct_df_value)/old_scrambling_pct_df_value*100}% increase.")
            if old_putt_avg_df_value>new_putt_avg_df_value:
                print(f"Yay. You improved from {old_putt_avg_df_value} to {new_putt_avg_df_value} for your putting average. A {(new_putt_avg_df_value - old_putt_avg_df_value)/old_putt_avg_df_value*100}% decrease.")
            if old_sand_saves_pct_df_value is not None and new_sand_saves_pct_df_value is not None and old_sand_saves_pct_df_value<new_sand_saves_pct_df_value :
                print(f"Yay. You improved from {old_sand_saves_pct_df_value} to {new_sand_saves_pct_df_value} for your sand save pct. A {(new_sand_saves_pct_df_value - old_sand_saves_pct_df_value)/old_sand_saves_pct_df_value*100}% increase.")




#4/1/2022
#do I want to average all of the players?




            #print(df)
            # self.df_round_melt=pd.melt(self.df_round, id_vars=['id','date','round_course','round_hole'],value_vars=['round_drive','round_green_reg','round_score','round_putt','round_fairway','round_proximity_to_hole',
            # 'round_scramble','round_notes','round_goals'])
            # print(self.df_round_melt)
            # melt the data figure out how to get unique ids
            
            #insert data here if round
            # id should be cascaded here
    def practice(self): # can use arguements here if I want to
        #*arg and **kwags maybe here
            try:
                self.num_type=int(input("How many types of shots were you try this time? i.e 2 "))
            except ValueError:
                print("Has to be a number")
                self.ch_1.rollback()

            self.practice_list=[]
            self.practice_dict={}
            for num in range(1,self.num_type+1):
                try:
                    self.practice_shot_type=str(input("What is the shot type? ie. chip, drive, putt, pitch, sand, iron "))
                except ValueError:
                    print("Has to be text.")
                    self.ch_1.rollback()

                try: 
                    self.practice_success=int(input(f"What many times did you success the {self.practice_shot_type} i.e. 2 "))
                    self.practice_total=int(input(f"How many total {self.practice_shot_type} did you make? i.e. 3"))
                    self.practice_distance=int(input(f"What was the distance of {self.practice_shot_type} were you trying in yards? i.e. 123 "))

                except ValueError:
                    print("Has to be a number")
                    self.ch_1.rollback()

                self.practice_dict["session_id"]=self.session_id
                self.practice_club=input(f"What club did you use for the {self.practice_shot_type}? i.e. 9_iron ")


                shot_type_query="SELECT DISTINCT shot_id from golf.shot_type WHERE name=%s;"


                self.cursor_1.execute(shot_type_query, (self.practice_shot_type, ))

                shot_type_record=self.cursor_1.fetchall()

                #not sure where to put a lambda. But, I can probably put this as a list comp again
                self.practice_shot_type_id=shot_type_record[0][0]

                # self.sess_dict["course_id"]=self.course_id

                self.practice_dict["player_id"]='00000000-0000-0000-0000-000000000001'

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
                    practice_insert_query="CALL GOLF.insert_PRACTICE(%(player_id)s,%(session_id)s, %(shot_type_id)s, %(success)s, %(total)s, %(distance)s, %(club_id)s);"
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



