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
        fig = px.scatter(putting_distance_accurary_graph_df, x="world_rank", y="putt_avg", )
        fig.show()





