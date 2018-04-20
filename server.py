
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

if __name__ == "__main__":
    app.run()
