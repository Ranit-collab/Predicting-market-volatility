#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:33:05 2021

@author: bidhya
"""

from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("stock_log_reg.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        # Date
        date_all = request.form["date"]
        date_day = int(pd.to_datetime(date_all, format="%Y-%m-%dT%H:%M").day)
        date_month = int(pd.to_datetime(date_all, format ="%Y-%m-%dT%H:%M").month)
        date_year = int(pd.to_datetime(date_all, format ="%Y-%m-%dT%H:%M").year)
        
        
        # Sentiment Analysis
        sent_pol = request.form["polarity"]
        if(sent_pol == 'Positive'):
            sent_pos = 1
            sent_neu = 0
            sent_neg = 0
            
        elif(sent_pol == 'Negative'):
            sent_pos = 0
            sent_neu = 0
            sent_neg = 1
                
        elif(sent_pol == 'Neutral'):
            sent_pos = 0
            sent_neu = 1
            sent_neg = 0
            
        else:
            sent_pos = 0
            sent_neu = 0
            sent_neg = 0
            
            
        # Opening price
        open_price = request.form["open"]   
        
        # Closing price
        close = request.form["close"] 
        
         # Highest price
        high = request.form["high"]  
        
        # Lowest price
        low = request.form["low"]  
            
        # Content length
        cont_len = request.form["cont_len"] 
        
        # Volume
        volume = request.form["vol"] 
        
        prediction=model.predict([[
                date_year,
                date_month,
                date_day,
                sent_pos,
                sent_neu,
                sent_neg,
                open_price,
                close,
                high,
                low,
                cont_len,
                volume
        ]])
    
        output = 0
        if prediction == 1:
            output = "Profit"
        else:
            output = "Loss"
            

        return render_template('home.html', prediction_text="The inserted data will lead to {}.".format(output))

    return render_template("home.html")

                
                
        
            
if __name__ == "__main__":
    app.run(debug=True)
