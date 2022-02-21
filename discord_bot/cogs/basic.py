from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def ping(self, ctx) -> None:
        await ctx.send(f'Bot ping is {round(self.client.latency * 1000)}ms')

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def clear(self, ctx, amount=100) -> None:
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(BasicCommands(client))
