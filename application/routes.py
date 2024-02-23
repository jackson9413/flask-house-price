import pandas as pd
import io
import plotly.express as px
from plotly import utils
import plotly 
import json
from application import app
from flask import render_template


@app.route('/')
def index():
    # Load the data
    df = pd.read_csv(r'kc_house_data.csv')
    
    # use plotly to create a scatter plot
    fig = px.scatter(df, x='sqft_living', y='price', title='Price vs Square Feet', height=500, width=700)
    
    # convert the figure to a json object by using the utils.PlotlyJSONEncoder
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # use plotly to create a heatmap to show the correlation between the features
    fig2 = px.imshow(df[["price", "bedrooms", "bathrooms", "sqft_living", "sqft_above", "sqft_basement"]].corr(), 
                     title='Correlation Matrix', height=500, width=700)
    
    # convert the figure to a json object by using the utils.PlotlyJSONEncoder
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    
    # use plotly to create a box plot to show the relationship between the number of bedrooms and the price
    fig3 = px.box(df, x='bedrooms', y='price', title='Price vs Bedrooms', height=500, width=700)
    
    # convert the figure to a json object by using the utils.PlotlyJSONEncoder
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', graphJSON=graphJSON, graphJSON2=graphJSON2, graphJSON3=graphJSON3)

