import discord
import datetime
from discord.ext import commands

class botinfo(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="botinfo")
    async def botinfo(self,ctx):
        embed = discord.Embed(color=discord.Colour.random(), title=f"{self.bot.user.name}'s info")
        embed.add_field(name='Library', value='```Discord.py```' , inline=False)
        embed.add_field(name='Server OS', value='```Linux x64```' , inline=False)
        embed.add_field(name="Server count:", value=f"```{len(self.bot.guilds)}```", inline=False)
        embed.add_field(name="Owner", value="```ilker.#4052```")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.reply(embed=embed)
def setup(bot):
    bot.add_cog(botinfo(bot))