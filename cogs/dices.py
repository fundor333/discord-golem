import logging
import random

from discord.ext import commands


class Dices(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    async def cog_load(self):
        logging.info("The Dices cog is loaded.")

    @commands.command(name="d4")
    async def d4(self, ctx, num=1):
        """Rolls a d4"""
        tot = 0
        for i in range(num):
            tot += random.randint(1, 4)
        await ctx.send(f"You rolled {tot}.")

    @commands.command(name="d6")
    async def d6(self, ctx, num=1):
        """Rolls a d6"""
        tot = 0
        for i in range(num):
            tot += random.randint(1, 6)
        await ctx.send(f"You rolled {tot}.")

    @commands.command(name="d8")
    async def d8(self, ctx, num=1):
        """Rolls a d8"""
        tot = 0
        for i in range(num):
            tot += random.randint(1, 8)
        await ctx.send(f"You rolled {tot}.")

    @commands.command(name="d12")
    async def d12(self, ctx, num=1):
        """Rolls a d12"""
        tot = 0
        for i in range(num):
            tot += random.randint(1, 12)
        await ctx.send(f"You rolled {tot}.")

    @commands.command(name="d20")
    async def d20(self, ctx, num=1):
        """Rolls a d20"""
        tot = 0
        for i in range(num):
            tot += random.randint(1, 20)
        await ctx.send(f"You rolled {tot}.")


async def setup(client):
    await client.add_cog(Dices(client))
