import plotly.express as px
from Database import *
import pandas as pd
import plotly.graph_objects as go


"""
Functions for the different graphs
"""
class Graph: 
    def __init__(self,ch_1):
        self.ch_1=ch_1
        self.cursor_1 = self.ch_1.cursor() 
        self.pga_graph_query="SELECT * from golf.player_pga_data;"
        self.round_graph_query='SELECT * FROM golf.round_data;'
        self.practice_graph_query='SELECT * FROM golf.practice_data;'
   

    """
    Graph for putting distance accuracy
    """
    def putting_distance_accuracy(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"


        putting_distance_accurary_graph_df=pd.read_sql(self.practice_graph_query, self.ch_1)
        putting_distance_accurary_graph_df_select=putting_distance_accurary_graph_df[["DATE","SHOT_TYPE_NAME","SUCCESS","TOTAL","DISTANCE","CLUB_NAME"]]
        # creating accuracy
        putting_distance_accurary_graph_df_select["ACCURACY"] =  round(putting_distance_accurary_graph_df_select["SUCCESS"] / putting_distance_accurary_graph_df_select["TOTAL"],2)
        putting_distance_accurary_graph_df_clean = putting_distance_accurary_graph_df_select[putting_distance_accurary_graph_df_select["SHOT_TYPE_NAME"]=="putt"]

        print(putting_distance_accurary_graph_df_clean)
        putting_distance_accurary_graph_df.sort_values(by="DATE", ascending=True)
        putting_distance_accuracy_fig = px.scatter(putting_distance_accurary_graph_df_clean, x="DISTANCE", y="ACCURACY", 
        title="Putting Distance Accuracy", range_x=(0,max(putting_distance_accurary_graph_df_clean.DISTANCE)), range_y=(0,max(putting_distance_accurary_graph_df_clean.ACCURACY)))
        putting_distance_accuracy_fig.show()
#actually need to change this data


    """
    Graph for earnings comparision
    """
    def earnings(self):


        earnings_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        earnings_graph_df.sort_values(by="world_rank", ascending=True)
        earnings_fig = px.scatter(earnings_graph_df, x="world_rank", y="earnings",  color="country",size='earnings',
        title="Earnings Comparision", hover_data=["first_name", "last_name","earnings"], range_y=(0,max(earnings_graph_df.earnings)))
        earnings_fig.show()

    """
    Graph for greens in regulation comparision
    """
    def gir_pct(self):


        gir_pct_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        gir_pct_graph_df.sort_values(by="world_rank", ascending=True)
        gir_pct_fig = px.scatter(gir_pct_graph_df, x="world_rank", y="gir_pct", color="player_type",
        title="GIR Comparision", hover_data=["first_name", "last_name","gir_pct"], range_y=(0,max(gir_pct_graph_df.gir_pct)))
        gir_pct_fig.show()

    """
    Graph for driving average
    """
    def drive_avg(self):


        drive_avg_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        drive_avg_graph_df.sort_values(by="world_rank", ascending=True)
        drive_avg_fig = px.scatter(drive_avg_graph_df, x="world_rank", y="drive_avg", color="player_type",
        title="Drive Avg Comparision", hover_data=["first_name", "last_name","drive_avg"], range_y=(0,max(drive_avg_graph_df.drive_avg)))
        drive_avg_fig.show()

    """
    Graph for sand save percentage
    """
    def sand_saves_pct(self):


        sand_saves_pct_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        sand_saves_pct_graph_df.sort_values(by="world_rank", ascending=True)
        sand_saves_pct_fig = px.scatter(sand_saves_pct_graph_df, x="world_rank", y="sand_saves_pct", color="player_type",
        title="Sand Save Pct Comparision", hover_data=["first_name", "last_name","sand_saves_pct"], range_y=(0,max(sand_saves_pct_graph_df.sand_saves_pct)))
        sand_saves_pct_fig.show()

#personal fairway

#average scores

#distance tracking
#average putting per round
#proximity to hole

    """
    Graph for putting average comparision
    """
    def avg_putting(self):


        avg_putting_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        avg_putting_graph_df.sort_values(by="world_rank", ascending=True)
        avg_putting_fig = px.scatter(avg_putting_graph_df, x="world_rank", y="putt_avg", title="Putting Average Comparision", range_y=(0,max(avg_putting_graph_df.putt_avg)))
        avg_putting_fig.show()


    """
    Graph for personal score tracking
    """
    def score(self):

#maybe at the date in the future
        score_graph_df=pd.read_sql(self.round_graph_query, self.ch_1)
        score_graph_df_select=score_graph_df[["SESSION_ID","SCORE"]]
        # #change this so that it actually uses putting
        score_graph_df_clean=score_graph_df_select.groupby([score_graph_df_select.SESSION_ID]).sum()
        score_graph_df_clean_filtered= score_graph_df_clean[score_graph_df_clean["SCORE"]>0]

        score_fig = px.bar(score_graph_df_clean_filtered, x=score_graph_df_clean.index, y="SCORE", 
        title="Score Tracking",range_y=(0,max(score_graph_df_clean_filtered.SCORE)))
        score_fig.show()
#how to filter out the nas