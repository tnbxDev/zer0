from json import load

from aiogram import Bot


async def startup(bot: Bot) -> None:
    botUser = await bot.me()

    # TODO: create config file
    lang = "en"

    # welcome message
    with open(f'locales/terminal/{lang}.json') as file:
        templates = load(file)

        # logotype
        print("\n".join(templates["onStartup"]))

        # account
        print(templates["selectedAccount"].format("\033[3m" + botUser.username + "\033[0m",
                                                  "\033[3m" + str(botUser.id) + "\033[0m"))
