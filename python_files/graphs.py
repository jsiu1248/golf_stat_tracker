from msilib.schema import Class
import plotly.express as px
from Database import *
import pandas as pd

class Graph: 
    def __init__(self,ch_1):
        self.ch_1=ch_1
        self.cursor_1 = self.ch_1.cursor() 
        self.pga_graph_query="SELECT * from golf.pga_data;"


    def putting_distance_accuracy(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        putting_distance_accurary_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        putting_distance_accurary_graph_df.sort_values(by="world_rank", ascending=True)
        putting_distance_accuracy_fig = px.scatter(putting_distance_accurary_graph_df, x="world_rank", y="putt_avg", )
        putting_distance_accuracy_fig.show()


    def earnings(self):
        # putting_distance_accurary_graph_query="CALL GOLF.PUTTING_DISTANCE_ACCURARY_GRAPH;"

#I need to add title

        earnings_graph_df=pd.read_sql(self.pga_graph_query, self.ch_1)
        earnings_graph_df.sort_values(by="world_rank", ascending=True)
        earnings_fig = px.scatter(earnings_graph_df, x="world_rank", y="earnings", hover_data=["first_name", "last_name","earnings"])
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




