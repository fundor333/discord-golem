import logging

from discord.ext import commands


class MyCogs(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    async def cog_load(self):
        """Method called when the cog has been fully loaded."""
        logging.info("The Miscellaneous cog is loaded.")

    @commands.command(name="coolbot")
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send("This bot is cool. :)")

    @commands.command(name="ciao")
    async def test(self, ctx, arg1, arg2):
        await ctx.send(f"You passed {arg1} and {arg2}")


async def setup(client):
    await client.add_cog(MyCogs(client))
