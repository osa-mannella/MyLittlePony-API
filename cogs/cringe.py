import discord
from discord.ext import commands

class cringe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="I like dgsdgfskdjgoskjgd")
    async def cringe(self, ctx, avatar=None):
        await ctx.send("test")

def setup(client):
    client.add_cog(cringe(client))