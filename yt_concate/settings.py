import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('api_key')


DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, "videos")
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, "captions")
OUTPUT_DIR = 'output'