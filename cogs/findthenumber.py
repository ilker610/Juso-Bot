import discord
from discord.ext import commands
import random
import asyncio

class findthenumber(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="findthenumber", aliases=["ftn"])
    async def findthenumber(self,ctx):
        message = await ctx.reply("Choice difficulty [Easy,Normal,Hard] `You have 15 second for choice.`")
        check = lambda m: m.author == ctx.author and m.channel == ctx.channel
        try:
            select =  await self.bot.wait_for("message", check=check, timeout=15)
        except asyncio.TimeoutError:
            await message.edit("Time out !")

        if select.content == "Easy":
            await ctx.channel.send("Easy mode is enabled. Now I keep a number between 0 and 15")
            easy_number = str(random.randint(0,15))
            choicesy =  await self.bot.wait_for("message", check=check, timeout=15)
            if choicesy.content == easy_number:
                await ctx.channel.send(f"You can know my number !")
            else:
                await ctx.channel.send(f"You didn't know my number. My number is:`{easy_number}`")
                
        elif select.content == "Normal":
            await ctx.channel.send("Normal mode is enabled. Now I keep a number between 0 and 30")
            normal_number = str(random.randint(0,30))
            choicenrm =  await self.bot.wait_for("message", check=check, timeout=15)
            if choicenrm.content == normal_number:
                await ctx.channel.send(f"You can know my number !")
            else:
                await ctx.channel.send(f"You didn't know my number. My number is:`{normal_number}`")
                
        elif select.content == "Hard":
            await ctx.channel.send("Normal mode is enabled. Now I keep a number between 0 and 45")
            hard_number = str(random.randint(0,45))
            choicerd =  await self.bot.wait_for("message", check=check, timeout=15)
            if choicerd.content == hard_number:
                await ctx.channel.send(f"You can know my number !")
            else:
                await ctx.channel.send(f"You didn't know my number. My number is:`{hard_number}`")

def setup(bot):
    bot.add_cog(findthenumber(bot))