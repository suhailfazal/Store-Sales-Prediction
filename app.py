from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

file = open("./random_forest_regression_model.pkl", 'rb')
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
    Outlet_Year = request.form.get('Outlet_Year') 
    Item_Quantity = request.form.get('Item_Qty')

    prediction = model.predict(pd.DataFrame([[Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type,
    Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type, Outlet_Year]], columns=['Item_Weight', 
    'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
    'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Outlet_Establishment_Year']))

    return str(prediction[0])


if __name__ == '__main__':
    app.run(debug=True)   