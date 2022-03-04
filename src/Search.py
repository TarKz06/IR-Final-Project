import pandas as pd
from flask import Flask, request, jsonify
import main

app = Flask(__name__)

# Read csv file
cleanData = pd.read_csv('src/resources/new Food Ingredients and Recipe.csv')

@app.route('/searchName', methods=["POST"])
def SearcByName():
    if request.method == 'POST':
        body = request.get_json()



if __name__ == '__main__':
    errormgs = {"errormgs": "do not have data"}
    app.run(debug=True)