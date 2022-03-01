import discord
import random
from discord.ext import commands

class scan(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="scan")
    async def scan(self, ctx, user:discord.Member = None):
        list = ["{}, is imposter !", "{}, is crewmate"]
        
        if user is None:
            await ctx.reply(random.choice(list).format(ctx.author.mention))
        else:
            await ctx.reply(random.choice(list).format(user.mention))
        
def setup(bot):
    bot.add_cog(scan(bot))
    