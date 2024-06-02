
from config import *
import disnake
import os
from disnake.ext import commands


bot = commands.Bot(command_prefix="ewrffwe", intents=disnake.Intents.all())

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(TOKEN)