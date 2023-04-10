from aiogram import Dispatcher

from .events import *


def register_handlers(dp: Dispatcher) -> None:
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
