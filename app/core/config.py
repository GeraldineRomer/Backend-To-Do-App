import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:Suga01040309@localhost/tareas_db"
)
