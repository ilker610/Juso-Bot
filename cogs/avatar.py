import discord
import datetime
from discord.ext import commands

class avatar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, member:discord.Member = None):
        if member is None:
            member = ctx.author

        emb = discord.Embed(title=member.name, color=discord.Color.random())
        emb.set_image(url=member.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(avatar(bot))