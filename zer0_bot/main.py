from os import getenv

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from .handlers import register_handlers


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
