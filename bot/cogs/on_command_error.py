import discord
import traceback
import sys
from discord.ext import commands

class on_command_error(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=self.client.colour, description=f"**Missing Required Argument**\n-> `{ctx.prefix}{ctx.command.name}` `{ctx.command.signature}`")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.CheckFailure):
            return

def setup(client):
    client.add_cog(on_command_error(client))