import discord
import json
import random
import datetime
from discord.ext import commands

with open("./settings.json", "r") as settings:
    settings_data = json.load(settings)
    Owner_id = int(settings_data["owner_id"])

class ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(name="ping", description="Shows bot ping")
    async def ping(self,ctx):
        if ctx.author.id == Owner_id:
            emb = discord.Embed()
            emb.set_thumbnail(url=self.bot.user.avatar_url)
            emb.add_field(name=self.bot.user.name,value=f"Ping:{round(self.bot.latency * 1000)}ms")
            emb.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
            emb.timestamp = datetime.datetime.utcnow()
            await ctx.channel.send(embed=emb)
        else:
            await ctx.channel.send(f"This command just for {self.bot.user.name}'s owner.")


def setup(bot):
    bot.add_cog(ping(bot))