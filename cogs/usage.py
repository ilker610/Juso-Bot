import discord
from discord.ext import commands

class usage(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="usage")
    async def usage(self, ctx, commandname):
        if commandname == "usage":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Usage", value="j.usage [commandname]")
            await ctx.reply(embed=em)
        elif commandname == "avatar":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Avatar", value="j.avatar [user]")
            await ctx.reply(embed=em)
        elif commandname == "ban":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Ban", value="j.ban [user]")
            await ctx.reply(embed=em)
        elif commandname == "botinfo":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Botinfo", value="j.botinfo")
            await ctx.reply(embed=em)
        elif commandname == "help":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Help", value="j.help")
            await ctx.reply(embed=em)
        elif commandname == "kick":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Kick", value="j.kick [user]")
            await ctx.reply(embed=em)
        elif commandname == "ping":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Ping", value="j.ping")
            await ctx.reply(embed=em)
        elif commandname == "rename":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Rename", value="j.rename [user] [nick]")
            await ctx.reply(embed=em)
        elif commandname == "scan":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Scan", value="j.scan [user]")
            await ctx.reply(embed=em)
        elif commandname == "userinfo":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="User Info", value="j.userinfo [user]")
            await ctx.reply(embed=em)
        elif commandname == "wasted":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Wasted", value="j.wasted [user]")
            await ctx.reply(embed=em)
        elif commandname == "load":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Load", value="j.load [module]")
            await ctx.reply(embed=em)
        elif commandname == "reload":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Reload", value="j.reload [module]")
            await ctx.reply(embed=em)
        elif commandname == "findthenumber":
            em = discord.Embed(colour=discord.Colour.random())
            em.add_field(name="Find the number", value="j.findthenumber or j.ftn")
            await ctx.reply(embed=em)
            
            

def setup(bot):
    bot.add_cog(usage(bot))