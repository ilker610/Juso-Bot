from asyncio import wait_for
from tabnanny import check
import discord
import json
import datetime
from discord_components import Select, SelectOption
from discord.ext import commands

with open("./settings.json", "r") as settings:
    settings_data = json.load(settings)
    Prefix = settings_data["prefix"]

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self,ctx): 
        embed = discord.Embed(title=f"{self.bot.user.name}'s help menu !", description="Click on the relevant buttons to see the commands.", color=discord.Colour.darker_grey())
        embed.set_image(url="https://cdn.discordapp.com/attachments/938513267880493162/948592718169407498/standard.gif")
        await ctx.reply(embed=embed, mention_author=False, components=[
                Select(custom_id="selectmenu",placeholder="Choose what you want see !", options=[
                    SelectOption(emoji="⚜", label="Info", value="info",description="Shows Info commands"),
                    SelectOption(emoji="⚜", label="Moderation", value="moderation",description="Shows Moderation commands"),
                    SelectOption(emoji="⚜", label="Fun", value="fun",description="Shows Fun commands"),
                    SelectOption(emoji="⚜", label="User", value="user",description="Shows User commands"),
                    SelectOption(emoji="⚜", label="Support", value="support",description="Shows Support commands"),

                ])
        ])
        e1 = discord.Embed(color=discord.Colour.random(), title=f"Info", description="`botinfo` `userinfo`")
        e2 = discord.Embed(color=discord.Colour.random(), title=f"Moderation", description="`ban` `kick` `giverole` `removerole` `createrole`")
        e3 = discord.Embed(color=discord.Colour.random(), title=f"Fun", description="`scan` `wanted` `findthenumber`")
        e4 = discord.Embed(color=discord.Colour.random(), title=f"User", description="`rename` `avatar` `addrole`")
        e5 = discord.Embed(color=discord.Colour.random(), title=f"Support", description="`support`")

        event = await self.bot.wait_for("select_option", check=lambda inter: inter.user == ctx.author)
          

        label = event.values[0]

        if label == "info":
            await event.respond(embed=e1)
            
        elif label == "fun":
            await event.respond(embed=e3)

            
        elif label == "moderation":
            await event.respond(embed=e2)
            
        elif label == "user":
            await event.respond(embed=e4)
            
            
        elif label == "support":
            await event.respond(embed=e5)

def setup(bot):
    bot.add_cog(help(bot))