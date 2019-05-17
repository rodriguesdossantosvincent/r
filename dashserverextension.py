from subprocess import Popen
import json

def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    #Popen(["cd", "dash", "&&", "python", "app.py"])
    web_app = nbapp.web_app
    open('/tmp/url.json', 'w').write(json.dumps({'base_url': web_app.settings['base_url']}))
    Popen(["python", "app.py"], cwd="dash")