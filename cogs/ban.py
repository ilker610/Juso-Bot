import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class ban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user:discord.Member = None):
        if user is None:
            await ctx.reply("User must enter !")
        if user.id == self.bot.user.id:
            await ctx.reply("I can't ban myself")
        elif user.id == ctx.author.id:
            await ctx.reply("You can't kick yourself")
        else:
            await user.ban()
            msg = await ctx.reply(f"{user.name} banned !")
            await msg.add_reaction("✅")

def setup(bot):
    bot.add_cog(ban(bot))