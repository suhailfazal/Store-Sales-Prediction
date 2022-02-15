from flask import Flask, jsonify, request, render_template
import pandas as pd
import pickle
import sklearn
import os
import numpy as np

app = Flask(__name__)

file = open("./random_forest_regressor_model.pkl", 'rb')
model = pickle.load(file)

data = pd.read_csv('./train_data_clean.csv')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    Item_Weight = float(request.form.get('Item_Weight'))
    Item_Fat_Content = request.form.get('Item_Fat_Content')
    Item_Visibility = request.form.get('Item_Visibility')
    Item_Type = request.form.get('Item_Type')
    Item_MRP = request.form.get('Item_MRP')
    Outlet_Size = request.form.get('Outlet_Size')
    Outlet_Location_Type = request.form.get('Outlet_Location_Type')
    Outlet_Type = request.form.get('Outlet_Type')
    Outlet_Years = request.form.get('Outlet_Years')
    New_Item_Type = request.form.get('New_Item_Type')

    prediction = model.predict(pd.DataFrame([[Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type,
    Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type, Outlet_Years, New_Item_Type]], columns=['Item_Weight',
    'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
    'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Outlet_Years', 'New_Item_Type']))

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)   