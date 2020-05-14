import plotly 
import plotly.express as px
from cleaning_data import data_kredit
import json

def RevolvingUtilizationOfUnsecuredLines():
    df = data_kredit()
    # fig = px.histogram(df, x='RevolvingUtilizationOfUnsecuredLines', marginal="rug")
    fig = px.scatter(df, x="RevolvingUtilizationOfUnsecuredLines", y="MonthlyIncome_AVG", color="SeriousDlqin2yrs")
    ## proses convert ploty to json
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def NumberOfTimes90DaysLate():
    df = data_kredit()
    # fig = px.histogram(df, x='NumberOfTimes90DaysLate', marginal="rug")
    fig = px.scatter(df, x="NumberOfTimes90DaysLate", y="MonthlyIncome_AVG", color="SeriousDlqin2yrs")
    ## proses convert ploty to json
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json