import discord
from discord import embeds
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @client.group(invoke_without_command=True)
    async def help(self, ctx):
    embeds = discord.Embed(
        title="Penny The Lamma's Help Desk",
        description="`?help [category]` - View specific category.\nPrefix - `?`. ```[] - Required Argument | () - Optional Argument```",
        color=discord.Colour.red()
    )

    embed.add_field(
        name=":books: Categories",
        value="> :wrench: **Moderation**\n> :musical_note: **Music**\n> :chart_with_upwards_trend: **Leveling**\n> :reminder_ribbon: **Fun**"
    )

    embed.set_footer(
        text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    @help.command(aliases=['mod', 'Mod', 'Moderation'])
    async def moderation(self, ctx):
    embed = discord.Embed(
        title="Penny The Lamma's Help Desk",
        description="Moderation Commands\n```[] - Required Argument | () - Optional Argument```",
        color=discord.Colour.red()
    )

    embed.add_field(
        name=":wrench: Moderation",
        value="> `kick [member] [reason]` - Kick Member. \n> `ban [member] [reason]` - Bans a member. \n> `unban [user]` - unbans a user. \n> `purge [amount]` - Deletes a certain amount of messages. \n> `mute [member] [reason]` - Mutes a member. \n> `unmute [member]` - Unmutes a member. \n> `slowmode [amount in seconds]` - Changes the slowmode.\n> `warn [member] [reason]` - Warn a member. \n> `warnings [member]` - Check a member's warnings. \n> `toggle [command]` - Toggle a command."
    )
    embed.set_footer(
        text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    @help.command(aliases=['Music'])
    async def music(self, ctx):
    embed = discord.Embed(
        title="Penny The Lamma's Help Desk",
        description="Music Commands \n```[] - Required Argument | () - Optional Argument```",
        color=discord.Colour.red()
    )

    embed.add_field(
        name=":musical_note: Music",
        value="> `join` - The bot joins your voice channel. \n> `play [yt-link]` - Play music. \n> `pause` - Pauses the song. \n> `resume` - Resumes the song. \n> `disconnect` - The bot disconnects from the channel."
    )

    embed.set_footer(
        text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    @help.command(aliases=['Leveling', 'level', 'Level'])
    async def leveling(self, ctx):
    embed = discord.Embed(
        title="Penny The Lamma's Help Desk",
        description="Leveling Commands \n```[] - Required Argument | () - Optional Argument```",
        color=discord.Colour.red()
    )

    embed.add_field(
        name=":chart_with_upwards_trend: Leveling",
        value="> `rank` - Shows your rank. \n> `leaderboard` - See the server's leaderboard."
    )

    embed.set_footer(
        text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

    @help.command(aliases=['Fun'])
    async def fun(self, ctx):
    embed = discord.Embed(
        title="Penny The Lamma's Help Desk",
        description="Fun Commands \n```[] - Required Argument | () - Optional Argument```",
        color=discord.Colour.red()
    )

    embed.add_field(
        name=":reminder_ribbon: Fun",
        value="> `ping` - Shows the bot's ping. \n> `8ball [question]` - Answers you question. \n> `userinfo [member]` - Get info about a member. \n> `pfp [member]` - Get the pfp of a member. \n> `wanted [member]` - Make a member wanted."
    )

    embed.set_footer(
        text=f"Requested by {ctx.author}.", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))
