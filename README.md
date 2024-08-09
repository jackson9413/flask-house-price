# HousePriceApp

HousePriceApp is a Flask web application that provides data analysis and visualization for house prices in King County, USA. It also includes machine learning models to predict house prices based on various features.

## Features

1. **Data Analysis (Visualization)**
   - Analyze the data and create visualizations to identify important factors for predicting house prices.
   - Visualizations include scatter plots, heatmaps, and box plots.

2. **Machine Learning**
   - Train a machine learning model using the provided data.
   - Save the trained model for future predictions.

3. **Flask Web Application**
   - User can input and delete data.
   - Update visualizations based on user input.
   - Predict house prices using the trained machine learning model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/HousePriceApp.git
    cd HousePriceApp
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python run.py
    ```

2. Open your web browser and go to [`http://127.0.0.1:5000/`].

## File Descriptions

- [`application/`]: Contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `form.py`: Contains form definitions.
  - [`models.py`]: Contains database models.
  - [`routes.py`]: Contains the application routes.
  - `templates/`: Contains HTML templates for the application.
    - [`add.html`]: Template for adding new data.
    - [`dashboard.html`]: Template for the dashboard with visualizations.
    - [`index.html`]: Template for the home page.
    - [`layout.html`]: Base template for the application.

- [`data_analysis_machine_learning.ipynb`]: Jupyter notebook for data analysis and machine learning model training.
- [`instance/`]: Contains instance-specific files.
- [`kc_house_data.csv`]: Dataset used for analysis and model training.
- [`lm.pkl`]: Saved machine learning model.
- [`README.md`]: Project documentation.
- [`requirements.txt`]: List of required Python packages.
- [`run.py`]: Entry point for running the Flask application.

## Dependencies

- Flask==1.1.2
- flask_sqlalchemy==3.1.1
- flask_wtf==1.2.1
- pandas==1.4.2
- plotly==5.6.0
- WTForms==3.1.2

## License

This project is licensed under the MIT License.# 1 Data Analysis (Visualization)
