import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self, message, user:discord.Member):
        if user.id == self.bot.user.id:
            await message.channel.send("I can't kick myself")
        elif user.id == message.author.id:
            await message.channel.send("You can't kick yourself")
        else:
            await user.kick()
            msg = await message.channel.send(f"{user.name} kicked.")
            await msg.add_reaction("✅")

def setup(bot):
    bot.add_cog(kick(bot))