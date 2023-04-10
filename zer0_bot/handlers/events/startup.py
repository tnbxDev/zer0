from aiogram import Bot


async def startup(bot: Bot) -> None:
    botUser = await bot.me()

    print(botUser.id)
