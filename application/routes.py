import pandas as pd
import io
import plotly.express as px
from plotly import utils
import plotly 
import json
from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import House


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
    fig3 = px.box(df[df['bedrooms'] <= 6], x='bedrooms', y='price', title='Price vs Bedrooms', height=500, width=700)
    
    # convert the figure to a json object by using the utils.PlotlyJSONEncoder
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('index.html', graphJSON=graphJSON, graphJSON2=graphJSON2, graphJSON3=graphJSON3)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = House(num_bedrooms=form.num_bedrooms.data, 
                      num_bathrooms=form.num_bathrooms.data, 
                      sqft_living=form.sqft_living.data, 
                      sqft_above=form.sqft_above.data, 
                      sqft_basement=form.sqft_basement.data, 
                      price=form.price.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful entry", "success")
        return redirect(url_for('index'))
    return render_template('add.html', title = 'add', form=form)