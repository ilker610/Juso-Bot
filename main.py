import discord
import json
import keep_alive
import random
import youtube_dl
import asyncio
from discord_components import *    
from async_timeout import timeout
from pathlib import Path
import os
from discord.ext import commands

keep_alive.keep_alive()

with open("./settings.json", "r") as settings:
    settings_data = json.load(settings)
    Prefix = settings_data["prefix"]
    Owner_id = int(settings_data["owner_id"])

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=Prefix, help_command=None, intents=intents, 
        activity=discord.Game(name=f"If you need help {Prefix}help 😉 | #stopwar 🌷"),
        status=discord.Status.idle)

DiscordComponents(bot)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"{bot.user.name} ready !")

"""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.BadArgument): cogs/errorhandler.py
        await ctx.channel.send(f'{error}')
    elif isinstance(error, discord.BotMissingPermissions):
        await ctx.channel.send(f'ERROR: Forbidden. Missing Permissions!')
    elif isinstance(error, discord.BotMissingAnyRole):
        await ctx.channel.send(f'ERROR: Bot Missing Any Role')
    elif isinstance(error, discord.BotMissingRole):
        await ctx.channel.send(f'ERROR: Bot Missing Role')
    elif isinstance(error, discord.CommandInvokeError):
        await ctx.send(f'{error}')"""
        
@bot.event
async def on_message(message):
    if message.content == "hi":
        await message.reply(f"Hi, {message.author.mention}")
    await bot.process_commands(message)
    
@bot.command(aliases=["rl"])
@commands.is_owner()
async def reload(ctx, module: str):
    await ctx.channel.trigger_typing()
    for path in Path("./cogs").glob("**/*.py"):
        path = str(path).replace("/", ".")[:-3]
        name = path.split(".")[-1]
        if name != module:
            continue
        try:
            bot.reload_extension(path)
        except commands.ExtensionNotLoaded:
            try:
                bot.load_extension(path)
            except Exception:
                return await ctx.reply(f"Couldn't reload **{module}**")
        else:
            return await ctx.reply(f"Successfully reloaded **{module}**")
    await ctx.reply(f"There is no such module named **{module}**")


@bot.command(aliases=["l"])
@commands.is_owner()
async def load(ctx, module: str):
    await ctx.channel.trigger_typing()
    for path in Path("./cogs").glob("**/*.py"):
        path = str(path).replace("/", ".")[:-3]
        name = path.split(".")[-1]
        if name != module:
            continue
        try:
            bot.load_extension(path)
        except commands.ExtensionAlreadyLoaded:
            return await ctx.reply(f"The module **{module}** is already loaded")
        except Exception:
            return await ctx.reply(f"Couldn't load **{module}**")
        else:
            return await ctx.reply(f"Successfully loaded **{module}**")
    await ctx.reply(f"There is no such module named **{module}**")


bot.run(os.environ['token'])
