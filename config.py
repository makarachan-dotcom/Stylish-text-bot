import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "7054329150:AAEcMcP-nm2ZOOXd0x4Hxyv-cJ0Bg5R6RyU")
      API_ID = int(os.environ.get("API_ID", 26291592))
      API_HASH = os.environ.get("API_HASH", "9e4fda5c1044e2ce815c3b5af5454913")
      OWNER_ID = int(os.environ.get("OWNER_ID", "6401809092"))

