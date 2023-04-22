"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch14p4orddl13a5fcvd0-a.oregon-postgres.render.com",
        database="todo_hbwh",
        user="todo_hbwh_user",
        password="VKbpqAt506ARDOkhryWan105mMWupzxS")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
