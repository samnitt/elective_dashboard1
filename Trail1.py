import dash
import pandas as pd
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Sample data for button labels
button_labels = [f"Button {i}" for i in range(1, 21)]
elective = pd.read_excel('elective.xlsx')
global student_details
student_details = pd.read_excel('student_details.xlsx')
button = student_details['Roll'].tolist()
electivefive = elective['Q5'].tolist()
electivesix = elective['Q6'].tolist()
electiveseven = elective['Q7'].tolist()


app = dash.Dash(__name__)
app.run_server(debug=True, port=8051)


app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown1',
        options=[{'label': i, 'value': i} for i in button],
        multi=True,
        placeholder="Select Roll Number of yours"
    ),
    
    dcc.Dropdown(
        id='dropdown2',
        options=[{'label': i, 'value': i} for i in electivefive],
        multi=True,
        placeholder="Select Q5 electives"
    ),
    
    dcc.Dropdown(
        id='dropdown3',
        options=[{'label': i, 'value': i} for i in electivesix],
        multi=True,
        placeholder="Select Q6 electives"
    ),
    
    dcc.Dropdown(
        id='dropdown4',
        options=[{'label': i, 'value': i} for i in electiveseven],
        multi=True,
        placeholder="Select Q7 electives4"
    ),
    
    html.Button('Submit', id='submit-button', n_clicks=0),
    
    html.Div(id='output-container-button', children=[]),
])

@app.callback(
    Output('output-container-button', 'children'),
    Output('submit-button', 'n_clicks'),
    Input('submit-button', 'n_clicks'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('dropdown3', 'value'),
    Input('dropdown4', 'value')
)
def display_output(n_clicks, dropdown1, dropdown2, dropdown3, dropdown4):
    # Process the selected buttons
    selected_buttons1 = []
    selected_buttons2 = []
    selected_buttons3 = []
    selected_buttons4 = []
    selected_buttons5 = []
    list = []
    if dropdown1:
        selected_buttons1.extend(dropdown1)
    if dropdown2:
        selected_buttons2.extend(dropdown2)
    if dropdown3:
        selected_buttons3.extend(dropdown3)
    if dropdown4:
        selected_buttons4.extend(dropdown4)

    if len(selected_buttons1) > 1:
        return "Error: Please One Roll number alone.", n_clicks
    if len(selected_buttons2) > 6:
        return "Error: Do not select more than 6 electives in Q5.", n_clicks
    if len(selected_buttons3) > 6:
        return "Error: Do not select more than 6 in Q6.", n_clicks
    if len(selected_buttons4) > 6:
        return "Error: Do not select more than 6 in Q7.", n_clicks
    if len(selected_buttons2) < 6:
        return "Error: Select 6 electives in Q5 add dummy to make 6.", n_clicks
    if len(selected_buttons3) < 6:
        return "Error: Select 6 electives in Q6 add dummy to make 6.", n_clicks
    if len(selected_buttons4) < 6:
        return "Error: Select 6 electives in Q7 add dummy to make 6.", n_clicks

    if n_clicks > 0:
        
        student_details.loc[student_details['Roll'] == selected_buttons1[0]] = selected_buttons1+selected_buttons1+selected_buttons2+selected_buttons3+selected_buttons4+selected_buttons5
        n_clicks = 0


    return f'Selected buttons: {selected_buttons1+selected_buttons1+selected_buttons2+selected_buttons3+selected_buttons4+selected_buttons5}', n_clicks



if __name__ == '__main__':
    app.run_server(debug=True)
