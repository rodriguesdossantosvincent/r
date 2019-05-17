# coding: utf-8

from ipykernel.comm import Comm
from urllib.parse import urlparse
import time

dash_comm = Comm(target_name='dash_viewer')
jupyterlab_url = None


import dash
import dash_html_components as html


app = dash.Dash(__name__)

# Describe the layout, or the UI, of the app
app.layout = html.Div([
    html.Div('page-content')
])


@dash_comm.on_msg
def _recv(msg):
    global jupyterlab_url
    msg_data = msg.get('content').get('data')
    msg_type = msg_data.get('type', None)
    if msg_type == 'url_response':
        jupyterlab_url = msg_data['url']


if __name__ == '__main__':
    dash_comm.send({
        'type': 'url_request'
    })
    
    while jupyterlab_url is None:
        time.sleep(2)

    path = urlparse(jupyterlab_url).path
    app.config.update({
        'requests_pathname_prefix': f'{path}proxy/8050/'})
    app.run_server(debug=True)

    
