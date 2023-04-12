from json import load

from aiogram import Bot


async def startup(bot: Bot) -> None:
    """welcome messages"""
    botUser = await bot.me()

    # set terminal language
    from zer0_bot.main import config
    lang = config["main"]["terminal_language"]

    with open(f'locales/terminal/logotype.json') as file:
        templates = load(file)

        # logotype
        print("\n".join(templates["logo"]))

        # links
        print("\n".join(templates["links"]), end="\n\n")

    with open(f'locales/terminal/{lang}.json') as file:
        templates = load(file)

        # account
        print(templates["selectedAccount"].format("\033[3m" + botUser.username + "\033[0m",
                                                  "\033[3m" + str(botUser.id) + "\033[0m"))
