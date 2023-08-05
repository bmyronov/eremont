import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = str(os.getenv("POSTGRES_DB"))
DB_USER = str(os.getenv("POSTGRES_USER"))
DB_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
DB_HOST = str(os.getenv("POSTGRES_HOST"))
DB_PORT = str(os.getenv("POSTGRES_PORT"))
TZ = str(os.getenv("TZ"))
DJANGO_SECRET_KEY = str(os.getenv("DJANGO_SECRET_KEY"))
ADMIN_PAGE = str(os.getenv("ADMIN_PAGE"))
