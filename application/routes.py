import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
from application import app
from flask import render_template

# read the data
df = pd.read_csv('kc_house_data.csv')


@app.route('/')
def index():
    fig,ax=plt.subplots(figsize=(6,6))
    ax=sns.set(style="darkgrid")
    sns.heatmap(df[["price", "bedrooms", "bathrooms", "sqft_living", "sqft_above", "sqft_basement"]].corr(), annot=True, cmap='coolwarm', center=0)
    canvas=FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return render_template('index.html', send_file=img, mimetype='image/png')

