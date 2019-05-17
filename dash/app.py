# coding: utf-8


import dash
import dash_html_components as html
import json

app = dash.Dash(__name__)

# Describe the layout, or the UI, of the app
app.layout = html.Div([
    html.Div('page-content')
])

if __name__ == '__main__':
    path = json.load(open('/tmp/url.json', 'r')).get('base_url')
    print('path', path)
    app.config.update({
        'requests_pathname_prefix': f'{path}proxy/8050/'})
    app.run_server(debug=True)

    
