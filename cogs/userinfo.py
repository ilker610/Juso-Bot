import discord
from discord.ext import commands

class userinfo(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self,message,user:discord.Member = None):

        if user is None:
            user = message.author


        emb13 = discord.Embed(title=f"{user.name}'s info:", colour=discord.Colour.random())
        emb13.set_thumbnail(url=user.avatar_url)
        emb13.add_field(name=f"Name", value=f"```{user.name}```", inline=True)
        emb13.add_field(name=f"Discord Joined date", value=f"```{user.created_at}```", inline=True)
        emb13.add_field(name=f"Server Joined date", value=f"```{user.joined_at}```", inline=True)
        emb13.add_field(name=f"ID", value=f"```{user.id}```", inline=True)
        await message.reply(embed=emb13)    

def setup(bot):
    bot.add_cog(userinfo(bot))