from os import getenv
from traceback import format_tb

from aiogram.types import BufferedInputFile


async def send_logs(e) -> None:
    # TODO: create config file
    chat_id = getenv("temp")

    # create document
    file = bytes(str(e), encoding='utf-8')
    document = BufferedInputFile(file, filename="full_error.txt")

    # create error text
    error_text = format_tb(e.record["exception"][-1])[-1]

    from zer0_bot.main import bot

    # send result
    msg = await bot.send_document(chat_id, document)
    await bot.send_message(chat_id, f'<code>{error_text}</code>', reply_to_message_id=msg.message_id)
