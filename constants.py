import configparser
import os

# Constants
parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config/config.local'))

YOUTUBE_API_KEY = parser.get('youtube', 'API_KEY')