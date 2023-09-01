from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_TOKEN = str(os.getenv('OPENAI_TOKEN'))
