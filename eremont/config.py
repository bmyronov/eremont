import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = str(os.getenv("DB_NAME"))
DB_USER = str(os.getenv("DB_USER"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_PORT = str(os.getenv("DB_PORT"))
DJANGO_SECRET_KEY = str(os.getenv("DJANGO_SECRET_KEY"))
ADMIN_PAGE = str(os.getenv("ADMIN_PAGE"))
