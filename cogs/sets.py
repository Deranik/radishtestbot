import disnake
from disnake.ext import commands
from Utils import SelectSends
from Utils import Send1
from Utils import Send2
from config import *

class send(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        channel = self.bot.get_channel(NABOR_CHANNEL)
        
        if not channel:
            return
        last_message = await channel.history(limit=1).find(lambda m: m.author == self.bot.user)
        main_embed = Send2()
        select_view = SelectSends()

        if last_message:
            await last_message.edit(embed=main_embed, view=select_view)
        else:
            await channel.send(embed=main_embed, view=select_view)

def setup(bot):
    bot.add_cog(send(bot))
    
