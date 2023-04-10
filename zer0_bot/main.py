from os import getenv

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

load_dotenv(".env")
BOT_TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    dp, bot = await initialization()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def initialization() -> tuple[Dispatcher, Bot]:
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    # register_all_handlers(dp)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    return dp, bot


async def on_startup(dispatcher) -> None:
    pass


async def on_shutdown(dispatcher) -> None:
    pass
