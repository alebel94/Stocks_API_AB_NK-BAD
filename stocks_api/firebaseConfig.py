# from flask import Flask
# from config import Config
# from pyrebase import pyrebase
# app = Flask(__name__)

# app.config.from_object(Config)

# firebaseConfig = {
#     'apiKey': "YOUR_API_KEY",
#     'authDomain': "YOUR_API_DOMAIN",
#     'databaseURL': "YOUR_URL",
#     'projectId': "YOUR_APP",
#     'storageBucket': "YOUR_STORAGE_BUCKET",
#     'messagingSenderId': "YOUR_MESSENGER_ID",
#     'appId': "YOUR_APP_ID",
#     'measurementId': "YOUR_MEASUREMENT_ID"
#     }

# firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()
# db = firebase.database()

# from application import routes