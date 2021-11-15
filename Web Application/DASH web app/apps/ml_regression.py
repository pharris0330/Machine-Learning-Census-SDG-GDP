import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import pathlib
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors,ensemble
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("data.csv"))


X = df['bachelors_2018'].values[:, None].reshape(-1, 1)
y = df['gdp_2018']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42)

models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor,
          'Extra Trees': ensemble.ExtraTreesRegressor,
          'RF': ensemble.RandomForestRegressor,
          'Ada Boost': ensemble.AdaBoostRegressor}

# app = dash.Dash(__name__)

layout = html.Div([

    html.H1('ML Regression', style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Pre("Select Model:"),
            dcc.Dropdown(
        id='model-name',
        options=[{'label': x, 'value': x}
                 for x in models],
        value='Regression',
        clearable=False),
    ], className='six columns'),
    ], className='row'),

    dcc.Graph(id="graph", figure={}),
])

@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id='model-name', component_property="value")])

def display_value(name):
    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train,
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test,
                   name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range,
                   name='prediction')
    ])
    return fig

# app.run_server(debug=True)