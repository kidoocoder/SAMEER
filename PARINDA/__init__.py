from PARINDA.core.bot import parinda
from PARINDA.core.dir import dirr
from PARINDA.core.git import git
from PARINDA.core.userbot import Userbot
from PARINDA.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = parinda()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
