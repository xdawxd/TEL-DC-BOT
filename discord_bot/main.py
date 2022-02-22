import os
import discord
from discord.ext import commands


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='.', intents=intents)


@client.command()
async def load(ctx, extension) -> None:
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}.')


@client.command()
async def unload(ctx, extension) -> None:
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}.')


@client.command()
async def reload(ctx, extension) -> None:
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded.')


for filename in os.listdir('./TEL-DC-BOT/discord_bot/cogs'):
    if filename.endswith('.py') and "__init__" not in filename:
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))
