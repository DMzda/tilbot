from tilbot import app, db,  models
from tilbot.config import ITEMS_PER_PAGE
from flask import render_template


@app.route("/")
@app.route("/page/<int:page>")
def index(page=1):
    comments = models.Comment.query.order_by(db.desc(models.Comment.timestamp)).paginate(page, ITEMS_PER_PAGE, True)

    return render_template("index.html", comments=comments)
