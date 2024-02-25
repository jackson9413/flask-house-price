import pandas as pd
import io
import plotly.express as px
from plotly import utils
import plotly 
import json
import pickle
from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import House

@app.route('/')
def index():
    entries = House.query.order_by(House.date.desc()).all()
    return render_template("index.html", title = 'index', entries = entries)


@app.route('/dashboard')
def dashboard():
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
    
    return render_template('dashboard.html', graphJSON=graphJSON, graphJSON2=graphJSON2, graphJSON3=graphJSON3)

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

@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    entry = House.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('index'))

@app.route('/predict/<int:entry_id>', methods=['GET', 'POST'])
def predict(entry_id):
    # if click on the predict button then make a prediction    
    entry = House.query.get_or_404(entry_id)
    num_bedrooms = entry.num_bedrooms
    num_bathrooms = entry.num_bathrooms
    sqft_living = entry.sqft_living
    sqft_above = entry.sqft_above
    sqft_basement = entry.sqft_basement
    
    # load the pkl model file
    model = pickle.load(open('lm.pkl', 'rb'))
    
    # make a prediction
    pred_price = model.predict([[num_bedrooms, num_bathrooms, sqft_living, sqft_above, sqft_basement]])[0]
    
    entry.pred_price = pred_price
    db.session.commit()
    flash("Prediction made", "success")
    return redirect(url_for('index'), entry_id=entry.id, pred_price=entry.pred_price)
    
