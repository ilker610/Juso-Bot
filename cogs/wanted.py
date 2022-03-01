import asyncio
import discord
import random
import os
from discord.ext import commands

from PIL import Image
from io import BytesIO

class wanted(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="wanted")
    async def wanted(self, ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author

        wanted = Image.open("wanted.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((255,255))

        wanted.paste(pfp, (100,201))

        wanted.save("profile.jpg")

        await ctx.channel.send(file = discord.File("profile.jpg"))

        os.remove("profile.jpg")

def setup(bot):
    bot.add_cog(wanted(bot))