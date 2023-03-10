# (c) @Md_Matin_Ashraf

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MovieSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Movie Search Bot.

π€ My Name: <a href='https://t.me/Newmoviespost_bot'>Movie Search Robot</a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ Server: <a href='https://heroku.com'>Heroku</a>

π¨βπ» Created By: <a href='https://t.me/Md_Matin_Ashraf'>MD</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» Developer : <a href='https://t.me/Md_Matin_Ashraf'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! Meri Jaan {}π,

I'm Powerfull Movie Search Robot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @Movie_Matin</a></b>
"""


    START_MSG = """
<b>Hey! Meri Jaan {}π,

I'm Powerfull Movie Search Robot.π€</a>

I Can Search π What You WantβIf Any Movie Not Available π» π₯π²πΎππ²ππ ππ²πΏπ² @MoviesandwebseriesrequestBot

<a>Made With β€ By @Movie_Matin</a></b>
"""


