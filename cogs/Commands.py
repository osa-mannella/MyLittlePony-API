import discord
import aiohttp
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def no_result(self, ctx, response):
        terms = ["`" + n.title() + "`, " for n in response]
        characters = " ".join(terms)
        embed = discord.Embed(colour=self.client.colour,
                              description=f"**Hm, I couldn't find that {ctx.command.name}, try one listed below.**\n\n{characters[:-2]}")
        await ctx.send(embed=embed)


    @commands.command(description="Shows information in relation to the supplied character")
    async def character(self, ctx, *, character_name):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://127.0.0.1:5000/character/{character_name.lower()}') as response:
                try:
                    response = await response.json()
                    colour = int(response['color'][1][1:], 16)
                    embed = discord.Embed(title=response['name'], colour=colour)
                    try:
                        embed.add_field(name="Age", value="{:,}".format(int(response['age'])), inline=True)
                    except ValueError:
                        embed.add_field(name="Age", value=response['age'], inline=True)
                    embed.add_field(name="Gender", value=response['gender'], inline=True)
                    embed.add_field(name="Type", value=response['type'], inline=True)
                    embed.add_field(name="Color", value=f"{response['color'][0]} ({response['color'][1]})")
                    embed.add_field(name="Description", value=response['description'], inline=False)
                    embed.set_thumbnail(url=response['thumbnail'])
                    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                except (KeyError, TypeError):
                    await self.no_result(ctx, response)

    @commands.command(description="Shows information in relation to the supplied location")
    async def place(self, ctx, *, place_name):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://127.0.0.1:5000/place/{place_name.lower()}') as response:
                try:
                    response = await response.json()
                    embed = discord.Embed(title=response['name'], colour=self.client.colour)
                    embed.add_field(name="First Appearance", value=response['first-appearance'], inline=True)
                    embed.add_field(name="Ruler", value=response['ruler'])
                    embed.add_field(name="Description", value=response['description'], inline=False)
                    embed.set_thumbnail(url=response['thumbnail'])
                    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                except (KeyError, TypeError):
                    await self.no_result(ctx, response)

    async def embed_episode(self, ctx, response):
        embed = discord.Embed(title=response['title'], colour=ctx.bot.colour)
        embed.add_field(name="Airdate", value=response['release-date'], inline=True)
        embed.add_field(name="Season and Episode", value=f"Season {response['season']} Episode {response['episode']}")
        embed.add_field(name="Writer", value=response['writer'])
        embed.add_field(name="Episode Overall", value=response['episode-overall'])
        embed.add_field(name="Description", value=response['description'], inline=False)
        embed.set_thumbnail(url=response['thumbnail'])
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        return embed

    @commands.command(description="Returns information about a specific episode")
    async def episode(self, ctx, *, episode_name):
        async with aiohttp.ClientSession() as session:
            try:
                if int(episode_name) <= 222:
                    async with session.get('http://127.0.0.1:5000/all_episodes/') as r:
                        response = await r.json()
                        for n in response:
                            r = response[n]['episode-overall']
                            if r == episode_name:
                                q = response[n]
                                break
                        embed = await self.embed_episode(ctx, q)
                        return await ctx.send(embed=embed)
            except ValueError:
                pass
            async with session.get(f'http://127.0.0.1:5000/episode/{episode_name.lower()}') as response:
                try:
                    response = await response.json()
                    embed = await self.embed_episode(ctx, response)
                    await ctx.send(embed=embed)
                except (KeyError, TypeError):
                    embed = discord.Embed(colour=self.client.colour, description=f"**Hm, I couldn't find that {ctx.command.name}.**")
                    embed.set_footer(text="Make sure you give the episode name or the overall episode number.", icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Commands(client))
