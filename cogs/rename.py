import discord
from discord.ext import commands

class rename(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="rename")
    @commands.has_permissions(administrator=True)
    async def rename(self,ctx,user:discord.Member, *, name):
        await user.edit(nick=name)
        await ctx.reply("Nick changed !")

def setup(bot):
    bot.add_cog(rename(bot))