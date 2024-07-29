import discord
from discord import app_commands
from discord.ext import commands
from utils.utils import random_proverb

class ProverbCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="proverb", description="says a chinese proverb")
    async def help(self, ctx: discord.Interaction):
        proverb = await random_proverb()
        await ctx.response.send_message(proverb)

async def setup(bot):
    await bot.add_cog(ProverbCommand(bot))