from dotenv import load_dotenv
import os

load_dotenv()
# OPEN API STUFF
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv("APP_SECRET_KEY")


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
