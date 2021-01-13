from flask import Flask, render_template, session

import settings
from database import db_session
from models import ViewsCount

app = Flask(__name__)
app.secret_key = settings.FLASK_SECRET_KEY


@app.route("/")
def hello():
    views_count = ViewsCount.query.first()
    if not views_count:
        views_count = ViewsCount()
        db_session.add(views_count)
        db_session.commit()

    if not session.get("is_visited_site"):
        session["is_visited_site"] = True
        views_count.count += 1

    db_session.add(views_count)
    db_session.commit()

    return render_template("hello.html", views_count=views_count.count)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
