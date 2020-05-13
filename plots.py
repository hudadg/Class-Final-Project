import plotly 
import plotly.express as px
from cleaning_data import data_kredit
import json

def mpg():
    df =data_mobil()
    fig = px.histogram(df, x='mpg', marginal="rug", hover_data=df.columns)
    ## proses convert ploty to json
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def horsepower():
    df = data_mobil()
    fig = px.histogram(df, x='horsepower', marginal="rug", hover_data=df.columns)
    ## proses convert ploty to json
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json