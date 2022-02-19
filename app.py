import math
import pickle

import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open("rf_regressor_ntscaled.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":
        Outlet_Years = request.form.get('Outlet_Years')
        Item_MRP = float(request.form.get('Item_MRP'))
        Item_Visibility = request.form.get('Item_Visibility')
        Item_Weight = float(request.form.get('Item_Weight'))

        #
        Item_Fat_Content = request.form['Item_Fat_Content']
        Item_Fat_Content_1 = 0
        if (Item_Fat_Content == 'Regular'):
            Item_Fat_Content_1 = 1


        Outlet_Size = request.form['Outlet_Size']
        Outlet_Size_2 = 0 #small = 2
        Outlet_Size_1 = 0 #medium = 1

        if (Outlet_Size == 'Small'):
            Outlet_Size_2 = 1
        elif (Outlet_Size == 'Medium'):
            Outlet_Size_1 = 1


        #
        Outlet_Location_Type = request.form['Outlet_Location_Type']
        Outlet_Location_Type_1 = 0 #1 Tier2
        Outlet_Location_Type_2 = 0 #2 Tier3
        if (Outlet_Location_Type == 'Tier_1'):
            Outlet_Location_Type_0= 1
        elif (Outlet_Location_Type == 'Tier_2'):
            Outlet_Location_Type_1 = 1
        else:
            Outlet_Location_Type_2 = 1

        #
        Outlet_Type = request.form['Outlet_Type']

        Outlet_Type_0 = 0 #0 Grocery_Store
        Outlet_Type_1 = 0 #1 Supermarket_Type1
        Outlet_Type_2 = 0 #2 Supermarket_Type2
        Outlet_Type_3 = 0 #3 Supermarket_Type3

        if (Outlet_Type == 'Supermarket_Type1'):
            Outlet_Type_1 = 1
        elif (Outlet_Type == 'Supermarket_Type2'):
            Outlet_Type_2 = 1
        elif (Outlet_Type == 'Supermarket_Type3'):
            Outlet_Type_3 = 1
        else:
            Outlet_Type_0 = 1

        #
        New_Item_Type =(request.form['New_Item_Type'])
        New_Item_Type_1 = 0 #1 Food
        New_Item_Type_2 = 0 #2 Non_Consumables
        New_Item_Type_0 = 0 #0 Drinks
        if (New_Item_Type == 'Food'):
            New_Item_Type_1 = 1

        elif (New_Item_Type == 'Non_Consumables'):
            New_Item_Type_2 = 1
        else:
            New_Item_Type_0 = 1

        #
        Item_Type = request.form['Item_Type']
        Item_Type_0 = 0
        Item_Type_1 = 0
        Item_Type_2 = 0
        Item_Type_3 = 0
        Item_Type_4 = 0
        Item_Type_5 = 0
        Item_Type_6 = 0
        Item_Type_7 = 0
        Item_Type_8 = 0
        Item_Type_9 = 0
        Item_Type_10 = 0
        Item_Type_11 = 0
        Item_Type_12 = 0
        Item_Type_13 = 0
        Item_Type_14 = 0
        Item_Type_15 = 0

        if (Item_Type == 'Fruits_and_Vegetables'):
            Item_Type_6 = 1
        elif (Item_Type == 'Snack_Foods'):
            Item_Type_13 = 1
        elif (Item_Type == 'Household'):
            Item_Type_9 = 1
        elif (Item_Type == 'Frozen_Foods'):
            Item_Type_5 = 1
        elif (Item_Type == 'Dairy'):
            Item_Type_4 = 1
        elif (Item_Type == 'Canned'):
            Item_Type_3 = 1
        elif (Item_Type == 'Baking_Goods'):
            Item_Type_0 = 1
        elif (Item_Type == 'Health_and_Hygiene'):
            Item_Type_8 = 1
        elif (Item_Type == 'Soft_Drinks'):
            Item_Type_14 = 1
        elif (Item_Type == 'Meat'):
            Item_Type_10 = 1
        elif (Item_Type == 'Breads'):
            Item_Type_1 = 1
        elif (Item_Type == 'Hard_Drinks'):
            Item_Type_7 = 1
        elif (Item_Type == 'Others'):
            Item_Type_11 = 1
        elif (Item_Type == 'Starchy_Foods'):
            Item_Type_15 = 1
        elif (Item_Type == 'Breakfast'):
            Item_Type_2 = 1
        elif (Item_Type == 'Seafood'):
            Item_Type_12 = 1
        list=[
            float(Item_Weight),
            float(Item_Visibility),
            float(Item_MRP),
            float(Outlet_Years),
            float(Item_Fat_Content_1),
            Item_Type_1,
            Item_Type_2,
            Item_Type_3,
            Item_Type_4,
            Item_Type_5,
            Item_Type_6,
            Item_Type_7,
            Item_Type_8,
            Item_Type_9,
            Item_Type_10,
            Item_Type_11,
            Item_Type_12,
            Item_Type_13,
            Item_Type_14,
            Item_Type_15,
            Outlet_Size_1,
            Outlet_Size_2,
            Outlet_Location_Type_1,
            Outlet_Location_Type_2,
            Outlet_Type_1,
            Outlet_Type_2,
            Outlet_Type_3,
            New_Item_Type_1,
            New_Item_Type_2]
        prediction = model.predict(pd.DataFrame([list]))

        output = round(prediction[0], 10)

        return render_template('index.html', prediction_text="Your Predicted Sales value is {}".format(math.exp(output)))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
