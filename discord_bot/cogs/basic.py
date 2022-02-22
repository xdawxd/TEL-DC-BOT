import discord
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

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban()
        await ctx.send(f"Member: {member.name} has been banned from the server, reason: {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick()
        await ctx.send(f"Member: {member.name} has been kicked from the server, reason: {reason}")

    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name and user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name} #{user.discriminator}')


def setup(client):
    client.add_cog(BasicCommands(client))
