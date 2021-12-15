import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = self

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user=None, reason=None):
        if not user:
            return await ctx.send("You must specify a user!")

        try:
            await user.ban(reason=reason)
            await ctx.send(f"{user.mention} was banned for {reason}.")
        except discord.Forbidden:
            return await ctx.send("You cannot ban someone higher than the bot!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user=None, reason=None):
        if not user:
            return await ctx.send("You must specify a user!")

        try:
            await user.kick(reason=reason)
            await ctx.send(f"{user.mention} was kicked for {reason}.")
        except discord.Forbidden:
            return await ctx.send("You cannot kick someone higher than the bot!")


def setup(client):
    client.add_cog(Moderation(client))
