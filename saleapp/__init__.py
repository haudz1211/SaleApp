import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "%^$DSD^%^%^%^%^DSSD"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2


login = LoginManager(app)
db = SQLAlchemy(app)


cloudinary.config(cloud_name='dgeyq5bpg',
                  api_key='124191785282462',
                  api_secret='-FwQxZuQW-YziPfCZ3ktdIkqeug')