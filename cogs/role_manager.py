import discord
from discord.ext import commands

class role_manager(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="addrole")
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, user:discord.Member = None, role:discord.Role = None):
        if user is None:
            await ctx.reply("User must enter !")
        else:
            pass
            
        if role is None:
            await ctx.reply("Role must enter !")
        else:
            pass

        try:
            await user.add_roles(role)
        except discord.Forbidden:
            await ctx.reply("You are not authorized to use this command")
            
        await ctx.reply("Done !")

    @commands.command(name="removerole")
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, user:discord.Member = None, role:discord.Role = None):
        if user is None:
            await ctx.reply("User must enter !")
        else:
            pass
                
        if role is None:
            await ctx.reply("Role must enter !")
        else:
            pass
    
        try:
            await user.remove_roles(role)
        except discord.Forbidden:
            await ctx.reply("You are not authorized to use this command")
                
        await ctx.reply("Done !")
        
    @commands.command(name="createrole")
    @commands.has_permissions(administrator=True)
    async def createrole(self, ctx, rolename = None):
        if rolename is None:
            await ctx.reply("You need role name")
        else:
            pass
        guild = ctx.guild
        await guild.create_role(name=rolename)
        await ctx.reply(f"{rolename} is created !")                                


def setup(bot):
    bot.add_cog(role_manager(bot))