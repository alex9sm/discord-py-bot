import discord
from discord import app_commands
from discord.ext import commands


class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="says hello")
    async def help(self, ctx: discord.Interaction):
        await ctx.response.send_message(f"hello {ctx.user.mention}")

async def setup(bot):
    await bot.add_cog(HelloCommand(bot))