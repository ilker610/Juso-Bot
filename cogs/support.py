import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, component

class support(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="support")
    async def support(self,ctx):
        await ctx.channel.send("Click the button to join the support server", components=[
            Button(style=ButtonStyle.URL, label="Support Server !", url="https://discord.gg/PMfqNKtEPJ")])

def setup(bot):
    bot.add_cog(support(bot))