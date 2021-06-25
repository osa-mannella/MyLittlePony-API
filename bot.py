import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix="?", intents=discord.Intents.default())
client.colour = 0xE972AF

class MyHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        n = ""
        r = await self.filter_commands(self.context.bot.commands)
        for command in r:
            if command.name == "help":
                continue
            v = command.signature
            if v != "":
                v = " " + command.signature
            n = n + f"`{self.clean_prefix}{command.name}{v}`\n{command.description}\n\n"
        embed = discord.Embed(title="Commands", description=n, colour=client.colour)
        embed.set_footer(text=f"Requested by {self.context.author}", icon_url=self.context.author.avatar_url)
        await self.context.send(embed=embed)

client.help_command = MyHelp()

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        client.load_extension(f"cogs.{cog[:-3]}")

load_dotenv(".env")
client.run(os.getenv("TOKEN"))