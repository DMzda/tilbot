import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(APP_ROOT, "til.db")
ITEMS_PER_PAGE = 20
