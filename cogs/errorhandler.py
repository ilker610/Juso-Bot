import math
import sys
import traceback
import os
import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands
import asyncio
import random
import string


def get_txt(text: str, filename: str) -> discord.File:
    fn = f"./cogs/txts/{''.join(random.choices(string.ascii_lowercase, k=10))}.txt"
    with open(fn, mode="w") as file:
        file.write(text)
    with open(fn, mode="rb") as file:
        file = discord.File(file, filename=f"{filename}.txt")
    asyncio.create_task(delete_file_after(fn, 5))
    return file


async def delete_file_after(path: str, cooldown: int) -> None:
    await asyncio.sleep(cooldown)
    if os.path.exists(path):
        os.remove(path)


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return
        if cog := ctx.cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        ignored = (commands.CommandNotFound, commands.DisabledCommand,
                   commands.NoPrivateMessage)
        error = getattr(error, "original", error)
        if isinstance(error, ignored):
            return
        elif isinstance(error, commands.BotMissingPermissions):
            missing = "\n".join(
                [f"`{perm}`" for perm in error.missing_permissions])
            try:
                await ctx.trigger_typing()
                await ctx.reply(
                    f"I don't have the required permissions to execute this command!\nMissing the following permissions: {missing}",
                    mention_author=False)
            except (discord.Forbidden, discord.HTTPException):
                pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.trigger_typing()
            await ctx.reply(f"You can't execute this command!\nYou are missing the permission(s): {', '.join([f'`{perm}`' for perm in error.missing_permissions])}")
        elif isinstance(error, commands.CommandOnCooldown):
            usable_after = math.ceil(error.retry_after)
            await ctx.trigger_typing()
            await ctx.reply(
                f"This command is on cooldown\nYou can use this command again in {usable_after} second{'s' if usable_after != 1 else ''}",
                mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.trigger_typing()
            await ctx.reply(
                f"Please fill all the required arguments\nMissing the argument `{error.param}`",
                mention_author=False,
            )
        elif isinstance(error, commands.MemberNotFound):
            await ctx.trigger_typing()
            await ctx.reply("Member not found !",
                mention_author=False)
        elif isinstance(error,
                        (commands.CheckFailure, commands.CheckAnyFailure)):
            await ctx.trigger_typing()
            await ctx.reply("You cannot use this command",
                            mention_author=False)
        else:
            full_error = f"\nIgnoring exception in command {ctx.command}:\n{''.join(traceback.format_exception(type(error), error, error.__traceback__))}"
            print(full_error, file=sys.stderr)
            await ctx.trigger_typing()
            await ctx.reply(
                "An unexpected error occured\nThe bot developers have been notified to fix this bug",
                mention_author=False,
            )
            webhook = Webhook.from_url(os.getenv("error_webhook"), adapter=RequestsWebhookAdapter())
            webhook.send(
                f"Error from the server `{ctx.guild.name}`",
                username="Error Log",
                file=get_txt(full_error, "error"),
            )


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
