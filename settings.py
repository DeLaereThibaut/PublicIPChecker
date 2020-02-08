# settings.py
from dotenv import load_dotenv

load_dotenv()

import os

EMAIL = os.getenv("EMAIL")
RECIEVER = os.getenv("RECIEVER")
EMAILPASSWORD = os.getenv("PASSWORD")
SERVERURL = os.getenv("SERVERURL")
SERVERPORT = os.getenv("SERVERPORT")