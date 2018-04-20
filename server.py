
from dwhConnection import get_tuples
from flask import Flask, request, send_from_directory, jsonify
import os

# set the project root directory as the static folder, you can set others.
#hardcoded = '/Users/samutamminen/Documents/Study/Sorbonne/S2/BI/visualisation'
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory(os.path.join('.', 'static', 'js'), filename)

@app.route('/')
def root():
    return app.send_static_file('worldmap.html')

@app.route('/countrys/<year>/<fact>')
def get_deficit(year,fact):
    #consider fact aussi
    result = {'data':[['Country', 'Popularity']] + get_tuples(fact,year)}
    return jsonify(result)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run()
