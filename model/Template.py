import os

import pymysql


class Template:
    def __init__(self):
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        name = os.getenv("DB_NAME")
        host = os.getenv("DB_HOST")
        self.myConnection = pymysql.connect(
            user=user,
            password=password,
            db=name,
            host=host)
