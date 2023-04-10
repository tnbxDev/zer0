import functools

from time import sleep

from aiogram import Dispatcher
from aiogram.types import Message


def cmd(delete: bool = False, time: float = 1.5):
    def input_func(handler):
        @functools.wraps(handler)
        def wrapper(dp: Dispatcher, msg: Message):
            if delete and time < 0:
                msg.delete()
            handler(dp, msg)
            if delete and time >= 0:
                sleep(time)
                msg.delete()
        return wrapper
    return input_func
