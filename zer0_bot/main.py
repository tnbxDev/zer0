from os import getenv
from dotenv import load_dotenv
from loguru import logger
from configparser import ConfigParser

from aiogram import Bot, Dispatcher

from zer0_bot.handlers import register_handlers
from zer0_bot.utils import send_logs


# read config
config = ConfigParser()
config.read("zer0_bot/data/config.ini")

# configurate logger
logger.add(send_logs, format=config["main"]["loguru_logger_format"])

# getting token from .env
load_dotenv(dotenv_path="zer0_bot/data/.env")

BOT_TOKEN = str(getenv("BOT_TOKEN"))

# initializing bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()

# registering all needed handlers
register_handlers(dp)


async def run_bot() -> None:
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
