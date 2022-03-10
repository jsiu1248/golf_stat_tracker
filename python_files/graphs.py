import plotly.express as px
from Database import *
import pandas as pd

class Graph: 
    def __init__(self,ch_1):
        self.ch_1=ch_1
        self.cursor_1 = self.ch_1.cursor() 
        self.pga_graph_query="SELECT * from golf.pga_data;"
        self.round_graph_query='SELECT * FROM golf.round_data;'
        self.practice_graph_query='SELECT * FROM golf.practice_data;'
   


    def putting_distance_accuracy(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        putting_distance_accurary_graph_df=pd.read_sql(self.practice_graph_query, self.ch_1)
        putting_distance_accurary_graph_df_select=putting_distance_accurary_graph_df[["DATE","SHOT_TYPE_NAME","SUCCESS","TOTAL","DISTANCE","CLUB_NAME"]]
        putting_distance_accurary_graph_df_select["ACCURACY"] =  round(putting_distance_accurary_graph_df_select["SUCCESS"] / putting_distance_accurary_graph_df_select["TOTAL"],2)
        putting_distance_accurary_graph_df_clean = putting_distance_accurary_graph_df_select[putting_distance_accurary_graph_df_select["SHOT_TYPE_NAME"]=="chip"]
        #change this so that it actually uses putting

        print(putting_distance_accurary_graph_df_clean)
        putting_distance_accurary_graph_df.sort_values(by="DATE", ascending=True)
        putting_distance_accuracy_fig = px.scatter(putting_distance_accurary_graph_df_clean, x="DISTANCE", y="ACCURACY" )
        putting_distance_accuracy_fig.show()
#actually need to change this data

    def earnings(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        earnings_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        earnings_graph_df.sort_values(by="world_rank", ascending=True)
        earnings_fig = px.scatter(earnings_graph_df, x="world_rank", y="earnings",  color="country",size='earnings', hover_data=["first_name", "last_name","earnings"])
        earnings_fig.show()

    def gir_pct(self):
    # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        gir_pct_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        gir_pct_graph_df.sort_values(by="world_rank", ascending=True)
        gir_pct_fig = px.scatter(gir_pct_graph_df, x="world_rank", y="gir_pct", hover_data=["first_name", "last_name","gir_pct"])
        gir_pct_fig.show()

    def drive_avg(self):
    # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        drive_avg_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        drive_avg_graph_df.sort_values(by="world_rank", ascending=True)
        drive_avg_fig = px.scatter(drive_avg_graph_df, x="world_rank", y="drive_avg", hover_data=["first_name", "last_name","drive_avg"])
        drive_avg_fig.show()

    def sand_saves_pct(self):
    # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        sand_saves_pct_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        sand_saves_pct_graph_df.sort_values(by="world_rank", ascending=True)
        sand_saves_pct_fig = px.scatter(sand_saves_pct_graph_df, x="world_rank", y="sand_saves_pct", hover_data=["first_name", "last_name","sand_saves_pct"])
        sand_saves_pct_fig.show()

#personal fairway

#average scores

#distance tracking
#score tracking
#average putting per round
#proximity to hold
    def avg_putting(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        avg_putting_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        avg_putting_graph_df.sort_values(by="world_rank", ascending=True)
        avg_putting_fig = px.scatter(avg_putting_graph_df, x="world_rank", y="putt_avg")
        avg_putting_fig.show()


    def score(self):
        # average_score_graph_query="CALL GOLF.average_score_GRAPH;"

#I need to add title
#maybe at the date in the future
        score_graph_df=pd.read_sql(self.round_graph_query, self.ch_1)
        score_graph_df_select=score_graph_df[["SESSION_ID","SCORE"]]
        # #change this so that it actually uses putting
        score_graph_df_clean=score_graph_df_select.groupby([score_graph_df_select.SESSION_ID]).sum()
        score_graph_df_clean_filtered= score_graph_df_clean[score_graph_df_clean["SCORE"]>0]

        score_fig = px.bar(score_graph_df_clean_filtered, x=score_graph_df_clean.index, y="SCORE")
        score_fig.show()
#how to filter out the nas