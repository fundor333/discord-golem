import logging

from discord.ext import commands
from discord.ext.commands import Cog


class Meme(Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    async def cog_load(self):
        logging.info("The Meme cog is loaded.")

    @commands.command(name="gne")
    async def gne(self, ctx, num=1):
        """gne"""
        await ctx.send("Gne gne gne gne gne")
        await ctx.send(":stuck_out_tongue_closed_eyes:")


async def setup(client):
    await client.add_cog(Meme(client))
