# NAME @: Diljyot Singh
# TOPIC @: Phone Price Prediction Model Deployment
# DATE @: 08/01/2022

# IMPORT THE DEPENDENCIES

import pickle
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, SubmitField


# LOAD THE MODEL:

model = pickle.load(open("model.pkl","rb"))

# CREATE A PREDICTION FUNCTION:
def return_prediction(pred):
    results = model.predict(pred)
    return results

# CREATE A FLASK FORM:

class InfoForm(FlaskForm):

    product = SelectField("Product Brand:", choices= [("0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0", "Samsung"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0", "Redmi"),
                                                      ("0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0", "OPPO"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "IKALL"),
                                                      ("1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "JIO"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0", "Techno"),
                                                      ("0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0", "One Plus"),
                                                      ("0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "Micromax"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0", "Vivo"),
                                                      ("0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0", "Nokia"),
                                                      ("0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "LAVA"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0", "iQOO"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0", "itel"),
                                                      ("0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0", "Realme"),
                                                      ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0", "Xiomi"),
                                                      ("0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "Moto"),
                                                      ("0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "KECHAODA"),
                                                      ("0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0", "Mi")
                                                      ])

    scnsize = StringField("Screen Size in inches: ", validators=[DataRequired()])

    scntype = RadioField("Screen Type: ", choices= [("0,0,0,0,0,1,0", "LCD"),
                                                    ("1,0,0,0,0,0,0", "AMOLED"),
                                                    ("0,0,0,0,0,0,0", "HD"),
                                                    ("0,0,0,1,0,0,0", "HD+"),
                                                    ("0,1,0,0,0,0,0", "FHD"),
                                                    ("0,0,1,0,0,0,0", "FHD+"),
                                                    ("0,0,0,0,0,0,1", "TFT"),
                                                    ("0,0,0,0,1,0,0", "Incell"),
                                                    ])
    batpower = StringField("Battery Capacity in mAh: ", validators= [DataRequired()])

    processor = SelectField("Processor Brand: ", choices= [("1,0,0,0,0,0,0,0,0", "Exynos"),
                                                           ("0,1,0,0,0,0,0,0,0", "MediaTek"),
                                                           ("0,0,0,1,0,0,0,0,0", "Qualcomm"),
                                                           ("0,0,0,0,0,0,0,0,1", "kios"),
                                                           ("0,0,0,0,0,0,1,0,0", "ThreadX"),
                                                           ("0,0,0,0,0,0,0,1,0", "Unisoc"),
                                                           ("0,0,0,0,1,0,0,0,0", "Spreadtrum"),
                                                           ("0,0,0,0,0,1,0,0,0", "Symbian"),
                                                           ("0,0,0,0,0,0,0,0,0", "Arm"),
                                                           ("0,0,1,0,0,0,0,0,0", "NA"),
                                                           ])

    ram = StringField("RAM in GBs: ", validators= [DataRequired()])

    inbuilt = StringField("Inbuilt Storage in GBs: ", validators=[DataRequired()])

    external = StringField("External Storage in GBs: ", validators= [DataRequired()])

    fcam = StringField("Front Camera in Megapixels: ", validators= [DataRequired()])

    rcam = StringField("Rear Camera in Megapixels:", validators= [DataRequired()])

    os = RadioField("Operating System: ", choices= [("0,0,1,0,0,0,0,0,0,0", "Android 6"),
                                                    ("0,0,0,1,0,0,0,0,0,0", "Android 7"),
                                                    ("0,0,0,1,0,0,0,0,0,0", "Android 8"),
                                                    ("0,0,0,0,1,0,0,0,0,0", "Android 9"),
                                                    ("1,0,0,0,0,0,0,0,0,0", "Android 10"),
                                                    ("0,1,0,0,0,0,0,0,0,0", "Android 11"),
                                                    ("0,0,0,0,0,0,0,0,1,0", "Oxygen"),
                                                    ("0,0,0,0,0,0,1,0,0,0", "MIUI"),
                                                    ])
    addcom = TextAreaField()
    submit = SubmitField("Submit")



