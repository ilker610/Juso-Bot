import discord
import json
import datetime
from discord_components import DiscordComponents, Button, ButtonStyle, component
from discord.ext import commands

with open("./settings.json", "r") as settings:
    settings_data = json.load(settings)
    Prefix = settings_data["prefix"]

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self,ctx): 
        await ctx.channel.send(f"If you need help you can use `usage <command_name>` command")
        embed = discord.Embed(color=discord.Colour.random(), title=f"{self.bot.user.name}'s commands:")
        embed.add_field(name='Owner Only', value=f'`ping` `load` `reload`' , inline=False)
        embed.add_field(name="Info", value=f"`botinfo` `userinfo`")
        embed.add_field(name='Fun:', value=f'`scan` `wanted` `findthenumber`' , inline=False)
        embed.add_field(name='Moderation:', value=f'`ban` `kick` `giverole` `removerole` `createrole`', inline=False)
        embed.add_field(name='User', value=f'`rename` `avatar` `addrole`', inline=False)
        
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed, components=[
            Button(style=ButtonStyle.URL, label="🤖 İnvite me !", url="https://discord.com/api/oauth2/authorize?client_id=938506594684117042&permissions=8&scope=bot%20applications.commands")])

def setup(bot):
    bot.add_cog(help(bot))