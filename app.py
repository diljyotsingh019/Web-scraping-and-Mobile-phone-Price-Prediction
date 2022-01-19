

# NAME @: Diljyot Singh
# TOPIC @: Phone Price Prediction Model Deployment
# DATE @: 08/01/2022


# IMPORT THE DEPENDENCIES

import numpy as np
from flask import Flask,render_template, request, session, redirect, url_for
from helper_functions import InfoForm, return_prediction

app = Flask(__name__)
# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = 'mysecretkey'


# 1. View point to show the form and collect the data from user
@app.route("/", methods = ["GET", "POST"])
def home():
    # Create instance of the form.
    form = InfoForm()

    # If the form is valid on submission
    if form.validate_on_submit():
        session["product"] = form.product.data
        session["scnsize"] = form.scnsize.data
        session["scntype"] = form.scntype.data
        session["batpower"] = form.batpower.data
        session["processor"] = form.processor.data
        session["ram"] = form.ram.data
        session["inbuilt"] = form.inbuilt.data
        session["external"] = form.external.data
        session["os"] = form.os.data
        session["rcam"] = form.rcam.data
        session["processor_html"] = form.processor
        session["product_html"] = form.product
        session["scntype_html"] = form.scntype
        session["os_html"]=form.os
        session["fcam"]=form.fcam.data

        # Redirect the data to Prediction function
        return redirect(url_for("predict"))

    # Show the form for first visit
    return render_template("home.html", form = form)

@app.route("/predict")
def predict():
    pred = []
    temp = ["scnsize", "batpower","ram","inbuilt","external","rcam","scntype","processor","os", "product"]
    for i in temp:
        pred.extend(session[i].split(","))

    pred_array = np.array(pred)

    pred_array = pred_array.astype("float")
    # PRINT THE DATA PRESENT IN THE REQUEST
    print("[INFO] DATA  - ", pred)

    #PREDICTING USING THIS FUNCTION
    results = return_prediction(pred=[pred])

    # PRINT THE RESULT
    print("[INFO] PREDICTION - ", results)
    return render_template("thankyou.html", results = results[0])

if __name__ == "__main__":
    app.run(debug=True)