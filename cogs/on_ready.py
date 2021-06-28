import discord
from discord.ext import commands

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("My Little Pony is ready")

def setup(client):
    client.add_cog(on_ready(client))