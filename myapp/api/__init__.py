
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ngimluxm:zK59sGLE3DXX41RwivZ3MoceL5zGMqSu@stampy.db.elephantsql.com:5432/ngimluxm"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Rushi$501145@db.lihthtudwhegeevkozgj.supabase.co:5432/postgres"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
print(db)



@app.route('/')
def hello():
    # db.create_all()
    # from datetime import datetime
    # from api.models import Post
    # current_date = datetime.today().date()
    # new_post = Post(title="A new morning", description="A new morning details", created_at=current_date)
    # db.session.add(new_post)
    # db.session.commit()
    return 'My First API !!'